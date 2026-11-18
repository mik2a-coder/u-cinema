# Journal des versions

Chaque version correspond au numéro de cache du service worker (`cinelux2-vNN` dans `sw.js`), affiché en bas de la page **Compte** (« Version vNN »). Pour passer d'une version à l'autre : recharger sans cache (Cmd + Option + R sur Safari).

## Fichiers créés ou modifiés (versions 82 à 86)

| Fichier ou dossier | Version | Modification |
|---|---|---|
| `index.html` | v82–v86 | Toutes les évolutions de l'application (fiches personnes, assistant, avoir, récompenses, en-têtes, vue de salle, extraits, page « Plus de réseau », mini-jeu) |
| `sw.js` | v82–v86 | Numéro de cache `cinelux2-v82` à `v86`, nouvelles icônes mises en cache |
| `manifest.webmanifest` | v82 | Icône « maskable » dédiée |
| `icons/` (favicon-32, favicon-48, icon-192, icon-512, apple-touch-icon, icon-512-maskable) | v82 | Nouvelles icônes à partir du logo du chat |
| `img/og.jpg` | v82 | Image d'aperçu de lien 1200×630 |
| `img/chat/` (`c01` à `c11`, `triste`, `raw01` à `raw11`, 3 planches) | v84–v86 | Poses du chat pour le mini-jeu et la page d'erreur |
| `tools/make-icons.mjs`, `tools/og.html` | v82 | Fabrication des icônes et de l'image d'aperçu |
| `tools/cut-chat.mjs`, `tools/clean-sprites.mjs` | v84–v86 | Découpe et nettoyage des poses du chat |
| `tools/scenarios/audit-entete.json` | v82 | Contrôle des chevauchements d'en-têtes |
| `tools/build-rendu.py` | v82 | Dossier de rendu au style « artefact », sans notes de notation |
| `documents/DIRECTION-ARTISTIQUE.md`, `documents/VERSIONS.md` | v82–v86 | Nouveaux documents |
| `BRIEF-PERSONA.md`, `PARCOURS.md`, `BAREME.md`, `DESIGN.md`, `TESTS.md`, `JOURNAL.md`, `README.md` | v82–v86 | Personas Mika (Ajaccio) et Ghjuvana Maria (Bastia), page d'erreur, tests, décisions |
| `RENDU-U-CINEMA.pdf`, `CHECKLIST-TEST-3-PERSONNES.pdf`, `CINELUX-autonome.html` | v82–v86 | Régénérés à chaque version |

**Page d'erreur réseau, à ouvrir :** https://mik2a-coder.github.io/u-cinema/#x:0:off

## Version 96 — 18 novembre 2026

| N° | Demande | Ce qui a été fait | Où le voir |
|---|---|---|---|
| 1 | Pages de bureau mal adaptées, barre de défilement « trop au milieu » | Sur grand écran, la **barre de défilement est au bord de la fenêtre** (séance, commande, billet, accueil) : seule la colonne de contenu est centrée. Le **plan de salle s'adapte à la hauteur** de la fenêtre : plus de légende cachée derrière « Acheter » ni de défilement dans le panneau (testé de 1024×768 à 1920×1080) | Toutes les pages, bureau |
| 2 | Contraste des étoiles dans « Films que j'ai vus » | Étoiles pleines en or foncé (clair) ou or vif (sombre) avec contour renforcé ; étoiles vides en contour plus marqué ; libellé « Votre note » plus gras | Compte |
| 3 | Bouton « Retour » de Google Chrome inutilisable chez une collègue | Cause probable : l'application n'enregistrait pas chaque écran dans l'historique du navigateur (Chrome ignore les entrées ajoutées sans geste de l'utilisateur). Chaque changement d'écran crée maintenant une entrée ; « Retour » ramène à l'écran précédent, ferme d'abord une fenêtre, l'assistant ou la vue depuis la place s'ils sont ouverts ; après un achat, « Retour » du billet ramène à l'accueil | Tout le parcours |
| 4 | Lien « Règles, confidentialité et mentions légales » toujours dans le pied de page, jamais derrière un bouton | Le lien est le **dernier élément de chaque page** (y compris le plan de salle), avec de la marge sous lui pour les barres de boutons ; le doublon de la fiche film est supprimé | Toutes les pages |
| 5 | Changement d'état quand on sélectionne une option | Les filtres « Audiodescription » et « Sous-titres… » deviennent **dorés avec une coche** une fois choisis | Séance |

## Version 95 — 18 novembre 2026

| Demande | Ce qui a été fait | Où le voir |
|---|---|---|
| Plus de possibilité d'annuler un billet | Cause : l'annulation n'existait que dans Compte › Mes réservations, plus sur le billet. Ajout d'un bouton **« Annuler la réservation »** directement sur la page du billet (juste après l'achat et depuis « Mes billets »), en deux temps (confirmation avec le montant de l'avoir), avec les mêmes règles : jusqu'à 2 h avant, avoir de 12 mois ; sinon message « Annulation impossible » | Billet |
| Mode sombre : le fond flouté en ovale n'est pas respecté comme en clair | La bande du haut était une barre noire pleine en mode sombre ; elle devient translucide pour laisser voir le fond coloré, comme en clair | Toutes les pages, mode sombre |

## Version 94 — 18 novembre 2026

| Demande | Ce qui a été fait | Où le voir |
|---|---|---|
| Dessin « Heureux » du chat pour la rubrique enfants | La tête « Heureux » de la planche de U Ghjattu-Volpe remplace la mascotte assise dans le bandeau « Rubrique enfants » (détourée en gardant le pelage blanc et les dents) | Accueil > Enfants |

## Version 93 — 18 novembre 2026

| N° | Demande | Ce qui a été fait | Où le voir |
|---|---|---|---|
| 1 | Checklist à cases à cocher, facile / difficile / à améliorer | Feuille d'une page : pour chaque tâche et chaque personne, **résultat** (réussi seul, aidé, échec), **difficulté** (facile, moyen, difficile) et **ce qu'il faut améliorer** (cases), plus l'avis général | `documents/CHECKLIST-TESTS.md`, `A-RENDRE/CHECKLIST-TEST-3-PERSONNES.pdf` |
| 2 | Politiques d'achat, d'annulation, avoir et horaires : être dans les règles, toutes les contraintes d'un cinéma | Nouvelles sections « Annulation, avoir et remboursement », « Horaires et organisation du cinéma » et « Règles du cinéma » dans les informations légales ; CGV complétées (frais de service, réservation, annulation) ; **avoir valable 12 mois** (date affichée, avoir périmé non proposé) ; remboursement intégral si le cinéma annule ; rappels sur les pages Séance et Commande ; horaires dans le choix du cinéma ; assistant qui répond sur horaires, règles et annulation. Document `POLITIQUES.md` avec références juridiques | Pied de page de chaque écran, étapes Séance et Commande |
| 3 | Paragraphe des idées ajoutées avec plus-value dans le rendu | Nouveau chapitre « Idées ajoutées et plus-values » (jeu hors connexion, billets hors ligne, assistant, vue depuis la place, règles claires, points, enfants, fiches personnes, personnages, accessibilité…) | `documents/IDEES.md`, PDF |

## Version 92 — 18 novembre 2026

| N° | Demande | Ce qui a été fait | Où le voir |
|---|---|---|---|
| 1 | Rubrique pour enfants, 5 dessins animés minimum | Nouvel onglet **Enfants** sur l'accueil avec bandeau « Rubrique enfants » : 8 titres (Toy Story 5, Super Mario Galaxy, Vaiana, Angry Birds 3 et **4 nouveaux** : Hoppers, Minions & Monsters, Paw Patrol: The Dino Movie, The Cat in the Hat). Données (dates, durées, distribution, réalisateurs) relevées sur Wikipédia ; note affichée = moyenne des critiques Rotten Tomatoes indiquée par Wikipédia ; bandes-annonces officielles contrôlées | Accueil > Enfants |
| 2 | Bouton de la première page perturbant et long | « Continuer » devient **« Suivant »** (« Commencer » à la dernière étape) ; « Passer l'introduction » devient un **vrai bouton « Passer l'intro »**, bien visible sous le bouton principal | Introduction |
| 3 | Une bande-annonce pour tous les films | Les 22 films ont une bande-annonce officielle contrôlée (réponse YouTube valide) ; chaque fenêtre de bande-annonce propose aussi « Ouvrir sur YouTube » si la vidéo intégrée ne s'affiche pas | Fiche film |
| 4 | Prompts pertinents et améliorés dans le dossier de rendu | Journal : conseils pour bien écrire un prompt, tableau « mon prompt / version améliorée / résultat » (14 lignes) et 4 exemples complets, dont celui du fond coloré tiré des affiches | `documents/JOURNAL.md`, PDF |

## Version 91 — 18 novembre 2026

| N° | Demande | Ce qui a été fait | Où le voir |
|---|---|---|---|
| 1 | Personnaliser la photo du compte avec des personnages de films (≈ 10) | 10 personnages dessinés, inspirés des films de la programmation ; choix dans Compte (touche la photo ou « Changer mon personnage ») ; retour à l'initiale possible | Compte |
| 2 | Choix des places sur toute la salle, pas par rang | Le plan montre toute la salle d'un coup ; plus de zoom par zone ; bouton « Voir depuis ma place » décalé pour ne plus recouvrir l'adresse sur téléphone | Places |
| 3 | Deux réalisateurs : fiche de chacun et choix du suivi | Chaque nom ouvre sa fiche ; « Suivre » propose de choisir l'un, l'autre ou les deux | Fiche film |
| 4 | Bande-annonce de la salle qui ne se lance pas | Cause trouvée : depuis la v82, la vidéo n'était révélée que si l'application YouTube envoyait l'état de lecture avec l'heure exacte ; l'état seul ne suffisait pas. Corrigé (valable aussi pour l'extrait de la fiche film, révélé ~2,5 s après l'affiche). Ajout d'un bouton de secours « Lancer la bande-annonce » | Vue depuis la place, fiche film |
| 5 | Documents à jour et test utilisateur simplifié | Test réduit à 3 tâches et 2 questions (une page) ; documents mis à jour | `documents/` |

## Version 90 — 18 novembre 2026

| Demande | Ce qui a été fait | Où le voir |
|---|---|---|
| Problème de paiement apparu récemment (vidéo Safari) | Cause trouvée : depuis la v83, la page « Plus de réseau » utilisait le nom de classe `off`, déjà employé par le bouton de commande grisé (CGV non cochées). Le bouton héritait de « plein écran » et recouvrait toute la page d'un voile gris, avec seul son texte visible au milieu. La page réseau a été renommée (`netoff`) : le bouton retrouve sa place en bas | Commande |
| Transitions de l'introduction à améliorer | Les trois affiches de l'étape suivante sont préchargées et décodées avant l'échange : plus de cartes noires pendant le changement | Introduction |

## Version 89 — 18 novembre 2026

| Demande | Ce qui a été fait | Où le voir |
|---|---|---|
| Bug à l'achat sur la page Commande, sur tous les supports | Cause trouvée : quand la séance choisie était déjà réservée, le message de refus apparaissait sous l'écran et le bouton semblait ne rien faire. Corrections : le message est amené à l'écran et doublé d'un bandeau ; « Acheter » sur le plan de salle refuse dès l'étape précédente et renvoie aux séances ; la séance proposée par défaut évite désormais les séances déjà prises (sur 5 jours) | Plan de salle, Commande |

## Version 88 — 18 novembre 2026

| Demande | Ce qui a été fait | Où le voir |
|---|---|---|
| Images du chat abîmées sur fond sombre (halo blanc, taches sombres sur le museau) | Nouveau détourage des poses : seul le fond relié au bord est retiré (le pelage blanc est conservé), les trous entre les pattes sont nettoyés et le liseré blanc est rogné ; poses et tête triste régénérées | Page « Plus de réseau », mode sombre |

## Version 87 — 18 novembre 2026

| Demande | Ce qui a été fait | Où le voir |
|---|---|---|
| Même effet de fond coloré sur la première page | L'introduction reçoit le fond flouté en ovale de l'accueil, qui change de couleur avec les affiches à chaque « Continuer » ; barre du haut transparente | Introduction |
| En-tête qui garde le fond flouté quand on descend | La barre du haut ne se remplit plus de crème au défilement de l'accueil : le fond coloré reste visible derrière elle sur toute la page | Accueil |

## Rangement du dossier (après la v86)
Le dossier du projet s'appelle désormais **U CINEMA**. Textes dans `documents/`, PDF à remettre dans `A-RENDRE/`, anciens essais dans `archives/`, version autonome renommée `U-CINEMA-autonome.html`, lanceurs « Ouvrir U CINEMA ». Le site (à la racine) n'a pas bougé.

## Version 86 — 18 novembre 2026

| Demande | Ce qui a été fait | Où le voir |
|---|---|---|
| Mini-jeu plus fluide, plus facile, chat non coupé | Jeu réécrit avec tes 11 poses remises dans l'ordre : départ assis, cycle de course en 5 images, saut en 3 temps (montée, sommet, descente), glissade à l'arrivée si on gagne, chute sur le dos sur un objet. Mouvement indépendant de la fréquence de l'écran, vitesse de départ plus douce, saut mémorisé juste avant l'atterrissage, collisions indulgentes, zone de jeu plus haute (le chat ne sort plus du cadre) | Page « Plus de réseau » |
| Garder les boîtes de pop-corn, ajouter d'autres objets de cinéma | Pop-corn (plus fréquent), claquette, bobine, gobelet, projecteur ; ligne d'arrivée à 260 m | Page « Plus de réseau » |

## Version 85 — 18 novembre 2026

| Demande | Ce qui a été fait | Où le voir |
|---|---|---|
| Utiliser la planche de sprites 2D | Cycle de course en 6 images, pose de saut, et obstacles de la planche (caisse, barrière, rocher) | Page « Plus de réseau » |

## Version 84 — 18 novembre 2026

| Demande | Ce qui a été fait | Où le voir |
|---|---|---|
| Chat qui court (et non assis) dans le mini-jeu, tête triste en haut de la page | Poses découpées dans les planches de U Ghjattu-Volpe : deux poses de course qui alternent, pose de saut en l'air ; tête « Triste » en haut de la page « Plus de réseau » (`img/chat/`, outil `tools/cut-chat.mjs`) | Page « Plus de réseau » |

## Version 83 — 18 novembre 2026

| Demande | Ce qui a été fait | Où le voir |
|---|---|---|
| Page dédiée en cas de réseau coupé ou instable, avec un mini-jeu du chat | Page « Plus de réseau » (mascotte, message rassurant, « Réessayer » qui vérifie vraiment la connexion, « Continuer hors ligne » pour garder ses billets) et mini-jeu façon dinosaure de Google : U Ghjattu-Volpe saute par-dessus des seaux de pop-corn (touche, clic ou Espace), score et record gardés sur l'appareil. Au paiement sans réseau : « Connexion nécessaire », commande conservée. Connexion très lente : bandeau « Connexion instable ». Test rapide : ajouter `#x:0:off` à l'adresse | Coupure du réseau, paiement hors ligne |

## Version 82 — 18 novembre 2026 (revue en 24 points)

Contrôles réalisés avant livraison : 0 défaut de débordement sur 6 largeurs (360 à 1440 px) ; 0 chevauchement avec la barre du haut sur 3 tailles de fenêtre ; 146 fiches personnes valides ; règle des 45 minutes cohérente sur tous les créneaux ; annulation, avoir, récompenses et « Mes billets » vérifiés de bout en bout.

| N° | Demande | Ce qui a été fait | Où le voir |
|---|---|---|---|
| 1 | Extrait vidéo : 2 s après l’affiche | Le lancement se fait ~2 s après l’affiche (au lieu de ~4 s) ; la vidéo n’apparaît que lorsque le contenu joue vraiment | Fiche film |
| 2 | Barre d’étapes plus lisible | Chaque étape atteinte est pleine, l’étape en cours porte un point lumineux : « étape 2 sur 4 » = 2 segments sur 4 | Séance, Places, Commande |
| 3 | Barre de défilement moderne | Fine, arrondie, discrète, qui s’éclaircit au survol (souris uniquement) | Grands écrans |
| 4 | Assistant qui parle à l’accueil | Bulle « Miaou ! 🐾 Donne-moi ton humeur, je te trouve le film idéal ! » 1,4 s après l’arrivée sur l’accueil, même message à l’ouverture | Accueil |
| 5 | Logo de la page web et du lien | Nouvelles icônes (onglet, écran d’accueil, maskable) et image d’aperçu de lien 1200×630 ; titre « U CINEMÀ » | Onglet, partage |
| 6 | Données et confidentialité | Retiré des préférences ; lien texte « Confidentialité et mentions légales » en pied de page de tous les écrans | Tous les écrans |
| 7 | Mode clair/sombre automatique | Mode « Auto » par défaut : suit les préférences de l’appareil | Affichage et accessibilité |
| 8 | Pas de double réservation | Même film même heure, deux films qui se chevauchent, ou moins de 45 min entre deux films : créneau grisé et message « Vous avez déjà une séance… » au paiement | Séance, Commande |
| 9 | Pages acteurs et réalisateurs | Nouvelle fiche personne : photo, rôles, biographie, filmographie, « Suivre », bouton retour | Fiche film > distribution |
| 10 | Liens vérifiés | Les 146 noms de la distribution, réalisation, production et musique ouvrent la bonne fiche (testé) ; fini le retour à l’accueil (James Newton Howard) | Fiche film, Compte, recherche |
| 11 | Assistant performant | Comprend « deux places côte à côte au fond pour un film drôle ce soir à 20 h », prépare la réservation et ouvre le récapitulatif avant paiement ; répond aussi sur tarifs, annulation, points, durée, casting, accessibilité, cinémas | Assistant |
| 12 | Superposition des textes | Le fondu de la barre du haut ne recouvre plus les titres ; en-tête du plan de salle décalé sous la barre ; 0 chevauchement sur 3 tailles de fenêtre | Toutes les pages |
| 13 | Écran de salle sans cadre | Liseré brun supprimé, seule la lueur reste | Vue depuis la place |
| 14 | Vue depuis la place | Écran plus grand (format cinéma), rangée du premier rang dégagée (plus de fauteuils devant soi), voisins réduits au bord | Vue depuis la place |
| 15 | Annulation = avoir | Annulation possible jusqu’à 2 h avant ; le montant devient un avoir (jamais un remboursement), utilisable à la commande | Compte, Commande |
| 16 | Points : friandise et −5 % | Friandise offerte (300 pts) et −5 % sur une place (500 pts) à débloquer, à activer dans la commande | Compte, Commande |
| 17 | Croix de l’assistant à droite | Alignée à droite de l’en-tête | Assistant |
| 18 | Animation de l’introduction | Les affiches glissent, changent et se décalent avec le texte à chaque « Continuer » ; bouton moins large (264 px) | Introduction |
| 19 | Dates de sortie redondantes | Une seule date par film à venir (accueil et fiche) | Accueil, Fiche film |
| 20 | Pas de publicités dans les extraits | La vidéo n’est révélée qu’après le point de départ de l’extrait : une publicité éventuelle reste cachée derrière l’affiche (limite : dépend de YouTube) | Fiche film, Vue depuis la place |
| 21 | Extraits au format vertical | Le cadre vertical affiche toujours la vidéo plein cadre (Shorts officiels pour 3 films, recadrage centré pour les autres) ; plus de bande 16:9 | Fiche film |
| 22 | « Mes billets » fonctionne | Ouvre le billet (ou la liste si plusieurs réservations), y compris après rechargement | Menu, barre du haut |
| 23 | Informations cachées par le positionnement | Même correction que le point 12, vérifiée sur toutes les pages | Toutes les pages |
| 24 | Encadré noir des affiches | Les bandes noires intégrées aux bandes-annonces sont rognées (plein cadre) | Fiche film |

**Reste à valider par l'auteur** : rendu dans Safari (vue depuis la place, en-tête) ; relecture des biographies ; liens des extraits verticaux pour les 15 autres films ; test à 3 personnes.

## Historique complet des versions

| Version | Date | Modification |
|---|---|---|
| Version | Date | Modification |
|---|---|---|
| v21 | 16/11/2026 | U CINEMÀ V2 : prototype de réservation de cinéma (PWA) |
| v22 | 16/11/2026 | Transitions : fondu simple entre les écrans (sauf l'affiche accueil/fiche), cache v22 |
|  | 16/11/2026 | Ajout du README |
| v23 | 16/11/2026 | Thème clair par défaut |
| v24 | 16/11/2026 | Vue depuis la place : la vidéo est recadrée dans l'écran (plus de bloc noir) |
| v25 | 16/11/2026 | Petite faim : photo du combo sur la proposition |
| v26 | 16/11/2026 | Boutons clairs : encre + or à plat ; photos Menu Solo et Duo gagnant |
| v27 | 16/11/2026 | Compte : deux colonnes sur bureau, état vide soigné |
| v28 | 16/11/2026 | Boutons clairs selon les règles de départ ; transitions séquentielles ; pas de doublon de réservation ; vidéo sans image figée ; fondu du chat |
| v29 | 16/11/2026 | Mode clair : boutons principaux en encre foncée partout |
| v31 | 16/11/2026 | Bug du bouton Réserver : l'onde au toucher agrandissait le bouton (règle .cta span) ; favicon U ; build autonome |
| v32 | 16/11/2026 | Logo en mode clair : billet encre et U or |
| v33 | 17/11/2026 | Nouveau logo : chat aux lunettes 3D (icônes, en-tête, favicon) |
| v34 | 17/11/2026 | Logo : le U se rapproche du chat |
| v35 | 17/11/2026 | Logo : petit espace entre le chat et le U |
| v36 | 17/11/2026 | Logo : espacements du fichier d'origine partout (en-tête, introduction) |
| v37 | 17/11/2026 | Logo : U un peu plus proche du chat |
| v38 | 17/11/2026 | Logo : fond du PNG entièrement transparent (plus de carré) |
| v39 | 17/11/2026 | Logo sur pastille de verre, U bronze renforcé : lisible sur tous les fonds |
| v40 | 17/11/2026 | Logo : sans cadre ni pastille, U ambre soutenu |
| v41 | 17/11/2026 | Fiche film : portraits réalisateurs, bouton Suivre ce film, recherche au clic sur un nom, retour mémorisé ; barre haute opaque, sans barres de défilement |
| v42 | 17/11/2026 | Fiche film bureau : affiche 2 s puis bande-annonce entière dans le cadre vertical (sans recadrage) |
| v43 | 17/11/2026 | Prêt pour les vidéos verticales : champ ytv par film (cadre plein) |
| v44 | 17/11/2026 | Vidéos verticales officielles : Project Hail Mary, Spider-Man, Heart of the Beast |
| v45 | 17/11/2026 | Compte : activité récente et annulation ; le chat du logo parle ; lien films à venir ; préchauffage vidéo après consentement |
| v46 | 17/11/2026 | Plan de salle mobile : bouton Voir depuis ma place ne cache plus la rangée A |
| v47 | 17/11/2026 | Logo : nouveau nom de fichier et page toujours rechargée depuis le réseau (plus de vieux cadre en cache) |
| v48 | 17/11/2026 | Logo : suppression de tout filtre autour de l'image (plus aucun cadre possible) |
| v49 | 17/11/2026 | Barre haute : fondu doux vers la page, plus de ligne dure |
| v50 | 17/11/2026 | Barre haute : verre progressif (flou et teinte qui s'estompent) |
|  | 17/11/2026 | Notes : grille Peaufiner réévaluée (19 sur 22, 3 à nuancer) |
| v51 | 17/11/2026 | Peaufiner : chat sans boucle décorative, 5 dates visibles sur petit écran, Compte sans débordement ; grille 21/22 |
| v52 | 17/11/2026 | D'après la vidéo : avatar mène au compte, messages au-dessus du bouton Réserver, fond de la bande-annonce plus lisible |
| v53 | 17/11/2026 | Chat : plus aucune ombre filtrée (cadre dans Safari) |
| v54 | 17/11/2026 | Suppression de la bulle animée du logo ; message d'accueil du chat sans mouvement |
| v55 | 17/11/2026 | Boutons Suivre : état « Suivi » plein et évident (encre en clair, or en sombre), coche et cloche pleine |
| v56 | 17/11/2026 | Suivre ce film : déplacé dans la barre d'action, à côté de Réserver |
|  | 18/11/2026 | Dossier de rendu : barème, brief, parcours, design system, tests, journal, PDF |
| v57 | 18/11/2026 | Plan de salle : vue d'ensemble puis zoom sur la zone des places proposées, choix de zone (Avant, Centre, Fond) |
| v58 | 18/11/2026 | Vue depuis la place : Changer de place / Acheter ; checklist de test (3 participants) en PDF paysage ; dossier de rendu mis à jour |
|  | 18/11/2026 | Checklist de test : format vertical 3:4 pour tablette reMarkable, colonnes d'écriture élargies |
| v59 | 18/11/2026 | Compte : section Mes suivis (films, acteurs, réalisateurs) ; suivre une personne depuis la recherche ; suivis réalisateurs mémorisés |
| v60 | 18/11/2026 | Téléphone : logo de l'app en haut à gauche de l'accueil (le compte reste dans le menu du bas) |
| v61 | 18/11/2026 | Vue depuis la place : écran 16:9 qui contient exactement la vidéo (plus de bloc noir sous Safari) |
| v62 | 18/11/2026 | Compte : ordre réservations / rappels / suivis / films vus, Retirer aligné à droite, activité récente retirée |
| v63 | 18/11/2026 | Accueil : fond en ovale doux (couleur de l'affiche au centre, bords neutres), aucun flou sur les boutons |
| v64 | 18/11/2026 | Barre haute : fondu sans flou ni masque (plus de ligne sous Safari) |
| v65 | 18/11/2026 | Accueil : contour de l'ovale de fond bien visible |
| v66 | 18/11/2026 | Accueil : bord de l'ovale adouci (fondu progressif) |
| v67 | 18/11/2026 | Accueil : la barre du haut est transparente en haut de page, l'ovale de couleur passe derrière elle |
| v68 | 18/11/2026 | Accueil : dégradé élargi au-delà des bords de l'écran (flèches comprises) |
| v69 | 18/11/2026 | Accueil clair : opacité du fond à 55 % |
| v70 | 18/11/2026 | Liste des films alignée, annexes complétées (parcours, design, tests, journal, barème, notes), captures et PDF régénérés |
| v71 | 18/11/2026 | Fenêtres : modales centrées avec voile adapté au thème, sur tout le site ; liste des films alignée |
| v72 | 18/11/2026 | Modales : voile plus accentué (80 % sombre, 62 % clair) |
| v73 | 18/11/2026 | Vue depuis la place refaite : scène en couches 2D, velours rouge, rangées en perspective, ambiance plus claire, fiable sous Safari |
| v74 | 18/11/2026 | Vue depuis la place : salle sombre sans détails, têtes discrètes, écran seul point clair |
| v75 | 18/11/2026 | Vue depuis la place : écran plus imposant, bande-annonce conservée |
| v76 | 18/11/2026 | Vue depuis la place immersive : écran presque pleine largeur avec la bande-annonce, sièges voisins visibles, salle plus sombre |
| v77 | 18/11/2026 | Compte : numéro de version affiché en bas de page (pour vérifier la mise à jour) |
| v78 | 18/11/2026 | Retour de la vue depuis la place : fondu avec léger recul au lieu de l'iris qui se coupe |
| v79 | 18/11/2026 | Commande : sans CGV cochées, le clic mène à la case à valider et la met en évidence |
| v80 | 18/11/2026 | Retour fiche → accueil : plus de vol d'affiche vers une carte hors écran, liste conservée sans rechargement des images |
| v81 | 18/11/2026 | Retour sur l'accueil : le dernier film choisi reste en vue et se signale par un anneau doré |
| v82 | 18/11/2026 | v82 : 24 points de la revue (fiches personnes, mes billets, assistant qui réserve, avoir/récompenses, annulation 2 h, 45 min entre séances, barre d'étapes, défilement, logo/icônes, écran de salle sans cadre, extraits sans bandes noires, en-têtes sans chevauchement) |
| v82 | 18/11/2026 | Revue en 24 points (voir ci-dessus) |
| v83 | 18/11/2026 | Page « Plus de réseau » avec mini-jeu du chat |
| v84 | 18/11/2026 | Mini-jeu : chat animé qui court et saute, tête triste en haut |
| v85 | 18/11/2026 | Mini-jeu : cycle de course en 6 images et obstacles de la planche de sprites |
| v86 | 18/11/2026 | Mini-jeu : poses remises dans l'ordre, départ, arrivée en glissade, chute, objets de cinéma, plus facile |
| v87 | 18/11/2026 | Fond flouté en ovale sur l'introduction ; en-tête de l'accueil transparent au défilement |
| v88 | 18/11/2026 | Détourage du chat refait pour le mode sombre |
| v89 | 18/11/2026 | Achat : refus d'une séance déjà réservée enfin visible, créneau par défaut sans doublon |
| v90 | 18/11/2026 | Correctif paiement (conflit de classe avec la page réseau) ; affiches de l'introduction préchargées |
| v91 | 18/11/2026 | Personnages du compte, plan de salle complet, deux réalisateurs, bande-annonce de la salle, test simplifié |
| v92 | 18/11/2026 | Onglet Enfants (4 films ajoutés), boutons de l'introduction, bandes-annonces pour tous, prompts du journal |
| v93 | 18/11/2026 | Politiques d'achat et horaires complets, avoir de 12 mois, checklist à cocher, chapitre « Idées ajoutées » |
| v94 | 18/11/2026 | Tête « Heureux » du chat dans la rubrique enfants |
| v95 | 18/11/2026 | Annulation depuis le billet ; bande du haut translucide en mode sombre |
| v96 | 18/11/2026 | Défilement au bord de la fenêtre, plan de salle ajusté, étoiles lisibles, bouton Retour du navigateur, lien légal en pied de page, état des filtres |
