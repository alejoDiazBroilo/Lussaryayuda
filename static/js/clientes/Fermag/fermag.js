window.addEventListener("scroll", function() {
    var nav = document.querySelector("nav");
    nav.classList.toggle("scroll", window.scrollY > 0);
  });  