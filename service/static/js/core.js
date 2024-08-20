// Manejo del toggle del sidebar
document.getElementById('toggleSidebar').addEventListener('click', function () {
    var sidebar = document.getElementById('sidebar');
    if (sidebar.style.display === 'none') {
        sidebar.style.display = 'block';
    } else {
        sidebar.style.display = 'none';
    }
});

// Manejo del cambio de tema
const themeToggle = document.getElementById('themeToggle');
const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");

themeToggle.addEventListener('change', function() {
    if (themeToggle.checked) {
        document.body.classList.add('dark-theme');
        document.body.classList.remove('light-theme');
    } else {
        document.body.classList.add('light-theme');
        document.body.classList.remove('dark-theme');
    }
});

// Inicialización del tema basado en la preferencia del usuario
if (prefersDarkScheme.matches) {
    document.body.classList.add('dark-theme');
    themeToggle.checked = true;
} else {
    document.body.classList.add('light-theme');
}
