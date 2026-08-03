from pathlib import Path
from datetime import date
import html
import json
import re

ROOT = Path("public")
BASE = "https://rodrigocantinhomaldonado.com"
TODAY = date.today().isoformat()

PAGES = [
    {
        "slug": "airbnb-em-ipanema",
        "title": "Airbnb em Ipanema | Rodrigo Cantinho Maldonado",
        "description": "Conheça a atuação de Rodrigo Cantinho Maldonado com apartamentos de temporada e hospedagens de alto padrão em Ipanema, Rio de Janeiro.",
        "h1": "Airbnb em Ipanema",
        "eyebrow": "Hospedagem de alto padrão",
        "intro": "Ipanema reúne praia, gastronomia, mobilidade e serviços em uma das localizações mais desejadas do Rio de Janeiro. Rodrigo Cantinho Maldonado atua com imóveis de temporada selecionados para hóspedes que valorizam localização, conforto e atendimento próximo.",
        "sections": [
            ("Experiência em Ipanema", "A proposta é oferecer estadias organizadas, com comunicação clara, orientação antes da chegada e suporte durante a hospedagem. Cada imóvel mantém identidade própria e informações transparentes sobre estrutura, regras e localização."),
            ("Para quem busca praticidade", "Os apartamentos atendem viagens de lazer, períodos de trabalho e estadias familiares. A seleção prioriza acesso fácil à praia, comércio, restaurantes e aos principais pontos da Zona Sul."),
            ("Reserva e disponibilidade", "As condições, datas e características variam por imóvel. Consulte o portfólio e solicite informações atualizadas antes de reservar.")
        ],
        "keywords": ["Airbnb em Ipanema", "apartamento de temporada em Ipanema", "hospedagem em Ipanema"]
    },
    {
        "slug": "casas-de-temporada-ipanema",
        "title": "Casas e apartamentos de temporada em Ipanema",
        "description": "Opções de casas e apartamentos de temporada em Ipanema associadas ao portfólio de Rodrigo Cantinho Maldonado.",
        "h1": "Casas e apartamentos de temporada em Ipanema",
        "eyebrow": "Rio de Janeiro",
        "intro": "Para quem deseja permanecer em Ipanema com mais privacidade e autonomia, imóveis de temporada podem oferecer uma experiência mais completa do que a hospedagem convencional.",
        "sections": [
            ("Localização estratégica", "Ipanema permite conciliar praia, restaurantes, compras, cultura e deslocamentos rápidos para Leblon, Copacabana e Lagoa."),
            ("Imóveis selecionados", "O portfólio valoriza boa apresentação, manutenção, organização e descrições objetivas para reduzir surpresas durante a estadia."),
            ("Atendimento direto", "O contato próximo facilita o alinhamento de expectativas e a resolução ágil de dúvidas antes e durante a hospedagem.")
        ],
        "keywords": ["casas de temporada Ipanema", "apartamentos por temporada Ipanema", "aluguel de temporada Ipanema"]
    },
    {
        "slug": "airbnb-barra-da-tijuca",
        "title": "Airbnb na Barra da Tijuca | Hospedagem de alto padrão",
        "description": "Airbnb e imóveis de temporada na Barra da Tijuca com foco em conforto, espaço e atendimento de alto padrão.",
        "h1": "Airbnb na Barra da Tijuca",
        "eyebrow": "Espaço, lazer e conforto",
        "intro": "A Barra da Tijuca é uma escolha estratégica para famílias, grupos e viajantes que procuram imóveis amplos, áreas de lazer e acesso a praias, centros empresariais, eventos e shopping centers.",
        "sections": [
            ("Perfil das hospedagens", "As opções podem incluir apartamentos e casas com estrutura para estadias curtas ou prolongadas, sempre com regras e capacidade informadas de forma objetiva."),
            ("Vantagens da Barra", "A região combina praia, condomínios completos, gastronomia, entretenimento e conexão com diferentes áreas do Rio de Janeiro."),
            ("Planejamento da estadia", "Antes da reserva, confirme localização, número de hóspedes, datas, necessidades específicas e condições de acesso ao condomínio.")
        ],
        "keywords": ["Airbnb Barra da Tijuca", "temporada Barra da Tijuca", "hospedagem de luxo Barra da Tijuca"]
    },
    {
        "slug": "casas-de-temporada-barra-da-tijuca",
        "title": "Casas de temporada na Barra da Tijuca",
        "description": "Casas de temporada na Barra da Tijuca para famílias e grupos que buscam espaço, lazer e boa localização no Rio de Janeiro.",
        "h1": "Casas de temporada na Barra da Tijuca",
        "eyebrow": "Portfólio de hospedagem",
        "intro": "Casas de temporada na Barra da Tijuca atendem quem procura mais espaço, privacidade e convivência, especialmente em viagens familiares e estadias em grupo.",
        "sections": [
            ("Conforto para grupos", "A distribuição dos ambientes, áreas sociais e infraestrutura de lazer pode tornar a estadia mais funcional para famílias e grupos maiores."),
            ("Condomínios e segurança", "Cada imóvel possui regras próprias de acesso, identificação de hóspedes, uso das áreas comuns e horários. Essas condições são informadas antes da confirmação."),
            ("Escolha responsável", "A melhor opção depende da composição do grupo, objetivo da viagem, deslocamentos previstos e orçamento total.")
        ],
        "keywords": ["casas de temporada Barra da Tijuca", "casa Airbnb Barra", "aluguel temporada Barra"]
    },
    {
        "slug": "quinta-do-lago-casas-de-temporada",
        "title": "Casas de temporada no Quinta do Lago",
        "description": "Portfólio de casas de temporada de Rodrigo Cantinho Maldonado no Quinta do Lago, com foco em lazer, privacidade e atendimento.",
        "h1": "Casas de temporada no Quinta do Lago",
        "eyebrow": "Portfólio especializado",
        "intro": "Rodrigo Cantinho Maldonado mantém atuação concentrada em casas de temporada no Quinta do Lago, reunindo imóveis voltados a famílias e grupos que buscam lazer, conforto e privacidade.",
        "sections": [
            ("Experiência no condomínio", "A familiaridade com a operação local permite orientar hóspedes sobre acesso, regras, estrutura das casas e planejamento da chegada."),
            ("Casas para diferentes perfis", "O portfólio contempla necessidades distintas de capacidade, lazer e configuração de quartos. A indicação deve considerar o tamanho do grupo e o objetivo da estadia."),
            ("Atendimento e transparência", "Informações sobre aquecimento de piscina, equipe de apoio, regras de uso e eventuais serviços adicionais devem ser confirmadas previamente.")
        ],
        "keywords": ["Quinta do Lago casas de temporada", "Airbnb Quinta do Lago", "casa de luxo Quinta do Lago"]
    },
    {
        "slug": "hospedagem-de-luxo-rio-de-janeiro",
        "title": "Hospedagem de luxo no Rio de Janeiro",
        "description": "Hospedagens de alto padrão em Ipanema, Barra da Tijuca e Quinta do Lago ligadas ao portfólio de Rodrigo Cantinho Maldonado.",
        "h1": "Hospedagem de luxo no Rio de Janeiro",
        "eyebrow": "Ipanema, Barra e Quinta do Lago",
        "intro": "O portfólio de Rodrigo Cantinho Maldonado reúne imóveis de temporada em regiões estratégicas do Rio de Janeiro, com propostas diferentes para praia, lazer, viagens familiares e estadias prolongadas.",
        "sections": [
            ("Alto padrão com clareza", "Luxo não se limita à decoração. Envolve limpeza, manutenção, comunicação, organização, localização e coerência entre anúncio e experiência real."),
            ("Escolha por região", "Ipanema oferece vida urbana e praia; a Barra favorece espaço e lazer; o Quinta do Lago atende grupos que priorizam casas completas e ambiente residencial."),
            ("Reserva consciente", "Compare capacidade, regras, taxas, serviços, política de cancelamento e custo total antes da decisão.")
        ],
        "keywords": ["hospedagem de luxo Rio de Janeiro", "Airbnb de luxo Rio", "temporada alto padrão Rio"]
    },
    {
        "slug": "administracao-de-airbnb",
        "title": "Administração de Airbnb e imóveis de temporada",
        "description": "Conheça os princípios de gestão de hospedagens e imóveis de temporada aplicados por Rodrigo Cantinho Maldonado.",
        "h1": "Administração de Airbnb e imóveis de temporada",
        "eyebrow": "Operação e experiência do hóspede",
        "intro": "A gestão de um imóvel de temporada exige rotina operacional, comunicação, manutenção preventiva e controle rigoroso da experiência oferecida ao hóspede.",
        "sections": [
            ("Operação consistente", "Checklists de limpeza, vistoria, enxoval, manutenção e preparação reduzem falhas e protegem o ativo imobiliário."),
            ("Comunicação objetiva", "Orientações de chegada, regras da casa e canais de suporte precisam ser simples, antecipados e facilmente acessíveis."),
            ("Reputação e melhoria contínua", "Avaliações devem ser analisadas como dados operacionais. Pontos recorrentes orientam investimentos e correções prioritárias.")
        ],
        "keywords": ["administração de Airbnb", "gestão de imóveis de temporada", "gestão de hospedagem"]
    },
    {
        "slug": "portfolio-de-hospedagens",
        "title": "Portfólio de hospedagens | Rodrigo Cantinho Maldonado",
        "description": "Visão geral do portfólio de hospedagens de Rodrigo Cantinho Maldonado em Ipanema, Barra da Tijuca e Quinta do Lago.",
        "h1": "Portfólio de hospedagens",
        "eyebrow": "Imóveis de temporada",
        "intro": "O portfólio reúne apartamentos e casas de temporada em Ipanema, Barra da Tijuca e Quinta do Lago, com opções voltadas a diferentes perfis de viagem.",
        "sections": [
            ("Ipanema", "Apartamentos para quem valoriza praia, serviços, gastronomia e localização central na Zona Sul."),
            ("Barra da Tijuca", "Imóveis amplos para famílias, grupos, eventos e estadias que demandam lazer e estrutura."),
            ("Quinta do Lago", "Casas de temporada com foco em privacidade, convivência e experiência residencial completa.")
        ],
        "keywords": ["portfólio Airbnb", "imóveis de temporada Rio", "Rodrigo Cantinho Maldonado Airbnb"]
    },
    {
        "slug": "quem-e-rodrigo-cantinho-maldonado",
        "title": "Quem é Rodrigo Cantinho Maldonado",
        "description": "Conheça a trajetória, os projetos e a atuação de Rodrigo Cantinho Maldonado em negócios, imóveis e hospedagem.",
        "h1": "Quem é Rodrigo Cantinho Maldonado",
        "eyebrow": "Perfil oficial",
        "intro": "Rodrigo Cantinho Maldonado é empresário e atua em projetos ligados a imóveis, hospitalidade, presença digital e oportunidades de negócio no Rio de Janeiro.",
        "sections": [
            ("Atuação", "Sua atuação combina visão empresarial, gestão de ativos imobiliários, desenvolvimento de projetos digitais e operação de hospedagens de temporada."),
            ("Projetos", "Entre as iniciativas estão o portfólio de casas e apartamentos de temporada e projetos digitais voltados ao mercado imobiliário de alto padrão."),
            ("Princípios", "Transparência, agilidade, valorização patrimonial e experiência do cliente orientam as decisões e a evolução dos projetos.")
        ],
        "keywords": ["Rodrigo Cantinho Maldonado", "quem é Rodrigo Cantinho Maldonado", "empresário Rodrigo Maldonado"]
    },
    {
        "slug": "projetos-de-rodrigo-cantinho-maldonado",
        "title": "Projetos de Rodrigo Cantinho Maldonado",
        "description": "Conheça os projetos empresariais, imobiliários, digitais e de hospedagem de Rodrigo Cantinho Maldonado.",
        "h1": "Projetos de Rodrigo Cantinho Maldonado",
        "eyebrow": "Negócios e ativos digitais",
        "intro": "Os projetos de Rodrigo Cantinho Maldonado conectam imóveis, hospitalidade, tecnologia, comunicação e construção de marcas digitais.",
        "sections": [
            ("Hospitalidade", "Desenvolvimento e operação de experiências de hospedagem em imóveis de temporada no Rio de Janeiro."),
            ("Mercado imobiliário", "Projetos de apresentação, divulgação e negociação de imóveis, com uso de canais digitais próprios."),
            ("Presença digital", "Criação de sites, conteúdos e ativos que organizam informações, ampliam alcance e fortalecem reputação.")
        ],
        "keywords": ["projetos Rodrigo Cantinho Maldonado", "negócios Rodrigo Maldonado", "empreendedorismo imobiliário"]
    },
    {
        "slug": "investimentos-imobiliarios-rio-de-janeiro",
        "title": "Investimentos imobiliários no Rio de Janeiro",
        "description": "Conteúdo sobre análise e gestão de investimentos imobiliários no Rio de Janeiro por Rodrigo Cantinho Maldonado.",
        "h1": "Investimentos imobiliários no Rio de Janeiro",
        "eyebrow": "Análise patrimonial",
        "intro": "Investir em imóveis exige comparar preço, liquidez, estado de conservação, documentação, custo de capital e potencial de uso ou renda.",
        "sections": [
            ("Análise financeira", "O preço de aquisição deve ser avaliado junto com condomínio, IPTU, reforma, manutenção, impostos e custo do financiamento."),
            ("Risco jurídico", "Matrícula, certidões, titularidade, ônus e condições contratuais precisam ser verificados antes de qualquer pagamento relevante."),
            ("Estratégia de saída", "Liquidez e público comprador importam tanto quanto a expectativa de valorização. Um bom ativo precisa ter alternativas de uso e venda.")
        ],
        "keywords": ["investimentos imobiliários Rio", "imóveis de alto padrão", "análise de imóveis"]
    },
    {
        "slug": "contato-hospedagens",
        "title": "Contato para hospedagens | Rodrigo Cantinho Maldonado",
        "description": "Entre em contato para informações sobre imóveis de temporada em Ipanema, Barra da Tijuca e Quinta do Lago.",
        "h1": "Contato para hospedagens",
        "eyebrow": "Disponibilidade e informações",
        "intro": "Para consultar imóveis, disponibilidade e condições de hospedagem em Ipanema, Barra da Tijuca ou Quinta do Lago, utilize os canais oficiais indicados neste site.",
        "sections": [
            ("Antes do contato", "Informe destino, datas, número de hóspedes, composição do grupo e necessidades específicas. Isso permite identificar opções compatíveis."),
            ("Informações atualizadas", "Valores, regras, capacidade e serviços podem variar entre os imóveis. Confirme todos os detalhes antes de efetuar qualquer pagamento."),
            ("Segurança", "Utilize apenas canais oficiais e confira os dados do anúncio e do responsável antes de concluir a reserva.")
        ],
        "keywords": ["contato hospedagem Rodrigo Maldonado", "reservar Airbnb Ipanema", "casas temporada Barra"]
    }
]

STYLE = """
:root{--ink:#18202a;--muted:#5c6570;--paper:#fff;--soft:#f4f1eb;--accent:#9a6a33;--line:#ded8cf}*{box-sizing:border-box}body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;color:var(--ink);background:var(--paper);line-height:1.65}a{color:inherit}.wrap{max-width:1080px;margin:auto;padding:0 24px}.top{border-bottom:1px solid var(--line);background:#fff}.nav{height:76px;display:flex;align-items:center;justify-content:space-between;gap:24px}.brand{text-decoration:none;font-weight:750;letter-spacing:-.02em}.links{display:flex;gap:20px;flex-wrap:wrap}.links a{text-decoration:none;color:var(--muted);font-size:.94rem}.hero{padding:96px 0 72px;background:linear-gradient(135deg,#f7f4ef,#fff)}.eyebrow{text-transform:uppercase;letter-spacing:.14em;font-size:.78rem;font-weight:800;color:var(--accent)}h1{font-family:Georgia,serif;font-size:clamp(2.5rem,6vw,5rem);line-height:1.02;max-width:900px;margin:.25em 0}.lead{font-size:1.18rem;max-width:780px;color:var(--muted)}.content{padding:70px 0}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.card{border:1px solid var(--line);border-radius:18px;padding:28px;background:#fff}.card h2{font-size:1.25rem;margin-top:0}.cta{margin-top:48px;padding:34px;border-radius:20px;background:var(--ink);color:#fff}.cta a{display:inline-block;margin-top:12px;padding:12px 18px;border-radius:999px;background:#fff;color:var(--ink);text-decoration:none;font-weight:700}.related{padding:64px 0;background:var(--soft)}.related h2{font-family:Georgia,serif;font-size:2rem}.related-list{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.related-list a{padding:18px;border:1px solid var(--line);border-radius:14px;text-decoration:none;background:white}.footer{padding:38px 0;color:var(--muted);font-size:.9rem;border-top:1px solid var(--line)}@media(max-width:760px){.nav{height:auto;padding:18px 0;align-items:flex-start;flex-direction:column}.links{gap:12px}.hero{padding:62px 0 52px}.grid,.related-list{grid-template-columns:1fr}}
"""

def render(page):
    url = f"{BASE}/{page['slug']}/"
    structured = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": page["h1"],
        "description": page["description"],
        "url": url,
        "about": {"@type": "Person", "name": "Rodrigo Cantinho Maldonado", "url": BASE},
        "isPartOf": {"@type": "WebSite", "name": "Rodrigo Cantinho Maldonado", "url": BASE},
        "inLanguage": "pt-BR",
        "dateModified": TODAY,
        "keywords": page["keywords"]
    }
    cards = "".join(f"<article class='card'><h2>{html.escape(title)}</h2><p>{html.escape(text)}</p></article>" for title, text in page["sections"])
    related = [p for p in PAGES if p["slug"] != page["slug"]][:6]
    related_html = "".join(f"<a href='/{p['slug']}/'>{html.escape(p['h1'])}</a>" for p in related)
    return f"""<!doctype html>
<html lang='pt-BR'>
<head>
<meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>{html.escape(page['title'])}</title>
<meta name='description' content='{html.escape(page['description'], quote=True)}'>
<meta name='robots' content='index,follow,max-image-preview:large'>
<link rel='canonical' href='{url}'>
<meta property='og:type' content='website'><meta property='og:locale' content='pt_BR'><meta property='og:title' content='{html.escape(page['title'], quote=True)}'><meta property='og:description' content='{html.escape(page['description'], quote=True)}'><meta property='og:url' content='{url}'>
<meta name='twitter:card' content='summary_large_image'>
<style>{STYLE}</style>
<script type='application/ld+json'>{json.dumps(structured, ensure_ascii=False)}</script>
</head>
<body>
<header class='top'><div class='wrap nav'><a class='brand' href='/'>Rodrigo Cantinho Maldonado</a><nav class='links' aria-label='Principal'><a href='/sobre/'>Sobre</a><a href='/portfolio-de-hospedagens/'>Hospedagens</a><a href='/projetos/'>Projetos</a><a href='/artigos/'>Artigos</a><a href='/contato/'>Contato</a></nav></div></header>
<main><section class='hero'><div class='wrap'><div class='eyebrow'>{html.escape(page['eyebrow'])}</div><h1>{html.escape(page['h1'])}</h1><p class='lead'>{html.escape(page['intro'])}</p></div></section>
<section class='content'><div class='wrap'><div class='grid'>{cards}</div><div class='cta'><h2>Consulte o portfólio e as condições atuais</h2><p>As informações específicas de cada imóvel, disponibilidade e regras são confirmadas pelos canais oficiais.</p><a href='/contato/'>Entrar em contato</a></div></div></section>
<section class='related'><div class='wrap'><h2>Conteúdos relacionados</h2><div class='related-list'>{related_html}</div></div></section></main>
<footer class='footer'><div class='wrap'>© {date.today().year} Rodrigo Cantinho Maldonado · Site oficial</div></footer>
</body></html>"""

for page in PAGES:
    folder = ROOT / page["slug"]
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.html").write_text(render(page), encoding="utf-8")

# Add a prominent hospitality block to the existing homepage while preserving its design.
home = ROOT / "index.html"
if home.exists():
    text = home.read_text(encoding="utf-8")
    marker = "<!-- seo-hospitality-hub -->"
    if marker not in text:
        block = f"""{marker}<section style='padding:64px 24px;background:#f4f1eb'><div style='max-width:1080px;margin:auto'><p style='text-transform:uppercase;letter-spacing:.14em;font-size:.78rem;font-weight:800;color:#9a6a33'>Hospedagens</p><h2 style='font:700 clamp(2rem,4vw,3.4rem)/1.08 Georgia,serif;margin:.2em 0'>Airbnbs e casas de temporada no Rio de Janeiro</h2><p style='max-width:780px;color:#5c6570;font-size:1.08rem'>Rodrigo Cantinho Maldonado mantém um portfólio de apartamentos e casas de temporada em Ipanema, Barra da Tijuca e Quinta do Lago, com foco em conforto, organização e atendimento próximo.</p><div style='display:flex;gap:12px;flex-wrap:wrap;margin-top:24px'><a href='/portfolio-de-hospedagens/' style='padding:12px 18px;border-radius:999px;background:#18202a;color:white;text-decoration:none;font-weight:700'>Ver portfólio</a><a href='/airbnb-em-ipanema/' style='padding:12px 18px;border-radius:999px;border:1px solid #18202a;color:#18202a;text-decoration:none;font-weight:700'>Airbnb em Ipanema</a><a href='/casas-de-temporada-barra-da-tijuca/' style='padding:12px 18px;border-radius:999px;border:1px solid #18202a;color:#18202a;text-decoration:none;font-weight:700'>Casas na Barra</a><a href='/quinta-do-lago-casas-de-temporada/' style='padding:12px 18px;border-radius:999px;border:1px solid #18202a;color:#18202a;text-decoration:none;font-weight:700'>Quinta do Lago</a></div></div></section>"""
        text = re.sub(r"</main>", block + "</main>", text, count=1, flags=re.I) if re.search(r"</main>", text, re.I) else text.replace("</body>", block + "</body>")
        home.write_text(text, encoding="utf-8")

# Add generated URLs to the existing sitemap, preserving all current entries.
sitemap = ROOT / "sitemap.xml"
if sitemap.exists():
    xml = sitemap.read_text(encoding="utf-8")
    entries = ""
    for page in PAGES:
        loc = f"{BASE}/{page['slug']}/"
        if loc not in xml:
            entries += f"\n  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>"
    xml = xml.replace("</urlset>", entries + "\n</urlset>")
    sitemap.write_text(xml, encoding="utf-8")

print(f"Generated {len(PAGES)} SEO landing pages and updated homepage/sitemap")
