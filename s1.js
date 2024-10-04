document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;

    function showNextSlide() {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
    }

    setInterval(showNextSlide, 3000); // Change slide every 3 seconds

    // Mobile menu toggle
    const menuIcon = document.querySelector('.menu-icon');
    const links = document.querySelector('.links');

    menuIcon.addEventListener('click', () => {
        links.classList.toggle('active');
    });
});


