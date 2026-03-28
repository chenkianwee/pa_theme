document.addEventListener("DOMContentLoaded", function() {
    // 1. Get the current URL path (e.g., "/about.html")
    const currentPath = window.location.pathname;

    // 2. Select all your navbar links
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    console.log(currentPath);
    navLinks.forEach(link => {
        // 3. Get the href attribute from the link
        const linkPath = link.getAttribute('href');
        console.log(linkPath);
        // 4. Check if the current URL contains the link's path
        // We check for "index.html" or "/" for the homepage specifically
        if (currentPath === linkPath || (currentPath === '/' && linkPath.includes('index.html'))) {
            link.classList.add('active');
            link.setAttribute('aria-current', 'page');
        } else {
            link.classList.remove('active');
        }
    });
});