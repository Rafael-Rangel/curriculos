(function aplicarDados() {
  var d = window.CV_DADOS || {};

  document.querySelectorAll("[data-cv]").forEach(function (el) {
    var key = el.getAttribute("data-cv");
    var value = d[key];
    if (value == null || value === "") return;

    if (el.tagName === "A") {
      el.textContent = value;
      if (key === "email") el.setAttribute("href", "mailto:" + d.email);
      if (key === "linkedin") el.setAttribute("href", d.linkedinUrl || "#");
      if (key === "github") el.setAttribute("href", d.githubUrl || "#");
      if (key === "portfolio" && d.portfolioUrl) el.setAttribute("href", d.portfolioUrl);
      if (key === "telefone") {
        var tel = String(d.telefone).replace(/\D/g, "");
        el.setAttribute("href", "tel:+55" + tel);
      }
      return;
    }

    el.textContent = value;
  });

  document.querySelectorAll("[data-cv-hide-empty]").forEach(function (block) {
    var key = block.getAttribute("data-cv-hide-empty");
    if (!d[key]) block.style.display = "none";
  });

  var sep = document.querySelector("[data-cv-portfolio-sep]");
  if (sep && !d.portfolio) sep.style.display = "none";

  var modelo = document.body && document.body.getAttribute("data-modelo");
  if (d.nome) {
    document.title = d.nome + (modelo ? " — " + modelo : " — Currículo");
  }
})();
