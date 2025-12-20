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
let botao_4 = document.querySelector('.botao_4');
let botao_5 = document.querySelector('.botao_5');

let secao_1 = document.querySelector('.secao_1');
let secao_2 = document.querySelector('.secao_2');
let secao_3 = document.querySelector('.secao_3');
let secao_4 = document.querySelector('.secao_4');
let secao_5 = document.querySelector('.secao_5');

function sidbar_agendaDia() {
    
    if (!botao_1.classList.contains('select')) {
        botao_1.classList.add('select');
        botao_2.classList.remove('select'); 
        botao_3.classList.remove('select');
        botao_4.classList.remove('select');
        botao_5.classList.remove('select');

        secao_1.classList.remove('ocuto');
        secao_1.classList.add('minhas-reservas');

        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
        secao_4.classList.remove('minhas-reservas');
        secao_4.classList.add('ocuto');
        secao_5.classList.remove('minhas-reservas');
        secao_5.classList.add('ocuto');
    }

} 

function sidbar_servicos() {
    if (!botao_2.classList.contains('select')) {

        botao_2.classList.add('select');
        botao_1.classList.remove('select'); 
        botao_3.classList.remove('select');
        botao_4.classList.remove('select');
        botao_5.classList.remove('select');

        secao_2.classList.remove('ocuto');
        secao_2.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
        secao_4.classList.remove('minhas-reservas');
        secao_4.classList.add('ocuto');
        secao_5.classList.remove('minhas-reservas');
        secao_5.classList.add('ocuto');
    }
}

function sidbar_profissionais() {
    if (!botao_3.classList.contains('select')) {

        botao_3.classList.add('select');
        botao_1.classList.remove('select'); 
        botao_2.classList.remove('select');
        botao_4.classList.remove('select');
        botao_5.classList.remove('select');

        secao_3.classList.remove('ocuto');
        secao_3.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
        secao_4.classList.remove('minhas-reservas');
        secao_4.classList.add('ocuto');
        secao_5.classList.remove('minhas-reservas');
        secao_5.classList.add('ocuto');
    }
}

function sidbar_cadProfissional() {
    if (!botao_4.classList.contains('select')) {

        botao_4.classList.add('select');
        botao_1.classList.remove('select'); 
        botao_2.classList.remove('select');
        botao_3.classList.remove('select');
        botao_5.classList.remove('select');

        secao_4.classList.remove('ocuto');
        secao_4.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
        secao_5.classList.remove('minhas-reservas');
        secao_5.classList.add('ocuto');
    }
}

function sidbar_cadServiço() {
    if (!botao_5.classList.contains('select')) {

        botao_5.classList.add('select');
        botao_1.classList.remove('select'); 
        botao_2.classList.remove('select');
        botao_3.classList.remove('select');
        botao_4.classList.remove('select');

        secao_5.classList.remove('ocuto');
        secao_5.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
        secao_4.classList.remove('minhas-reservas')
        secao_4.classList.add('ocuto');
    }
}



// FUNÇÕES DO MENU AMBURGUE CLIENTE
let botaoMenuBurger_1 = document.querySelector('.botaoMenuBurger_1');
let botaoMenuBurger_2 = document.querySelector('.botaoMenuBurger_2');
let botaoMenuBurger_3 = document.querySelector('.botaoMenuBurger_3');
let botaoMenuBurger_4 = document.querySelector('.botaoMenuBurger_4');
let botaoMenuBurger_5 = document.querySelector('.botaoMenuBurger_5');

function sidbarMenu_AgendaDia() {
    
    if (!botaoMenuBurger_1.classList.contains('select-menu')) {
        botaoMenuBurger_1.classList.add('select-menu');
        botaoMenuBurger_2.classList.remove('select-menu'); 
        botaoMenuBurger_3.classList.remove('select-menu');
        botaoMenuBurger_4.classList.remove('select-menu');
        botaoMenuBurger_5.classList.remove('select-menu');

        secao_1.classList.remove('ocuto');
        secao_1.classList.add('minhas-reservas');

        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
        secao_4.classList.remove('minhas-reservas');
        secao_4.classList.add('ocuto');
        secao_5.classList.remove('minhas-reservas');
        secao_5.classList.add('ocuto');
    }
    menuShow()
} 

function sidbarMenu_Servicos() {
    if (!botaoMenuBurger_2.classList.contains('select-menu')) {

        botaoMenuBurger_2.classList.add('select-menu');
        botaoMenuBurger_1.classList.remove('select-menu'); 
        botaoMenuBurger_3.classList.remove('select-menu');
        botaoMenuBurger_4.classList.remove('select-menu');
        botaoMenuBurger_5.classList.remove('select-menu');

        secao_2.classList.remove('ocuto');
        secao_2.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
        secao_4.classList.remove('minhas-reservas');
        secao_4.classList.add('ocuto');
        secao_5.classList.remove('minhas-reservas');
        secao_5.classList.add('ocuto');
    }
    menuShow()
}

function sidbarMenu_Profifionais() {
    if (!botaoMenuBurger_3.classList.contains('select-menu')) {

        botaoMenuBurger_3.classList.add('select-menu');
        botaoMenuBurger_1.classList.remove('select-menu'); 
        botaoMenuBurger_2.classList.remove('select-menu');
        botaoMenuBurger_4.classList.remove('select-menu');
        botaoMenuBurger_5.classList.remove('select-menu');

        secao_3.classList.remove('ocuto');
        secao_3.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
        secao_4.classList.remove('minhas-reservas');
        secao_4.classList.add('ocuto');
        secao_5.classList.remove('minhas-reservas');
        secao_5.classList.add('ocuto');
    }
    menuShow()
}

function sidbarMenu_CadProfissional() {
    if (!botaoMenuBurger_4.classList.contains('select-menu')) {

        botaoMenuBurger_4.classList.add('select-menu');
        botaoMenuBurger_1.classList.remove('select-menu'); 
        botaoMenuBurger_2.classList.remove('select-menu');
        botaoMenuBurger_3.classList.remove('select-menu');
        botaoMenuBurger_5.classList.remove('select-menu');

        secao_4.classList.remove('ocuto');
        secao_4.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
        secao_5.classList.remove('minhas-reservas');
        secao_5.classList.add('ocuto');
    }
    menuShow()
}

function sidbarMenu_cadServiço() {
    if (!botaoMenuBurger_5.classList.contains('select-menu')) {

        botaoMenuBurger_5.classList.add('select-menu');
        botaoMenuBurger_1.classList.remove('select-menu'); 
        botaoMenuBurger_2.classList.remove('select-menu');
        botaoMenuBurger_3.classList.remove('select-menu');
        botaoMenuBurger_4.classList.remove('select-menu');

        secao_5.classList.remove('ocuto');
        secao_5.classList.add('minhas-reservas');

        secao_1.classList.remove('minhas-reservas');
        secao_1.classList.add('ocuto');
        secao_2.classList.remove('minhas-reservas');
        secao_2.classList.add('ocuto');
        secao_3.classList.remove('minhas-reservas');
        secao_3.classList.add('ocuto');
        secao_4.classList.remove('minhas-reservas');
        secao_4.classList.add('ocuto');
    }
    menuShow()
}



// FUNÇÃO DE REAGENDAMENTO

const botoes = document.querySelectorAll('btn');
const modal = document.getElementById('modal');





