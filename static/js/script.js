function menuShow() {
    let icone = document.querySelector('.menuBuger');
    let menuMobile = document.querySelector('.menu-mobily');

    if (menuMobile.classList.contains('open')) {
        menuMobile.classList.remove('open');
        icone.classList.remove('fa-xmark');
        icone.classList.add('fa-bars');
    } else {
        menuMobile.classList.add('open');
        icone.classList.remove('fa-bars');
        icone.classList.add('fa-xmark');
    }

    



}