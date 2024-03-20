function mudarPagina(finalDaPagina) {
    
    var urlAtual = window.location.origin;
    var novaUrl = urlAtual + '/' + finalDaPagina;

    window.location.href = novaUrl;
}

function gotoPage(page) {
    window.open(page);
}