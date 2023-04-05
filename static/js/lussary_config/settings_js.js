function updateTime() {
    const now = new Date();
    const clock = document.getElementById('clock');
    clock.innerText = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
  }
  
setInterval(updateTime, 1000);

window.addEventListener("scroll", function() {
  var nav = document.querySelector("nav");
  nav.classList.toggle("scroll", window.scrollY > 0);
});  

window.addEventListener("scroll", function() {
  var logo = document.querySelector(".navBar-logo");
  logo.classList.toggle("scroll", window.scrollY > 0);
});  
  