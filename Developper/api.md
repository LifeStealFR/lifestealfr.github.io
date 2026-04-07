# 🌐 LifestealMC - Documentation API de la Communauté

Bienvenue sur l'API officielle de **LifestealMC**. Ce guide répertorie tous les points d'accès (endpoints) disponibles pour interagir avec notre infrastructure (Site web, Boutique, Serveur de jeu).

**URL de base :** `https://lifestealmc.fr/api`  
**Format :** `application/json`

---

## 🔐 1. Guide d'Authentification

La majorité des routes du module **API-Extender** nécessitent une clé API pour garantir la sécurité.

### Méthode A : Dans le Header HTTP (Recommandé pour les scripts)
C'est la méthode la plus propre pour vos applications (Node.js, Python, Bot Discord).
*   **Header :** `API-Key`
*   **Valeur :** `votre_cle_api`

**Exemple en JavaScript (Fetch) :**
```javascript
fetch("https://lifestealmc.fr/api/apiextender/users", {
    headers: {
        "API-Key": "VOTRE_CLE_API_ICI",
        "Accept": "application/json"
    }
})
.then(res => res.json())
.then(console.log);
```

### Méthode B : Directement dans l'URL (Pour navigateur/tests)
Si vous ne pouvez pas modifier les en-têtes (headers), utilisez l'authentification "Basic Auth" intégrée à l'URL.
*   **Format :** `https://cron:CLE_API@lifestealmc.fr/api/...`

**Exemple concret à coller dans votre navigateur :**
> `https://cron:VOTRE_CLE_API_ICI@lifestealmc.fr/api/apiextender/users`

---

## 🛠 2. Module : API-Extender (Fonctionnalités Étendues)
Ce module nécessite une clé API pour la plupart de ses routes.

| Méthode | Endpoint | Clé API ? | Notes |
| :--- | :--- | :---: | :--- |
| **GET** | `/apiextender/users` | ✅ Oui | Liste complète des joueurs et profils |
| **GET** | `/apiextender/money` | ✅ Oui | Statistiques économiques |
| **GET** | `/apiextender/roles` | ✅ Oui | Liste des grades (VIP, Joueur, etc.) |
| **GET** | `/apiextender/servers` | ✅ Oui | Infos détaillées de l'infrastructure |
| **GET** | `/apiextender/social` | ✅ Oui | Liens des réseaux sociaux officiels |
| **GET** | `/apiextender/shop/categories` | ✅ Oui | Catégories de la boutique |
| **GET** | `/apiextender/shop/payments` | ✅ Oui | Historique des paiements (Shop plugin) |
| **GET** | `/apiextender/cron/status` | ✅ Oui | État des tâches système automatisées |
| **GET** | `/apiextender/images/{t}/{r}/{p}`| ❌ **Non** | Rendu de skin via **Starlight SkinAPI** |

### 🖼️ Zoom sur le Rendu d'Images (Skins)
Vous pouvez générer des images de joueurs sans clé API.
*   **Format :** `/api/apiextender/images/{type}/{rendertype}/{pseudo}`
*   **Exemple :** `https://lifestealmc.fr/api/apiextender/images/default/bust/Steve`
*   *Types courants : head, bust, face.*

---

## 🎮 3. Module : AzLink (Sync Jeu-Web)
Gère les interactions directes avec le serveur Minecraft.

| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/azlink` | Statut du bridge AzLink |
| **GET** | `/azlink/user/{user}` | Récupérer les stats de jeu d'un joueur |
| **POST** | `/azlink/user/{id}/money/add` | Créditer de l'argent en jeu |
| **POST** | `/azlink/user/{id}/money/set` | Définir le solde d'un joueur |

---

## 🎨 4. Module : Skin-API (Apparences)
*Note : Ces images sont générées nativement par Azuriom.*

| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/skin-api/avatars/{type}/{user}.png` | Avatar PNG (ex: head, face) |
| **GET** | `/skin-api/skins/{user}.png` | Skin complet du joueur en PNG |
| **GET** | `/skin-api/capes/{user}.png` | Cape du joueur en PNG |

---

## 🛒 5. Boutique, News & Statut (Core)
Routes d'information générale.

| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/servers` | Nombre de joueurs en ligne et statut simple |
| **GET** | `/posts` | Liste des news et actualités du site |
| **GET** | `/mypurchases` | Vos achats personnels (Nécessite Bearer Token) |
| **GET** | `/vote/azlink` | Données sur les votes du serveur |

---

## 🚦 6. Limites & Règles (Rate Limiting)
*   **Sécurité :** Le plugin `ApiLimiter` surveille les abus. En cas de trop nombreuses requêtes, vous recevrez une erreur `429 Too Many Requests`.
*   **Cache :** Merci de mettre en cache les données (ex: 5 minutes pour les statistiques) pour ne pas surcharger le serveur.
*   **Debug :** Vous pouvez tester votre connexion et voir votre IP détectée ici : `https://lifestealmc.fr/api/api-limiter/debug-ip`

---

## 💡 Exemple Complet : Bot Discord (Node.js)

```javascript
const axios = require('axios');

async function getPlayerMoney(pseudo) {
    try {
        const response = await axios.get('https://lifestealmc.fr/api/apiextender/money', {
            headers: { 'API-Key': 'VOTRE_CLE_API_ICI' }
        });
        // Logique pour trouver le joueur dans la liste
        console.log(response.data);
    } catch (error) {
        console.error("Erreur d'accès à l'API");
    }
}
```
