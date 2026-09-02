/* OpenEndo — mobil navigation + a11y-hjælpere */
(function () {
  "use strict";

  var toggle = document.getElementById("nav-toggle");
  var mobileNav = document.getElementById("mobile-nav");
  var skipTarget = document.getElementById("main");

  // skip-link-mål: hvis main ikke har id, sæt det
  if (!skipTarget) {
    var main = document.querySelector("main");
    if (main) { main.id = "main"; skipTarget = main; }
  }

  // Byg mobil-menu fra de eksisterende nav-links (én kilde til sandheden)
  if (toggle && mobileNav) {
    var links = document.querySelector(".nav-links");
    if (links) {
      links.querySelectorAll("a").forEach(function (a) {
        var clone = a.cloneNode(true);
        mobileNav.appendChild(clone);
      });
    }

    function setOpen(open) {
      mobileNav.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Menu");
    }

    toggle.addEventListener("click", function () {
      setOpen(!mobileNav.classList.contains("open"));
    });

    // Luk ved klik på et link, Escape, eller klik udenfor
    mobileNav.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });
    document.addEventListener("click", function (e) {
      if (mobileNav.classList.contains("open") && !e.target.closest(".nav") && !e.target.closest("#mobile-nav")) {
        setOpen(false);
      }
    });

    // Gen-klon ved sprogskifte (data-i18n opdateres i app.js)
    if (window.__endoNavRebuild) return;
    window.__endoNavRebuild = setOpen;
  }
})();
