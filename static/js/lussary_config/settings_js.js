function updateTime() {
  const now = new Date();
  const clock = document.getElementById('clock');
  if (clock !== null) {
    clock.innerText = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
  }
}
  
