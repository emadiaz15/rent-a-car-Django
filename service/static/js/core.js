document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('theme-toggle');
    const logoDark = document.getElementById('logo-dark');
    const logoLight = document.getElementById('logo-light');
    const siteHeader = document.getElementById('site-header');
    const siteFooter = document.getElementById('site-footer');
    const siteNavbar = document.getElementById('site-navbar');
    const sidebar = document.getElementById('site-sidebar');  // Asegúrate de tener este ID en el sidebar

    // Función para aplicar el tema
    function applyTheme(theme) {
        document.body.classList.remove('light', 'dark');
        document.body.classList.add(theme);
        localStorage.setItem('theme', theme);

        if (theme === 'dark') {
            // Header
            siteHeader.classList.add('navbar-dark', 'bg-dark');
            siteHeader.classList.remove('navbar-light', 'bg-light');
            // Footer
            siteFooter.classList.add('bg-dark', 'text-light');
            siteFooter.classList.remove('bg-light', 'text-dark');
            // Sidebar
            sidebar.classList.add('bg-dark', 'text-light');
            sidebar.classList.remove('bg-light', 'text-dark');
            // Navbar
            siteNavbar.classList.add('navbar-dark', 'bg-dark');
            siteNavbar.classList.remove('navbar-light', 'bg-light');
            // Logos
            logoDark.style.opacity = '1';
            logoLight.style.opacity = '0.5';
            toggleButton.checked = true;
        } else {
            // Header
            siteHeader.classList.add('navbar-light', 'bg-light');
            siteHeader.classList.remove('navbar-dark', 'bg-dark');
            // Footer
            siteFooter.classList.add('bg-light', 'text-dark');
            siteFooter.classList.remove('bg-dark', 'text-light');
            // Sidebar
            sidebar.classList.add('bg-light', 'text-dark');
            sidebar.classList.remove('bg-dark', 'text-light');
            // Navbar
            siteNavbar.classList.add('navbar-light', 'bg-light');
            siteNavbar.classList.remove('navbar-dark', 'bg-dark');
            // Logos
            logoDark.style.opacity = '0.5';
            logoLight.style.opacity = '1';
            toggleButton.checked = false;
        }
    }

    // Detectar el tema preferido del navegador
    const preferredTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    const savedTheme = localStorage.getItem('theme') || preferredTheme;

    // Aplicar el tema guardado o el tema preferido por el navegador
    applyTheme(savedTheme);

    // Cambiar el tema al alternar el interruptor
    toggleButton.addEventListener('change', function () {
        const newTheme = toggleButton.checked ? 'dark' : 'light';
        applyTheme(newTheme);
    });

    // Cambiar el tema también al hacer clic en el logo opuesto
    logoDark.addEventListener('click', function () {
        applyTheme('dark');
    });

    logoLight.addEventListener('click', function () {
        applyTheme('light');
    });
});
