# U CINEMÀ — Journal : outils, prompts, choix

## Outils utilisés
| Outil | Pour quoi |
|---|---|
| **Claude Code** (assistant de code d'Anthropic, application de bureau) | Écrire et corriger le prototype (HTML/CSS/JavaScript en un seul fichier), les scripts, la documentation |
| **Chrome sans interface + protocole de débogage** | Captures automatiques, audit de débordement, vérification des boutons (`tools/shoot.mjs`) |
| **ffmpeg** | Découper mes **enregistrements d'écran** en images pour trouver des bugs de transition |
| **Safari / Chrome** (mes appareils) | Revue réelle : c'est là que sont apparus le carré autour du logo, le bug de « Réserver », etc. |
| **Python** (`tools/build-autonome.py`) | Générer une version autonome en un seul fichier |
| **sips, Chrome (canvas)** | Découper les images (logo, mascotte) et retirer leurs fonds |
| **Wikipédia / Wikimedia Commons** | Portraits des acteurs et réalisateurs, photos de produits ; affiches des films |
| **YouTube (mode sans cookie)** | Bandes-annonces, chargées **uniquement après consentement** |
| **GitHub + GitHub Pages** | Un seul lien à remettre, mises à jour en ligne |
| **Illustrations fournies par moi** | Logo (chat aux lunettes 3D) et mascotte, dessinés/choisis par moi |

## Méthode
Boucle courte, répétée une centaine de fois : **ma demande (souvent avec capture) → implémentation → vérification automatique → capture → ma validation**. Aucune idée n'est appliquée sans mon accord visuel (ex. : 5 propositions de logo avant d'en choisir). Chaque défaut vu sur mes appareils a été reproduit avant d'être corrigé quand c'était possible.

## Prompts marquants (extraits fidèles) et ce qu'ils ont produit
| Mon prompt | Résultat |
|---|---|
| « Je veux aussi une version claire en plus de la version sombre… harmonie des couleurs » | Mode clair déduit de la palette |
| « Améliorer la fonction de recherche avec suggestions… miniatures d'affiches » | Recherche avec films, personnes, cinémas |
| « Travailler les transitions entre les pages pour garder de la fluidité » | Transitions de page, puis simplifiées en fondus séquentiels |
| « Comme si nous étions assis avec vue des sièges de devant et de l'écran » | Vue 3D depuis la place, puis bande-annonce sur l'écran |
| « Propose-moi cinq logos et j'en validerai un » | Planches de logos (billets, noms corses, lettres-symboles) ; choix final : mon propre dessin |
| « Un agent intelligent… personnage attachant cliquable, qui suit du regard la souris » | Assistant « U Ghjattu-Volpe » (règles locales, pas d'IA externe, rien n'est envoyé) |
| « Inventer des cinémas en Corse » | 4 cinémas fictifs : Aiacciu, Bastia, Corti, Portivechju |
| « Ajouter des suggestions et inspire-toi des images pour les suppléments » | Bannières de petite faim avec photos |
| « Il ne peut pas y avoir deux réservations du même film aux mêmes heures » | Règle de non-chevauchement |
| « Toujours le bug de transition quand on clique sur réservé… analyse la vidéo » | Bug trouvé : onde au toucher qui agrandissait le bouton |
| « Garde l'affiche 2 secondes puis la bande-annonce au format vertical » | Affiche → vidéo (verticale officielle si elle existe) |
| « Analyse mon site avec l'énoncé… crée les documents du barème » | Ce dossier de rendu |
| Vidéo d'un plan de stade : « utiliser le même type de transitions pour le choix des places » | Plan de salle en zones avec zoom de caméra, vue de la place avec « Changer de place / Acheter » |
| « Dans mon compte, je ne retrouve pas mes suivis » | Section « Mes suivis », suivi des personnes depuis la recherche |
| Capture avec un ovale jaune : « je veux que le fond ait cette forme » (5 propositions avant de modifier) | Planche de 5 propositions, puis ovale de fond appliqué sans flou sur les boutons |
| « Élargir le dégradé en dehors de l'écran… remettre à 55 % en clair » | Ovale qui déborde ; opacité réglable (55 % clair / 90 % sombre) |
| « Mets-moi une checklist pour les 3 testeurs, en vertical pour ma reMarkable » | `CHECKLIST-TEST-3-PERSONNES.pdf` au format 3:4 |

## Choix expliqués
| Choix | Pourquoi |
|---|---|
| **Un seul fichier HTML**, sans framework | Prototype partageable par un seul lien, fonctionne hors ligne (PWA) |
| **Tout en local** (pas de serveur, pas de compte réel) | RGPD : les données ne quittent pas l'appareil ; démonstration honnête |
| **Assistant à règles, pas d'IA externe** | Aucun envoi de données ; comportement prévisible et testable |
| **Vidéos après consentement** | YouTube peut recevoir l'adresse IP : on demande d'abord |
| **Une seule couleur de signal (l'or)** | Lisibilité, cohérence (grille « Peaufiner ») |
| **Boutons principaux encre foncée en clair** | Contraste fort sur fond clair, cohérent partout |
| **Verre progressif pour la barre haute** | Pas de ligne dure, pas de contenu flou masqué |
| **Cinémas fictifs en Corse, mascotte corse** | Ancrage local assumé ; adaptation du sujet à signaler |
| **Aucune donnée inventée présentée comme vraie** | Notes et historique marqués « démonstration » ; tests à 3 personnes laissés vides |

## Erreurs et ce qu'elles m'ont appris
- **Un faux espace blanc autour du logo et du chat** : un filtre sur une image fait apparaître un cadre sous Safari → plus aucun filtre sur les images.
- **Un bouton qui grandit au clic** : une règle CSS écrasait le positionnement de l'effet d'onde. Trouvé seulement en filmant l'écran image par image : **mesurer plutôt que supposer**.
- **Un script cassé par une règle CSS posée dans le JavaScript** : vérifier la syntaxe à chaque modification.
- **Cache du navigateur** : après une mise à jour, on voit parfois l'ancienne version → noms de fichiers versionnés, rechargement forcé.
- **Mon propre jugement visuel** : plusieurs aller-retours (boutons dorés puis encre, logo, barre haute) → valider par une comparaison côte à côte avant d'appliquer.

## Décisions récentes
| Décision | Pourquoi |
|---|---|
| Garder 55 % d'opacité du fond en clair | Choix de l'auteur après comparaison côte à côte |
| Ovale de fond **sans** flou sur les éléments | Les boutons et textes doivent rester nets ; seul le fond change |
| Plan de salle : zoom de zone sans étape de plus | Garder l'objectif de réserver en moins de 60 secondes |
| Écran de vue de la place en 16:9 | Fiabilité sous Safari et vidéo sans recadrage |

## 18 novembre 2026 — version 82 : revue en 24 points
Détail point par point dans `VERSIONS.md`. Décisions de conception :

| Décision | Pourquoi |
|---|---|
| Annulation = **avoir** et jusqu'à 2 h avant | Règle commerciale demandée ; l'avoir est visible dans Compte et activable à la commande |
| Récompenses séparées du niveau | Dépenser des points ne fait pas redescendre le niveau (`ACC.spent` distinct des points cumulés) |
| Fiche personne dédiée plutôt qu'une recherche | Un nom cliqué doit ouvrir **sa** page, avec retour au même endroit |
| Assistant qui réserve jusqu'au récapitulatif | On ne paie jamais à la place de l'utilisateur : il contrôle avant de payer |
| Fondu de la barre du haut raccourci | Les titres des écrans à en-tête fixe restaient grisés sous le dégradé |
| Écran de salle au format cinéma (2,3 : 1) | Rogne les bandes noires des bandes-annonces et agrandit l'image utile |

## 18 novembre 2026 — versions 83 à 86 : page « Plus de réseau » et mini-jeu
| Décision | Pourquoi |
|---|---|
| Page dédiée plutôt qu'un simple bandeau | Un réseau coupé en plein trajet (train, zones blanches) doit être expliqué et rassurer |
| « Continuer hors ligne » toujours proposé | Le billet doit rester accessible sans réseau |
| Mini-jeu au chat, démarrage à l'action de l'utilisateur | Faire patienter sans imposer de mouvement (« Réduire les animations ») |
| Poses issues des planches de U Ghjattu-Volpe | Cohérence avec la mascotte, aucun dessin ajouté par l'assistant |
| Jeu rendu plus facile (vitesse douce, saut mémorisé, collisions indulgentes) | Retour de l'auteur : « trop difficile » |

## Limites et à valider
- Test à 3 personnes **non réalisé** (voir `TESTS.md`).
- Bandes-annonces verticales officielles trouvées pour 3 films sur 18 ; les autres s'affichent en 16:9 dans le cadre.
- « Suivre ce film » est enregistré sur l'appareil ; il n'envoie **pas** de vraie notification (il faudrait un serveur).
- Sujet adapté (Corse) par rapport à l'énoncé (« Ciné Lumière »).
- Photos et affiches : usage pédagogique, non commercial.
