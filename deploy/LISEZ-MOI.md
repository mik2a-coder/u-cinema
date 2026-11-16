# U CINEMÀ sur le Raspberry → Pixel

## 1. Publier sur le Raspberry (depuis le Mac)

Remplacez `mika@192.168.1.91` par votre utilisateur et l'adresse de votre Raspberry :

```bash
cd "/Users/mika/Desktop/CLAUDE CODE/CINELUX"
./deploy/deploy.sh mika@192.168.1.91
```

Le script envoie les fichiers, installe nginx si besoin et affiche l'adresse finale
(ex. `http://192.168.1.42:8080`). Pour un autre port : `PORT=9000 ./deploy/deploy.sh …`

Sans `rsync`/`ssh` : copiez `deploy/CINELUX-site.zip` sur le Raspberry (clé USB, `scp`),
dézippez, puis `sudo bash setup-pi.sh` dans le dossier obtenu.

## 2. Ouvrir sur le Pixel

Pixel et Raspberry sur le **même Wi-Fi** : ouvrez Chrome et allez sur `http://ADRESSE:8080`.
L'application s'affiche en plein écran, sans cadre de téléphone.

## 3. L'installer comme une vraie application (recommandé)

Chrome n'installe une application et n'active le mode hors ligne qu'en **HTTPS**.
Sur un réseau local en `http://`, vous n'aurez qu'un raccourci (avec la barre d'adresse).
Deux solutions simples pour avoir du HTTPS valide :

### Option A – Tailscale (gratuit, le plus simple, aussi utilisable hors de chez vous)
1. Installez Tailscale sur le Raspberry et sur le Pixel, connectez-les au même compte.
2. Dans l'admin Tailscale, activez **MagicDNS** et **HTTPS Certificates**.
3. Sur le Raspberry, **regardez d'abord ce qui est déjà publié** (un autre service peut utiliser Tailscale Serve) :
   ```bash
   tailscale serve status
   ```
   Puis publiez U CINEMÀ sur **un port HTTPS à part**, pour ne rien écraser :
   ```bash
   sudo tailscale serve --bg --https=8443 http://localhost:8080
   ```
   (n'utilisez pas `tailscale serve --bg 8080` seul : il remplace la configuration du port 443)
4. Sur le Pixel, ouvrez l'adresse `https://nom-du-raspberry.xxxx.ts.net:8443` affichée par la commande
   `tailscale serve status`. Seuls vos appareils Tailscale y ont accès : rien n'est exposé sur Internet.

### Option B – Certificat local avec Caddy (réseau maison uniquement)
Plus long : il faut installer le certificat racine de Caddy sur le Pixel
(Paramètres → Sécurité → Chiffrement et identifiants → Installer un certificat). Tailscale est préférable.

### Installer
Chrome (⋮) → **Installer l'application** (ou « Ajouter à l'écran d'accueil »).
L'icône « billet doré » apparaît sur l'écran d'accueil ; l'appli s'ouvre en plein écran et marche hors ligne.
Le bouton Retour du Pixel revient à l'écran précédent ; deux fois sur l'accueil pour quitter.

## Mises à jour
Modifiez `index.html` sur le Mac, relancez `./deploy/deploy.sh …`.
Si l'ancienne version reste affichée : dans `sw.js`, changez `cinelux-v1` en `cinelux-v2`, puis redéployez.

## Mode développeur (sur le Mac)
Ajoutez `?dev` à l'adresse pour retrouver la barre des 5 palettes et les raccourcis d'écrans.
Les adresses du type `index.html#seats:1` ouvrent directement un écran.

## Dépannage
- **La page n'apparaît pas** : vérifiez `sudo systemctl status nginx` et le pare-feu (`sudo ufw allow 8080/tcp`).
- **Pas d'« Installer l'application »** : l'adresse doit commencer par `https://` (option A).
- **Test rapide sans nginx** : `./deploy/serve-simple.sh`.
- Contenu : 4 vraies affiches de films (usage perso/maquette uniquement, droits d'auteur de leurs ayants droit).
