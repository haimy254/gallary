$(document).ready(function () {
  var imageCards = document.querySelectorAll(".image-card");

  for (var i = 0; i < imageCards.length; i++) {
    imageCards[i].addEventListener("click", function (e) {
      var title = this.querySelector(".card-title").textContent;
    });
  }
});
