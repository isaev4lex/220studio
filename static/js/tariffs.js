window.addEventListener('DOMContentLoaded', () => {
  const cardTitle = document.querySelectorAll('.page-card-block'),
    cardSubBlock = document.querySelectorAll('.page-card-subblock'),
    cardIcon = document.querySelectorAll('.page-card-icon'),
    cardClose = document.querySelectorAll('.page-card-close');

  // Аккордеон
  for (let i = 0; i < cardTitle.length; i++) {
    cardTitle[i].addEventListener('click', function () {
      const block = this.nextElementSibling;
      if (block.style.maxHeight) {
        block.style.maxHeight = null;
        block.style.marginBottom = null;
      } else {
        block.style.maxHeight = block.scrollHeight + 'px';
        block.style.marginBottom = 34 + 'px';
      }
    });
  }

  cardTitle.forEach((item, i) => {
    item.addEventListener('click', () => {
      cardClose[i].classList.toggle('card-rotate');
    });
  });
});
