// variáveis globais
let chat = document.querySelector("#chat");
let input = document.querySelector("#input");
let botaoEnviar = document.querySelector("#botao-enviar");

let imagemSelecionada;
let botaoAnexo = document.querySelector("#mais_arquivo");
let miniaturaImagem;

// Função para abrir seletor de imagem e fazer upload para o backend
async function pegarImagem(){
  let fileInput = document.createElement("input");
  fileInput.type = "file";
  fileInput.accept = "image/*"; // aceita apenas imagens

  fileInput.onchange = async e => {
    if(miniaturaImagem){
      miniaturaImagem.remove(); // remove a imagem anterior, se houver
    }

    imagemSelecionada = e.target.files[0];  // pega a imagem selecionada

    // Cria miniatura da imagem selecionada
    miniaturaImagem = document.createElement("img");
    miniaturaImagem.src = URL.createObjectURL(imagemSelecionada);
    miniaturaImagem.style.maxWidth = "3rem";
    miniaturaImagem.style.maxHeight = "3rem";
    miniaturaImagem.style.margin = "0.5rem";

    document.querySelector(".entrada__container").insertBefore(miniaturaImagem, input);

    // Envia imagem para o backend
    let formData = new FormData();
    formData.append("imagem", imagemSelecionada);

    const response = await fetch("http://127.0.0.1:5000/upload_imagem", {
      method: "POST",
      body: formData
    });

    const resposta = await response.text();
    console.log(resposta);
    console.log(imagemSelecionada);
  }

  fileInput.click(); // abre o seletor de arquivos
}

// Função para enviar mensagem de texto para o backend e exibir resposta
async function enviarMensagem(){
  if(input.value == "" || input.value == null) return;
  let mensagem = input.value;
  input.value = "";

  if(miniaturaImagem){
    miniaturaImagem.remove(); // remove a miniatura se havia imagem
  }

  // Cria bolha de usuario e adiciona ao chat
  let novaBolha = criaBolhaUsuario();
  novaBolha.innerHTML = mensagem;
  chat.appendChild(novaBolha);

  // Cria bolha do bot com animação de "Analisando..."
  let novaBolhaBot = criaBolhaBot();
  chat.appendChild(novaBolhaBot);
  vaiParaFinalDoChat();
  novaBolhaBot.innerHTML = "Analisando";

  let estados = ["Analisando .", "Analisando ..", "Analisando ...", "Analisando ."];
  let indiceEstado = 0;

  // Animação de carregamento
  let intervaloAnimacao = setInterval(() => {
    novaBolhaBot.innerHTML = estados[indiceEstado];
    indiceEstado = (indiceEstado + 1) % estados.length;
  }, 500);

  // Envia a mensagem ao backend Flask
  const resposta = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ "msg": mensagem })
  });
  
  const textoDaResposta = await resposta.text();
  console.log(textoDaResposta);

  clearInterval(intervaloAnimacao); // interrompe a animação

  // Exibe a resposta do bot
  novaBolhaBot.innerHTML = textoDaResposta.replace(/\n/g, "<br>");
  vaiParaFinalDoChat();
}

// Função para criar a bolha com estilo do usuario
function criaBolhaUsuario(){
  let bolha = document.createElement("p");
  bolha.classList.add("chat__bolha chat__bolha--usuario");
  return bolha;
}

// Função para criar a bolha com estilo do bot
function criaBolhaBot(){
  let bolha = document.createElement("p");
  bolha.classList.add("chat__bolha chat__bolha--bot");
  return bolha;
}

// Função para mover o chat para o final da tela
function vaiParaFinalDoChat(){
  chat.scrollTop = chat.scrollHeight;
}

// Eventos: clique no botão de enviar ou teclar Enter
botaoEnviar.addEventListener("click", enviarMensagem);
input.addEventListener("keyup", function(event){
  event.preventDefault();
  if(event.keyCode == 13) {
    botaoEnviar.click();
  }
});

// Evento para abrir o seletor de imagens
botaoAnexo.addEventListener("click", pegarImagem);

