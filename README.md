# lifestealmc.fr — Studio & Projets

Portail officiel statique (GitHub Pages, domaine `lifestealmc.fr`) : vitrine du
studio d'outils web, des bots Discord (dont Kurotsuki Studio), de l'API Gateway
et de l'infrastructure, avec documentation technique et pages légales séparées
(exigence audit Google AdSense « contenu de faible valeur » : profondeur du site).

## Structure (multi-pages, URL propres sans extension)

| URL                                              | Fichier                                              |
|--------------------------------------------------|------------------------------------------------------|
| `https://lifestealmc.fr/`                        | `index.html` (hub : vitrine, teasers, résumés légaux)|
| `…/guides/architecture-bot-discord-production/`  | `guides/…/index.html` (guide 1 complet)              |
| `…/guides/securisation-webhooks-api/`            | `guides/…/index.html` (guide 2 complet)              |
| `…/guides/infrastructure-nodejs-nextjs/`         | `guides/…/index.html` (guide 3 complet)              |
| `…/about/` `…/contact/` `…/privacy/` `…/terms/`   | `about|contact|privacy|terms/index.html`              |
| Sitemap / robots                                 | `sitemap.xml` (8 URL), `robots.txt`                  |
| Divers                                           | `ads.txt`, `CNAME`, `subdomains.json`                |

Astuce GitHub Pages : chaque page est un `index.html` dans son dossier, ce qui
produit des URL propres (`/about/`) sans configuration.

## Conventions

- Zéro dépendance : chaque page embarque son CSS dans `<style>`.
- Zéro lien mort : vérifier avec `python3 check` — toute ancre `#x` doit exister
  sur la page qui la porte ; seuls liens sortants autorisés :
  `https://kurotsuki.lifestealmc.fr/en-US`, `/ads.txt`, `mailto:contact@lifestealmc.fr`.
- Chaque page : `canonical` vers sa propre URL + meta `google-adsense-account`.
- Pas de contenu dupliqué entre l'accueil (teasers) et les pages guides (articles
  complets) ; maillage interne systématique (fil d'Ariane, pager, « pour aller
  plus loin », footer).
- Pas d'encart publicitaire vide ni de mention « Annonce ».
