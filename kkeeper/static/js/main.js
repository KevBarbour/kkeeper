function initMap() {
  var uluru = {lat: 53.278316, lng: -110.005493};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 6,
    center: uluru
  });
  var marker = new google.maps.Marker({
    position: uluru,
    map: map
  });

}

// Card Navigation Bar

function dhide() {
    var x = document.getElementById("diamonds");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
function chide() {
    var x = document.getElementById("clubs");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
function hhide() {
    var x = document.getElementById("hearts");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
function shide() {
    var x = document.getElementById("spades");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}