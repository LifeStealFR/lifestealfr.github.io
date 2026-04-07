# 🌐 Référence API Complète - LifestealFR

Bienvenue dans la documentation exhaustive de l'API LifestealMC. Ce document liste l'intégralité des points de terminaison générés par le CMS Azuriom et ses plugins (`ApiExtender`, `ApiLimiter`, `SkinApi`, `Shop`, etc.).

> **URL de base :** `https://lifestealmc.fr/`  
> **Format :** `JSON` par défaut.  
> **Protection :** Toutes les routes publiques sont protégées par **ApiLimiter** (Niveaux AL, AL2, AL3).

---

## 🔐 1. Règles d'Authentification

Selon la route appelée, le système requiert une authentification spécifique :

1. **ApiExtender (`API-Key`) :** Requis pour les routes `/api/apiextender/*`.  
   ```http
   API-Key: votre_cle_secrete
   ```
2. **Utilisateur (`Bearer Token`) :** Requis pour les actions de compte (`/auth`, `/mypurchases`).  
   ```http
   Authorization: Bearer votre_token
   ```
3. **Admin (`Session`) :** Les routes `/admin/*` nécessitent d'être connecté au panel en tant qu'administrateur.

---

## 🛠 2. Plugin : ApiExtender
*Le cœur des données étendues pour la communauté. Nécessite le header `API-Key`.*

| Méthode | Endpoint | Description | Rate Limit |
| :--- | :--- | :--- | :---: |
| `GET` | `/api/apiextender` | Index des fonctionnalités étendues | AL |
| `GET` | `/api/apiextender/users` | Liste exhaustive des utilisateurs | AL |
| `GET` | `/api/apiextender/money` | Statistiques de l'économie | AL |
| `GET` | `/api/apiextender/roles` | Liste des grades et rôles | AL |
| `GET` | `/api/apiextender/servers` | Statut détaillé des serveurs | AL |
| `GET` | `/api/apiextender/social` | Liens des réseaux sociaux | AL |
| `GET` | `/api/apiextender/shop/categories` | Catégories de la boutique | AL |
| `GET` | `/api/apiextender/shop/payments` | Historique des paiements | AL |
| `POST` | `/api/apiextender/shop/giftcard` | Génération/Validation carte cadeau | AL |
| `GET` | `/api/apiextender/cron/status` | État des tâches Cron | AL 2 |
| `GET/POST`| `/api/apiextender/cron/execute` | Lancement forcé des tâches Cron | AL 2 |
| `GET` | `/api/apiextender/images/{t}/{r}/{p}`| Rendu d'image (Skins) | AL |

---

## 🎮 3. Core : AzLink (Sync Jeu-Web)
*Communication officielle entre le site et le serveur Minecraft.*

| Méthode | Endpoint | Description | Rate Limit |
| :--- | :--- | :--- | :---: |
| `GET` | `/api/azlink` | Statut de l'intégration AzLink | AL 2 |
| `POST` | `/api/azlink` | Envoi de données du serveur vers le site | AL 2 |
| `GET` | `/api/azlink/user/{user}` | Données spécifiques d'un joueur | AL 2 |
| `POST` | `/api/azlink/user/{user}/money/add` | Ajouter de l'argent en jeu | AL 2 |
| `POST` | `/api/azlink/user/{user}/money/remove`| Retirer de l'argent en jeu | AL 2 |
| `POST` | `/api/azlink/user/{user}/money/set` | Définir un solde exact en jeu | AL 2 |
| `POST` | `/api/azlink/register` | Inscription depuis le jeu | AL 2 |
| `POST` | `/api/azlink/email` | Mise à jour email depuis le jeu | AL 2 |
| `POST` | `/api/azlink/password` | Mise à jour mot de passe depuis le jeu| AL 2 |

---

## 🎨 4. Plugin : SkinApi
*Génération et manipulation des apparences (Skins et Capes).*

| Méthode | Endpoint | Description | Auth |
| :--- | :--- | :--- | :---: |
| `GET` | `/api/skin-api/avatars/{type}/{user}` | Info JSON sur l'avatar généré | Libre |
| `GET` | `/api/skin-api/avatars/{type}/{user}.png` | Image PNG de l'avatar | Libre |
| `GET` | `/api/skin-api/skins/{user}` | Info JSON du skin complet | Libre |
| `GET` | `/api/skin-api/skins/{user}.png` | Image PNG du skin | Libre |
| `GET` | `/api/skin-api/capes/{user}` | Info JSON de la cape | Libre |
| `GET` | `/api/skin-api/capes/{user}.png` | Image PNG de la cape | Libre |
| `POST` | `/api/skin-api/skins` | Uploader/Modifier son skin | Bearer |
| `POST` | `/api/skin-api/skins/update` | Forcer la mise à jour du skin | Bearer |
| `DELETE` | `/api/skin-api/skins` | Supprimer son skin | Bearer |
| `POST` | `/api/skin-api/capes` | Uploader/Modifier sa cape | Bearer |
| `DELETE` | `/api/skin-api/capes` | Supprimer sa cape | Bearer |

---

## 🛒 5. Plugins : Shop, MyPurchases & Tebex
*Tout ce qui concerne l'économie réelle et la boutique.*

| Méthode | Endpoint | Description | Auth |
| :--- | :--- | :--- | :---: |
| `GET` | `/api/mypurchases` | Vos achats personnels | Bearer |
| `GET` | `/api/mypurchases/payment/{id}` | Détail d'une transaction | Bearer |
| `GET` | `/api/shop/azlink` | Synchronisation boutique/jeu | AzLink |
| `ANY` | `/api/shop/payments/{gw}/notification/{id?}`| Webhook paiements (Shop) | API |
| `POST` | `/api/tebex/buy` | Interface de paiement Tebex | Public |

---

## 📰 6. Core : Utilisateurs, News & Votes
*Routes natives d'Azuriom pour la navigation globale.*

| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/auth/authenticate` | Connexion (récupère un token) |
| `POST` | `/api/auth/verify` | Vérifier la validité du token |
| `POST` | `/api/auth/logout` | Déconnexion (révoque le token) |
| `GET` | `/api/servers` | Index des serveurs (Ping & Joueurs) |
| `GET` | `/api/posts` | Index des articles de blog |
| `GET` | `/api/posts/{post}` | Lire un article de blog complet |
| `GET` | `/api/rss` | Flux RSS officiel du site |
| `GET` | `/api/atom` | Flux Atom officiel du site |
| `GET` | `/api/vote/azlink` | Synchro des votes avec le jeu |
| `ANY` | `/api/vote/pingback/{site}` | Callback des sites de classement |

---

## 🛡 7. Plugin : ApiLimiter (Debug & Securité)
*Outils pour vérifier si vos requêtes sont bloquées.*

| Méthode | Endpoint | Description | Statut |
| :--- | :--- | :--- | :---: |
| `GET` | `/api/api-limiter/debug-ip` | Voir comment le pare-feu lit votre IP | AL 2 |
| `GET` | `/api/api-limiter/test-middleware` | Tester le passage au middleware | AL 3 |
| `GET` | `/api/api-limiter/rate-limiter-test`| **Restreint** - Test interne | 🚫 |

---

## ⚙️ 8. Espace Administration (Interne)
*Ces routes sont réservées à l'administration du site (`/admin`). Elles nécessitent les privilèges Kernel/Admin.*

### Gestion ApiLimiter
- `GET` `/admin/api-limiter/settings` - Voir les paramètres
- `POST` `/admin/api-limiter/settings` - Mettre à jour les paramètres
- `GET` `/admin/api-limiter/api-routes` - Découverte des routes API
- `GET` `/admin/api-limiter/logs` - Voir les logs de requêtes
- `POST` `/admin/api-limiter/logs/settings` - Configurer les logs
- `POST` `/admin/api-limiter/logs/cleanup` - Nettoyer les anciens logs
- `POST` `/admin/api-limiter/logs/clear` - Vider tous les logs
- `GET` `/admin/api-limiter/logs/download` - Télécharger les logs
- `POST` `/admin/api-limiter/clear` - Vider le cache du limiteur

### Gestion ApiExtender
- `GET` `/admin/apiextender` - Index du plugin
- `GET` `/admin/apiextender/api-keys` - Liste des clés API
- `POST` `/admin/apiextender/api-keys/generate` - **Créer une clé API**
- `POST` `/admin/apiextender/api-keys/{apiKey}/toggle` - Activer/Désactiver une clé
- `DELETE` `/admin/apiextender/api-keys/{apiKey}` - Supprimer une clé API
- `GET` `/admin/apiextender/cron` - Paramètres Cron
- `POST` `/admin/apiextender/cron/test` - Tester une tâche Cron
- `POST` `/admin/apiextender/cron/toggle` - Activer/Désactiver une tâche Cron
- `GET` `/admin/apiextender/images` - Paramètres de cache des images

### Gestion SkinApi
- `GET` `/admin/skin-api/skins` - Gestion globale des skins
- `POST` `/admin/skin-api/skins.update` - Forcer la mise à jour d'un skin joueur
- `GET` `/admin/skin-api/capes` - Gestion globale des capes
- `POST` `/admin/skin-api/capes.update` - Forcer la mise à jour d'une cape joueur

---
*LifestealMC API Reference*
