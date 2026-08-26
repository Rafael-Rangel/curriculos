var ICONS = {
  ia: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="3"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M18.4 5.6 17 7M7 17l-1.4 1.4"/></svg>',
  arch: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 20V10l8-6 8 6v10"/><path d="M9 20v-6h6v6"/></svg>',
  eng: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="4" y="5" width="16" height="14" rx="1"/><path d="M8 9h8M8 13h5"/></svg>',
  ana: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 19V5h12l4 4v10z"/><path d="M16 5v4h4M8 13h8M8 16h5"/></svg>',
  dev: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="m8 9-4 3 4 3M16 9l4 3-4 3M13 7l-2 10"/></svg>',
};

var META = {
  "engenheiro-ia": { icon: "ia", blurb: "RAG · embeddings · agents" },
  "ai-engineer": { icon: "ia", blurb: "RAG · embeddings · agents" },
  "arquiteto-software": { icon: "arch", blurb: "SaaS · escala · AWS/Azure" },
  "software-architect": { icon: "arch", blurb: "SaaS · scale · AWS/Azure" },
  "engenheiro-software-pleno": { icon: "eng", blurb: "Full stack TypeScript" },
  "software-engineer": { icon: "eng", blurb: "Full stack TypeScript" },
  "analista-sistemas": { icon: "ana", blurb: "Requisitos · processos" },
  "systems-analyst": { icon: "ana", blurb: "Requirements · processes" },
  "desenvolvedor-pleno": { icon: "dev", blurb: "React · Node · APIs" },
  "full-stack-developer": { icon: "dev", blurb: "React · Node · APIs" },
};

var langAtual = "pt-br";
var lista = [];

function boot() {
  lista = window.CATALOGO || [];
  if (!lista.length) {
    document.getElementById("tree").textContent = "Catálogo indisponível.";
    return;
  }
  document.querySelectorAll(".lang-btn").forEach(function (btn) {
    btn.addEventListener("click", function () {
      langAtual = btn.getAttribute("data-lang");
      document.querySelectorAll(".lang-btn").forEach(function (b) {
        b.classList.toggle("is-on", b === btn);
      });
      renderLista();
    });
  });
  document.getElementById("back").addEventListener("click", function () {
    document.body.classList.remove("is-preview");
  });
  renderLista();
  var hash = (location.hash || "").replace("#", "");
  var inicial = lista.find(function (i) {
    return i.id === hash;
  });
  if (inicial) {
    langAtual = inicial.lang;
    document.querySelectorAll(".lang-btn").forEach(function (b) {
      b.classList.toggle("is-on", b.getAttribute("data-lang") === langAtual);
    });
    renderLista();
    abrir(inicial);
  }
  animarEntrada();
}

function renderLista() {
  var tree = document.getElementById("tree");
  tree.innerHTML = "";
  lista
    .filter(function (i) {
      return i.lang === langAtual;
    })
    .forEach(function (item) {
      var meta = META[item.id] || { icon: "dev", blurb: item.cargo };
      var a = document.createElement("a");
      a.className = "file";
      a.href = item.html;
      a.innerHTML =
        '<span class="ico">' +
        ICONS[meta.icon] +
        "</span><span><h2>" +
        item.pasta +
        "</h2><p>" +
        meta.blurb +
        '</p></span><span class="chev">›</span>';
      a.addEventListener("click", function (ev) {
        ev.preventDefault();
        abrir(item);
      });
      tree.appendChild(a);
    });
}

function abrir(item) {
  document.querySelectorAll(".file").forEach(function (el) {
    el.classList.toggle("is-on", el.getAttribute("href") === item.html);
  });
  document.getElementById("empty").hidden = true;
  document.getElementById("empty").setAttribute("aria-hidden", "true");
  var frame = document.getElementById("frame");
  frame.hidden = false;
  frame.src = item.html;
  document.getElementById("bar-title").textContent = item.pasta + " · " + item.cargo;
  document.getElementById("actions").innerHTML =
    '<a class="ghost" href="' +
    item.html +
    '" target="_blank" rel="noopener">Abrir</a>' +
    '<a href="' +
    item.pdf +
    '" download>Baixar PDF</a>';
  document.getElementById("back").hidden = false;
  document.body.classList.add("is-preview");
  history.replaceState(null, "", "#" + item.id);
}

function animarEntrada() {
  if (!window.gsap || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  gsap.from(".top, .sidebar, .stage", {
    y: 16,
    opacity: 0,
    duration: 0.7,
    stagger: 0.08,
    ease: "power3.out",
  });
  gsap.from(".file", {
    y: 10,
    opacity: 0,
    duration: 0.45,
    stagger: 0.06,
    delay: 0.15,
    ease: "power2.out",
  });
}

boot();
