function menuShow() {
    let icone = document.querySelector('.fa-solid fa-bars');
    let menuMobile = document.querySelector('.menu-mobily');
    if (menuMobile.classList.contains('open')) {
        menuMobile.classList.remove('open');
    } else {
        menuMobile.classList.add('open');
    }

    if (icone.classList.contains('fa-solid fa-bars')) {
        menuMobile.classList.remove('fa-solid fa-bars');
    } else {
        icone.classList.add('fa-solid fa-xmark')
    }




}