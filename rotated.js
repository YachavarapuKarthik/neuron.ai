const card = document.querySelector('.card');

        function clickRotate() {
            card.classList.toggle('rotated');
        }
        card.addEventListener('click', clickRotate);


        let currentSlide = 0;

        function showSlide(index) {
            const slides = document.querySelectorAll('.testimonial-slide');
            if (index >= slides.length) {
                currentSlide = 0;
            } else if (index < 0) {
                currentSlide = slides.length - 1;
            } else {
                currentSlide = index;
            }
            const offset = -currentSlide * 100;
            slides.forEach(slide => {
                slide.style.transform = `translateX(${offset}%)`;
            });
        }

        function moveSlide(step) {
            showSlide(currentSlide + step);
        }

        // Initialize the slider
        showSlide(currentSlide);
        setTimeout(showSlides, 3000);


        /*nav var*/

        // document.querySelector(".navbar")
// gsap.from(".navbar",{
//     y:70,
//     opacity:0,
//     // scale:0.7,
//     delay:0.1,
//     stagger:0.1
// })
// document.querySelector(".hero")
// gsap.from(".hero",{
//     y:70,
//     opacity:0,
//     // scale:0.7,
//     delay:0.3,
//     stagger:0.1
// })
// document.querySelector(".head1")
// gsap.from(".head1",{
//     y:70,
//     opacity:0,
//     // scale:0.7,
//     delay:0.6,
//     stagger:0.1
// })
// document.querySelector(".head2")
// gsap.from(".head2",{
//     y:70,
//     opacity:0,
//     // scale:0.7,
//     delay:0.9,
//     stagger:0.1
// })
// document.querySelector(".m1box")
// gsap.from(".m1box p",{
//     y:70,
//     opacity:0,
//     // scale:0.7,
//     delay:1.2,
//     stagger:0.1
// })
// document.querySelector(".m1box")
// gsap.from(".m1box button",{
//     y:70,
//     opacity:0,
//     // scale:0.7,
//     delay:1.5,
//     stagger:0.9
// })
// document.querySelector(".imgbox1")
// gsap.from(".imgbox1",{
//     y:70,
//     opacity:0,
//     // scale:0.7,
//     delay:1.5,
//     stagger:0.9
// })
// ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
const textSets = [
    {
        head1: "Unlock Your",
        head2: "Potential with Expert Training",
        p: "Offers Top-tier Web Development Services",
        button: "Explore Us! <i class='ri-arrow-right-line'></i>"
    },
    {
        head1: "Discover Your",
        head2: "Future with Our Courses",
        p: "Providing Exceptional Education Services",
        button: "Join Now! <i class='ri-arrow-right-line'></i>"
    }
];

let currentTextIndex = 0;

function updateTextContent() {
    const { head1, head2, p, button } = textSets[currentTextIndex];

    document.querySelector(".head1").innerHTML = head1;
    document.querySelector(".head2").innerHTML = head2;
    document.querySelector(".m1box p").innerHTML = p;
    document.querySelector(".m1box button").innerHTML = button;

    currentTextIndex = (currentTextIndex + 1) % textSets.length;
}

function animateContent() {
    const tl = gsap.timeline({ repeat: -1, repeatDelay: 1 });

    tl.fromTo(".head1", { y: 70, opacity: 0 }, { y: 0, opacity: 1, delay: 0.5, duration: 0.6, stagger: 0.1 })
        .fromTo(".head2", { y: 70, opacity: 0 }, { y: 0, opacity: 1,delay:0.6, duration: 0.5, stagger: 0.02},"-=0.9")
        .fromTo(".m1box p", { y: 70, opacity: 0 }, { y: 0, opacity: 1,delay:0.7, duration: 0.5, stagger: 0.02 },"-=0.9")
        .fromTo(".m1box button", { y: 70, opacity: 0 }, { y: 0, opacity: 1,delay:0.8, duration: 0.5, stagger: 0.02 },"-=0.9")
        .to(".head1, .head2, .m1box p, .m1box button", { y: 70, opacity: 0, stagger: 0.1, delay: 5, onComplete: updateTextContent });

    // Initial content setup
    updateTextContent();
}

document.addEventListener("DOMContentLoaded", () => {
    animateContent();
});

document.querySelector(".navbar")
gsap.from(".navbar", {
    y: 70,
    opacity: 0,
    delay: 0.1,
    stagger: 0.1
});

document.querySelector(".hero")
gsap.from(".hero", {
    y: 70,
    opacity: 0,
    delay: 0.3,
    stagger: 0.1
});
document.querySelector(".wave-svg")
gsap.from(".wave-svg", {
    y: 70,
    opacity: 0,
    delay: 0.3,
    stagger: 0.1
});



function toggleMenu() {
    const mobileMenu = document.getElementById('mobileMenu');
    mobileMenu.classList.toggle('show');
}

/*ourstory*/

function toggleMenu() {
    var mobileMenu = document.getElementById('mobileMenu');
    if (mobileMenu.classList.contains('show')) {
        mobileMenu.classList.remove('show');
    } else {
        mobileMenu.classList.add('show');
    }
}

/*webdev*/


