# U CINEMÀ V2 — Protocole de test (3 personnes)

> À mener avec de vraies personnes. Les résultats ci-dessous sont **volontairement vides** : ne rien inventer.
> Le cours : « cinq participants suffisent » ; ici, 3 pour la version améliorée.

## Le test en 5 minutes par personne (version simplifiée)
**Pour qui ?** 3 personnes, de préférence avec un téléphone. **Matériel ?** le lien du prototype (https://mik2a-coder.github.io/u-cinema/) et la feuille `CHECKLIST-TESTS.md`.

**À dire en une phrase :** « On teste l'application, pas vous. Dites à voix haute ce que vous pensez. » Ne jamais aider.

**3 tâches seulement** (cocher ✔ réussi sans aide ou ✖ aidé / échec, noter les secondes) :
1. « Vous voulez voir un film **ce soir** avec un ami : réservez **deux places**. » (objectif : moins de 60 s)
2. « **Retrouvez votre billet** » (la carte de paiement de test passe toute seule). (objectif : moins de 20 s)
3. « **Choisissez votre personnage** dans le compte. » (objectif : moins de 20 s)

**2 questions :** « Qu'est-ce qui vous a arrêté ? » · « Qu'est-ce qui vous a plu ? »

## Résultats (à remplir avec de vraies personnes : ne rien inventer)
| Tâche | Personne 1 | Personne 2 | Personne 3 |
|---|---|---|---|
| 1. Réserver 2 places | | | |
| 2. Retrouver le billet | | | |
| 3. Choisir son personnage | | | |
| Ce qui l'a arrêté | | | |
| Ce qui lui a plu | | | |

## Synthèse (gravité × fréquence) → corrections → nouveau test
| Problème | Gravité (1–3) | Fréquence | Correction prévue | Corrigé ? |
|---|---|---|---|---|
| | | | | |


---

## Contrôles automatiques (réalisés, reproductibles)
| Contrôle | Comment | Résultat (18 nov. 2026) |
|---|---|---|
| Débordement horizontal et boutons coupés | `node tools/shoot.mjs <l> <h> sortie tools/scenarios/audit-debordement.json` sur 360×640, 390×844, 430×932, 768×1024, 1024×768, 1440×900 ; 6 écrans (accueil, fiche, réservation, places, commande, compte) | **0 défaut** sur les 6 tailles |
| Parcours complet captures | `tools/scenarios/parcours-mobile.json` et `parcours-bureau.json` | 9 captures mobile + 6 bureau (`rendu/captures/`) |
| Suite de vérifications fonctionnelles | 95 vérifications pendant le développement (recherche, parcours, tarifs, paiement refusé, modes clair/sombre, assistant, contrastes) | 95 / 95 au dernier passage complet, avant les ajouts du 17 novembre (le script n'est pas versionné) |
| En-têtes sans chevauchement | `tools/scenarios/audit-entete.json` sur 1000×640, 1280×800, 1440×900 : titres, boutons retour et barres d'étapes de 7 écrans comparés à la barre du haut | aucun chevauchement (18 nov. 2026, v82) |
| Fiches personnes | Pour les 146 noms de la programmation : la fiche s'ouvre, affiche le bon nom et au moins un film | 146 / 146 |
| Règle des 45 minutes | Pour chaque créneau : conflit calculé = conflit attendu (fin du film + 45 min) | cohérent sur les 6 créneaux |
| Assistant | « deux places côte à côte au fond… ce soir 20h » mène au récapitulatif avec les bonnes places, l'horaire le plus proche et le total | vérifié ; refus propre pour un film pas encore en salle |
| Page « Plus de réseau » | Joueur automatique : 3 parties sur 3 gagnées jusqu'à l'arrivée ; une partie sans saut finit par la chute du chat sur un objet ; saut visible en entier dans le cadre | vérifié (Chrome, v86) ; à essayer sur iPhone et Safari |
| Bouton de commande | Sur la page Commande, le bouton garde sa taille (≈ 52 px de haut, en bas de page) avec et sans CGV cochées ; achat jusqu'au billet | vérifié (v90) après un conflit de classe repéré sur une vidéo d'écran |
| Bandes-annonces | Pour les 22 films : lien YouTube vérifié (réponse « oEmbed » valide) et extrait de la fiche révélé en environ 2,5 s (Chrome) | voir v92 |
| Contraste | Mesure des paires texte/fond sur 5 palettes | ≥ 4,5 : 1 (voir `DESIGN.md`) |

## Revues déjà intégrées — la version améliorée (1 relecteur : l'auteur)
> Ce **n'est pas** le test à 3 personnes : ce sont des retours de revue de l'auteur sur ses appareils (Chrome, Safari), chacun ayant conduit à une correction visible.

| Retour observé | Correction |
|---|---|
| Mode clair illisible sur fond orangé | Palette claire déduite de la palette active, îlots sombres sous les textes sur images |
| Nom et logo peu convaincants | Nom « U Cinemà », logo repris du dessin de l'auteur (chat aux lunettes 3D), espacements d'origine |
| Vue depuis la place « pas optimisée » | Scène 3D refaite, simplifiée et sombre, avec la bande-annonce sur l'écran |
| Bande-annonce : titre YouTube visible, image figée au début, boutons parasites | Recadrage sans titre ; la vidéo n'apparaît que quand elle joue ; cadre vertical sans zoom |
| Bug de transition au clic sur « Réserver » | Cause trouvée sur la vidéo d'écran : l'onde au toucher agrandissait le bouton ; corrigée et vérifiée sur 133 boutons |
| Boutons « pas du tout design » en clair | Boutons principaux encre foncée + texte crème, secondaires en verre ; règle écrite dans `DESIGN.md` |
| Même film réservé deux fois à la même heure | Séances en conflit grisées, refus au paiement avec explication |
| Photos de petite faim absentes | Bannières de suggestions avec photos, combos, onglets |
| Contraste dur entre la barre du haut et la page | Verre progressif : opaque en haut, fondu vers le contenu |
| Carré autour du logo et du chat sous Safari | Suppression de tout filtre sur les images |
| Bouton « Suivre » : état suivi peu visible | État plein (coche, cloche pleine), déplacé à côté de « Réserver » |
| Animations décoratives du chat | Suppression des boucles et de la bulle du logo |
| Résultats de recherche, plan de salle, 5 dates qui débordent | Centrage, rangée A dégagée, dates sur 5 colonnes |
| Suivis introuvables dans le compte | Section « Mes suivis » (films, acteurs, réalisateurs), « Retirer » aligné à droite |
| Transition du choix de places jugée moins fluide qu'un plan de stade | Vue d'ensemble puis zoom sur la zone ; « Changer de place / Acheter » depuis la vue de la place |
| Vue depuis la place cassée sous Safari (bloc noir, côtés manquants) | Écran 16:9 qui contient exactement la vidéo |
| Ligne dure entre la barre du haut et la page (Safari) | Fondu sans flou ni masque ; barre transparente sur l'accueil |
| Fond de l'accueil sans forme | Ovale doux qui déborde de l'écran, opacité 55 % / 90 % |
| Affiches de la liste mal alignées | Grille alignée sur le titre, aucune élévation au survol |
| Barre d'étapes qui ne donne pas l'impression d'avancer | Segments atteints pleins et point lumineux sur l'étape en cours |
| Titres coupés ou grisés sous la barre du haut | Fondu de la barre raccourci, en-tête du plan de salle décalé |
| « Mes billets » sans effet malgré une réservation | Ouvre le billet ou la liste des billets, même après rechargement |
| Nom d'acteur ou de compositeur qui ramène à l'accueil | Fiche personne dédiée (biographie, filmographie, retour) |
| Vue depuis la place : fauteuils devant soi au premier rang, cadre autour de l'écran | Premier rang dégagé, écran sans cadre et plus grand |
| Bandes noires dans le cadre vertical des affiches | Extraits recadrés plein cadre |

## Test à 3 personnes — à compléter
Remplir la « Grille de résultats » ci-dessus avec de **vraies** observations, puis la synthèse gravité × fréquence, puis cocher « Corrigé ? ». Livrer ensuite un avant/après d'au moins 2 corrections.
