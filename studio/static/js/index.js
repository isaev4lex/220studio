window.addEventListener('DOMContentLoaded', () => {
  const headerBtn = document.querySelector('.header-btn'),
    modal = document.querySelector('.modal'),
    modalOverlay = document.querySelector('.modal-overlay'),
    modalClose = document.querySelector('.modal-close'),
    modalWindow = document.querySelector('.modal-window'),
    body = document.querySelector('body'),
    stepsAcc = document.querySelectorAll('.steps-accordion'),
    mobileAcc = document.querySelectorAll('.mobile-services-title'),
    deactive = document.querySelectorAll('.deactivate');

  deactive.forEach((item) => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
    });
  });

  const mobileWindow = document.querySelector('.mobile-window');
  const mobileServices = document.querySelector('.mobile-services');
  const mobServicesButton = document.querySelector('.__services');
  const mobMenuButton = document.querySelector('.__menu');

  const mobileMenu = document.querySelector('.mobile-menu');
  const mobileClose = document.querySelectorAll('.mobile-close');

  mobileClose.forEach((item) => {
    item.addEventListener('click', () => {
      if (mobileWindow.classList.contains('mobile-window-show')) {
        mobileWindow.classList.remove('mobile-window-show');
        mobServicesButton.classList.remove('mobile-active');
        mobMenuButton.classList.remove('mobile-active');
      }
      if (mobileServices.classList.contains('mobile-services-show')) {
        mobileServices.classList.remove('mobile-services-show');
        mobServicesButton.classList.remove('mobile-active');
        mobMenuButton.classList.remove('mobile-active');
      }
      if (mobileMenu.classList.contains('mobile-menu-show')) {
        mobileMenu.classList.remove('mobile-menu-show');
        mobServicesButton.classList.remove('mobile-active');
        mobMenuButton.classList.remove('mobile-active');
      }
    });
  });

  mobServicesButton.addEventListener('click', (e) => {
    e.preventDefault();
    if (mobileMenu.classList.contains('mobile-menu-show')) {
      mobileMenu.classList.remove('mobile-menu-show');
      mobileWindow.classList.add('mobile-window-show');
      mobileServices.classList.add('mobile-services-show');
      mobMenuButton.classList.remove('mobile-active');
      mobServicesButton.classList.add('mobile-active');
    } else {
      if (
        mobileWindow.classList.contains('mobile-window-show') &&
        mobileServices.classList.contains('mobile-services-show')
      ) {
        mobileWindow.classList.remove('mobile-window-show');
        mobileServices.classList.remove('mobile-services-show');
        mobServicesButton.classList.remove('mobile-active');
      } else {
        mobileWindow.classList.add('mobile-window-show');
        mobileServices.classList.add('mobile-services-show');
        mobServicesButton.classList.add('mobile-active');
      }
    }
  });

  mobMenuButton.addEventListener('click', (e) => {
    e.preventDefault();
    if (mobileServices.classList.contains('mobile-services-show')) {
      mobileServices.classList.remove('mobile-services-show');
      mobileWindow.classList.add('mobile-window-show');
      mobileMenu.classList.add('mobile-menu-show');
      mobServicesButton.classList.remove('mobile-active');
      mobMenuButton.classList.add('mobile-active');
    } else {
      if (
        mobileWindow.classList.contains('mobile-window-show') &&
        mobileMenu.classList.contains('mobile-menu-show')
      ) {
        mobileWindow.classList.remove('mobile-window-show');
        mobileMenu.classList.remove('mobile-menu-show');
        mobMenuButton.classList.remove('mobile-active');
      } else {
        mobileWindow.classList.add('mobile-window-show');
        mobileMenu.classList.add('mobile-menu-show');
        mobMenuButton.classList.add('mobile-active');
      }
    }
  });

  //Моб аккордеон
  mobileAcc.forEach((item) => {
    item.addEventListener('click', (e) => {
      const mobileText = item.nextElementSibling;
      if (mobileText.style.maxHeight) {
        mobileText.style.maxHeight = null;
      } else {
        mobileText.style.maxHeight = mobileText.scrollHeight + 'px';
      }
    });
  });

  // Аккордеон
  stepsAcc.forEach((item) => {
    item.addEventListener('click', () => {
      const stepsText = item.previousElementSibling;
      if (stepsText.style.maxHeight) {
        stepsText.style.maxHeight = null;
        item.innerHTML = 'Подробнее...';
      } else {
        stepsText.style.maxHeight = stepsText.scrollHeight + 'px';
        item.innerHTML = 'Скрыть';
      }
    });
  });

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

  // Smooth scroll
  const anchors = document.querySelectorAll('a[href*="#"]');

  anchors.forEach((item) => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const blockID = item.getAttribute('href');
      document.querySelector('' + blockID).scrollIntoView({
        behavior: 'smooth',
        block: 'start',
      });
    });
  });
});
