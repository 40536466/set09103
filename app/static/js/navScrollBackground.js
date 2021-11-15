// Toggle navbar background on page scroll

// Variables
const nav = document.querySelector('.nav');
const navTop = nav.offsetTop;


// Toggle bg on page scroll (only non-mobile devices)
window.onscroll = () => {
  
  if (window.innerWidth > 1024) {
    if (window.pageYOffset >= navTop + 50) {
  
      nav.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
  
    } else {
  
      nav.style.backgroundColor = 'transparent';
    }
  }

}