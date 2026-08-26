"""Gera HTML + PDF de todas as versões e o catálogo da interface."""

from __future__ import annotations

import html
import json
from pathlib import Path

from reportlab.lib.colors import black, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from catalogo import CERTS_EN, CERTS_PT, CONTATO, FORMACAO_EN, FORMACAO_PT, VERSOES

ROOT = Path(__file__).resolve().parent
FONTS = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("Calibri", str(FONTS / "calibri.ttf")))
pdfmetrics.registerFont(TTFont("Calibri-Bold", str(FONTS / "calibrib.ttf")))
pdfmetrics.registerFontFamily("Calibri", normal="Calibri", bold="Calibri-Bold")

FONT = "Calibri"
FONT_BOLD = "Calibri-Bold"
SIZE = 10.5
LEADING = 13.6


def S(name, **kwargs):
    base = dict(
        fontName=FONT,
        fontSize=SIZE,
        leading=LEADING,
        textColor=black,
        spaceBefore=0,
        spaceAfter=0,
    )
    base.update(kwargs)
    return ParagraphStyle(name, **base)


def bullets(texts, item_style):
    return ListFlowable(
        [
            ListItem(Paragraph(t, item_style), leftIndent=8, bulletColor=black)
            for t in texts
        ],
        bulletType="bullet",
        bulletFontName=FONT,
        bulletFontSize=SIZE,
        leftIndent=12,
        spaceBefore=1,
        spaceAfter=3,
    )


def secao(titulo, style):
    return KeepTogether(
        [
            Paragraph(titulo, style),
            HRFlowable(width="100%", thickness=0.7, color=black, spaceBefore=1, spaceAfter=4),
        ]
    )


def timeline_job(job, styles):
    data = [
        [Paragraph(job["periodo"], styles["data"]), Paragraph(job["cargo"], styles["cargo"])],
        ["", Paragraph(job["empresa"], styles["empresa"])],
    ]
    head = Table(data, colWidths=[3.5 * cm, 12.2 * cm])
    head.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("BACKGROUND", (0, 0), (-1, -1), white),
                ("LINEBEFORE", (0, 0), (0, -1), 1, black),
                ("LEFTPADDING", (0, 0), (0, -1), 7),
            ]
        )
    )
    body = Table([["", bullets(job["itens"], styles["item"])]], colWidths=[3.5 * cm, 12.2 * cm])
    body.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LINEBEFORE", (0, 0), (0, -1), 1, black),
                ("LEFTPADDING", (0, 0), (0, -1), 7),
            ]
        )
    )
    return KeepTogether([head, body, Spacer(1, 3)])


def pasta_versao(v):
    return ROOT / "versoes" / v["lang"] / v["id"]


def labels(lang):
    if lang == "en":
        return {
            "resumo": "SUMMARY",
            "exp": "EXPERIENCE",
            "proj": "FEATURED PROJECTS",
            "form": "EDUCATION",
            "cert": "CERTIFICATES",
            "skill": "TECHNICAL SKILLS",
            "print": "Print / Save PDF",
            "back": "All resumes",
        }
    return {
        "resumo": "RESUMO",
        "exp": "EXPERIÊNCIA PROFISSIONAL",
        "proj": "PROJETOS EM DESTAQUE",
        "form": "FORMAÇÃO",
        "cert": "CERTIFICADOS",
        "skill": "COMPETÊNCIAS TÉCNICAS",
        "print": "Imprimir / Salvar PDF",
        "back": "Todos os currículos",
    }


def gerar_pdf(v, out: Path):
    L = labels(v["lang"])
    formacao = FORMACAO_EN if v["lang"] == "en" else FORMACAO_PT
    certs = CERTS_EN if v["lang"] == "en" else CERTS_PT
    cidade = CONTATO["cidade_en"] if v["lang"] == "en" else CONTATO["cidade_pt"]

    styles = {
        "nome": S("nome", fontName=FONT_BOLD, fontSize=13.5, leading=16, alignment=TA_CENTER, spaceAfter=1),
        "headline": S("headline", alignment=TA_CENTER, fontSize=10, leading=13, spaceAfter=2),
        "contato": S("contato", alignment=TA_CENTER, fontSize=9.5, leading=12.5, spaceAfter=6),
        "secao": S("secao", fontName=FONT_BOLD, fontSize=10.5, leading=13),
        "resumo": S("resumo", alignment=TA_JUSTIFY, spaceAfter=3),
        "data": S("data", fontName=FONT_BOLD, fontSize=9, leading=12),
        "cargo": S("cargo", fontName=FONT_BOLD),
        "empresa": S("empresa", spaceAfter=1),
        "item": S("item", alignment=TA_JUSTIFY, leading=13),
        "proj": S("proj", alignment=TA_LEFT, spaceAfter=1),
        "desc": S("desc", alignment=TA_JUSTIFY, spaceAfter=3),
        "cert": S("cert", leading=12.8, spaceAfter=2),
        "skill": S("skill", leading=13),
    }

    story = [
        Paragraph(CONTATO["nome"].upper(), styles["nome"]),
        Paragraph(v["cargo"], styles["headline"]),
        Paragraph(v["headline"], styles["headline"]),
        Paragraph(
            f"{cidade} · {CONTATO['telefone']} · "
            f'<link href="mailto:{CONTATO["email"]}" color="black">{CONTATO["email"]}</link><br/>'
            f'<link href="{CONTATO["github_url"]}" color="black"><u>{CONTATO["github"]}</u></link> · '
            f'<link href="{CONTATO["portfolio_url"]}" color="black"><u>{CONTATO["portfolio"]}</u></link>',
            styles["contato"],
        ),
        secao(L["resumo"], styles["secao"]),
        Paragraph(v["resumo"], styles["resumo"]),
        secao(L["exp"], styles["secao"]),
    ]
    for job in v["jobs"]:
        story.append(timeline_job(job, styles))

    story.append(secao(L["proj"], styles["secao"]))
    for p in v["projetos"]:
        url = p["url"]
        shown = url.replace("https://", "")
        story.append(
            Paragraph(
                f'<b>{p["nome"]}</b> — <link href="{url}" color="black"><u>{shown}</u></link>',
                styles["proj"],
            )
        )
        story.append(Paragraph(p["desc"], styles["desc"]))

    story.append(secao(L["form"], styles["secao"]))
    story.append(Paragraph(formacao, styles["cert"]))
    story.append(secao(L["cert"], styles["secao"]))
    story.append(Paragraph("<br/>".join(f"• {c}" for c in certs), styles["cert"]))
    story.append(secao(L["skill"], styles["secao"]))
    story.append(Paragraph("<br/>".join(f"• {s}" for s in v["skills"]), styles["skill"]))

    doc = SimpleDocTemplate(
        str(out),
        pagesize=A4,
        leftMargin=1.6 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.1 * cm,
        title=f"{CONTATO['nome']} — {v['cargo']}",
        author=CONTATO["nome"],
    )
    doc.build(story)


def gerar_html(v, html_path: Path, pdf_name: str):
    L = labels(v["lang"])
    formacao = FORMACAO_EN if v["lang"] == "en" else FORMACAO_PT
    certs = CERTS_EN if v["lang"] == "en" else CERTS_PT
    cidade = CONTATO["cidade_en"] if v["lang"] == "en" else CONTATO["cidade_pt"]
    lang_attr = "en" if v["lang"] == "en" else "pt-BR"

    jobs_html = []
    for job in v["jobs"]:
        itens = "".join(f"<li>{html.escape(i)}</li>" for i in job["itens"])
        jobs_html.append(
            f"""<div class="job">
        <time>{html.escape(job["periodo"])}</time>
        <div>
          <h3>{html.escape(job["cargo"])}</h3>
          <p class="empresa">{html.escape(job["empresa"])}</p>
          <ul>{itens}</ul>
        </div>
      </div>"""
        )

    projetos_html = []
    for p in v["projetos"]:
        shown = p["url"].replace("https://", "")
        projetos_html.append(
            f"""<div class="projeto">
        <p><strong>{html.escape(p["nome"])}</strong> —
        <a href="{html.escape(p["url"])}">{html.escape(shown)}</a></p>
        <p>{html.escape(p["desc"])}</p>
      </div>"""
        )

    certs_html = "".join(f"<li>{html.escape(c)}</li>" for c in certs)
    skills_html = "".join(f"<li>{s}</li>" for s in v["skills"])

    html_path.write_text(
        f"""<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(CONTATO["nome"])} — {html.escape(v["cargo"])}</title>
  <link rel="stylesheet" href="../../../assets/curriculo.css" />
</head>
<body>
  <div class="toolbar">
    <a href="../../../index.html">{html.escape(L["back"])}</a>
    <button type="button" onclick="window.print()">{html.escape(L["print"])}</button>
    <a href="{html.escape(pdf_name)}">PDF</a>
  </div>
  <article class="doc">
    <h1>{html.escape(CONTATO["nome"])}</h1>
    <p class="headline">{html.escape(v["cargo"])}</p>
    <p class="headline">{html.escape(v["headline"])}</p>
    <p class="contato">
      {html.escape(cidade)} · {html.escape(CONTATO["telefone"])} ·
      <a href="mailto:{html.escape(CONTATO["email"])}">{html.escape(CONTATO["email"])}</a><br />
      <a href="{html.escape(CONTATO["github_url"])}">{html.escape(CONTATO["github"])}</a> ·
      <a href="{html.escape(CONTATO["portfolio_url"])}">{html.escape(CONTATO["portfolio"])}</a>
    </p>
    <h2>{html.escape(L["resumo"])}</h2>
    <p class="resumo">{html.escape(v["resumo"])}</p>
    <h2>{html.escape(L["exp"])}</h2>
    {"".join(jobs_html)}
    <h2>{html.escape(L["proj"])}</h2>
    {"".join(projetos_html)}
    <h2>{html.escape(L["form"])}</h2>
    <p>{html.escape(formacao)}</p>
    <h2>{html.escape(L["cert"])}</h2>
    <ul>{certs_html}</ul>
    <h2>{html.escape(L["skill"])}</h2>
    <ul>{skills_html}</ul>
  </article>
</body>
</html>
""",
        encoding="utf-8",
    )


def main():
    catalog = []
    for v in VERSOES:
        dest = pasta_versao(v)
        dest.mkdir(parents=True, exist_ok=True)
        pdf_path = dest / v["pdf"]
        html_path = dest / v["arquivo"]
        gerar_pdf(v, pdf_path)
        gerar_html(v, html_path, v["pdf"])
        rel = f"versoes/{v['lang']}/{v['id']}"
        catalog.append(
            {
                "id": v["id"],
                "lang": v["lang"],
                "pasta": v["pasta"],
                "cargo": v["cargo"],
                "html": f"{rel}/{v['arquivo']}",
                "pdf": f"{rel}/{v['pdf']}",
            }
        )
        print(f"ok {rel}")

    (ROOT / "assets").mkdir(exist_ok=True)
    payload = json.dumps(catalog, ensure_ascii=False, indent=2)
    (ROOT / "catalogo.json").write_text(payload, encoding="utf-8")
    (ROOT / "assets" / "catalogo.js").write_text(
        "window.CATALOGO = " + json.dumps(catalog, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    print("catalogo.json e assets/catalogo.js atualizados")


if __name__ == "__main__":
    main()
