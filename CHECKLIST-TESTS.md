# U CINEMÀ — Checklist de test (3 participants)

> À imprimer (A4 paysage) ou à remplir à l'écran. **Ne jamais aider** le participant. Cocher ☑ (réussi) ou ☒ (problème) dans la colonne de chaque participant : **P1 · P2 · P3**.
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
Critère de réussite = **sans aide**. Noter le temps (secondes) et les hésitations.
| # | Consigne lue au participant | Réussi sans aide (P1 / P2 / P3) | Temps P1 / P2 / P3 | Objectif | Si échec → piste de modification |
|---|---|---|---|---|---|
| S1 | « Vous voulez voir un film **ce soir** avec un ami. Réservez **deux places**. » | ☐ / ☐ / ☐ | __ / __ / __ s | ≤ 60 s | Raccourcir : séances du jour plus visibles, bouton plus clair |
| S2 | « Votre ami est **étudiant** : retrouvez le tarif adapté. » | ☐ / ☐ / ☐ | __ / __ / __ s | ≤ 20 s | Afficher un tarif réduit par défaut |
| S3 | « Choisissez des places **au fond** de la salle. » (zones du plan) | ☐ / ☐ / ☐ | __ / __ / __ s | ≤ 15 s | Rendre les zones plus visibles, texte « Voir toute la salle » |
| S4 | « Regardez **la vue depuis votre place**. » | ☐ / ☐ / ☐ | __ / __ / __ s | ≤ 10 s | Déplacer ou renommer le bouton |
| S5 | « Ajoutez un **pop-corn** à votre commande. » | ☐ / ☐ / ☐ | __ / __ / __ s | ≤ 20 s | Montrer la petite faim plus tôt |
| S6 | « Au moment de payer, la carte est **refusée** : terminez quand même. » (carte de test •••• 0002) | ☐ / ☐ / ☐ | __ / __ / __ s | ≤ 30 s | Message plus clair, bouton « Changer de moyen » plus visible |
| S7 | « **Suivez** ce film pour être prévenu des nouveautés. » | ☐ / ☐ / ☐ | __ / __ / __ s | ≤ 10 s | Déplacer la cloche, changer le libellé |
| S8 | « Retrouvez votre **billet** sans connexion. » (mode avion) | ☐ / ☐ / ☐ | __ / __ / __ s | ≤ 20 s | Lien plus direct vers le billet |
| S9 | « **Annulez** cette réservation. » (Compte › Mes réservations) | ☐ / ☐ / ☐ | __ / __ / __ s | ≤ 30 s | Rendre l'annulation plus visible |
| S10 | *(accessibilité)* « Agrandissez le texte, puis choisissez vos places **au clavier** ou au lecteur d'écran. » | ☐ / ☐ / ☐ | __ / __ / __ s | sans blocage | Voir `DESIGN.md` (cibles, focus) |

## C. Points à vérifier écran par écran
Cocher **OK** si le critère est vrai pour le participant, **Pb** s'il y a un problème (noter lequel dans la colonne de droite).
| Écran | Critère à observer | P1 | P2 | P3 | Problème / citation | Modification possible |
|---|---|:-:|:-:|:-:|---|---|
| **Accueil** | Comprend en 3 s ce qu'il peut faire (affiche, séances, bouton) | OK / Pb | OK / Pb | OK / Pb | | |
| | Voit les séances du jour sans défiler | OK / Pb | OK / Pb | OK / Pb | | |
| | Trouve les onglets Films / Nouveautés / Prochainement | OK / Pb | OK / Pb | OK / Pb | | |
| **Recherche** | Les suggestions (film, acteur, cinéma) sont comprises | OK / Pb | OK / Pb | OK / Pb | | |
| **Fiche film** | Trouve « Réserver » sans hésiter | OK / Pb | OK / Pb | OK / Pb | | |
| | Comprend la cloche « Suivre » à côté de Réserver | OK / Pb | OK / Pb | OK / Pb | | |
| | La bande-annonce (consentement, lancement) est comprise et non gênante | OK / Pb | OK / Pb | OK / Pb | | |
| **Séance** | Repère une séance **complète** ou **déjà réservée** (grisée) | OK / Pb | OK / Pb | OK / Pb | | |
| | Trouve les tarifs réduits repliés | OK / Pb | OK / Pb | OK / Pb | | |
| | La barre de progression (1/4…) aide | OK / Pb | OK / Pb | OK / Pb | | |
| **Places** | Comprend que des places sont **déjà proposées** | OK / Pb | OK / Pb | OK / Pb | | |
| | Le zoom sur la zone puis « Voir toute la salle » sont compris | OK / Pb | OK / Pb | OK / Pb | | |
| | Touche un siège **sans erreur** (cibles, une main) | OK / Pb | OK / Pb | OK / Pb | | |
| | Trouve les places fauteuil roulant (si besoin) | OK / Pb | OK / Pb | OK / Pb | | |
| | « Voir depuis ma place » : compris, bande-annonce non gênante | OK / Pb | OK / Pb | OK / Pb | | |
| **Commande** | Voit le **total TTC** et les frais avant de payer | OK / Pb | OK / Pb | OK / Pb | | |
| | Comprend « Commande avec obligation de paiement » | OK / Pb | OK / Pb | OK / Pb | | |
| | La « petite faim » est trouvée **si voulue**, ignorée **sinon** | OK / Pb | OK / Pb | OK / Pb | | |
| **Paiement refusé** | Comprend que rien n'est débité et sait quoi faire | OK / Pb | OK / Pb | OK / Pb | | |
| **Billet** | Reconnaît le QR et le message de fin ; billet lisible hors ligne | OK / Pb | OK / Pb | OK / Pb | | |
| **Compte** | Comprend la carte, les réservations, l'activité récente | OK / Pb | OK / Pb | OK / Pb | | |
| | Annule une réservation avec confirmation | OK / Pb | OK / Pb | OK / Pb | | |
| **Assistant** | Comprend que le chat est cliquable, obtient une proposition utile | OK / Pb | OK / Pb | OK / Pb | | |
| **Visuel** | Texte lisible en clair **et** en sombre | OK / Pb | OK / Pb | OK / Pb | | |
| | Logo, mascotte, boutons : style cohérent (rien d'anormal : cadre, flou, coupure) | OK / Pb | OK / Pb | OK / Pb | | |
| **Mouvement** | Les transitions aident (pas de saut, pas de scintillement) | OK / Pb | OK / Pb | OK / Pb | | |
| **Accessibilité** | Texte 130 % sans coupure ; contraste élevé ; animations réduites respectées | OK / Pb | OK / Pb | OK / Pb | | |
| **Grand écran** *(si testé sur ordinateur)* | Mise en page aérée, rien de coupé à droite ni sous la barre du haut | OK / Pb | OK / Pb | OK / Pb | | |

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
