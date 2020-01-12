var slideIndex;

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("item");
    var dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }

    slides[2 * slideIndex].style.display = "block";
    slides[2 * slideIndex + 1].style.display = "block";
    dots[slideIndex].className += " active";
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}