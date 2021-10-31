window.addEventListener('DOMContentLoaded', () => {
  // const swiper = new Swiper('.swiper-container-case', {
  //   direction: 'horizontal',
  //   loop: true,
  //   centerInsufficientSlides: true,
  //   slidesPerView: 1,

  //   autoplay: {
  //     delay: 3000,
  //   },

  //   pagination: {
  //     el: '.swiper-pagination-case',
  //     bulletClass: 'dots',
  //     bulletActiveClass: 'dots-active',
  //     clickable: 'true',
  //   },
  // });

  // Эффект hover для 'Топ Услуги'
  $(function () {
    $('.services-card')
      .on('mouseenter', function (e) {
        var parentOffset = $(this).offset(),
          relX = e.pageX - parentOffset.left,
          relY = e.pageY - parentOffset.top;
        $(this).find('span').css({ top: relY, left: relX });
      })
      .on('mouseout', function (e) {
        var parentOffset = $(this).offset(),
          relX = e.pageX - parentOffset.left,
          relY = e.pageY - parentOffset.top;
        $(this).find('span').css({ top: relY, left: relX });
      });
  });

  // Эффект hover для 'Effect'
  $(function () {
    $('.effect')
      .on('mouseenter', function (e) {
        var parentOffset = $(this).offset(),
          relX = e.pageX - parentOffset.left,
          relY = e.pageY - parentOffset.top;
        $(this).find('span').css({ top: relY, left: relX });
      })
      .on('mouseout', function (e) {
        var parentOffset = $(this).offset(),
          relX = e.pageX - parentOffset.left,
          relY = e.pageY - parentOffset.top;
        $(this).find('span').css({ top: relY, left: relX });
      });
  });
});
