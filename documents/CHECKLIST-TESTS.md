# U CINEMÀ — Checklist de test (3 participants)

> À remplir au stylet sur tablette (format vertical) ou à imprimer. **Ne jamais aider** le participant. Cocher ☑ (réussi) ou ☒ (problème) dans la colonne de chaque participant : **P1 · P2 · P3**.
> Prototype : https://mik2a-coder.github.io/u-cinema/ (recharger avec Cmd + Maj + R avant chaque test)

## A. Avant le test
| ☐ | À faire |
|---|---|
| ☐ | Participant prévenu : « On teste l'application, pas vous. Pensez à voix haute. » |
| ☐ | Appareil du participant (ou prêté) : téléphone, **une seule main**, luminosité normale |
| ☐ | Mode avion **éteint** (sauf scénario 6) ; mode d'affichage clair (ou celui du participant) |
| ☐ | Chronomètre prêt · feuille de notes · enregistrement d'écran avec accord oral |
| ☐ | Participant 1 : âge ___ · usage du cinéma ___ · besoin d'accessibilité : oui / non |
| ☐ | Participant 2 : âge ___ · usage du cinéma ___ · besoin d'accessibilité : oui / non |
| ☐ | Participant 3 : âge ___ · usage du cinéma ___ · besoin d'accessibilité : oui / non |

## B. Scénarios (à lire tels quels)
Réussi **sans aide** = ☑. Noter le temps en secondes. Cases : ☐ réussi · ☒ échec.
| # | Consigne · objectif · si échec | P1 | P2 | P3 |
|---|---|---|---|---|
| S1 | « Vous voulez voir un film **ce soir** avec un ami. Réservez **deux places**. »<br>**Objectif ≤ 60 s** · *si échec : raccourcir : séances du jour et bouton plus clairs* | ☐ ___ s | ☐ ___ s | ☐ ___ s |
| S2 | « Votre ami est **étudiant** : retrouvez le tarif adapté. »<br>**Objectif ≤ 20 s** · *si échec : afficher un tarif réduit par défaut* | ☐ ___ s | ☐ ___ s | ☐ ___ s |
| S3 | « Choisissez des places **au fond** de la salle. » (zones du plan)<br>**Objectif ≤ 15 s** · *si échec : zones plus visibles, texte « Voir toute la salle »* | ☐ ___ s | ☐ ___ s | ☐ ___ s |
| S4 | « Regardez **la vue depuis votre place**. »<br>**Objectif ≤ 10 s** · *si échec : déplacer ou renommer le bouton* | ☐ ___ s | ☐ ___ s | ☐ ___ s |
| S5 | « Ajoutez un **pop-corn** à votre commande. »<br>**Objectif ≤ 20 s** · *si échec : montrer la petite faim plus tôt* | ☐ ___ s | ☐ ___ s | ☐ ___ s |
| S6 | « La carte est **refusée** : terminez quand même. » (carte de test •••• 0002)<br>**Objectif ≤ 30 s** · *si échec : message plus clair, « Changer de moyen » plus visible* | ☐ ___ s | ☐ ___ s | ☐ ___ s |
| S7 | « **Suivez** ce film pour être prévenu des nouveautés. »<br>**Objectif ≤ 10 s** · *si échec : déplacer la cloche, changer le libellé* | ☐ ___ s | ☐ ___ s | ☐ ___ s |
| S8 | « Retrouvez votre **billet** sans connexion. » (mode avion)<br>**Objectif ≤ 20 s** · *si échec : lien plus direct vers le billet* | ☐ ___ s | ☐ ___ s | ☐ ___ s |
| S9 | « **Annulez** cette réservation. » (Compte › Mes réservations)<br>**Objectif ≤ 30 s** · *si échec : annulation plus visible* | ☐ ___ s | ☐ ___ s | ☐ ___ s |
| S10 | *(accessibilité)* « Agrandissez le texte, puis choisissez vos places **au clavier** ou au lecteur d'écran. »<br>**Objectif sans blocage** · *si échec : voir `DESIGN.md` (cibles, focus)* | ☐ ___ s | ☐ ___ s | ☐ ___ s |

## C. Points à vérifier écran par écran
Encercler **OK** ou **Pb** pour chaque participant ; noter le problème (et la modification possible) dans « Notes ».
| Écran · critère | P1 | P2 | P3 | Notes / modification possible |
|---|:-:|:-:|:-:|---|
| **Accueil** · Comprend en 3 s ce qu'il peut faire (affiche, séances, bouton) | OK·Pb | OK·Pb | OK·Pb | |
| Voit les séances du jour sans défiler | OK·Pb | OK·Pb | OK·Pb | |
| Trouve les onglets Films / Nouveautés / Prochainement | OK·Pb | OK·Pb | OK·Pb | |
| **Recherche** · Les suggestions (film, acteur, cinéma) sont comprises | OK·Pb | OK·Pb | OK·Pb | |
| **Fiche film** · Trouve « Réserver » sans hésiter | OK·Pb | OK·Pb | OK·Pb | |
| Comprend la cloche « Suivre » à côté de Réserver | OK·Pb | OK·Pb | OK·Pb | |
| Bande-annonce (consentement, lancement) comprise et non gênante | OK·Pb | OK·Pb | OK·Pb | |
| **Séance** · Repère une séance **complète** ou **déjà réservée** (grisée) | OK·Pb | OK·Pb | OK·Pb | |
| Trouve les tarifs réduits repliés | OK·Pb | OK·Pb | OK·Pb | |
| La barre de progression (1/4…) aide | OK·Pb | OK·Pb | OK·Pb | |
| **Places** · Comprend que des places sont **déjà proposées** | OK·Pb | OK·Pb | OK·Pb | |
| Zoom sur la zone puis « Voir toute la salle » compris | OK·Pb | OK·Pb | OK·Pb | |
| Touche un siège **sans erreur** (cibles, une main) | OK·Pb | OK·Pb | OK·Pb | |
| Trouve les places fauteuil roulant (si besoin) | OK·Pb | OK·Pb | OK·Pb | |
| « Voir depuis ma place » compris, vidéo non gênante | OK·Pb | OK·Pb | OK·Pb | |
| **Commande** · Voit le **total TTC** et les frais avant de payer | OK·Pb | OK·Pb | OK·Pb | |
| Comprend « Commande avec obligation de paiement » | OK·Pb | OK·Pb | OK·Pb | |
| « Petite faim » trouvée **si voulue**, ignorée **sinon** | OK·Pb | OK·Pb | OK·Pb | |
| **Paiement refusé** · Comprend que rien n'est débité et sait quoi faire | OK·Pb | OK·Pb | OK·Pb | |
| **Billet** · Reconnaît le QR ; billet lisible hors ligne | OK·Pb | OK·Pb | OK·Pb | |
| **Compte** · Comprend carte, réservations, rappels, suivis | OK·Pb | OK·Pb | OK·Pb | |
| Annule une réservation avec confirmation | OK·Pb | OK·Pb | OK·Pb | |
| **Assistant** · Comprend que le chat est cliquable, reçoit une proposition utile | OK·Pb | OK·Pb | OK·Pb | |
| **Visuel** · Texte lisible en clair **et** en sombre | OK·Pb | OK·Pb | OK·Pb | |
| Logo, mascotte, boutons cohérents (rien d'anormal : cadre, flou, coupure) | OK·Pb | OK·Pb | OK·Pb | |
| **Mouvement** · Transitions utiles (pas de saut ni de scintillement) | OK·Pb | OK·Pb | OK·Pb | |
| **Accessibilité** · Texte 130 % sans coupure ; contraste élevé ; animations réduites respectées | OK·Pb | OK·Pb | OK·Pb | |
| **Grand écran** · *(si testé sur ordinateur)* mise en page aérée, rien de coupé | OK·Pb | OK·Pb | OK·Pb | |

## D. Débrief (poser tel quel, noter les mots du participant)
| Question | P1 | P2 | P3 |
|---|---|---|---|
| « Qu'attendiez-vous à cet endroit ? » (écran du blocage) | | | |
| « Qu'est-ce qui vous a arrêté ou surpris ? » | | | |
| « Qu'est-ce qui était le plus agréable ? » | | | |
| « Le texte et les couleurs étaient-ils faciles à lire ? » | | | |
| « Referiez-vous une réservation avec cette application ? » (oui / non / pourquoi) | | | |
| Facilité globale, de 1 (difficile) à 5 (très facile) | __ / 5 | __ / 5 | __ / 5 |

## E. Synthèse après les 3 tests (gravité × fréquence)
Gravité : **1** gêne légère · **2** ralentit · **3** bloque. Fréquence : nombre de participants (sur 3).
| # | Problème observé | Gravité (1-3) | Fréq. (/3) | Priorité (G × F) | Modification décidée | Fait ? | Avant → après (capture) |
|---|---|:-:|:-:|:-:|---|:-:|---|
| 1 | | | | | | ☐ | |
| 2 | | | | | | ☐ | |
| 3 | | | | | | ☐ | |
| 4 | | | | | | ☐ | |
| 5 | | | | | | ☐ | |

**Règle de décision** : corriger d'abord les priorités ≥ 6 (ex. : gravité 3 vue par 2 personnes) ; garder **au moins 2 corrections visibles** (avant/après) pour le barème « Test et version améliorée ».

## F. Verdict
| Objectif | Atteint ? (P1 / P2 / P3) |
|---|---|
| Réserver 2 places en **moins de 60 s**, sans aide | ☐ / ☐ / ☐ |
| Retrouver le billet hors ligne | ☐ / ☐ / ☐ |
| Aucun blocage de gravité 3 restant | ☐ |
