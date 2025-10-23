document.addEventListener("DOMContentLoaded", function () {
  const bolumler = document.querySelectorAll(".anim-sol, .anim-sag");

  const observer = new IntersectionObserver((girisler) => {
    girisler.forEach(giris => {
      if (giris.isIntersecting) {
        giris.target.classList.add("aktif");

        // İçindeki metinleri tetikle
        const metinler = giris.target.querySelectorAll(".anim-giris");
        metinler.forEach(m => m.classList.add("aktif"));
      }
    });
  }, {
    threshold: 0.2
  });

  bolumler.forEach(bolum => observer.observe(bolum));
});


document.addEventListener("DOMContentLoaded", function () {
  const sayilar = document.querySelectorAll(".say-anim");

  const observer = new IntersectionObserver((girisler) => {
    girisler.forEach(giris => {
      if (giris.isIntersecting) {
        const el = giris.target;
        const hedef = parseInt(el.dataset.hedef);
        let baslangic = 0;
        const sure = 1500; // ms
        const basla = performance.now();

        function saydir(t) {
          const ilerleme = Math.min((t - basla) / sure, 1);
          const deger = Math.floor(ilerleme * hedef);
          if (el.textContent.includes("%")) {
            el.textContent = `%${deger}`;
          } else if (el.textContent.includes("+")) {
            el.textContent = `${deger}+Yıl`;
          } else {
            el.textContent = `${deger}`;
          }
          if (ilerleme < 1) requestAnimationFrame(saydir);
        }

        requestAnimationFrame(saydir);
        observer.unobserve(el); // tekrar tetiklenmesin
      }
    });
  }, {
    threshold: 0.5
  });

  sayilar.forEach(s => observer.observe(s));
});
