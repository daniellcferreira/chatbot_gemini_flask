# MusiMart Chatbot – Atendimento com IA Generativa
[![Python](https://img.shields.io/badge/Python-Scripting-blue?style=flat-square&logo=python)](https://www.python.org/)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-blue?style=flat-square&logo=flask)
![Gemini](https://img.shields.io/badge/Gemini-IA%20da%20Google-ffce00?style=flat-square&logo=google)
![HTML5](https://img.shields.io/badge/HTML5-Marcação%20de%20páginas-e34f26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Estilização-1572b6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Interatividade-f7df1e?style=flat-square&logo=javascript&logoColor=black)

## Descrição

O projeto MusiMart Chatbot é uma aplicação web baseada em inteligência artificial generativa desenvolvida com o objetivo de simular o atendimento ao cliente em um ambiente de e-commerce. Com a integração da API Gemini da Google e o framework Flask, a aplicação responde de maneira contextualizada a perguntas sobre produtos e políticas da loja fictícia MusiMart.

As respostas são geradas com base em um contexto textual previamente carregado e mantido no servidor. O bot é capaz de adaptar seu estilo de resposta conforme o sentimento da mensagem do usuário. A interface permite o envio de texto e imagem, oferecendo uma experiência multimodal ao cliente virtual.

Todo o histórico de conversas é considerado para garantir respostas consistentes. O modelo não responde perguntas fora do escopo definido, respeitando rigorosamente o conteúdo da base do e-commerce.

## Funcionalidades

- Interface interativa com entrada de texto no estilo chat
- Envio de mensagens com detecção de tecla Enter
- Upload de imagens para análise visual
- Integração com a API do Gemini da Google para processamento de linguagem natural
- Personalização de respostas com base no sentimento identificado
- Seleção automática de personas (neutro, amigável, sarcástico etc.)
- Respostas limitadas ao contexto carregado da loja
- Geração de respostas com histórico de conversas preservado
- Limitação de histórico para evitar sobrecarga de contexto
- Respostas assíncronas com atualização dinâmica via JavaScript
- Exclusão automática de imagens temporárias após o uso
- Modularização do código com separação por responsabilidade
- Templates HTML renderizados com Jinja2
- Estilo limpo e responsivo utilizando CSS3

## Tecnologias abordadas por extenso

**Python**  
Linguagem principal utilizada para desenvolvimento da aplicação backend, controle de rotas, integração com a API e manipulação de arquivos.

**Flask**  
Framework web leve para construção de aplicações web com rotas simples, renderização de templates e endpoints para requisições assíncronas.

**Gemini (Google Generative AI)**  
Modelo de linguagem natural desenvolvido pela Google, responsável por interpretar entradas textuais, analisar imagens e gerar respostas baseadas no contexto fornecido.

**HTML5**  
Linguagem de marcação utilizada para estruturar a interface do chatbot, incluindo a área de chat, entrada de mensagem e botões de ação.

**CSS3**  
Linguagem de estilo utilizada para definir o layout, cores, espaçamento e responsividade da interface do chatbot.

**JavaScript**  
Linguagem de programação client-side utilizada para capturar eventos de usuário (como pressionar Enter), enviar requisições via AJAX e atualizar o DOM com novas mensagens.

**jQuery**  
Biblioteca JavaScript usada para facilitar chamadas AJAX e manipulação do DOM, garantindo envio e recepção das mensagens sem recarregar a página.

**dotenv**  
Biblioteca Python para gerenciamento seguro de variáveis de ambiente, como a chave da API Gemini.

**uuid**  
Módulo utilizado para gerar nomes únicos de arquivos de imagem enviados pelo usuário.

**Estrutura de pastas organizada**  
Separação do código em arquivos como `app.py`, `helper.py`, `selecionar_persona.py`, `gerenciar_historico.py`, `gerenciar_imagem.py`, além de pastas como `templates`, `static`, `assets` e `imagens_temporarias`.

Este projeto é um exemplo de como a IA generativa pode ser aplicada a contextos práticos, respeitando regras de negócio, mantendo coerência e promovendo interações naturais e eficazes com o usuário.
 
