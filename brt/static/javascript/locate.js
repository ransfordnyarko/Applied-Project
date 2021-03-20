var mymap = L.map('mapid').setView([0, 0], 5);

var attribution = '&copy; <a href = "https:www.openstreetmap.org/Copyright">OpenStreetMap</a> contributors';

var titleUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var tiles = L.tileLayer(titleUrl, {attribution});
tiles.addTo(mymap);
var api_url = 'https://api.wheretheiss.at/v1/satellites/25544';