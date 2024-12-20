function carousel() {
    const carouselImages = document.querySelector('.carousel-images');
    const images = document.querySelectorAll('.carousel-images img');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    let currentIndex = 0;

    if (images.length === 1 || images.length === 0) {
        prevBtn.style.display = 'none';
        nextBtn.style.display = 'none';
    }

    function updateCarousel() {
        const offset = -currentIndex * 100;
        carouselImages.style.transform = `translateX(${offset}%)`;
    }

    prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateCarousel();
    });

    nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % images.length;
        updateCarousel();
    });
}
document.addEventListener('DOMContentLoaded', carousel);