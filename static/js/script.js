function menuShow() {
    let icone = document.querySelector('.menuBuger');
    let menuMobile = document.querySelector('.menu-mobily');

    if (menuMobile.classList.contains('menu-active')) {
        menuMobile.classList.remove('menu-active');
        icone.classList.remove('fa-xmark');
        icone.classList.add('fa-bars');
    } else {
        menuMobile.classList.add('menu-active');
        icone.classList.remove('fa-bars');
        icone.classList.add('fa-xmark');
    }

}

// FUNÇÕES DO SIDBAR CLIENTE
let botao_1 = document.querySelector('.botao_1');
let botao_2 = document.querySelector('.botao_2');
let botao_3 = document.querySelector('.botao_3');

let secao_1 = document.querySelector('.secao_1');
let secao_2 = document.querySelector('.secao_2');
let secao_3 = document.querySelector('.secao_3');

function sidbar_minhas_reservas() {
    
    if (!botao_1.classList.contains('select')) {
        botao_1.classList.add('select');
        botao_2.classList.remove('select'); 
        botao_3.classList.remove('select');

        secao_1.classList.remove('ocuto');
        secao_1.classList.add('minhas-reservas');

        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
    }

} 

function sidbar_novo_agendamento() {
    if (!botao_2.classList.contains('select')) {

        botao_2.classList.add('select');
        botao_1.classList.remove('select'); 
        botao_3.classList.remove('select');

        secao_2.classList.remove('ocuto');
        secao_2.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
    }
}

function sidbar_perfil() {
    if (!botao_3.classList.contains('select')) {

        botao_3.classList.add('select');
        botao_1.classList.remove('select'); 
        botao_2.classList.remove('select');

        secao_3.classList.remove('ocuto');
        secao_3.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
    }
}

// FUNÇÕES DO MENU AMBURGUE CLIENTE
let botaoMenuBurger_1 = document.querySelector('.botaoMenuBurger_1');
let botaoMenuBurger_2 = document.querySelector('.botaoMenuBurger_2');
let botaoMenuBurger_3 = document.querySelector('.botaoMenuBurger_3');

function sidbarMenu_reservas() {
    
    if (!botaoMenuBurger_1.classList.contains('select-menu')) {
        botaoMenuBurger_1.classList.add('select-menu');
        botaoMenuBurger_2.classList.remove('select-menu'); 
        botaoMenuBurger_3.classList.remove('select-menu');

        secao_1.classList.remove('ocuto');
        secao_1.classList.add('minhas-reservas');

        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
    }
    menuShow()
} 

function sidbarMenu_agendamento() {
    if (!botaoMenuBurger_2.classList.contains('select-menu')) {

        botaoMenuBurger_2.classList.add('select-menu');
        botaoMenuBurger_1.classList.remove('select-menu'); 
        botaoMenuBurger_3.classList.remove('select-menu');

        secao_2.classList.remove('ocuto');
        secao_2.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
    }
    menuShow()
}

function sidbarMenu_perfil() {
    if (!botaoMenuBurger_3.classList.contains('select-menu')) {

        botaoMenuBurger_3.classList.add('select-menu');
        botaoMenuBurger_1.classList.remove('select-menu'); 
        botaoMenuBurger_2.classList.remove('select-menu');

        secao_3.classList.remove('ocuto');
        secao_3.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
    }
    menuShow()
}


// FUNÇÃO DE REAGENDAMENTO

const botoes = document.querySelectorAll('.btn-reagendar');
const modal = document.getElementById('modal');
const closeBtn = document.querySelector('.close');

botoes.forEach(botao => {
  botao.addEventListener('click', () => {
    const card = botao.closest('.card-servico');

    const servicoTexto = card.querySelector('.descricao h2').textContent.trim();
    const profissional = card.querySelector('.descricao span').textContent.replace('Com ', '').trim();
    const spans = card.querySelectorAll('.data-hora span');
    const data = spans[0].textContent.trim();
    const hora = spans[1].textContent.trim();

    // Converter data para formato yyyy-mm-dd
    const [dia, mes, ano] = data.split('/');
    const dataFormatada = `${ano}-${mes}-${dia}`;

    // Mapeamento dos serviços
    const mapaServicos = {
      "Corte Masculino": "Corte_Mascolino",
      "Corte Feminino": "Corte_Femenino",
      "Barba & Bigode": "Barba_&_Bigode",
      "Hidratação": "Hidratação"
    };
    const valorSelect = mapaServicos[servicoTexto] || "";

    // Mapeamento dos profissionais
    const mapaProfissionais = {
      "João de Deus": "Joao_de_Deus",
      "Marina Silvia": "Marina_Silvia",
      "Frederico": "Frederico",
    };
    const valorProf = mapaProfissionais[profissional] || "";


    // Preenche o formulário
    document.getElementById('servico').value = valorSelect;
    document.getElementById('profissional').value = valorProf;
    document.getElementById('input-data').value = dataFormatada;
    document.getElementById('input-hora').value = hora;

    // Abre o modal
    modal.style.display = 'block';
  });
});

// Fecha o modal ao clicar no "X"
closeBtn.addEventListener('click', () => {
  modal.style.display = 'none';
});

// Fecha o modal clicando fora dele
window.addEventListener('click', (e) => {
  if (e.target === modal) {
    modal.style.display = 'none';
  }
});
