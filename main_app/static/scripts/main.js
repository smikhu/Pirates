const swiper = new Swiper('.swiper', {
    // Optional parameters
    // direction: 'vertical',
    slidesPerView: 5,
    loop: false,
    freeMode: true,
    speed: 500,
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    breakpoints: {
        // when window width is >= 1200px
        1200: {
            slidesPerView: 4,
            // spaceBetween: 8,
        },
        // when window width is >= 960px
        960: {
            slidesPerView: 3,
            // spaceBetween: 8,
        },
        // when window width is >= 720px
        720: {
            slidesPerView: 2,
            // spaceBetween: 6,
        },
        // when window width is >= 540px
        540: {
            slidesPerView: 1,
            // spaceBetween: 4,
        },
        // when window width is >= 320px
        320: {
            slidesPerView: 1,
            // spaceBetween: 2,
        },

    },

    observer: true,
    observeParents: true,

  });