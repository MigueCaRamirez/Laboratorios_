// script14.js

// Agrega un evento al botón de menú para abrir y cerrar el menú en pantallas pequeñas
document.getElementById('nav-toggle').addEventListener('click', function() {
    document.querySelector('nav').classList.toggle('nav-open'); // Alterna la clase 'nav-open'
});