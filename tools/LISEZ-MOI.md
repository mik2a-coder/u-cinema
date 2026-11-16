# Images de scène pour l'écran de la salle

L'écran de la salle affiche une image 16:9 tirée de chaque film, s'il en existe une dans `img/scene/<id>.jpg`
(`drive.jpg`, `dune.jpg`, …). Sans image, il affiche l'affiche sur un fond flou, comme avant.

## Les récupérer automatiquement (TMDB, gratuit)
1. Créez un compte sur https://www.themoviedb.org, puis Paramètres › API › « Demander une clé » (usage personnel).
2. Dans le Terminal :
   ```bash
   cd "/Users/mika/Desktop/CLAUDE CODE/CINELUX"
   TMDB_KEY=VOTRE_CLE python3 tools/fetch-scenes.py
   ```
3. Rechargez CINÉLUX (Cmd+Maj+R). Pour le Pixel, republiez : `./deploy/deploy.sh mika@192.168.1.91`.

## Ou à la main
Déposez simplement une image 16:9 (idéalement 1280 × 720 ou plus) nommée `<id>.jpg` dans `img/scene/`.

Les images TMDB demandent la mention : « This product uses the TMDB API but is not endorsed or certified by TMDB. »
Le script l'écrit dans `img/scene/CREDITS.txt`.
