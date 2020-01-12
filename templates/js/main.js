var slideIndex;

var slides = document.getElementsByClassName("item");
var dots = document.getElementsByClassName("dot");

function showSlides() {
    var i;

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
    if (w <= 850) {
        showOneSlide(slideIndex = n)
    } else {
        showSlides(slideIndex = n);
    }
}

//reponsive small device 

var w = window.innerWidth

if (w <= 850) {
    for (i = 0; i < slides.length; i++) {
        slides[i].style.width = "100%";
        slides[i].style.display = "none";
        dots[i].style.display = "inline-block";
    }
    slides[0].style.display = "block";
}

function showOneSlide() {
    var i;

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }

    slides[slideIndex].style.display = "block";
    dots[slideIndex].className += " active";
}