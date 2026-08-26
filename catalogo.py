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
        "headline": "AI Engineer  ·  RAG  ·  Embeddings  ·  Agents  ·  LLM APIs  ·  Segurança de modelos",
        "resumo": (
            "Eu projeto e implemento inteligência artificial dentro de produtos reais: RAG, embeddings, "
            "agentes, knowledge base e automação de atendimento. Eu conecto LLMs a CRMs, WhatsApp e APIs "
            "com isolamento de contexto por tenant, avaliação de custo/latência e guardrails. "
            "Eu atuo na Genesis Company como Diretor do Departamento de Software e Software Engineer."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Atual",
                "cargo": "Diretor do Departamento de Software & Software Engineer",
                "empresa": "Genesis Company · Rio de Janeiro, RJ",
                "itens": [
                    "Eu dirigi a engenharia de IA aplicada a CRM e atendimento: agentes, RAG, FAQ e roteamento.",
                    "Eu implementei pipelines de RAG (chunking, embeddings, retrieval, rerank e grounding no contexto).",
                    "Eu modelei bases vetoriais e políticas de atualização da knowledge base por organização.",
                    "Eu desenhei agentes com function calling, memória de sessão e handoff para humano.",
                    "Eu apliquei guardrails: prompt injection, PII, isolamento de tenant e controle de tokens.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Webmaker · Rio de Janeiro, RJ",
                "itens": [
                    "Eu desenvolvi aplicações web e integrei APIs que depois passaram a alimentar fluxos com IA.",
                    "Eu otimizei performance e SEO técnico em React, Next.js, HTML, CSS e JavaScript.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "SaaS de CRM com agentes de IA, RAG e atendimento omnichannel (WhatsApp/Instagram).",
            },
            {
                "nome": "Rubi 2.0 / Conversation AI",
                "url": "https://github.com/Rafael-Rangel/rubi-teste",
                "desc": "Agentes conversacionais, system prompts, knowledge base e RAG em produto de atendimento.",
            },
            {
                "nome": "Inglês conversacional para Devs",
                "url": "https://github.com/Rafael-Rangel/ingles-conversacional-devs",
                "desc": "Professor de IA com embeddings de contexto e prática de prompt para desenvolvedores.",
            },
        ],
        "skills": [
            "<b>IA:</b> RAG, embeddings, vector search, rerank, agents, function calling, prompt engineering, evals",
            "<b>Modelos e APIs:</b> OpenAI, LLMOps, token/custo, cache de embeddings, transcrição, knowledge base",
            "<b>Engenharia:</b> TypeScript, Python, Node.js, NestJS, React, Next.js, PostgreSQL, APIs REST, webhooks",
            "<b>Cloud e segurança:</b> AWS, Azure, Docker, isolamento de tenant, OWASP, PII, secrets",
        ],
    },
    {
        "id": "ai-engineer",
        "lang": "en",
        "pasta": "AI Engineering",
        "arquivo": "Resume.html",
        "pdf": "Resume.pdf",
        "cargo": "AI Engineer",
        "headline": "AI Engineer  ·  RAG  ·  Embeddings  ·  Agents  ·  LLM APIs  ·  Model security",
        "resumo": (
            "I design and ship AI inside real products: RAG, embeddings, agents, knowledge bases, and "
            "automated support. I connect LLMs to CRMs, WhatsApp, and APIs with per-tenant context isolation, "
            "cost/latency evaluation, and guardrails. I currently work at Genesis Company as Software "
            "Engineering Director and Software Engineer."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Present",
                "cargo": "Software Engineering Director & Software Engineer",
                "empresa": "Genesis Company · Rio de Janeiro, Brazil",
                "itens": [
                    "I led applied AI engineering for CRM and support: agents, RAG, FAQ, and routing.",
                    "I implemented RAG pipelines (chunking, embeddings, retrieval, rerank, and grounded answers).",
                    "I modeled vector stores and knowledge-base refresh policies per organization.",
                    "I designed agents with function calling, session memory, and human handoff.",
                    "I applied guardrails: prompt injection, PII, tenant isolation, and token control.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Webmaker · Rio de Janeiro, Brazil",
                "itens": [
                    "I built web apps and API integrations that later fed AI-backed workflows.",
                    "I improved performance and technical SEO with React, Next.js, HTML, CSS, and JavaScript.",
                ],
            },
        ],
        "projetos": [
            {
                "nome": "KoruVision CRM",
                "url": "https://github.com/Rafael-Rangel/koruvision-landing",
                "desc": "SaaS CRM with AI agents, RAG, and omnichannel support (WhatsApp/Instagram).",
            },
            {
                "nome": "Rubi 2.0 / Conversation AI",
                "url": "https://github.com/Rafael-Rangel/rubi-teste",
                "desc": "Conversational agents, system prompts, knowledge base, and RAG in a support product.",
            },
            {
                "nome": "Conversational English for Devs",
                "url": "https://github.com/Rafael-Rangel/ingles-conversacional-devs",
                "desc": "AI tutor with contextual embeddings and prompt practice for developers.",
            },
        ],
        "skills": [
            "<b>AI:</b> RAG, embeddings, vector search, rerank, agents, function calling, prompt engineering, evals",
            "<b>Models & APIs:</b> OpenAI, LLMOps, token/cost, embedding cache, transcription, knowledge base",
            "<b>Engineering:</b> TypeScript, Python, Node.js, NestJS, React, Next.js, PostgreSQL, REST, webhooks",
            "<b>Cloud & security:</b> AWS, Azure, Docker, tenant isolation, OWASP, PII, secrets",
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
            "Eu defino arquitetura de sistemas SaaS ponta a ponta: multi-tenancy, APIs, filas, segurança e "
            "escala horizontal. Eu transformo requisitos de negócio em contratos, limites de isolamento e "
            "decisões de cloud (AWS e Azure). Eu dirijo o Departamento de Software na Genesis Company."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Atual",
                "cargo": "Diretor do Departamento de Software & Software Engineer",
                "empresa": "Genesis Company · Rio de Janeiro, RJ",
                "itens": [
                    "Eu dirigi as decisões de arquitetura de plataformas SaaS multi-tenant (workspaces, RBAC, isolamento de dados).",
                    "Eu projetei APIs, webhooks, filas e processamento assíncrono para picos de mensageria (WhatsApp/Meta).",
                    "Eu defini caminhos de escala: load balancing, múltiplas instâncias, rate limit e circuit breaker.",
                    "Eu modelei segurança: autenticação, autorização, secrets, OWASP API e isolamento por tenant.",
                    "Eu orientei deploy em VPS/Docker e desenhei o uso de AWS e Azure (compute, identity, storage).",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Webmaker · Rio de Janeiro, RJ",
                "itens": [
                    "Eu estruturei frontends e integrações com foco em performance, SEO e contratos de API.",
                    "Eu documentei fluxos e evoluí sistemas de clientes sem quebrar operação.",
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
            "I define end-to-end SaaS architecture: multi-tenancy, APIs, queues, security, and horizontal scale. "
            "I turn business requirements into contracts, isolation boundaries, and cloud decisions (AWS and Azure). "
            "I lead the Software Department at Genesis Company."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Present",
                "cargo": "Software Engineering Director & Software Engineer",
                "empresa": "Genesis Company · Rio de Janeiro, Brazil",
                "itens": [
                    "I led architecture for multi-tenant SaaS (workspaces, RBAC, data isolation).",
                    "I designed APIs, webhooks, queues, and async processing for messaging spikes (WhatsApp/Meta).",
                    "I defined scale paths: load balancing, multi-instance, rate limiting, and circuit breaking.",
                    "I modeled security: authn/authz, secrets, OWASP API, and per-tenant isolation.",
                    "I guided Docker/VPS delivery and cloud usage on AWS and Azure (compute, identity, storage).",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Webmaker · Rio de Janeiro, Brazil",
                "itens": [
                    "I structured frontends and integrations with performance, SEO, and API contracts in mind.",
                    "I documented flows and evolved client systems without breaking operations.",
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
            "Eu desenvolvo software full stack em TypeScript: React/Next.js, Node.js/NestJS, PostgreSQL, "
            "APIs REST e webhooks. Eu entrego produto com qualidade de engenharia — testes mentais de contrato, "
            "performance e operação. Eu atuo na Genesis Company na liderança técnica e na implementação."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Atual",
                "cargo": "Diretor do Departamento de Software & Software Engineer",
                "empresa": "Genesis Company · Rio de Janeiro, RJ",
                "itens": [
                    "Eu desenvolvi plataformas SaaS multi-tenant (CRM, inbox, permissões, dashboards) em React e Node.js.",
                    "Eu implementei APIs REST, webhooks e filas para WhatsApp, Instagram e Meta Cloud API.",
                    "Eu integrei IA (RAG e agentes) sem acoplar o domínio de negócio ao provedor do modelo.",
                    "Eu acompanhei performance (Core Web Vitals) e evolução contínua dos sistemas.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Webmaker · Rio de Janeiro, RJ",
                "itens": [
                    "Eu desenvolvi sites, landing pages e SPAs com HTML, CSS, JavaScript, React e Next.js.",
                    "Eu integrei APIs, corrigi falhas e otimizei Lighthouse/SEO técnico.",
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
            "I build full-stack software in TypeScript: React/Next.js, Node.js/NestJS, PostgreSQL, REST APIs, "
            "and webhooks. I ship with engineering quality — contracts, performance, and operations. "
            "I work at Genesis Company in technical leadership and hands-on implementation."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Present",
                "cargo": "Software Engineering Director & Software Engineer",
                "empresa": "Genesis Company · Rio de Janeiro, Brazil",
                "itens": [
                    "I built multi-tenant SaaS platforms (CRM, inbox, permissions, dashboards) with React and Node.js.",
                    "I implemented REST APIs, webhooks, and queues for WhatsApp, Instagram, and Meta Cloud API.",
                    "I integrated AI (RAG and agents) without coupling domain logic to a single model vendor.",
                    "I tracked Core Web Vitals and continuous system evolution.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Webmaker · Rio de Janeiro, Brazil",
                "itens": [
                    "I developed sites, landing pages, and SPAs with HTML, CSS, JavaScript, React, and Next.js.",
                    "I integrated APIs, fixed defects, and improved Lighthouse/technical SEO.",
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
            "Eu analiso processos, levanto requisitos e transformo regras de negócio em especificações "
            "técnicas executáveis. Eu mapeio integrações, eventos, dados e riscos de sistemas SaaS. "
            "Eu atuo na Genesis Company ligando negócio, produto e engenharia."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Atual",
                "cargo": "Diretor do Departamento de Software & Software Engineer",
                "empresa": "Genesis Company · Rio de Janeiro, RJ",
                "itens": [
                    "Eu levantei requisitos de CRM, atendimento e multi-tenancy e os traduzi em fluxos e contratos de API.",
                    "Eu analisei integrações WhatsApp/Meta/Instagram: webhooks, filas, falhas e regras de horário.",
                    "Eu modelei dados de organizações, permissões, conversas, leads e métricas.",
                    "Eu documentei regras de automação, IA e handoff humano para o time executar com clareza.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Webmaker · Rio de Janeiro, RJ",
                "itens": [
                    "Eu levantei necessidades de clientes e transformei em sites, landing pages e integrações.",
                    "Eu especifiquei ajustes de SEO, performance e manutenção contínua.",
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
            "I analyze processes, gather requirements, and turn business rules into executable technical specs. "
            "I map integrations, events, data, and risk in SaaS systems. I work at Genesis Company connecting "
            "business, product, and engineering."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Present",
                "cargo": "Software Engineering Director & Software Engineer",
                "empresa": "Genesis Company · Rio de Janeiro, Brazil",
                "itens": [
                    "I gathered CRM, support, and multi-tenancy requirements and translated them into flows and API contracts.",
                    "I analyzed WhatsApp/Meta/Instagram integrations: webhooks, queues, failure modes, and business hours.",
                    "I modeled data for organizations, permissions, conversations, leads, and metrics.",
                    "I documented automation, AI, and human-handoff rules so delivery stayed unambiguous.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Webmaker · Rio de Janeiro, Brazil",
                "itens": [
                    "I gathered client needs and turned them into sites, landing pages, and integrations.",
                    "I specified SEO, performance, and ongoing maintenance work.",
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
            "Eu desenvolvo aplicações web full stack com TypeScript, React, Next.js, Node.js e PostgreSQL. "
            "Eu entrego interface, API, integração e publish. Eu trabalho na Genesis Company construindo "
            "produtos SaaS e canais de comunicação."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Atual",
                "cargo": "Diretor do Departamento de Software & Software Engineer",
                "empresa": "Genesis Company · Rio de Janeiro, RJ",
                "itens": [
                    "Eu desenvolvi CRM e painéis administrativos em React/Next.js com TypeScript.",
                    "Eu implementei backends Node.js/NestJS, APIs REST e webhooks de WhatsApp e Instagram.",
                    "Eu integrei recursos de IA (agentes e RAG) em fluxos de atendimento.",
                    "Eu publiquei e mantive aplicações em Docker/VPS.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Webmaker · Rio de Janeiro, RJ",
                "itens": [
                    "Eu desenvolvi websites, landing pages e SPAs com HTML, CSS, JavaScript e React.",
                    "Eu integrei APIs, corrigi bugs e melhorei performance mobile.",
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
            "I build full-stack web applications with TypeScript, React, Next.js, Node.js, and PostgreSQL. "
            "I deliver UI, API, integration, and deploy. I work at Genesis Company building SaaS products "
            "and communication channels."
        ),
        "jobs": [
            {
                "periodo": "Jul 2025 – Present",
                "cargo": "Software Engineering Director & Software Engineer",
                "empresa": "Genesis Company · Rio de Janeiro, Brazil",
                "itens": [
                    "I developed CRM and admin dashboards in React/Next.js with TypeScript.",
                    "I implemented Node.js/NestJS backends, REST APIs, and WhatsApp/Instagram webhooks.",
                    "I integrated AI features (agents and RAG) into support flows.",
                    "I deployed and maintained apps on Docker/VPS.",
                ],
            },
            {
                "periodo": "Jul 2024 – Jul 2025",
                "cargo": "Web Developer / Software Developer",
                "empresa": "Webmaker · Rio de Janeiro, Brazil",
                "itens": [
                    "I built websites, landing pages, and SPAs with HTML, CSS, JavaScript, and React.",
                    "I integrated APIs, fixed bugs, and improved mobile performance.",
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
