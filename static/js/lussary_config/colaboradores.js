var content = document.getElementById("content");
var center_content = document.getElementById("centro_content")
var difuminado = document.getElementById("difuminado")


center_content.addEventListener('mouseover', function() {
  difuminado.style.backdropFilter = "blur(0)"
});
center_content.addEventListener('mouseout', function() {
  difuminado.style.backdropFilter = "blur(2px)"
}); /* */


setTimeout(() => {
    content.className = "content";
    console.log('Colaboradores')
  }, "200");

  







