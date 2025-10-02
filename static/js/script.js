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