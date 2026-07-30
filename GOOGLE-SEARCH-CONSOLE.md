# Google Search Console — Checklist de Configuração

**Data:** 30/07/2026  
**Domínio:** https://rodrigocantinhomaldonado.com  
**Email:** rodmaldonado8@gmail.com

---

## ✅ Passo 1: Adicionar Propriedade

1. Acesse: https://search.google.com/search-console
2. Clique **Adicionar propriedade**
3. Escolha **Prefixo de URL**
4. Cole: `https://rodrigocantinhomaldonado.com`
5. Clique **Continuar**

**Status:** ⏳ Aguardando você fazer...

---

## ✅ Passo 2: Validar via TXT no Cloudflare

Google vai fornecer um código como:

```
Registro TXT: google-site-verification=ABC123XYZ...
```

### No Cloudflare:
1. Acesse: https://dash.cloudflare.com
2. Selecione seu domínio → **DNS**
3. Clique **Adicionar registro**
4. Configure:
   - **Tipo:** TXT
   - **Nome:** @ (ou deixe vazio)
   - **Conteúdo:** Cole o código `google-site-verification=...`
5. Clique **Salvar**
6. Aguarde propagação (~5 min)

### Volte ao Search Console:
7. Clique **Verificar** (no Search Console)

**Status:** ⏳ Aguardando você fazer...

---

## ✅ Passo 3: Enviar Sitemap

1. No Search Console → menu esquerdo → **Sitemaps**
2. Cole em "Adicionar um novo sitemap":
   ```
   https://rodrigocantinhomaldonado.com/sitemap.xml
   ```
3. Clique **Enviar**
4. Aguarde processamento (pode levar horas)

**Status:** ⏳ Aguardando você fazer...

---

## ✅ Passo 4: Solicitar Indexação de URLs Principais

No Search Console → menu esquerdo → **URL Inspection**

Inspecione e solicite indexação para:

1. **Home:**
   - URL: `https://rodrigocantinhomaldonado.com/`
   - Clique "Solicitar indexação"

2. **Sobre:**
   - URL: `https://rodrigocantinhomaldonado.com/sobre/`
   - Clique "Solicitar indexação"

3. **Projetos:**
   - URL: `https://rodrigocantinhomaldonado.com/projetos/`
   - Clique "Solicitar indexação"

4. **Artigos:**
   - URL: `https://rodrigocantinhomaldonado.com/artigos/`
   - Clique "Solicitar indexação"

**Status:** ⏳ Aguardando você fazer...

---

## ✅ Passo 5 (Opcional): Bing Webmaster Tools

1. Acesse: https://www.bing.com/webmasters
2. Adicione o site
3. Importe do Google Search Console (mais rápido)

---

## ✨ Pronto!

Depois de seguir os passos acima, seu site estará totalmente indexado nos motores de busca.

**Links úteis:**
- Search Console: https://search.google.com/search-console
- Cloudflare DNS: https://dash.cloudflare.com
- Netlify Deploy: https://app.netlify.com/sites/rodrigo-cantinho-maldonado/deploys

---

**Gerado por:** Claude Code  
**Branch:** claude/site-current-status-zw2j1u
