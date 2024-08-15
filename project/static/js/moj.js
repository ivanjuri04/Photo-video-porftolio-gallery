document.addEventListener("DOMContentLoaded", function() {
    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function onScroll() {
        const images = document.querySelectorAll('.gallery-image-container');
        images.forEach(image => {
            if (isInViewport(image)) {
                image.classList.add('active');
            } else {
                image.classList.remove('active');
            }
        });
    }

    window.addEventListener('scroll', onScroll);
    onScroll();  // Check on page load
});
