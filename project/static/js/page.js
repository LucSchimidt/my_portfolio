function mudarPagina(finalDaPagina) {
    
    var urlAtual = window.location.origin;
    var novaUrl = urlAtual + '/' + finalDaPagina;

    window.location.href = novaUrl;
}

function gotoPage(page) {
    window.open(page);
}

function openPortfolio(popup_page) {

    var urlAtual = window.location.origin;
    var novaUrl = urlAtual + '/' + popup_page;

    window.location.href = novaUrl;

}

function showElement() {
    var elemento = document.getElementById("popup");
    if (elemento) {
        elemento.style.display = "flex";
    }
}

function hideElement() {
    var elemento = document.getElementById("popup");
    var elemento_dois = document.getElementById("inicial-msg");
    if (elemento) {
        elemento.style.display = "none";
    }

    if (elemento_dois) {
        elemento_dois.style.display = "none";
    }
}