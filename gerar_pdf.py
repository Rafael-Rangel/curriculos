"""Currículo ATS: resumo, timeline, projetos com link, certificados, skills em lista."""

from pathlib import Path

from reportlab.lib.colors import black, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
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

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT = Path(__file__).resolve().parent / "Rafael-Rangel-dos-Santos-Farinha-ATS.pdf"

# Calibri: melhor equilíbrio ATS + leitura (Gupy, Greenhouse, Workday, LinkedIn).
# Times New Roman é ATS-ok, mas cansa na triagem humana.
_FONTS = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("Calibri", str(_FONTS / "calibri.ttf")))
pdfmetrics.registerFont(TTFont("Calibri-Bold", str(_FONTS / "calibrib.ttf")))
pdfmetrics.registerFontFamily(
    "Calibri",
    normal="Calibri",
    bold="Calibri-Bold",
)

FONT = "Calibri"
FONT_BOLD = "Calibri-Bold"
SIZE = 11
LEADING = 14.5


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
            ListItem(Paragraph(t, item_style), leftIndent=10, bulletColor=black)
            for t in texts
        ],
        bulletType="bullet",
        bulletFontName=FONT,
        bulletFontSize=SIZE,
        leftIndent=14,
        spaceBefore=2,
        spaceAfter=4,
    )


def secao(titulo, secao_style):
    return KeepTogether(
        [
            Paragraph(titulo, secao_style),
            HRFlowable(
                width="100%",
                thickness=0.7,
                color=black,
                spaceBefore=1,
                spaceAfter=6,
            ),
        ]
    )


def timeline_job(periodo, cargo, empresa, itens, styles):
    data = [
        [
            Paragraph(periodo, styles["data"]),
            Paragraph(cargo, styles["cargo"]),
        ],
        [
            "",
            Paragraph(empresa, styles["empresa"]),
        ],
    ]
    head = Table(data, colWidths=[3.6 * cm, 11.9 * cm])
    head.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("BACKGROUND", (0, 0), (-1, -1), white),
                ("LINEBEFORE", (0, 0), (0, -1), 1.1, black),
                ("LEFTPADDING", (0, 0), (0, -1), 8),
            ]
        )
    )
    body = [
        ["", bullets(itens, styles["item"])],
    ]
    block = Table(body, colWidths=[3.6 * cm, 11.9 * cm])
    block.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LINEBEFORE", (0, 0), (0, -1), 1.1, black),
                ("LEFTPADDING", (0, 0), (0, -1), 8),
            ]
        )
    )
    return KeepTogether([head, block, Spacer(1, 4)])


def projeto(nome, url, descricao, styles):
    titulo = (
        f'<b>{nome}</b> — <link href="{url}" color="black">'
        f'<u>{url.replace("https://", "")}</u></link>'
    )
    return KeepTogether(
        [
            Paragraph(titulo, styles["proj_title"]),
            Paragraph(descricao, styles["proj_desc"]),
        ]
    )


def build():
    styles = {
        "nome": S("nome", fontName=FONT_BOLD, fontSize=14, leading=17, alignment=TA_CENTER, spaceAfter=2),
        "headline": S("headline", alignment=TA_CENTER, spaceAfter=3),
        "contato": S("contato", alignment=TA_CENTER, fontSize=10, leading=13, spaceAfter=6),
        "secao": S("secao", fontName=FONT_BOLD, fontSize=11, leading=13, spaceBefore=2, spaceAfter=0),
        "resumo": S("resumo", alignment=TA_JUSTIFY, spaceAfter=4),
        "data": S("data", fontName=FONT_BOLD, fontSize=9.5, leading=12, alignment=TA_LEFT),
        "cargo": S("cargo", fontName=FONT_BOLD, alignment=TA_LEFT),
        "empresa": S("empresa", alignment=TA_LEFT, spaceAfter=2),
        "item": S("item", alignment=TA_JUSTIFY, leading=13),
        "proj_title": S("proj_title", alignment=TA_LEFT, spaceBefore=2, spaceAfter=1),
        "proj_desc": S("proj_desc", alignment=TA_JUSTIFY, spaceAfter=2),
        "cert": S("cert", alignment=TA_LEFT, leading=13, spaceAfter=1),
        "skill_cat": S("skill_cat", fontName=FONT_BOLD, alignment=TA_LEFT, spaceAfter=1),
        "skill_item": S("skill_item", alignment=TA_LEFT, leading=13),
    }

    story = [
        Paragraph("RAFAEL RANGEL DOS SANTOS FARINHA", styles["nome"]),
        Paragraph("Engenheiro de Software Full Stack", styles["headline"]),
        Paragraph(
            "Rio de Janeiro – RJ · (21) 92036-1740 · "
            '<link href="mailto:stackflow.soft@gmail.com" color="black">'
            "stackflow.soft@gmail.com</link><br/>"
            '<link href="https://github.com/Rafael-Rangel/" color="black">'
            "<u>github.com/Rafael-Rangel</u></link> · "
            '<link href="https://rafael-rangel.github.io/portfolio/" color="black">'
            "<u>rafael-rangel.github.io/portfolio</u></link>",
            styles["contato"],
        ),
        secao("RESUMO", styles["secao"]),
        Paragraph(
            "Engenheiro de Software Full Stack com atuação na construção de plataformas SaaS "
            "multi-tenant, CRMs, integrações de APIs e produtos com Inteligência Artificial. "
            "Experiência ponta a ponta: requisitos, arquitetura, frontend, backend, dados, "
            "automação e implantação. Atualmente Diretor do Departamento de Software e "
            "Software Engineer na Genesis Company. Stack principal: TypeScript, React, Next.js, "
            "Node.js, NestJS e PostgreSQL.",
            styles["resumo"],
        ),
        secao("EXPERIÊNCIA PROFISSIONAL", styles["secao"]),
        timeline_job(
            "Jul 2025 – Atual",
            "Diretor do Departamento de Software &amp; Software Engineer",
            "Genesis Company · Rio de Janeiro, RJ",
            [
                "Dirige o Departamento de Software: arquitetura, prioridades, padrões de engenharia e entrega de produtos digitais.",
                "Desenvolve plataformas SaaS multi-tenant (CRM, atendimento, workspaces, permissões e isolamento de dados).",
                "Integra WhatsApp, Instagram, Messenger e webchat com APIs, webhooks, filas e múltiplas instâncias.",
                "Incorpora agentes de IA, RAG e knowledge base em fluxos de atendimento e automação.",
            ],
            styles,
        ),
        timeline_job(
            "Jul 2024 – Jul 2025",
            "Web Developer / Software Developer",
            "Webmaker · Rio de Janeiro, RJ",
            [
                "Desenvolveu websites, landing pages e aplicações web com HTML, CSS, JavaScript, React e Next.js.",
                "Implementou integrações com APIs, manutenção de sistemas, performance e SEO técnico.",
            ],
            styles,
        ),
        secao("PROJETOS EM DESTAQUE", styles["secao"]),
        projeto(
            "KoruVision CRM",
            "https://github.com/Rafael-Rangel/koruvision-landing",
            "SaaS multi-tenant de CRM e atendimento, com IA e integração WhatsApp / Instagram.",
            styles,
        ),
        projeto(
            "Pulse — controle financeiro",
            "https://pulse-rangel1.vercel.app",
            "Controle financeiro pessoal em TypeScript. "
            '<link href="https://github.com/Rafael-Rangel/pulse" color="black">'
            "<u>github.com/Rafael-Rangel/pulse</u></link>.",
            styles,
        ),
        projeto(
            "Inglês conversacional para Devs",
            "https://github.com/Rafael-Rangel/ingles-conversacional-devs",
            "Estudo e conversação com professor de IA para desenvolvedores (TypeScript).",
            styles,
        ),
        secao("FORMAÇÃO", styles["secao"]),
        Paragraph(
            "<b>Análise e Desenvolvimento de Sistemas</b> — FIAP. Conclusão em 2025 (2 anos).",
            styles["cert"],
        ),
        secao("CERTIFICADOS", styles["secao"]),
        Paragraph(
            "• Certificado de Qualificação Profissional em Estratégia e Inovação Tecnológica "
            "com aplicações em IA e IoT (2025)<br/>"
            "• Certificado de Qualificação Profissional em Desenvolvimento de Aplicações Móveis (2025)<br/>"
            "• Certificado de Qualificação Profissional em Análise e Design Web 2.0 (2024)<br/>"
            "• Certificado de Qualificação Profissional em Análise de Sistemas e Prototipação Web (2024)<br/>"
            "• Certificado de Qualificação Profissional em Análise de Sistemas e Prototipagem Web (2024)<br/>"
            "• Certificado de Qualificação Profissional em Desenvolvimento e Designer Web 2.0 (2024)",
            styles["cert"],
        ),
        secao("COMPETÊNCIAS TÉCNICAS", styles["secao"]),
        Paragraph(
            "• <b>Linguagens:</b> TypeScript, JavaScript, Python, HTML, CSS, SQL<br/>"
            "• <b>Frontend:</b> React, Next.js, SPA, PWA, WordPress<br/>"
            "• <b>Backend e dados:</b> Node.js, NestJS, APIs REST, webhooks, PostgreSQL<br/>"
            "• <b>IA, integrações e infra:</b> OpenAI, RAG, WhatsApp Cloud API, Meta APIs, AWS, n8n, Docker, VPS, Git",
            styles["skill_item"],
        ),
    ]

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=2.2 * cm,
        rightMargin=2 * cm,
        topMargin=1.4 * cm,
        bottomMargin=1.2 * cm,
        title="Rafael Rangel dos Santos Farinha — Currículo",
        author="Rafael Rangel dos Santos Farinha",
    )
    doc.build(story)
    print(f"PDF gerado: {OUT}")


if __name__ == "__main__":
    build()
