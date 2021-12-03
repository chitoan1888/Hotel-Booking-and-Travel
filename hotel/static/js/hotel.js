(function ($) {
    'use strict';
    // aos
    AOS.init({
        duration: 1000
    });

    // home slider
    $('.home-slider').owlCarousel({
        loop: true,
        autoplay: true,
        margin: 10,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        nav: true,
        autoplayHoverPause: true,
        items: 1,
        autoheight: true,
        navText: ["<span class='ion-chevron-left'></span>", "<span class='ion-chevron-right'></span>"],
        responsive: {
            0: {
                items: 1,
                nav: false
            },
            600: {
                items: 1,
                nav: false
            },
            1000: {
                items: 1,
                nav: true
            }
        }
    });

    // owl carousel
    var majorCarousel = $('.js-carousel-1');
    majorCarousel.owlCarousel({
        loop: true,
        autoplay: true,
        stagePadding: 7,
        margin: 20,
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        nav: true,
        autoplayHoverPause: true,
        items: 3,
        navText: ["<span class='ion-chevron-left'></span>", "<span class='ion-chevron-right'></span>"],
        responsive: {
            0: {
                items: 1,
                nav: false
            },
            600: {
                items: 2,
                nav: false
            },
            1000: {
                items: 3,
                nav: true,
                loop: false
            }
        }
    });

    // owl carousel
    var major2Carousel = $('.js-carousel-2');
    major2Carousel.owlCarousel({
        loop: true,
        autoplay: true,
        stagePadding: 7,
        margin: 20,
        // animateOut: 'fadeOut',
        // animateIn: 'fadeIn',
        nav: true,
        autoplayHoverPause: true,
        autoHeight: true,
        items: 3,
        navText: ["<span class='ion-chevron-left'></span>", "<span class='ion-chevron-right'></span>"],
        responsive: {
            0: {
                items: 1,
                nav: false
            },
            600: {
                items: 2,
                nav: false
            },
            1000: {
                items: 3,
                dots: true,
                nav: true,
                loop: false
            }
        }
    });

    var siteStellar = function () {
        $(window).stellar({
            responsive: false,
            parallaxBackgrounds: true,
            parallaxElements: true,
            horizontalScrolling: false,
            hideDistantElements: false,
            scrollProperty: 'scroll'
        });
    }
    siteStellar();
})(jQuery);