document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (toggleBtn && navLinks) {
        toggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            navLinks.classList.toggle('mobile-active');
            // Toggle icon from hamburger to close
            if (navLinks.classList.contains('mobile-active')) {
                toggleBtn.innerHTML = '✕';
            } else {
                toggleBtn.innerHTML = '☰';
            }
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (navLinks.classList.contains('mobile-active') && !navLinks.contains(e.target) && e.target !== toggleBtn) {
                navLinks.classList.remove('mobile-active');
                toggleBtn.innerHTML = '☰';
            }
        });
        
        // Close menu when clicking a link
        const links = navLinks.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('mobile-active');
                toggleBtn.innerHTML = '☰';
            });
        });
    }
});
