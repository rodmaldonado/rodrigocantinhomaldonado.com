# Publicação: GitHub → Netlify, com DNS no Cloudflare

## Arquitetura

- GitHub: repositório-fonte `rodmaldonado/rodrigocantinhomaldonado.com`.
- Netlify: hospedagem e deploy automático da branch `main`.
- Cloudflare: administração do DNS.
- Domínio principal: `https://rodrigocantinhomaldonado.com`; `www` redireciona para o domínio sem `www`.

## Netlify

1. Vincular o repositório `rodmaldonado/rodrigocantinhomaldonado.com`.
2. Build command: `sh scripts/build.sh`.
3. Publish directory: `public`.
4. Adicionar `rodrigocantinhomaldonado.com` e `www.rodrigocantinhomaldonado.com`.
5. Definir o domínio sem `www` como principal.
6. Ativar HTTPS.

## Cloudflare DNS

- `@` → CNAME achatado para `apex-loadbalancer.netlify.com`, ou A para `75.2.60.5` quando essa for a instrução específica da Netlify.
- `www` → CNAME para o subdomínio real do projeto, no formato `nome-do-site.netlify.app`.
- Durante a validação de domínio e emissão do certificado, usar `DNS only`.

## Depois da publicação

1. Criar propriedade de domínio no Google Search Console.
2. Verificar via TXT no Cloudflare.
3. Enviar `https://rodrigocantinhomaldonado.com/sitemap.xml`.
4. Solicitar indexação da home, `/sobre/`, `/projetos/` e `/artigos/`.
5. Criar Bing Webmaster Tools e importar do Search Console.
6. Confirmar o recebimento do formulário no Netlify Forms.

## Conteúdo externo

Os seis textos em `conteudo-externo/` são versões originais para LinkedIn, Medium e Substack. Não republicar os artigos internos de forma idêntica; manter URL canônica e textos distintos.
