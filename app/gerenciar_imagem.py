import google.generativeai as genai
from dotenv import load_dotenv
import os

# carrega variaveis de ambiente do arquivo .env
load_dotenv()

# recupera a chave da API do Gemini e configura o modelo escolhido
CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
MODELO_ESCOLHIDO = "gemini-1.5-flash"
genai.configure(api_key=CHAVE_API_GOOGLE)

# função para fazer upload de uma imagem e retornar o objeto de imagem temporaria
def gerar_imagem_gemini(caminho_imagem):
  try:
    # faz upload da imagem para o Gemini
    arquivo_temporario = genai.upload_file(
      path=caminho_imagem,
      display_name="Imagem Enviada"
    )

    # para fins de debug: exibe a URI do arquivo temporario
    print(f"Imagem Enviada: {arquivo_temporario.uri}")

    return arquivo_temporario
  
  except Exception as erro:
    # em caso de falha no upload, exibe mensagem se erro
    print(f"Erro ao enviar imagem para Gemini: {erro}")
    return None