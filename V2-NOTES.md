# U CINEMÀ V2 — Notes de conception

Ce que le cours *Prototyper en 2026* a changé dans le prototype, écran par écran, avec la fonction du code correspondante.
La V1 reste intacte dans `../CINELUX`. Ouvrir la V2 : `Ouvrir CINELUX V2.command`.

## 1. Grille « Peaufiner » (diapositive 92) — contrôle du 16 novembre 2026

> Auto-évaluation vérifiée sur la version actuelle (écrans téléphone, tablette, bureau ; modes sombre et clair), à confirmer par les tests utilisateurs (`TESTS.md`).

| Famille | Critère | État | Preuve dans l'app |
|---|---|---|---|
| **Geste** | Le mouvement aide | ✅ | Transitions de page directionnelles (View Transitions), affiche qui voyage vers la fiche, vue de place « plongée » ; transitions séquentielles (l'ancien écran s'efface, le nouveau arrive) ; plus aucune animation décorative en boucle (le chat ne bouge qu'à votre geste : regard, clignement à l'ouverture, bulle une seule fois par visite) ; tout coupé avec « Réduire les animations » |
| | Le toucher se sent | ✅ | `haptic()` : tic, succès, erreur ; onde au toucher sur les boutons |
| | Gestes naturels | ✅ | Carrousel qui suit le doigt, feuille glissable, carte de fidélité qui s'incline, regard de U Ghjattu-Volpe qui suit la souris |
| | L'objet se transforme | ✅ | Menu duo → « Ajouté », carte de fidélité qui se retourne, billet → vue de place |
| **Aspect** | Illustrations à vous | ✅ | Logo (billet + U), mascotte **U Ghjattu-Volpe** (chat-renard illustré, yeux animés par l’app) ; les affiches et photos sont celles des films et des produits |
| | Icônes assorties au texte | ✅ | Icônes au trait de 2 px, bouts ronds |
| | Peu de couleurs | 🟡 | Un seul signal (or) ; en mode clair le fond prend une teinte douce de l'affiche (volontaire) |
| | Beau et simple | ✅ | Échelle 1,125, rayons imbriqués, grille de 4 pt, boutons principaux en encre foncée (clair) ou or (sombre), secondaires en verre |
| **Parcours** | Progression visible | ✅ | `.stp` 4 étapes |
| | Retour après chaque action | ✅ | Toasts avec Annuler (rappel, note, snack, duo) |
| | Un écran, un but | ✅ | Accueil : choisir un film ; un seul bouton principal (« Toutes les séances ») |
| **États** | Chargement et erreur prévus | ✅ | Squelettes d'affiches, hors ligne, séance annulée, paiement refusé, recherche vide, U Ghjattu-Volpe qui explique quand rien ne correspond |
| | Ce qui reste à faire | ✅ | « Encore 1 place à choisir », jauge « bonbons offerts » |
| | Erreur réparable | ✅ | `showPayErr()` : commande conservée |
| | Réponse rapide | ✅ | Tout est local (< 400 ms) |
| **Densité** | Densité adaptée | ✅ | Audit automatique le 17 novembre 2026 : 6 tailles (360, 390, 430, 768, 1024, 1440 px) × 6 écrans (accueil, fiche, réservation, places, commande avec snacks, compte) → aucun débordement |
| | L'espace groupe | ✅ | Séances groupées sous le titre, snacks par onglets |
| | L'image d'abord | ✅ | Affiches entières (plus de voile), photos de produits |
| | Compris en 3 secondes | ✅ | Affiche, titre, séances du jour, un bouton |
| **Esprit** | Peu de choix | ✅ | 3 onglets, 4 séances en puces, snacks repliés par défaut |
| | L'important au début et à la fin | ✅ | Progression en haut, action en bas |
| | Un motif connu | ✅ | Onglets, feuilles, steppers, puces, assistant de chat |

**Score : 21 sur 22** (🟡 « Peu de couleurs » : le mode clair teinte le fond avec l'affiche, choix assumé de l'auteur).

### U Ghjattu-Volpe, l'assistant
Mascotte cliquable (un chat-renard, « ghjattu-volpe » en corse : le symbole de la classe, orthographe à faire valider) sur l'accueil. Ses yeux suivent la souris sur bureau ; clignement, humeurs (réfléchit, content, déçu). Elle comprend des demandes en français (« un film drôle ce soir en famille », « avec Brad Pitt », « court, avant 21 h », « surprends-moi », « bientôt en salle ») ou des suggestions à toucher, croise les genres, les acteurs, la durée, les horaires réellement libres et les goûts du compte (notes ≥ 4 favorisées, films déjà vus écartés), et propose trois films avec des puces de séance qui ouvrent directement la réservation. Critères affichés et retirables. Tout est calculé sur l'appareil, rien n'est envoyé.

## 2. Lois de l'usage appliquées

| Loi | Application |
|---|---|
| **Charge cognitive / Hick** | Tarifs réduits repliés ; séances rapides limitées à 4 ; sièges suggérés d'office |
| **Pareto / Occam** | Accueil : 4 éléments portent le sens (affiche, titre, prochaine séance, CTA) |
| **Miller / position sérielle** | Barre de navigation à 4 entrées ; progression 4 étapes |
| **Gestalt** | Proximité, similarité, continuité (carrousel), clôture (carte coupée au bord), région commune |
| **Zeigarnik** | « Encore 1 emplacement fauteuil roulant à choisir » : ce qui reste est dit |
| **Goal-gradient** | Le segment courant de la progression est déjà à 55 % ; jauge « bonbons offerts » |
| **Fitts** | Action principale en bas, sièges jusqu'à 44 px, cibles ≥ 44 px |
| **Postel** | Recherche tolérante (titre ou genre, partiel, sans accent exigé) ; suggestions si rien trouvé |
| **Doherty** | Réponses locales instantanées ; attente simulée de paiement signalée par un indicateur |
| **Jakob** | Motifs connus (feuilles, onglets, steppers, plan de salle à légende) |
| **Peak-end** | Le billet est le sommet : coche animée, vibration de succès, « Bonne séance ! » |
| **Esthétique-utilisabilité** | Soin visuel cohérent (variables) pour acheter de la patience |
| **Fogg** | Facilité d'abord : présélection des places, séances en un tap, paiement en un geste |
| **Nudge, pas dark pattern** | Voir §3 |

## 3. Contrôle « dark patterns » (DSA article 25)

| Pratique | U CINEMÀ |
|---|---|
| Fausse urgence / compte à rebours | ❌ Absente. « Plus que 8 places » ne s'affiche que si c'est une donnée de la séance |
| Case précochée | ❌ Absente : la case des conditions de vente est décochée |
| Refus culpabilisant | ❌ Absent : « Je refuse » et « Fermer » sont neutres |
| Frais cachés | ❌ Absents : frais de service et TTC affichés avant le paiement |
| Résiliation labyrinthique | ❌ Sans objet (pas d'abonnement) ; retrait du consentement en un geste |
| Relances sans fin | ❌ Aucune notification |
| Test : « ferait-on le même choix en comprenant tout l'écran ? » | ✅ Oui |

## 4. Responsive

| Largeur | Disposition |
|---|---|
| ≤ 599 px | Téléphone plein écran |
| 600–1023 px | Tablette : barre du haut, grille 3 colonnes, fiche 2 colonnes |
| ≥ 1024 px | Bureau : carrousel agrandi, grille auto, plan de salle centré |

Contrôle automatique des boutons coupés ou inatteignables et des débordements : 8 tailles (360 × 640 à 1440 × 900) × 2 échelles de texte (100 % et 130 %) → **aucun défaut** à la dernière exécution.

## 5. Limites connues
- Affiches, photos et scènes : droits des ayants droit, usage de démonstration seulement.
- Vibrations : Android (l'API n'existe pas sur iPhone).
- Pas d'audit RGAA ; déclaration d'accessibilité « non évaluée » (voir `CONFORMITE.md`).
- Les tests utilisateurs (3 personnes) restent à mener : `TESTS.md`.

## 6. Catalogue et nouvelles fonctions (novembre 2026)
**Catalogue** : 18 films de 2026 (`FILMS`) : 12 à l'affiche, 6 à venir. Distributions, équipes et résumés d'après Wikipédia ; dates de sortie France **indicatives** ; notes du public = démonstration. Onglets : **Films** (à l'affiche), **Nouveautés** (sorties des 4 derniers mois), **Prochainement** (« Me prévenir à la sortie » à la place de « Réserver », rappel gardé sur l'appareil).
**Affiche** : plus de pastilles en bas ; la note est dans une pastille dorée à côté de l'année et du genre, sous le titre.
**Fiche** : cartes de distribution sous le synopsis (photo, nom, nombre de films), fiche acteur en feuille, équipe (réalisation, production, musique).
**Extrait de bande-annonce** : 3,5 s après l'affiche, la vidéo (YouTube sans cookie, muette, en boucle) apparaît en fondu dans l'affiche ; bouton de son ; « Bande-annonce » ouvre la vidéo complète. **Consentement avant tout chargement** (feuille « Extraits de bandes-annonces », oui/non d'égale importance) ; réglable dans *Affichage et accessibilité* ; coupé avec « Réduire les animations » ou économie de données. Nécessite un serveur http (`Ouvrir CINELUX V2.command` en lance un sur localhost:8731) : YouTube refuse les pages ouvertes en `file://`.
**Vue depuis ma place** : sur le plan de salle, « Voir depuis ma place » plonge dans le siège choisi (zoom, cercle qui s'ouvre) et montre l'écran en perspective selon le rang et la colonne, les spectateurs devant, parallaxe au pointeur, flèches pour passer d'une place à l'autre. Simulation indicative.
**Billet** : l'affiche entière en vedette sur fond flou, « 2 places » au lieu de « ADMET DEUX ».
**Compte** (onglet « Compte ») : carte de fidélité (niveaux Bronze à Platine, points = 1 par euro, se retourne pour montrer le code), réservations à venir, rappels de sortie, historique des films vus avec notes en étoiles (annulables), préférences. Tout est en `localStorage` (`cinelux-acc`) ; inclus dans l'export et effacé avec « Tout effacer ». Historique et notes de départ : démonstration.
**Boutons** : reflet qui suit le pointeur, onde au toucher, relief, retour en ressort ; désactivés en « Réduire les animations ».
**Mode clair** : on garde la transparence colorée de l'affiche en arrière-plan et sur les boutons (verre dépoli).

## Cinémas (démonstration)
Les 4 cinémas sont **fictifs** et situés en Corse : U Cinemà Aiacciu (Ajaccio), Bastia, Corti (Corte), Portivechju (Porto-Vecchio). Adresses et distances inventées pour la maquette.


## 7. Évolutions du 18 novembre 2026
- **Plan de salle en zones** (Avant, Centre, Fond) avec zoom de caméra ; vue depuis la place avec « Changer de place / Acheter ».
- **Compte** : réservations, rappels de sortie, suivis (films, acteurs, réalisateurs), films vus ; annulation d'une réservation.
- **Accueil** : fond en ovale doux qui déborde de l'écran (55 % en clair, 90 % en sombre), barre du haut transparente en haut de page, logo en haut à gauche sur téléphone.
- **Fiche film** : « Suivre ce film » à côté de « Réserver » ; portraits des réalisateurs ; vidéo verticale pour 3 films.
- **Dossier de rendu** : `BAREME.md`, `PARCOURS.md`, `JOURNAL.md`, `CHECKLIST-TESTS.md`, `RENDU-U-CINEMA.pdf`.
