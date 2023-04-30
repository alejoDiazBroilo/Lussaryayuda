var cards = []
var difuminados

var card1 = document.getElementById("card-1")
var difuminado1 = document.getElementById("difuminado-1")

var card2 = document.getElementById("card-2")
var difuminado2 = document.getElementById("difuminado-2")

var cards = [
  [card1,difuminado1],
  [card2,difuminado2],
]



function addEvento(card, difuminado){
  card.addEventListener('mouseover', function() {
    difuminado.style.backdropFilter = "blur(0)";
  });
  card.addEventListener('mouseout', function() {
    difuminado.style.backdropFilter = "blur(2px)";
  });
}

cards.forEach(i => {
  addEvento(i[0],i[1])
});


setTimeout(() => {
  cards.forEach(i => {
    i[0].className = "content";
  });
}, "2000");










/*  */







