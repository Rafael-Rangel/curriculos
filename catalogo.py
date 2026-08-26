"""Catálogo de currículos — PT-BR e EN. Verbos na 1ª pessoa."""

CONTATO = {
    "nome": "Rafael Rangel dos Santos Farinha",
    "cidade_pt": "Rio de Janeiro – RJ",
    "cidade_en": "Rio de Janeiro, Brazil",
    "telefone": "(21) 92036-1740",
    "email": "stackflow.soft@gmail.com",
    "github": "github.com/Rafael-Rangel",
    "github_url": "https://github.com/Rafael-Rangel/",
    "portfolio": "rafael-rangel.github.io/portfolio",
    "portfolio_url": "https://rafael-rangel.github.io/portfolio/",
}

FORMACAO_PT = "Análise e Desenvolvimento de Sistemas — FIAP. Conclusão em 2025 (2 anos)."
FORMACAO_EN = "Analysis and Systems Development — FIAP. Completed in 2025 (2-year degree)."

CERTS_PT = [
    "Certificado de Qualificação Profissional em Estratégia e Inovação Tecnológica com aplicações em IA e IoT (2025)",
    "Certificado de Qualificação Profissional em Desenvolvimento de Aplicações Móveis (2025)",
    "Certificado de Qualificação Profissional em Análise e Design Web 2.0 (2024)",
    "Certificado de Qualificação Profissional em Análise de Sistemas e Prototipação Web (2024)",
    "Certificado de Qualificação Profissional em Análise de Sistemas e Prototipagem Web (2024)",
    "Certificado de Qualificação Profissional em Desenvolvimento e Designer Web 2.0 (2024)",
]

CERTS_EN = [
    "Professional Qualification in Technology Strategy and Innovation with AI and IoT (2025)",
    "Professional Qualification in Mobile Application Development (2025)",
    "Professional Qualification in Web 2.0 Analysis and Design (2024)",
    "Professional Qualification in Systems Analysis and Web Prototyping (2024)",
    "Professional Qualification in Systems Analysis and Web Prototype Design (2024)",
    "Professional Qualification in Web 2.0 Development and Design (2024)",
]

# slug, pasta, idioma, label na UI, cargo, headline, resumo, jobs, projetos, skills
VERSOES = [
    {
        "id": "engenheiro-ia",
        "lang": "pt-br",
        "pasta": "Engenharia de IA",
        "arquivo": "Curriculo.html",
        "pdf": "Curriculo.pdf",
        "cargo": "Engenheiro de Inteligência Artificial",
        "headline": "AI Engineer  ·  RAG  ·  Multiagente  ·  System prompt  ·  Economia de tokens  ·  Evals  ·  Escala",
        "resumo": (
            "Engenheiro de IA e software: LLM, RAG, embeddings, hybrid search, BM25, rerank, grounding, "
            "citações, knowledge base, multiagente, orquestração, planner/executor, tool calling, function calling, "
            "system prompt, context engineering, prompt caching, token budget, economia de tokens, model routing, "
            "streaming, evals, faithfulness, hallucination control, LLM-as-judge, human-in-the-loop, precisão de agentes. "
            "SaaS multi-tenant, CRM, omnichannel, WhatsApp Cloud API, Instagram, Meta, webhooks, APIs REST, filas, "
            "escala horizontal, load balancing, isolamento de tenant, ACL, RBAC, pgvector, PostgreSQL, TypeScript, "
            "Python, React, Next.js, Node.js, NestJS, Docker, AWS, Azure, LLMOps, guardrails, PII, prompt injection."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Atual",
                "cargo": "Diretor do Departamento de Software & Software Engineer",
                "empresa": "SaaS · Rio de Janeiro, RJ",
                "itens": [
                    "Dirigi a engenharia de IA em CRM e atendimento: orquestração multiagente, tool calling, planner/executor e human-in-the-loop.",
                    "Implementei RAG ponta a ponta: ingestão, chunking, embeddings, hybrid search, rerank, grounding, citações e fidelidade da resposta.",
                    "Otimizei economia de tokens: system prompt, context engineering, prompt caching, compressão de contexto, model routing e budget de tokens.",
                    "Aumentei precisão de agentes com evals (tool-call accuracy, faithfulness, regressão de prompts) e fallback quando o retrieval falha.",
                    "Escalei inferência e filas por tenant: isolamento de contexto, ACL na knowledge base, streaming, retries e observabilidade LLMOps.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "SaaS multi-tenant com RAG, multiagentes, system prompts e canais WhatsApp/Instagram em escala.",
            },
            {
                "nome": "Rubi 2.0 / Conversation AI",
                "url": "https://github.com/Rafael-Rangel/rubi-teste",
                "desc": "Agentes especializados, knowledge base, evals de precisão e handoff para humano.",
            },
            {
                "nome": "Inglês conversacional para Devs",
                "url": "https://github.com/Rafael-Rangel/ingles-conversacional-devs",
                "desc": "Tutor com embeddings, context window controlada e prática de system/user prompt.",
            },
        ],
        "skills": [
            "<b>IA:</b> RAG, embeddings, hybrid search, rerank, multi-agent, tool calling, function calling, system prompt, context engineering, evals",
            "<b>Tokens e qualidade:</b> token budget, prompt caching, model routing, streaming, faithfulness, hallucination control, LLM-as-judge",
            "<b>Escala e cloud:</b> filas, pgvector, PostgreSQL, tenant ACL, LLMOps, Python, TypeScript, OpenAI, Node.js, NestJS, AWS, Azure, Docker, guardrails, PII, prompt injection",
        ],
    },
    {
        "id": "ai-engineer",
        "lang": "en",
        "pasta": "AI Engineering",
        "arquivo": "Resume.html",
        "pdf": "Resume.pdf",
        "cargo": "AI Engineer",
        "headline": "AI Engineer  ·  RAG  ·  Multi-agent  ·  System prompt  ·  Token economics  ·  Evals  ·  Scale",
        "resumo": (
            "AI and software engineer: LLM, RAG, embeddings, hybrid search, BM25, rerank, grounding, citations, "
            "knowledge base, multi-agent orchestration, planner/executor, tool calling, function calling, "
            "system prompt, context engineering, prompt caching, token budget, token economics, model routing, "
            "streaming, evals, faithfulness, hallucination control, LLM-as-judge, human-in-the-loop, agent precision. "
            "Multi-tenant SaaS, CRM, omnichannel, WhatsApp Cloud API, Instagram, Meta, webhooks, REST APIs, queues, "
            "horizontal scale, load balancing, tenant isolation, ACL, RBAC, pgvector, PostgreSQL, TypeScript, "
            "Python, React, Next.js, Node.js, NestJS, Docker, AWS, Azure, LLMOps, guardrails, PII, prompt injection."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Present",
                "cargo": "Software Engineering Director & Software Engineer",
                "empresa": "SaaS · Rio de Janeiro, Brazil",
                "itens": [
                    "Led AI engineering for CRM and support: multi-agent orchestration, tool calling, planner/executor, and human-in-the-loop.",
                    "Shipped end-to-end RAG: ingestion, chunking, embeddings, hybrid search, rerank, grounding, citations, and answer faithfulness.",
                    "Cut token cost with system prompts, context engineering, prompt caching, context compression, model routing, and token budgets.",
                    "Raised agent precision with evals (tool-call accuracy, faithfulness, prompt regression) and retrieval-failure fallbacks.",
                    "Scaled inference and queues per tenant: context isolation, knowledge-base ACLs, streaming, retries, and LLMOps observability.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Web · Rio de Janeiro, Brazil",
                "itens": [
                    "Built apps and APIs that later fed RAG pipelines and agents.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "Multi-tenant SaaS with RAG, multi-agent flows, system prompts, and WhatsApp/Instagram at scale.",
            },
            {
                "nome": "Rubi 2.0 / Conversation AI",
                "url": "https://github.com/Rafael-Rangel/rubi-teste",
                "desc": "Specialized agents, knowledge base, precision evals, and human handoff.",
            },
            {
                "nome": "Conversational English for Devs",
                "url": "https://github.com/Rafael-Rangel/ingles-conversacional-devs",
                "desc": "Tutor with embeddings, controlled context window, and system/user prompt practice.",
            },
        ],
        "skills": [
            "<b>AI:</b> RAG, embeddings, hybrid search, rerank, multi-agent, tool calling, function calling, system prompt, context engineering, evals",
            "<b>Tokens & quality:</b> token budget, prompt caching, model routing, streaming, faithfulness, hallucination control, LLM-as-judge",
            "<b>Scale:</b> queues, async processing, pgvector, PostgreSQL, tenant isolation, ACL, LLMOps observability",
            "<b>Stack & cloud:</b> Python, TypeScript, OpenAI, Node.js, NestJS, AWS, Azure, Docker, guardrails, PII, prompt injection",
        ],
    },
    {
        "id": "arquiteto-software",
        "lang": "pt-br",
        "pasta": "Arquitetura de Software",
        "arquivo": "Curriculo.html",
        "pdf": "Curriculo.pdf",
        "cargo": "Arquiteto de Software",
        "headline": "Arquitetura  ·  SaaS multi-tenant  ·  Escalabilidade  ·  Segurança  ·  AWS  ·  Azure",
        "resumo": (
            "Arquiteto de software: SaaS, multi-tenancy, workspaces, RBAC, isolamento de dados, APIs REST, "
            "webhooks, event-driven, filas, processamento assíncrono, microserviços, modularização, C4, "
            "escala horizontal, load balancing, rate limit, circuit breaker, observabilidade, métricas. "
            "Segurança: authn, authz, OWASP API, secrets, PII. Cloud: AWS, Azure, Docker, VPS, CI/CD, "
            "PostgreSQL, TypeScript, Node.js, NestJS, React, Next.js, WhatsApp Cloud API, Meta, CRM, IA, RAG."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Atual",
                "cargo": "Diretor do Departamento de Software & Software Engineer",
                "empresa": "SaaS · Rio de Janeiro, RJ",
                "itens": [
                    "Dirigi as decisões de arquitetura de plataformas SaaS multi-tenant (workspaces, RBAC, isolamento de dados).",
                    "Projetei APIs, webhooks, filas e processamento assíncrono para picos de mensageria (WhatsApp/Meta).",
                    "Defini caminhos de escala: load balancing, múltiplas instâncias, rate limit e circuit breaker.",
                    "Modelei segurança: autenticação, autorização, secrets, OWASP API e isolamento por tenant.",
                    "Orientei deploy em VPS/Docker e desenhei o uso de AWS e Azure (compute, identity, storage).",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Web · Rio de Janeiro, RJ",
                "itens": [
                    "Estruturei frontends e integrações com foco em performance, SEO e contratos de API.",
                    "Documentei fluxos e evoluí sistemas de clientes sem quebrar operação.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "Arquitetura SaaS multi-tenant, omnichannel, filas e agentes de IA.",
            },
            {
                "nome": "Pulse",
                "url": "https://pulse-rangel1.vercel.app",
                "desc": "Aplicação TypeScript com modelagem de dados e deploy em cloud. github.com/Rafael-Rangel/pulse",
            },
        ],
        "skills": [
            "<b>Arquitetura:</b> multi-tenancy, event-driven, filas, webhooks, modularização, observabilidade",
            "<b>Escala e segurança:</b> load balancing, horizontal scaling, RBAC, OWASP, secrets, PII, rate limit",
            "<b>Cloud:</b> AWS, Azure, Docker, VPS, CI/CD básico, PostgreSQL",
            "<b>Stack:</b> TypeScript, Node.js, NestJS, React, Next.js, APIs REST",
        ],
    },
    {
        "id": "software-architect",
        "lang": "en",
        "pasta": "Software Architecture",
        "arquivo": "Resume.html",
        "pdf": "Resume.pdf",
        "cargo": "Software Architect",
        "headline": "Architecture  ·  Multi-tenant SaaS  ·  Scalability  ·  Security  ·  AWS  ·  Azure",
        "resumo": (
            "Software architect: SaaS, multi-tenancy, workspaces, RBAC, data isolation, REST APIs, webhooks, "
            "event-driven, queues, async processing, microservices, modularization, C4, horizontal scale, "
            "load balancing, rate limiting, circuit breaker, observability, metrics. Security: authn, authz, "
            "OWASP API, secrets, PII. Cloud: AWS, Azure, Docker, VPS, CI/CD, PostgreSQL, TypeScript, Node.js, "
            "NestJS, React, Next.js, WhatsApp Cloud API, Meta, CRM, AI, RAG."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Present",
                "cargo": "Software Engineering Director & Software Engineer",
                "empresa": "SaaS · Rio de Janeiro, Brazil",
                "itens": [
                    "Led architecture for multi-tenant SaaS (workspaces, RBAC, data isolation).",
                    "Designed APIs, webhooks, queues, and async processing for messaging spikes (WhatsApp/Meta).",
                    "Defined scale paths: load balancing, multi-instance, rate limiting, and circuit breaking.",
                    "Modeled security: authn/authz, secrets, OWASP API, and per-tenant isolation.",
                    "Guided Docker/VPS delivery and cloud usage on AWS and Azure (compute, identity, storage).",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Web · Rio de Janeiro, Brazil",
                "itens": [
                    "Structured frontends and integrations with performance, SEO, and API contracts in mind.",
                    "Documented flows and evolved client systems without breaking operations.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "Multi-tenant SaaS architecture, omnichannel, queues, and AI agents.",
            },
            {
                "nome": "Pulse",
                "url": "https://pulse-rangel1.vercel.app",
                "desc": "TypeScript app with data modeling and cloud deploy. github.com/Rafael-Rangel/pulse",
            },
        ],
        "skills": [
            "<b>Architecture:</b> multi-tenancy, event-driven, queues, webhooks, modularization, observability",
            "<b>Scale & security:</b> load balancing, horizontal scaling, RBAC, OWASP, secrets, PII, rate limiting",
            "<b>Cloud:</b> AWS, Azure, Docker, VPS, basic CI/CD, PostgreSQL",
            "<b>Stack:</b> TypeScript, Node.js, NestJS, React, Next.js, REST APIs",
        ],
    },
    {
        "id": "engenheiro-software-pleno",
        "lang": "pt-br",
        "pasta": "Engenharia de Software Pleno",
        "arquivo": "Curriculo.html",
        "pdf": "Curriculo.pdf",
        "cargo": "Engenheiro de Software Pleno",
        "headline": "Full Stack  ·  TypeScript  ·  React  ·  Node.js  ·  NestJS  ·  PostgreSQL  ·  APIs",
        "resumo": (
            "Engenheiro de software full stack: TypeScript, JavaScript, Python, React, Next.js, Node.js, NestJS, "
            "PostgreSQL, SQL, APIs REST, webhooks, filas, SaaS multi-tenant, CRM, dashboards, SPA, PWA, "
            "WhatsApp Cloud API, Instagram, Meta, n8n, Docker, AWS, Azure, Git, Core Web Vitals, Lighthouse, "
            "RAG, system prompt, agentes, tool calling, performance, SEO técnico, UX, design system."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Atual",
                "cargo": "Diretor do Departamento de Software & Software Engineer",
                "empresa": "SaaS · Rio de Janeiro, RJ",
                "itens": [
                    "Desenvolvi plataformas SaaS multi-tenant (CRM, inbox, permissões, dashboards) em React e Node.js.",
                    "Implementei APIs REST, webhooks e filas para WhatsApp, Instagram e Meta Cloud API.",
                    "Integrei IA em produto: RAG, system prompt, agentes e tool calling sem acoplar o domínio ao provedor.",
                    "Acompanhei performance (Core Web Vitals) e evolução contínua dos sistemas.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Web · Rio de Janeiro, RJ",
                "itens": [
                    "Desenvolvi sites, landing pages e SPAs com HTML, CSS, JavaScript, React e Next.js.",
                    "Integrei APIs, corrigi falhas e otimizei Lighthouse/SEO técnico.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "SaaS full stack de CRM e atendimento, multi-tenant, com IA e canais Meta.",
            },
            {
                "nome": "Pulse",
                "url": "https://pulse-rangel1.vercel.app",
                "desc": "Controle financeiro em TypeScript. github.com/Rafael-Rangel/pulse",
            },
        ],
        "skills": [
            "<b>Linguagens:</b> TypeScript, JavaScript, Python, HTML, CSS, SQL",
            "<b>Frontend:</b> React, Next.js, SPA, PWA",
            "<b>Backend:</b> Node.js, NestJS, APIs REST, webhooks, PostgreSQL",
            "<b>Cloud e qualidade:</b> Docker, AWS, Azure, Git, Lighthouse",
        ],
    },
    {
        "id": "software-engineer",
        "lang": "en",
        "pasta": "Software Engineer (Mid)",
        "arquivo": "Resume.html",
        "pdf": "Resume.pdf",
        "cargo": "Software Engineer",
        "headline": "Full Stack  ·  TypeScript  ·  React  ·  Node.js  ·  NestJS  ·  PostgreSQL  ·  APIs",
        "resumo": (
            "Full-stack software engineer: TypeScript, JavaScript, Python, React, Next.js, Node.js, NestJS, "
            "PostgreSQL, SQL, REST APIs, webhooks, queues, multi-tenant SaaS, CRM, dashboards, SPA, PWA, "
            "WhatsApp Cloud API, Instagram, Meta, n8n, Docker, AWS, Azure, Git, Core Web Vitals, Lighthouse, "
            "RAG, system prompt, agents, tool calling, performance, technical SEO, UX, design systems."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Present",
                "cargo": "Software Engineering Director & Software Engineer",
                "empresa": "SaaS · Rio de Janeiro, Brazil",
                "itens": [
                    "Built multi-tenant SaaS platforms (CRM, inbox, permissions, dashboards) with React and Node.js.",
                    "Implemented REST APIs, webhooks, and queues for WhatsApp, Instagram, and Meta Cloud API.",
                    "Integrated AI in product: RAG, system prompts, agents, and tool calling without coupling to one vendor.",
                    "Tracked Core Web Vitals and continuous system evolution.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Web · Rio de Janeiro, Brazil",
                "itens": [
                    "Developed sites, landing pages, and SPAs with HTML, CSS, JavaScript, React, and Next.js.",
                    "Integrated APIs, fixed defects, and improved Lighthouse/technical SEO.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "Full-stack SaaS CRM and support, multi-tenant, with AI and Meta channels.",
            },
            {
                "nome": "Pulse",
                "url": "https://pulse-rangel1.vercel.app",
                "desc": "Personal finance in TypeScript. github.com/Rafael-Rangel/pulse",
            },
        ],
        "skills": [
            "<b>Languages:</b> TypeScript, JavaScript, Python, HTML, CSS, SQL",
            "<b>Frontend:</b> React, Next.js, SPA, PWA",
            "<b>Backend:</b> Node.js, NestJS, REST APIs, webhooks, PostgreSQL",
            "<b>Cloud & quality:</b> Docker, AWS, Azure, Git, Lighthouse",
        ],
    },
    {
        "id": "analista-sistemas",
        "lang": "pt-br",
        "pasta": "Analista de Sistemas",
        "arquivo": "Curriculo.html",
        "pdf": "Curriculo.pdf",
        "cargo": "Analista de Sistemas",
        "headline": "Requisitos  ·  Processos  ·  Integrações  ·  APIs  ·  Dados  ·  SaaS",
        "resumo": (
            "Analista de sistemas: levantamento de requisitos, regras de negócio, casos de uso, fluxos, BPM, "
            "documentação, modelagem de dados, PostgreSQL, APIs REST, webhooks, integrações, CRM, omnichannel, "
            "WhatsApp Cloud API, Instagram, Meta, SaaS multi-tenant, permissões, RBAC, filas, automações, n8n, "
            "IA, RAG, agentes, handoff humano, métricas, dashboards, TypeScript, React, Node.js, SQL."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Atual",
                "cargo": "Diretor do Departamento de Software & Software Engineer",
                "empresa": "SaaS · Rio de Janeiro, RJ",
                "itens": [
                    "Levantei requisitos de CRM, atendimento e multi-tenancy e os traduzi em fluxos e contratos de API.",
                    "Analisei integrações WhatsApp/Meta/Instagram: webhooks, filas, falhas e regras de horário.",
                    "Modelei dados de organizações, permissões, conversas, leads e métricas.",
                    "Documentei regras de automação, IA e handoff humano para o time executar com clareza.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Web · Rio de Janeiro, RJ",
                "itens": [
                    "Levantei necessidades de clientes e transformei em sites, landing pages e integrações.",
                    "Especifiquei ajustes de SEO, performance e manutenção contínua.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "Mapeamento de módulos, papéis, funil, inbox e integrações omnichannel.",
            },
            {
                "nome": "GSALES CRM",
                "url": "https://github.com/Rafael-Rangel/",
                "desc": "Análise de fluxos comerciais e conexão com sistemas externos.",
            },
        ],
        "skills": [
            "<b>Análise:</b> requisitos, regras de negócio, casos de uso, fluxos, documentação",
            "<b>Sistemas:</b> APIs REST, webhooks, modelagem PostgreSQL, multi-tenancy",
            "<b>Integrações:</b> WhatsApp Cloud API, Meta, CRM, n8n",
            "<b>Técnico:</b> TypeScript, React, Node.js, SQL",
        ],
    },
    {
        "id": "systems-analyst",
        "lang": "en",
        "pasta": "Systems Analyst",
        "arquivo": "Resume.html",
        "pdf": "Resume.pdf",
        "cargo": "Systems Analyst",
        "headline": "Requirements  ·  Processes  ·  Integrations  ·  APIs  ·  Data  ·  SaaS",
        "resumo": (
            "Systems analyst: requirements gathering, business rules, use cases, flows, BPM, documentation, "
            "data modeling, PostgreSQL, REST APIs, webhooks, integrations, CRM, omnichannel, WhatsApp Cloud API, "
            "Instagram, Meta, multi-tenant SaaS, permissions, RBAC, queues, automation, n8n, AI, RAG, agents, "
            "human handoff, metrics, dashboards, TypeScript, React, Node.js, SQL."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Present",
                "cargo": "Software Engineering Director & Software Engineer",
                "empresa": "SaaS · Rio de Janeiro, Brazil",
                "itens": [
                    "Gathered CRM, support, and multi-tenancy requirements and translated them into flows and API contracts.",
                    "Analyzed WhatsApp/Meta/Instagram integrations: webhooks, queues, failure modes, and business hours.",
                    "Modeled data for organizations, permissions, conversations, leads, and metrics.",
                    "Documented automation, AI, and human-handoff rules so delivery stayed unambiguous.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Web · Rio de Janeiro, Brazil",
                "itens": [
                    "Gathered client needs and turned them into sites, landing pages, and integrations.",
                    "Specified SEO, performance, and ongoing maintenance work.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "Module, role, pipeline, inbox, and omnichannel integration mapping.",
            },
            {
                "nome": "GSALES CRM",
                "url": "https://github.com/Rafael-Rangel/",
                "desc": "Commercial-flow analysis and external system connections.",
            },
        ],
        "skills": [
            "<b>Analysis:</b> requirements, business rules, use cases, flows, documentation",
            "<b>Systems:</b> REST APIs, webhooks, PostgreSQL modeling, multi-tenancy",
            "<b>Integrations:</b> WhatsApp Cloud API, Meta, CRM, n8n",
            "<b>Technical:</b> TypeScript, React, Node.js, SQL",
        ],
    },
    {
        "id": "desenvolvedor-pleno",
        "lang": "pt-br",
        "pasta": "Desenvolvedor Pleno",
        "arquivo": "Curriculo.html",
        "pdf": "Curriculo.pdf",
        "cargo": "Desenvolvedor Full Stack Pleno",
        "headline": "React  ·  Next.js  ·  Node.js  ·  TypeScript  ·  PostgreSQL  ·  Integrações",
        "resumo": (
            "Desenvolvedor full stack: HTML, CSS, JavaScript, TypeScript, React, Next.js, Node.js, NestJS, "
            "PostgreSQL, REST, webhooks, SPA, PWA, WordPress, Git, Docker, AWS, Azure, Vercel, integrações, "
            "WhatsApp, Instagram, APIs, landing pages, e-commerce, SEO, Lighthouse, Core Web Vitals, "
            "dashboards, UX/UI, componentes, SaaS, CRM, IA, RAG."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Atual",
                "cargo": "Diretor do Departamento de Software & Software Engineer",
                "empresa": "SaaS · Rio de Janeiro, RJ",
                "itens": [
                    "Desenvolvi CRM e painéis administrativos em React/Next.js com TypeScript.",
                    "Implementei backends Node.js/NestJS, APIs REST e webhooks de WhatsApp e Instagram.",
                    "Integrei recursos de IA (agentes e RAG) em fluxos de atendimento.",
                    "Publiquei e mantive aplicações em Docker/VPS.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Web · Rio de Janeiro, RJ",
                "itens": [
                    "Desenvolvi websites, landing pages e SPAs com HTML, CSS, JavaScript e React.",
                    "Integrei APIs, corrigi bugs e melhorei performance mobile.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "Produto SaaS full stack de CRM e atendimento.",
            },
            {
                "nome": "Pulse",
                "url": "https://pulse-rangel1.vercel.app",
                "desc": "App TypeScript de controle financeiro. github.com/Rafael-Rangel/pulse",
            },
            {
                "nome": "Portfólio",
                "url": "https://rafael-rangel.github.io/portfolio/",
                "desc": "Portfólio atual: rafael-rangel.github.io/portfolio",
            },
        ],
        "skills": [
            "<b>Frontend:</b> React, Next.js, HTML, CSS, JavaScript, TypeScript",
            "<b>Backend:</b> Node.js, NestJS, PostgreSQL, REST, webhooks",
            "<b>Ferramentas:</b> Git, Docker, AWS, Azure, WordPress",
        ],
    },
    {
        "id": "full-stack-developer",
        "lang": "en",
        "pasta": "Full Stack Developer (Mid)",
        "arquivo": "Resume.html",
        "pdf": "Resume.pdf",
        "cargo": "Full Stack Developer",
        "headline": "React  ·  Next.js  ·  Node.js  ·  TypeScript  ·  PostgreSQL  ·  Integrations",
        "resumo": (
            "Full-stack developer: HTML, CSS, JavaScript, TypeScript, React, Next.js, Node.js, NestJS, "
            "PostgreSQL, REST, webhooks, SPA, PWA, WordPress, Git, Docker, AWS, Azure, Vercel, integrations, "
            "WhatsApp, Instagram, APIs, landing pages, e-commerce, SEO, Lighthouse, Core Web Vitals, "
            "dashboards, UX/UI, components, SaaS, CRM, AI, RAG."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Present",
                "cargo": "Software Engineering Director & Software Engineer",
                "empresa": "SaaS · Rio de Janeiro, Brazil",
                "itens": [
                    "Developed CRM and admin dashboards in React/Next.js with TypeScript.",
                    "Implemented Node.js/NestJS backends, REST APIs, and WhatsApp/Instagram webhooks.",
                    "Integrated AI features (agents, RAG, system prompts) into support flows.",
                    "Deployed and maintained apps on Docker/VPS.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Web · Rio de Janeiro, Brazil",
                "itens": [
                    "Built websites, landing pages, and SPAs with HTML, CSS, JavaScript, and React.",
                    "Integrated APIs, fixed bugs, and improved mobile performance.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "Full-stack SaaS CRM and support product.",
            },
            {
                "nome": "Pulse",
                "url": "https://pulse-rangel1.vercel.app",
                "desc": "TypeScript personal-finance app. github.com/Rafael-Rangel/pulse",
            },
            {
                "nome": "Portfolio",
                "url": "https://rafael-rangel.github.io/portfolio/",
                "desc": "Current portfolio: rafael-rangel.github.io/portfolio",
            },
        ],
        "skills": [
            "<b>Frontend:</b> React, Next.js, HTML, CSS, JavaScript, TypeScript",
            "<b>Backend:</b> Node.js, NestJS, PostgreSQL, REST, webhooks",
            "<b>Tools:</b> Git, Docker, AWS, Azure, WordPress",
        ],
    },
]
