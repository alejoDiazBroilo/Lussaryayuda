var index = 0;

    var listaimg = ["/Lussary/Lussary/static/src/clientes/Fermag/fondo1.jpg", "/Lussary/Lussary/static/src/clientes/Fermag/fondo2.jpg", "/Lussary/Lussary/static/src/clientes/Fermag/fondo3.jpg", "/Lussary/Lussary/static/src/clientes/Fermag/fondo4.jpg"];

$(function() {
  
    setInterval(changeImage, 2000);
  
});

function changeImage() {
  
 
   $('inicio-img').img("background-image", 'url(' + listaimg[index] + ')');
                  
   index++;
                  
   if(index == 4)
      index = 0;
    
    
}