$(document).ready(function () {
  var imageCards = document.querySelectorAll(".image-card");

  for (var i = 0; i < imageCards.length; i++) {
    imageCards[i].addEventListener("click", function (e) {
      var title = this.querySelector(".card-title").textContent;
      var description = this.querySelector(".card-text").textContent;
      var location = this.querySelector("#card-subtext").textContent;
      var thumbnailUrl =
        this.querySelector(".card-img-top").getAttribute("src");

      //setting of overlay items
      var img = document.getElementById("image-details-img");
      img.setAttribute("src", thumbnailUrl);

      var imgDetailsName = document.getElementById("image-details-name");
      imgDetailsName.textContent = title;

      var imgDetailsDescription = document.getElementById(
        "image-details-description"
      );
      imgDetailsDescription.textContent = description;

      var imgDetailsLocation = document.getElementById(
        "image-details-location"
      );
      imgDetailsLocation.textContent = location;

      //show the overlay
      var imgDetailsOverlay = document.getElementById("image-details-overlay");
      imgDetailsOverlay.classList.remove("hide");
    });
  }

  var closebtn = document.getElementById("close-btn");
  closebtn.addEventListener("click", function () {
    var imgDetailsOverlay = document.getElementById("image-details-overlay");
    imgDetailsOverlay.classList.add("hide");
  });

  //copy functionality

  function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();

    return true;
  }

  var copyBtns = document.querySelectorAll(".copy-btn");
  for (var i = 0; i < copyBtns.length; i++) {
    copyBtns[i].addEventListener("click", function (e) {
      var imgDetailsOverlay = document.getElementById("image-details-overlay");
      imgDetailsOverlay.classList.add("hide");

      if (copyToClipboard(this.parentNode.querySelector(".copy-target"))) {
        this.innerHTML = "copied";

        setTimeout(function () {
          e.target.innerHTML = "copy link";
        }, 2000);
        alert("copied")
      }
    });
  }
});
