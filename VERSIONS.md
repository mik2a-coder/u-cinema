# Journal des versions

Chaque version correspond au numéro de cache du service worker (`cinelux2-vNN` dans `sw.js`), affiché en bas de la page **Compte** (« Version vNN »). Pour passer d'une version à l'autre : recharger sans cache (Cmd + Option + R sur Safari).

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
