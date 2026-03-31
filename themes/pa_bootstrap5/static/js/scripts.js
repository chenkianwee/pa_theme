// Highlight the top navbar when selected
document.addEventListener("DOMContentLoaded", function() {
    // 1. Get the current URL path (e.g., "/about.html")
    const currentPath = window.location.href;
    // 2. Select all your navbar links
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(link => {
        // 3. Get the href attribute from the link
        const linkPath = link.href;
        // 4. Check if the current URL contains the link's path
        // We check for "index.html" or "/" for the homepage specifically
        if (currentPath === linkPath) {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        } else {
            link.classList.remove('active');
        }
    });
});