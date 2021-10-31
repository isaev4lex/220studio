window.addEventListener('DOMContentLoaded', () => {
  const acc = document.querySelectorAll('.accordion_title'),
    tabs = document.querySelectorAll('.tab_header'),
    tabsContent = document.querySelectorAll('.tab_content'),
    tabsParent = document.querySelector('.tab_headers');

  // Таб
  function hideTabContent() {
    tabsContent.forEach((item) => {
      item.classList.add('tab_hide');
      item.classList.remove('tab_show', 'fade');
    });
    tabs.forEach((item) => {
      item.classList.remove('tab_header__active');
    });
  }
  function showTabContent(i = 0) {
    tabsContent[i].classList.add('tab_show', 'fade');
    tabsContent[i].classList.remove('tab_hide');
    tabs[i].classList.add('tab_header__active');
  }
  hideTabContent();
  showTabContent();
  tabsParent.addEventListener('click', (event) => {
    const target = event.target;
    if (target && target.classList.contains('tab_header')) {
      tabs.forEach((item, i) => {
        if (target == item) {
          hideTabContent();
          showTabContent(i);
        }
      });
    }
  });

  // Аккордеон
  for (let i = 0; i < acc.length; i++) {
    acc[i].addEventListener('click', function () {
      this.classList.toggle('accordion_rotate');
      const panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
      } else {
        panel.style.maxHeight = panel.scrollHeight + 'px';
      }
    });
  }
});
