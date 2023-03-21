/*
var cantidadDeImagenes = 3;
var imagenes = [];
var cont = 0

for (var i = 1; i <= cantidadDeImagenes; i++) {
    imagenes.push('/static/src/clientes/Fermag/fondo'+i+'.png');
}

setInterval(function(){
    let img = inicio.querySelector('img');

    if(cont < imagenes.length - 1){
        img.src = imagenes[cont + 1];
        cont++;
    } else {
        img.src = imagenes[0];
        cont = 0;
    }
    console.log('aaa')
}, 10000);


function carrousel(inicio){
    inicio.addEventListener('click', e => {
        let atras = inicio.querySelector('.atras'),
            adelante = inicio.querySelector('.adelante'),
            img = inicio.querySelector('img'),
            tgt = e.target;

        if(tgt == atras){
            if(cont > 0){
                img.src = imagenes[cont - 1];
                cont--;
            } else {
                img.src = imagenes[imagenes.length - 1 ];
                cont = imagenes.length - 1;
            }
        } else if(tgt == adelante){
            if(cont < imagenes.length - 1){
                img.src = imagenes[cont + 1];
                cont++;
            } else {
                img.src = imagenes[0];
                cont = 0;
            }
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
    let inicio = document.querySelector('.inicio');

    carrousel(inicio);
});
*/

window.addEventListener("scroll", function() {
    var nav = document.querySelector("nav");
    nav.classList.toggle("scroll", window.scrollY > 0);
  });