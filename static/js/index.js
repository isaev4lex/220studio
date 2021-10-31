window.addEventListener('DOMContentLoaded', () => {
  const headerBtn = document.querySelector('.header-btn'),
    modal = document.querySelector('.modal'),
    modalOverlay = document.querySelector('.modal-overlay'),
    modalClose = document.querySelector('.modal-close'),
    modalWindow = document.querySelector('.modal-window'),
    body = document.querySelector('body'),
    mobileOverlay = document.querySelector('.mobile'),
    mobileMenu = document.querySelector('#menu'),
    mobileWindow = document.querySelector('.mobile-window'),
    mobileClose = document.querySelector('.mobile-close');

  const mobileHandler = () => {
    mobileWindow.classList.toggle('mobile-window__open');
    mobileOverlay.classList.toggle('mobile-open');
  };

  mobileMenu.addEventListener('click', () => {
    mobileHandler();
    if (!mobileMenu.classList.contains('mobile-active')) {
      mobileMenu.classList.add('mobile-active');
    } else {
      mobileMenu.classList.remove('mobile-active');
    }
  });

  mobileClose.addEventListener('click', () => {
    mobileHandler();
    if (mobileMenu.classList.contains('mobile-active')) {
      mobileMenu.classList.remove('mobile-active');
    }
  });

  mobileOverlay.addEventListener('click', (e) => {
    if (e.target.classList.contains('mobile-open')) {
      mobileHandler();
      mobileMenu.classList.remove('mobile-active');
    }
  });

  let btn = document.querySelector('#toTop');
  window.addEventListener('scroll', function () {
    // Если прокрутили дальше 599px, показываем кнопку
    if (pageYOffset > 100) {
      btn.classList.add('see');
      // Иначе прячем
    } else {
      btn.classList.remove('see');
    }
  });

  btn.onclick = function (click) {
    click.preventDefault();
    // Вызываем функцию, первый аргумент - отступ, второй - скорость скролла, чем больше значение, тем медленнее скорость прокрутки
    scrollTo(0, 400);
  };

  function scrollTo(to, duration = 700) {
    const element = document.scrollingElement || document.documentElement,
      start = element.scrollTop,
      change = to - start,
      startDate = +new Date(),
      // t = current time
      // b = start value
      // c = change in value
      // d = duration
      easeInOutQuad = function (t, b, c, d) {
        t /= d / 2;
        if (t < 1) return (c / 2) * t * t + b;
        t--;
        return (-c / 2) * (t * (t - 2) - 1) + b;
      },
      animateScroll = function () {
        const currentDate = +new Date();
        const currentTime = currentDate - startDate;
        element.scrollTop = parseInt(easeInOutQuad(currentTime, start, change, duration));
        if (currentTime < duration) {
          requestAnimationFrame(animateScroll);
        } else {
          element.scrollTop = to;
        }
      };
    animateScroll();
  }

  // Кнопка вверх при прокрутке сайта
  // $(function () {
  //   $(window).scroll(function () {
  //     if ($(this).scrollTop() != 0) {
  //       $('#toTop').fadeIn();
  //     } else {
  //       $('#toTop').fadeOut();
  //     }
  //   });
  //   $('#toTop').click(function () {
  //     $('body,html').animate({ scrollTop: 0 }, 800);
  //   });
  // });

  // Маска для input (телефонный номер)
  $(function () {
    $('#tel').mask('+(998) 77 777-77-77');
    $('#tel2').mask('+(998) 77 777-77-77');
  });

  // Мини форма: модальное окно
  function miniForm() {
    let showModal = () => {
      headerBtn.addEventListener('mousedown', (e) => {
        e.preventDefault();
        modal.classList.add('modal-show');
        body.classList.add('no-scroll');
      });
      modalOverlay.addEventListener('mousedown', () => {
        modal.classList.toggle('modal-show');
        body.classList.toggle('no-scroll');
      });
    };
    let hideModal = () => {
      modalClose.addEventListener('mousedown', () => {
        modal.classList.remove('modal-show');
        body.classList.toggle('no-scroll');
      });
    };
    modalWindow.addEventListener('mousedown', (e) => {
      e.stopPropagation();
    });
    hideModal();
    showModal();
  }

  miniForm();
});
