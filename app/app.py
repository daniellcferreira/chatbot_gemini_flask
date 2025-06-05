from flask import Flask, render_template, request, Response
import google.generativeai as genai
from dotenv import load_dotenv
import os
import uuid
from time import sleep
from helper import carrega, salva
from selecionar_persona import personas, selecionar_persona
from gerenciar_historico import remover_mensagens_mais_antigas
from gerenciar_imagem import gerar_imagem_gemini

# carrega variaveis de ambiente do .env
load_dotenv()

# configura a API do Gemini
CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-1.5-flash"
genai.configure(api_key=CHAVE_API_GOOGLE)

# inicializa a aplicação Flask
app = Flask(__name__)
app.secret_key = "teste"

# carrega o contexto do e-commerce
contexto = carrega("assets/musimart.txt")

# diretorio para salvar imagens temporarias
caminho_imagem_enviada = None
UPLOAD_FOLDER = "imagens_temporarias"

# cria um objeto do chabot com o contexto e configuração inicial
def criar_chatbot():
  personalidade = "neutro"  # personalidade padrão

  prompt_do_sistema = f"""
    # PERSONA

    Você é um chatbot de atendimento a clientes de um e-commerce. 
    Você não deve responder perguntas que não sejam dados do ecommerce informado!

    Você deve utilizar apenas dados que estejam dentro do 'contexto'

    # CONTEXTO
    {contexto}

    # PERSONALIDADE
    {personalidade}

    # Histórico
    Acesse sempre o históricio de mensagens, e recupere informações ditas anteriormente.
    """
  
  configuracao_modelo = {
    "temperature": 0.1,
    "max_output_tokens": 8192
  }

  llm = genai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt_do_sistema,
    generation_config=configuracao_modelo
  )

  # cria uma sessão de chat com historico vazio
  chatbot = llm.start_chat(history=[])
  return chatbot

# instancia inicial do chatbot
chatbot = criar_chatbot()

# função principal que interage com o modelo e decide se usa imagem
def bot(prompt):
  maximo_tentativas = 1
  repeticao = 0
  global caminho_imagem_enviada

  while True:
    try:
      # analisa o sentimento e escolhe a persona correspondente
      personalidade = personas[selecionar_persona(prompt)]

      mensagem_usuario = f"""
      Considere esta personalidade para responder a mensagem:
      {personalidade}

      Responda a seguinte mensagem, sempre lembrando do histórico:
      {prompt}
      """

      # caso haja imagem, envia imagem + texto ao modelo
      if caminho_imagem_enviada:
        mensagem_usuario += "\n Utilize as características da imagem em sua resposta"
        arquivo_imagem = gerar_imagem_gemini(caminho_imagem_enviada)
        resposta = chatbot.send_message([arquivo_imagem, mensagem_usuario])
        os.remove(caminho_imagem_enviada)
        caminho_imagem_enviada = None
      else:
        resposta = chatbot.send_message(mensagem_usuario)

      # limita o historico para o maximo de 10 mensagens
      if len(chatbot.history) > 10:
        chatbot.history = remover_mensagens_mais_antigas(chatbot.history)

      return resposta.text
    
    except Exception as erro:
      repeticao += 1
      if repeticao >= maximo_tentativas:
        return f"Erro no Gemini: {erro}"
      
      # limpa imagem temporaria caso ocorra erro
      if caminho_imagem_enviada:
        os.remove(caminho_imagem_enviada)
        caminho_imagem_enviada = None

      sleep(50)  # espera antes de tentar novamente

# Rota para upload da imagem via POST
@app.route("/upload_imagem", methods=["POST"])
def upload_imagem():
  global caminho_imagem_enviada

  if "imagem" in request.files:
    imagem_enviada = request.files["imagem"]
    # gera nome unico e salva imagem em pasta temporaria
    nome_arquivo = str(uuid.uuid4()) + os.path.splitext(imagem_enviada.filename)[1]
    caminho_arquivo = os.path.join(UPLOAD_FOLDER, nome_arquivo)
    imagem_enviada.save(caminho_arquivo)
    caminho_imagem_enviada = caminho_arquivo
    return "Imagem enviada com sucesso", 200
  
  return "Nenhhum arquivo enviado", 400

# Rota de chat: recebe mensagem do front-end, retorna resposta do bot
@app.route("/chat", methods=["POST"])
def chat():
  prompt = request.json["msg"]
  resposta = bot(prompt)
  return resposta

# Rota principal que carrega o interface HTML
@app.route("/")
def home():
  return render_template("index.html")

# Inicia o servidor Flasj em mode debug
if __name__ == "__main__":
  app.run(debug=True)



