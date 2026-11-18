# U CINEMÀ — Réponse à la page « Barème » (19 points, plus un)

> Auto-évaluation honnête. Chaque ligne renvoie à une preuve consultable. Les points marqués « à compléter » dépendent d'un travail qui ne peut pas être simulé (test avec de vraies personnes).
> Lien du prototype : https://mik2a-coder.github.io/u-cinema/ · Code : https://github.com/mik2a-coder/u-cinema

| # | Critère | Points | Visés | Statut |
|---|---|:-:|:-:|---|
| 1 | Brief et persona | 2 | **2** | ✅ |
| 2 | Parcours utilisateur | 2 | **2** | ✅ |
| 3 | Prototype mobile | 4 | **4** | ✅ |
| 4 | Grand écran | 2 | **2** | ✅ |
| 5 | Soin visuel | 3 | **3** | ✅ |
| 6 | Lois de l'usage et accessibilité | 2 | **2** | ✅ |
| 7 | Variables et composants | 2 | **2** | ✅ |
| 8 | Test et version améliorée | 1 | **0 → 1** | 🟡 protocole prêt, **3 tests réels à mener** |
| 9 | Journal | 1 | **1** | ✅ |
| | **Le travail** | **19** | **18 (19 après les tests)** | |
| | Le point du public | +1 | — | décidé par le vote de la classe |

---

## 1. Brief et persona — 2 points
**Attendu** : un problème clair, une personne crédible.
**Livré** : `BRIEF-PERSONA.md` (une page) : problème, objectif mesurable (réserver 2 places en moins de 60 s), périmètre, contraintes, mesure de réussite ; persona principal (Mika, Ajaccio) et persona d'accessibilité (Ghjuvana Maria, Bastia) ; tableau « besoin → réponse de l'app ».
**Écart à signaler** : le sujet est adapté (réseau de 4 cinémas fictifs en Corse au lieu de « Ciné Lumière, 12 salles »).

## 2. Parcours utilisateur — 2 points
**Attendu** : les étapes, les choix, les erreurs.
**Livré** : `PARCOURS.md` : schéma du parcours, tableau étape par étape (action, écran vu, émotion, risque), **7 imprévus** prévus, parcours secondaires. Chaque étape renvoie à une capture (`rendu/captures/`).

## 3. Prototype mobile — 4 points
**Attendu** : le parcours complet, cliquable, avec les imprévus.
**Livré** : le prototype en ligne couvre, sur téléphone :
- **Parcours** : accueil → fiche → séance (dates, séances, tarifs) → places (plan, vue depuis la place) → commande (petite faim, CGV) → billet QR → compte.
- **Imprévus** : séance complète / annulée / déjà réservée, paiement refusé (carte de test), hors ligne (page dédiée avec mini-jeu), recherche vide, double réservation refusée.
- **Plan de salle complet** : toute la salle visible d'un coup, places proposées déjà sélectionnées, « Voir depuis ma place » avec « Changer de place / Acheter ».
- **Plus** : recherche avec suggestions (films, personnes, cinémas), assistant « U Ghjattu-Volpe », carte de fidélité, historique et notes, suivis (films, acteurs, réalisateurs) dans le compte, annulation de réservation, installation sur l'écran d'accueil (PWA).
**Preuves** : captures `mobile_01` à `mobile_09` ; audit de débordement sur 360, 390 et 430 px (`tools/scenarios/audit-debordement.json`, 0 défaut le 18 novembre 2026).

## 4. Grand écran — 2 points
**Attendu** : une mise en page pensée, pas étirée.
**Livré** : au-delà de 600 px, la mise en page change vraiment : barre de navigation du haut, carrousel de 5 affiches, fiche en deux colonnes (affiche à gauche, informations à droite, bande-annonce dans le cadre), page Compte en deux colonnes, plan de salle centré, feuilles centrées. Trois paliers documentés (≤ 599, 600–1023, ≥ 1024).
**Preuves** : captures `bureau_01` à `bureau_06` ; audit sur 768, 1024 et 1440 px (0 défaut).

## 5. Soin visuel — 3 points
**Attendu** : hiérarchie, typo, couleur, détails.
**Livré** : titres condensés façon affiche (Bebas Neue) + texte Inter, échelle typographique de ratio 1,125 ; palette « Noir & Or » et version claire déduite ; un seul signal de couleur ; logo (chat aux lunettes 3D et « U CINEMÀ ») et mascotte illustrée ; photos de produits, portraits des réalisateurs et acteurs ; vue depuis la place ; carte de fidélité qui se retourne ; transitions séquentielles ; barre du haut en verre progressif. Détails : suppression de tout filtre autour des images (cadres parasites sous Safari), zéro animation décorative en boucle.
**Écart assumé** : en mode clair, le fond prend la teinte de l'affiche (choix de l'auteur) ; cela réduit le critère « peu de couleurs » de la grille Peaufiner.

## 6. Lois de l'usage et accessibilité — 2 points
**Attendu** : charge, cibles, contrastes.
**Livré** : `V2-NOTES.md` § 2 (lois de Hick, Fitts, Pareto, goal-gradient, peak-end, etc. avec leur application) ; cibles ≥ 44 px ; contrastes mesurés ≥ 4,5 : 1 sur les 5 palettes (`DESIGN.md`) ; réglages (texte 100/115/130 %, contraste élevé, police lisible, animations réduites, vibrations, consentement vidéo) ; plan de salle au clavier ; emplacements fauteuil roulant ; audiodescription et sous-titres sourds indiqués ; `CONFORMITE.md` (RGPD, droit de la consommation, directive d'accessibilité) ; grille « Peaufiner » 21/22 dans `V2-NOTES.md`.

## 7. Variables et composants — 2 points
**Attendu** : un système propre et réutilisé.
**Livré** : `DESIGN.md` : jetons de couleur (15 clés × 5 palettes + mode clair déduit), échelle typographique, rayons imbriqués, espacements sur grille de 4 pt, points de rupture, **tableau de composants** (boutons primaire/secondaire/Réserver/Acheter/Suivre, séances rapides, progression, tarifs, siège, bannières de petite faim, toast, erreur de paiement, hors ligne, squelette, feuille, logo, barre haute, carte de fidélité, activité…). Tout vient de variables CSS (`--bg`, `--accent`, `--fs-*`, `--r-*`, `--sp-*`…) réutilisées partout.

## 8. Test et version améliorée — 1 point
**Attendu** : 3 personnes, des corrections visibles.
**Livré** : le **protocole complet** (`TESTS.md` : objectifs, 5 scénarios, consigne, grille, débrief, synthèse gravité × fréquence) et la **version améliorée** déjà issue de revues répétées de l'auteur (liste datée des corrections dans `TESTS.md` § « Revues déjà intégrées »).
**À compléter** : les **résultats des 3 personnes** sont volontairement vides — je n'invente aucun test. Le point n'est acquis qu'une fois la grille remplie et 2 corrections issues de ces tests visibles (avant/après).

## 9. Journal — 1 point
**Attendu** : outils, prompts, choix expliqués.
**Livré** : `JOURNAL.md` : outils (assistant de code, Chrome sans interface pour les tests, ffmpeg, GitHub Pages…), méthode, **prompts marquants** et ce qu'ils ont produit, **choix argumentés**, erreurs et corrections, limites.

---

## Un seul lien
Tout le rendu tient dans un lien : **https://github.com/mik2a-coder/u-cinema** (dépôt) · prototype : **https://mik2a-coder.github.io/u-cinema/** · dossier remis : `RENDU-U-CINEMA.pdf`.
