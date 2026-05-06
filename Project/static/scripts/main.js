// Hamburger Menu Toggle
const hamburger = document.getElementById('hamburger');
const nav = document.getElementById('nav');
const navLinks = nav.querySelectorAll('a');

// Toggle menu on hamburger click
hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('active');
  nav.classList.toggle('active');
});

// Close menu when a link is clicked
navLinks.forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('active');
    nav.classList.remove('active');
  });
});

// Close menu when clicking outside
document.addEventListener('click', (e) => {
  if (!e.target.closest('header')) {
    hamburger.classList.remove('active');
    nav.classList.remove('active');
  }
});


// apper icon toggle for password form
const icon = document.querySelector('.apper');
const passForm = document.querySelector('form.pass');

icon.addEventListener('click', () => {
  passForm.style.display = passForm.style.display === 'block' ? 'none' : 'block';
});


// document.addEventListener("click", function (e) {
//     const btn = e.target.closest(".delete-btn");

//     if (btn) {
//         const table = btn.closest(".theTable");

//         if (confirm("متأكد إنك عايز تحذف العنصر ده؟")) {
//             table.remove();
//         }
//     }
// });













const map = L.map('map').setView([30.0444,31.2357],13);

// Tile
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
  attribution:'© OpenStreetMap'
}).addTo(map);

// Marker 1
L.marker([30.0444,31.2357])
  .addTo(map)
  ;

// Marker 2
L.marker([30.0500,31.2400])
  .addTo(map)
  ;



























function openModal(place, distance){
  document.getElementById("m-name").innerText = place.name;
  document.getElementById("m-desc").innerText = place.desc;
  document.getElementById("m-distance").innerText = "المسافة: " + distance;

  document.getElementById("modal").classList.add("show");
}

function closeModal(){
  document.getElementById("modal").classList.remove("show");
}