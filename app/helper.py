# função para carregar dados binarios de um arquivo
def carrega(nome_do_arquivo):
  try:
    # abre o arquivo no modo binario de leitura
    with open(nome_do_arquivo, "rb") as arquivo:
      dados = arquivo.read()
      return dados
  except IOError as e:
    # captura erro de leitura, como arquivo inexistente ou permissão negada
    print(f"Erro no carregamento do arquivo: {e}")

# função para salvar conteudo de texto em um arquivo
def salva(nome_do_arquivo, conteudo):
  try:
    with open(nome_do_arquivo, "w", encoding="uft-8") as arquivo:
      arquivo.write(conteudo)
  except IOError as e:
    print(f"Erro ao salvar o arquivo: {e}")