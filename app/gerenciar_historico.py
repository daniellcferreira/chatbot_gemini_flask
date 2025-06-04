# remove as duas mensagens mais antigas do historico
# isso ajuda a evitar que o histórico fique muito longo, respeitando os limites do modelo
# a função assume que o histórico é uma lista de mensagens trocadas com o chatbot

def remover_mensagens_mais_antigas(historico):
  return historico[2:]