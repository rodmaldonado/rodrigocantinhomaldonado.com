from pathlib import Path
from datetime import date
import html
import json
import re

ROOT = Path('public')
BASE = 'https://rodrigocantinhomaldonado.com'
TODAY = date.today().isoformat()

PAGES = [
    {
        'slug': 'biografia-rodrigo-cantinho-maldonado',
        'title': 'Biografia de Rodrigo Cantinho Maldonado',
        'description': 'Biografia institucional de Rodrigo Cantinho Maldonado e visão geral de sua atuação em negócios, imóveis, hospitalidade e projetos digitais.',
        'h1': 'Biografia de Rodrigo Cantinho Maldonado',
        'intro': 'Rodrigo Cantinho Maldonado é empresário com atuação em projetos ligados a imóveis, hospitalidade, gestão de ativos e presença digital. Este perfil reúne informações institucionais verificáveis sobre sua trajetória e seus projetos.',
        'topics': [
            ('Atuação empresarial', 'Sua atuação combina análise de oportunidades, gestão patrimonial, desenvolvimento de projetos e organização de operações voltadas ao cliente.'),
            ('Imóveis e hospitalidade', 'Parte relevante de seus projetos está ligada a imóveis de alto padrão, hospedagens de temporada e apresentação digital de ativos imobiliários.'),
            ('Presença digital', 'Sites próprios, conteúdo institucional e canais oficiais são utilizados para organizar informações e reforçar transparência e reputação.')
        ]
    },
    {
        'slug': 'trajetoria-profissional',
        'title': 'Trajetória profissional | Rodrigo Cantinho Maldonado',
        'description': 'Conheça os principais eixos da trajetória profissional de Rodrigo Cantinho Maldonado em negócios, imóveis e hospitalidade.',
        'h1': 'Trajetória profissional',
        'intro': 'A trajetória profissional de Rodrigo Cantinho Maldonado é apresentada por áreas de atuação, sem criar datas, cargos ou resultados que não estejam documentados publicamente.',
        'topics': [
            ('Gestão e negócios', 'A tomada de decisão é orientada por análise de risco, custo de capital, liquidez e potencial de valorização.'),
            ('Mercado imobiliário', 'A atuação inclui avaliação de oportunidades, negociação, apresentação de imóveis e desenvolvimento de ativos digitais de apoio.'),
            ('Experiência do cliente', 'Na hospitalidade, o foco está em organização, comunicação clara, manutenção e melhoria contínua baseada em feedback.')
        ]
    },
    {
        'slug': 'empreendedorismo-imobiliario',
        'title': 'Empreendedorismo imobiliário no Rio de Janeiro',
        'description': 'Conteúdo institucional sobre empreendedorismo imobiliário, análise de oportunidades e gestão de ativos no Rio de Janeiro.',
        'h1': 'Empreendedorismo imobiliário',
        'intro': 'Empreendedorismo imobiliário exige combinar visão comercial, rigor documental, análise financeira e capacidade de posicionar corretamente cada ativo.',
        'topics': [
            ('Análise antes da compra', 'Preço, documentação, reforma, condomínio, impostos e liquidez devem ser avaliados em conjunto.'),
            ('Posicionamento do ativo', 'Fotografia, vídeo, descrição, canais de divulgação e atendimento influenciam diretamente percepção e conversão.'),
            ('Proteção de capital', 'Contratos, diligência e estrutura de pagamento são essenciais para reduzir risco operacional e jurídico.')
        ]
    },
    {
        'slug': 'gestao-de-imoveis-de-temporada',
        'title': 'Gestão de imóveis de temporada',
        'description': 'Princípios de gestão de imóveis de temporada: operação, manutenção, comunicação, reputação e controle financeiro.',
        'h1': 'Gestão de imóveis de temporada',
        'intro': 'Uma operação de temporada eficiente depende de processos repetíveis, controle de custos e consistência na experiência entregue ao hóspede.',
        'topics': [
            ('Operação', 'Check-in, limpeza, enxoval, vistoria e manutenção precisam seguir padrões claros.'),
            ('Reputação', 'Avaliações ajudam a identificar falhas recorrentes e prioridades de investimento.'),
            ('Resultado financeiro', 'Receita deve ser analisada líquida de taxas, manutenção, impostos, equipe e períodos sem ocupação.')
        ]
    },
    {
        'slug': 'faq-airbnb-ipanema',
        'title': 'Perguntas frequentes sobre Airbnb em Ipanema',
        'description': 'Respostas objetivas para dúvidas comuns sobre Airbnb e apartamentos de temporada em Ipanema.',
        'h1': 'Perguntas frequentes sobre Airbnb em Ipanema',
        'intro': 'Estas respostas ajudam hóspedes a avaliar localização, regras, custos e adequação do imóvel antes da reserva.',
        'topics': [
            ('O que confirmar antes de reservar?', 'Datas, número de hóspedes, configuração dos quartos, regras do condomínio, taxas e política de cancelamento.'),
            ('A localização faz diferença?', 'Sim. Distância da praia, metrô, restaurantes e serviços pode alterar significativamente a experiência.'),
            ('Como evitar problemas?', 'Use canais oficiais, confira avaliações, leia regras e mantenha toda a comunicação registrada na plataforma.')
        ],
        'faq': True
    },
    {
        'slug': 'faq-casas-temporada-barra',
        'title': 'Perguntas frequentes sobre casas de temporada na Barra',
        'description': 'Dúvidas comuns sobre casas de temporada na Barra da Tijuca, capacidade, acesso, regras e custos.',
        'h1': 'Perguntas frequentes sobre casas de temporada na Barra',
        'intro': 'Casas amplas exigem atenção especial à capacidade, regras do condomínio, uso das áreas de lazer e logística de chegada.',
        'topics': [
            ('A casa aceita grupos grandes?', 'A capacidade máxima deve ser respeitada e confirmada antes da reserva.'),
            ('Há regras de condomínio?', 'Sim. Cadastro, estacionamento, visitantes, ruído e áreas comuns podem ter regras específicas.'),
            ('Quais custos devo comparar?', 'Além da diária, considere taxa de limpeza, caução, serviços opcionais e deslocamentos.')
        ],
        'faq': True
    },
    {
        'slug': 'faq-quinta-do-lago',
        'title': 'Perguntas frequentes sobre o Quinta do Lago',
        'description': 'Perguntas frequentes sobre casas de temporada no Quinta do Lago, acesso, piscinas, equipe e regras.',
        'h1': 'Perguntas frequentes sobre casas no Quinta do Lago',
        'intro': 'Antes de reservar, é importante entender a estrutura da casa, os serviços incluídos e as regras aplicáveis ao condomínio e à hospedagem.',
        'topics': [
            ('Como funciona o acesso?', 'Dados dos hóspedes e veículos normalmente precisam ser enviados com antecedência.'),
            ('A piscina é aquecida?', 'Isso varia por imóvel e pode exigir acionamento antecipado ou taxa adicional.'),
            ('Há equipe na casa?', 'A presença e o escopo da equipe variam. Confirme horários, serviços e responsabilidades antes da chegada.')
        ],
        'faq': True
    },
    {
        'slug': 'imprensa-e-presenca-digital',
        'title': 'Imprensa e presença digital | Rodrigo Cantinho Maldonado',
        'description': 'Canais oficiais, presença digital e referências públicas de Rodrigo Cantinho Maldonado.',
        'h1': 'Imprensa e presença digital',
        'intro': 'Esta página reúne os canais oficiais e serve como ponto de referência para verificar informações públicas sobre Rodrigo Cantinho Maldonado.',
        'topics': [
            ('Canais oficiais', 'Informações institucionais devem ser confirmadas neste site e nos perfis oficialmente vinculados.'),
            ('Uso de nome e imagem', 'Referências externas devem preservar contexto, precisão e identificação correta.'),
            ('Atualizações', 'Novos projetos, publicações e aparições relevantes podem ser incorporados quando houver fonte verificável.')
        ]
    }
]

STYLE = """
:root{--ink:#18202a;--muted:#5c6570;--soft:#f4f1eb;--accent:#9a6a33;--line:#ded8cf}*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui,sans-serif;color:var(--ink);line-height:1.65}a{color:inherit}.wrap{max-width:1080px;margin:auto;padding:0 24px}.top{border-bottom:1px solid var(--line)}.nav{min-height:76px;display:flex;align-items:center;justify-content:space-between;gap:24px}.brand{text-decoration:none;font-weight:800}.links{display:flex;gap:18px;flex-wrap:wrap}.links a{text-decoration:none;color:var(--muted)}.crumbs{padding:18px 0;font-size:.9rem;color:var(--muted)}.hero{padding:72px 0;background:linear-gradient(135deg,#f7f4ef,#fff)}h1{font:700 clamp(2.5rem,6vw,4.8rem)/1.04 Georgia,serif;margin:.2em 0}.lead{max-width:800px;font-size:1.16rem;color:var(--muted)}.content{padding:64px 0}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.card{border:1px solid var(--line);border-radius:18px;padding:26px}.card h2{font-size:1.2rem;margin-top:0}.cta{margin-top:40px;background:var(--ink);color:white;border-radius:20px;padding:30px}.cta a{display:inline-block;background:white;color:var(--ink);padding:11px 17px;border-radius:999px;text-decoration:none;font-weight:700}.footer{border-top:1px solid var(--line);padding:36px 0;color:var(--muted)}@media(max-width:760px){.nav{align-items:flex-start;flex-direction:column;padding:18px 0}.grid{grid-template-columns:1fr}}
"""

def render(page):
    url = f"{BASE}/{page['slug']}/"
    crumbs = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Início', 'item': BASE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': page['h1'], 'item': url}
        ]
    }
    schemas = [{
        '@context': 'https://schema.org', '@type': 'WebPage', 'name': page['h1'],
        'description': page['description'], 'url': url, 'inLanguage': 'pt-BR',
        'dateModified': TODAY,
        'about': {'@type': 'Person', 'name': 'Rodrigo Cantinho Maldonado', 'url': BASE}
    }, crumbs]
    if page.get('faq'):
        schemas.append({
            '@context': 'https://schema.org', '@type': 'FAQPage',
            'mainEntity': [
                {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}}
                for q, a in page['topics']
            ]
        })
    cards = ''.join(f"<article class='card'><h2>{html.escape(q)}</h2><p>{html.escape(a)}</p></article>" for q,a in page['topics'])
    jsonld = ''.join(f"<script type='application/ld+json'>{json.dumps(s, ensure_ascii=False)}</script>" for s in schemas)
    return f"""<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{html.escape(page['title'])}</title><meta name='description' content='{html.escape(page['description'], quote=True)}'><meta name='robots' content='index,follow,max-image-preview:large'><link rel='canonical' href='{url}'><meta property='og:type' content='website'><meta property='og:locale' content='pt_BR'><meta property='og:title' content='{html.escape(page['title'], quote=True)}'><meta property='og:description' content='{html.escape(page['description'], quote=True)}'><meta property='og:url' content='{url}'><meta name='twitter:card' content='summary_large_image'><style>{STYLE}</style>{jsonld}</head><body><header class='top'><div class='wrap nav'><a class='brand' href='/'>Rodrigo Cantinho Maldonado</a><nav class='links'><a href='/sobre/'>Sobre</a><a href='/portfolio-de-hospedagens/'>Hospedagens</a><a href='/projetos/'>Projetos</a><a href='/artigos/'>Artigos</a><a href='/contato/'>Contato</a></nav></div></header><main><div class='wrap crumbs'><a href='/'>Início</a> › {html.escape(page['h1'])}</div><section class='hero'><div class='wrap'><h1>{html.escape(page['h1'])}</h1><p class='lead'>{html.escape(page['intro'])}</p></div></section><section class='content'><div class='wrap'><div class='grid'>{cards}</div><div class='cta'><h2>Informações oficiais</h2><p>Consulte os canais oficiais para dados atualizados sobre projetos, imóveis e hospedagens.</p><a href='/contato/'>Entrar em contato</a></div></div></section></main><footer class='footer'><div class='wrap'>© {date.today().year} Rodrigo Cantinho Maldonado · Site oficial</div></footer></body></html>"""

for page in PAGES:
    folder = ROOT / page['slug']
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'index.html').write_text(render(page), encoding='utf-8')

sitemap = ROOT / 'sitemap.xml'
if sitemap.exists():
    xml = sitemap.read_text(encoding='utf-8')
    additions = ''
    for page in PAGES:
        loc = f"{BASE}/{page['slug']}/"
        if loc not in xml:
            additions += f"\n  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>"
    sitemap.write_text(xml.replace('</urlset>', additions + '\n</urlset>'), encoding='utf-8')

# Add links from generated hospitality pages to relevant authority and FAQ pages.
for path in ROOT.rglob('index.html'):
    text = path.read_text(encoding='utf-8')
    if 'Rodrigo Cantinho Maldonado' not in text or '<!-- authority-phase-2 -->' in text:
        continue
    block = """<!-- authority-phase-2 --><section style='padding:52px 24px;background:#f4f1eb'><div style='max-width:1080px;margin:auto'><h2 style='font:700 2rem Georgia,serif'>Conheça mais</h2><p><a href='/biografia-rodrigo-cantinho-maldonado/'>Biografia</a> · <a href='/trajetoria-profissional/'>Trajetória profissional</a> · <a href='/gestao-de-imoveis-de-temporada/'>Gestão de temporada</a> · <a href='/imprensa-e-presenca-digital/'>Presença digital</a></p></div></section>"""
    text = re.sub(r'</main>', block + '</main>', text, count=1, flags=re.I) if re.search(r'</main>', text, re.I) else text
    path.write_text(text, encoding='utf-8')

print(f'Generated {len(PAGES)} authority and FAQ pages')
