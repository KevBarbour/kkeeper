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
function toggleDivs(idToShow){
    document.getElementById("diamonds").style.display = 'none';
    document.getElementById("hearts").style.display = 'none';
    document.getElementById("clubs").style.display = 'none';
    document.getElementById("spades").style.display = 'none';
    document.getElementById(idToShow).style.display = 'block';
}
