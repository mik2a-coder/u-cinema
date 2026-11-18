# U CINEMÀ — Parcours utilisateur

Parcours principal de Mika, du premier regard au billet. Chaque étape a un **seul but**, un retour visible et un plan B.

**Accueil → Fiche film → Séance → Places → Commande → Billet → Compte**

À chaque étape, un imprévu a son plan B (tableau « Imprévus prévus » plus bas) : séance complète ou annulée, paiement refusé, hors ligne, double réservation, recherche vide.

| Étape | Ce que Mika fait | Ce qu'elle voit | Émotion / risque | Écran |
|---|---|---|---|---|
| 1. Découvrir | Ouvre l'app | Affiche du film du moment, titre, **séances du jour**, un bouton « Toutes les séances » | Curiosité | `01-accueil` |
| 2. Comprendre | Touche l'affiche | Fiche : note, durée, séances rapides, réalisateur, synopsis replié, distribution ; bouton **Réserver** | Rapide | `02-fiche` |
| 3. Séance | Vérifie le jour, garde 2 places | Progression 1/4, dates, séances (complète grisée), tarifs réduits repliés | Confiance | `03-seance` |
| 4. Places | Les sièges sont déjà proposés ; la caméra zoome sur leur zone | Plan de **toute la salle** d'un coup (8 rangées), « Voir depuis ma place » (avec Changer de place / Acheter), **Acheter · 36 €** | Contrôle | `04-places` |
| 5. Payer | Ajoute une gourmandise (facultatif), coche les CGV, valide | Bannières de suggestions, total TTC, « Commande avec obligation de paiement · 38,40 € TTC » | Vigilance | `05-commande`, `06-petite-faim` |
| **Imprévu** | Carte refusée | « Paiement refusé par la banque. **Rien n'a été débité**, commande conservée » + [Changer de moyen] [Réessayer] | Inquiétude → soulagement | `07-paiement-refuse` |
| 6. Entrer | Montre son billet | QR, coche animée, « Profitez de la séance », disponible hors ligne | **Pic** et fin positifs | `08-billet` |
| 7. Revenir | Ouvre le compte | Carte d'abonné, réservations, rappels de sortie, suivis, films vus et notes | Appartenance | `09-compte` |

## Imprévus prévus
| Imprévu | Comportement |
|---|---|
| Séance **complète** | Créneau grisé « Complet » |
| Séance **annulée** | Barrée, « Annulée · voir 23:15 » |
| **Déjà réservé** / séance qui chevauche | Créneau grisé « Déjà réservé » ou « Autre séance prévue » ; refus au paiement avec explication |
| Paiement **refusé** | Message clair, commande conservée |
| **Hors ligne ou réseau instable** | Page « Plus de réseau » : chat triste, message rassurant, **mini-jeu** (le chat court, saute des objets de cinéma, glisse à l'arrivée), « Réessayer » (teste vraiment la connexion) et « Continuer hors ligne » ; billet toujours lisible. Au paiement sans réseau : « Connexion nécessaire », commande conservée. Voir la page : https://mik2a-coder.github.io/u-cinema/#x:0:off |
| **Recherche vide** | Suggestions de genres + « Effacer la recherche » |
| **Annulation** d'une réservation | Depuis « Mon billet » : confirmation, points rendus |

## Parcours secondaires
- **Choisir avec l'aide du chat** : « un film drôle ce soir en famille » → propositions tenant compte des séances et des goûts (notes).
- **Suivre un film** : cloche à côté de « Réserver » ; le film apparaît dans « Mes suivis » du compte (comme les acteurs et réalisateurs suivis).
- **Vue depuis ma place** : on « s'assoit » à la place choisie et la bande-annonce passe sur l'écran.
