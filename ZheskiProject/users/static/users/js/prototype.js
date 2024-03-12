// Переключение видимости всплывающего окна
function toggleModal(modalId) {
  var modal = document.getElementById(modalId);
  if (modal.style.display === "block") {
    modal.style.display = "none";
  } else {
    modal.style.display = "block";
  }
}

// Закрытие всплывающего окна при клике за его пределами
window.onclick = function(event) {
  var modals = document.getElementsByClassName("modal");
  for (var i = 0; i < modals.length; i++) {
    if (event.target == modals[i]) {
      modals[i].style.display = "none";
    }
  }
}