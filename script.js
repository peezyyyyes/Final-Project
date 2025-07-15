document.addEventListener('DOMContentLoaded', () => {
    const categoryCards = document.querySelectorAll('.category-card');
    const ctaButton = document.querySelector('.cta-button');
  
    categoryCards.forEach(card => {
      card.addEventListener('mouseenter', () => {
        card.style.transform = 'scale(1.05) rotate(2deg)';
      });
  
      card.addEventListener('mouseleave', () => {
        card.style.transform = 'scale(1) rotate(0deg)';
      });
    });
  
    ctaButton.addEventListener('mouseenter', () => {
      ctaButton.style.animation = 'pulse 1s infinite';
    });
  
    ctaButton.addEventListener('mouseleave', () => {
      ctaButton.style.animation = 'none';
    });
  });
  