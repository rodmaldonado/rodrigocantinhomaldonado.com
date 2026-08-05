# Rodrigo Cantinho Maldonado — site oficial

Site estático da marca pessoal de Rodrigo Cantinho Maldonado, preparado para deploy automático pelo fluxo GitHub → Netlify, com DNS administrado no Cloudflare.

## Conteúdo publicado

- Home, Sobre, Projetos, Artigos e Contato
- 12 artigos autorais e páginas temáticas aprofundadas
- páginas dos projetos The Quinta Experience e Morar em Ipanema
- guias sobre imóveis de alto padrão, coberturas em Ipanema, negociação e venda
- conteúdo sobre gestão de Airbnb, custos operacionais e experiência do hóspede
- perfil empresarial, biografia, trajetória e presença digital
- sitemap, robots.txt, RSS, dados estruturados, Open Graph e Twitter Cards
- headers de segurança, cache e redirecionamento de `www`
- 6 textos externos originais em `conteudo-externo/`

## Build

O conteúdo público está em um pacote compacto versionado em cinco partes. O build recria a pasta `public/` e executa as três fases de expansão:

```bash
sh scripts/build.sh
```

## Validação

```bash
pip install beautifulsoup4 lxml
python -m unittest tests/test_expand_authority_phase3.py -v
python scripts/validate_site.py public
```

## Deploy

- Netlify: build command `sh scripts/build.sh`; publish directory `public`
- Cloudflare Pages, se utilizado: build command `sh scripts/build.sh`; output directory `public`
- Produção: branch `main`
- Domínio canônico: `https://rodrigocantinhomaldonado.com`

As instruções completas estão em `DEPLOY.md`; a auditoria está em `SEO-AUDIT.md`.
