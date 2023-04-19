// Variables
const nav = document.querySelector("nav");
const menu = document.getElementById('menu');
const links = menu.querySelectorAll("ul li a");
const logo = document.getElementById('logo');


// EVENTOS
// Evento loader
window.addEventListener("load", function(){
  const loader = document.querySelector("#loader");
  const loader_container = document.querySelector("#loader-container");
  
  console.log('2 por uno en cabras')
  setTimeout(function() {
    console.log('AAAAAAAAAAAAAAAAAAAAAAAA')
    loader.className += " hidden";
    loader_container.className += " hidden";
  }, 800); 
});




// Evento hover links
links.forEach(link => {
  link.addEventListener('mouseover', function() {
    this.style.color = 'white';
  });
  link.addEventListener('mouseout', function() {
    if(window.scrollY > 0){
      this.style.color = 'rgb(0, 0, 40)';
    }
    else{
      this.style.color = '#fff';
    }
  });
});

// Evento Hover Img
logo.addEventListener('mouseover', function() {
  changeImage(logo,"logoFermagBlanco.png");
});
logo.addEventListener('mouseout', function() {
  if(window.scrollY > 0){
    changeImage(logo,"logoFermagColor.png");
  }
  else{
    changeImage(logo,"logoFermagBlanco.png");
  }
});

// Evento Scroll page
window.addEventListener("scroll", function() {
  if(window.scrollY > 0){
    nav.classList.toggle("scroll",true);
    changeColorLinks(true);
    console.log('aaaaaaa')
  }
  else{
    nav.classList.toggle("scroll",false);
    changeColorLinks(false);
  }
  
});  


// FUNCIONES
function changeImage(img,name_image,timeout = 0){
  setTimeout(()=>{
    img.setAttribute("src","/static/src/clientes/Fermag/"+name_image);
  },timeout);
}

function changeColorLinks(state){
  if(state){
    links.forEach(link => {
      link.style.color = 'rgb(0, 0, 40)';
    });
    changeImage(logo,"logoFermagColor.png",100);
  }
  else{
    links.forEach(link => {
      link.style.color = 'white';
    });
    changeImage(logo,"logoFermagBlanco.png",100);
  }
}








