(function () {
  "use strict";

  // Menú móvil
  var toggle = document.querySelector(".nav-toggle");
  var mobileNav = document.getElementById("mobile-nav");
  if (toggle && mobileNav) {
    toggle.addEventListener("click", function () {
      var isOpen = mobileNav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });
  }

  // Banner de cookies (placeholder simple; sustituir por un CMP certificado
  // por Google antes de servir anuncios de AdSense en producción).
  var CONSENT_KEY = "autoconsumopro_cookie_consent";
  var banner = document.getElementById("cookie-banner");
  var acceptBtn = document.getElementById("cookie-accept");
  var rejectBtn = document.getElementById("cookie-reject");

  function getConsent() {
    try {
      return window.localStorage.getItem(CONSENT_KEY);
    } catch (e) {
      return null;
    }
  }

  function setConsent(value) {
    try {
      window.localStorage.setItem(CONSENT_KEY, value);
    } catch (e) {
      /* localStorage no disponible: no persistimos, el banner reaparecerá */
    }
    if (banner) banner.hidden = true;
  }

  if (banner && !getConsent()) {
    banner.hidden = false;
  }
  if (acceptBtn) acceptBtn.addEventListener("click", function () { setConsent("accepted"); });
  if (rejectBtn) rejectBtn.addEventListener("click", function () { setConsent("rejected"); });
})();
