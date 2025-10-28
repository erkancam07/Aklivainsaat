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
  const format = el.dataset.format;
  const span = el.querySelector(".say-deger");

  let metin = "";

  if (format === "percent") {
    metin = `%${deger} Memnuniyet`;
  } else if (format === "plus-year") {
    metin = `${deger}+Yıl`;
  } else if (format === "plus") {
    metin = `${deger}+`;
  } else if (format === "plus-calisan") {
    metin = `${deger}+ Çalışan`;
  } else {
    metin = `${deger}`;
  }

  if (span) {
    span.textContent = metin;
  } else {
    el.textContent = metin;
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
