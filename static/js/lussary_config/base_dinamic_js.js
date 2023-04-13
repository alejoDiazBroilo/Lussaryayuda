setInterval(updateTime, 1000);

window.addEventListener("scroll", function() {
  var nav = document.querySelector("nav");
  nav.classList.toggle("scroll", window.scrollY > 0);
});  

window.addEventListener("scroll", function() {
  var logo = document.querySelector(".navBar-logo");
  logo.classList.toggle("scroll", window.scrollY > 0);
});  

window.addEventListener("load", function(){
  const loader = document.querySelector("#loader-container");
  setTimeout(function() {
    loader.className += " hidden";
  }, 800); // espera 2 segundos antes de ocultar la pantalla de carga
});
  