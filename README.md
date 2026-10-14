# lifestealmc.fr — Studio & Projets

Portail officiel statique (GitHub Pages, domaine `lifestealmc.fr`) : vitrine du
studio d'outils web, des bots Discord (dont Kurotsuki Studio), de l'API Gateway
et de l'infrastructure, avec documentation technique intégrée.

## Structure (single-page)

| Fichier          | Rôle                                                        |
|------------------|-------------------------------------------------------------|
| `index.html`     | Page unique : hero, vitrine projets, 3 guides techniques, mentions légales, footer |
| `sitemap.xml`    | Sitemap : unique URL canonique `https://lifestealmc.fr/`    |
| `robots.txt`     | Autorise tout + déclare le sitemap                          |
| `ads.txt`        | Déclaration vendeurs autorisés (Google AdSense)             |
| `CNAME`          | Domaine personnalisé `lifestealmc.fr`                       |
| `subdomains.json`| Inventaire des sous-domaines (Kurotsuki, Solus Store, Craftok) |

## Conventions

- Fichier unique `index.html`, CSS intégré, zéro dépendance.
- Navigation interne à 100 % en ancres (`#ecosysteme`, `#kurotsuki`,
  `#documentation`, `#legal`) — aucun lien mort.
- Seuls liens sortants autorisés : `https://kurotsuki.lifestealmc.fr/en-US`,
  `/ads.txt` et `mailto:contact@lifestealmc.fr`.
- Pas d'encart publicitaire vide ni de mention « Annonce ».
- Ne pas recréer de pages séparées : tout contenu éditorial va dans `index.html`
  (exigence audit AdSense « contenu de faible valeur »).
