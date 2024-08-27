document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.body.classList.add(currentTheme);

    toggleButton.textContent = currentTheme === 'dark' ? 'Tema Claro' : 'Tema Oscuro';

    toggleButton.addEventListener('click', function () {
        const newTheme = document.body.classList.contains('light') ? 'dark' : 'light';
        document.body.classList.remove('light', 'dark');
        document.body.classList.add(newTheme);
        localStorage.setItem('theme', newTheme);
        toggleButton.textContent = newTheme === 'dark' ? 'Tema Claro' : 'Tema Oscuro';
    });
});