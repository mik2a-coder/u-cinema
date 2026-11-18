# Direction artistique et palette

*Dossier de livraison : passation design et développement. Version du prototype : **v95** (18 novembre 2026).*

## 1. Synthèse de la direction artistique

**Client / projet** : U CINEMÀ, réseau de quatre cinémas corses (Aiacciu, Bastia, Corti, Portivechju). **Objectif** : permettre de choisir un film, une séance et ses places en moins d'une minute, sur téléphone comme sur grand écran, et de retrouver son billet sans réseau.

**Parti pris visuel : « la salle obscure, mais chaleureuse ».** Les affiches sont les héros ; l'interface reste en retrait, comme le noir d'une salle avant la projection. Le mode clair (par défaut) s'appuie sur un crème chaud et une encre presque noire ; le mode sombre inverse ces rôles. **Un seul signal lumineux, l'or**, guide l'œil : étape en cours, place choisie, note, dernier film consulté.

**Expérience utilisateur.** Une intention par écran (choisir, réserver, payer, présenter). Le mouvement aide sans décorer : l'affiche voyage de la liste à la fiche, la vue depuis la place plonge dans la salle, l'affiche de l'écran d'accueil change avec le texte. La mascotte **U Ghjattu-Volpe** (chat-renard à lunettes 3D) incarne la marque et sert d'assistant : « Miaou ! Donne-moi ton humeur, je te trouve le film idéal ! » Elle peut même préparer une réservation complète à partir d'une phrase.

**Ton.** Professionnel, clair, rassurant : prix toujours en euros TTC, dates humaines (« Aujourd'hui », « Demain »), règles dites avant d'être subies (annulation jusqu'à 2 h avant, avoir et non remboursement, 45 minutes entre deux films).

## 2. Palette de couleurs (règle 60-30-10)

La palette est déclinée en variables (`--bg`, `--surface`, `--text`, `--accent`…) : changer un mode ou un thème revient à redéfinir ces variables. Le thème suit par défaut les préférences de l'appareil (**mode Auto**, clair ou sombre).

| Rôle | Teinte | HEX | RGB | Usage dans l'interface |
|---|---|---|---|---|
| 60 % · Fond | **Crème** | `#FAF6EB` | 250, 246, 235 | Fond des écrans (mode clair, par défaut) et du site |
| 60 % · Fond | **Papier** | `#FDFBF6` | 253, 251, 246 | Cartes, créneaux, fenêtres modales |
| 60 % · Fond | **Sable** | `#F6EFDE` | 246, 239, 222 | Éléments posés sur une carte (puces, champs) |
| 30 % · Structure | **Encre** | `#16120A` | 22, 18, 10 | Texte principal, titres |
| 30 % · Structure | **Encre douce** | `#5F5642` | 95, 86, 66 | Texte secondaire, légendes (contraste 6,5 : 1) |
| 30 % · Structure | **Encre boutons** | `#1E1810` | 30, 24, 16 | Boutons principaux en mode clair (texte crème) |
| 30 % · Structure | **Crème bouton** | `#F4E4B6` | 244, 228, 182 | Texte des boutons principaux |
| 10 % · Signal | **Or lumière** | `#F0C05A` | 240, 192, 90 | Seul accent : étapes, sélection, étoiles, anneau du dernier film |
| 10 % · Signal | **Or profond** | `#B98322` | 185, 131, 34 | Fin du dégradé, interrupteurs activés |
| 10 % · Signal | **Or texte** | `#87611B` | 135, 97, 27 | Or utilisé comme texte sur fond clair (contraste 5,1 : 1) |
| 10 % · Signal | **Or du logo** | `#B06F06` | 176, 111, 6 | La lettre U du logo |
| Salle sombre | **Noir salle** | `#0B0A08` | 11, 10, 8 | Fond du mode sombre |
| Salle sombre | **Charbon** | `#181510` | 24, 21, 16 | Cartes du mode sombre |
| Salle sombre | **Velours** | `#1D0709` | 29, 7, 9 | Vue depuis la place : mur et fauteuils (dégradé vers #0B0305) |

**Lecture 60-30-10.** 60 % de surfaces douces (crème, papier, sable), 30 % d'encre (textes, boutons principaux), 10 % d'or (le seul signal). Contrastes mesurés : texte principal 17 : 1, texte secondaire ≥ 6,5 : 1, or sur fond clair ≥ 5,1 : 1, soit au-delà de 4,5 : 1 (AA).

## 3. Architecture des pages

Le prototype est codé (HTML), il n'existe donc pas de maquette Figma : chaque écran est un **lien direct vers le prototype en ligne**.

| Écran | Objectif clé | Lien |
|---|---|---|
| Introduction (3 étapes) | Présenter le service, images qui changent avec le texte | [Ouvrir](https://mik2a-coder.github.io/u-cinema/) |
| Accueil | Trouver un film : carrousel, liste, recherche, assistant | [#home](https://mik2a-coder.github.io/u-cinema/#home) |
| Rubrique enfants | Proposer des dessins animés (8 titres) dans un onglet dédié | [Accueil > Enfants](https://mik2a-coder.github.io/u-cinema/#home:0:tab=3) |
| Fiche film | Convaincre : extrait vidéo, note, séances du jour, distribution | [#detail](https://mik2a-coder.github.io/u-cinema/#detail:0) |
| Fiche personne | Découvrir un acteur, un réalisateur ou un compositeur : biographie, filmographie, suivre | Depuis la distribution d'une fiche film |
| Séance | Choisir cinéma, jour, heure, tarifs | [#book](https://mik2a-coder.github.io/u-cinema/#book:0) |
| Places | Choisir ses sièges, voir la vue depuis la place | [#seats](https://mik2a-coder.github.io/u-cinema/#seats:0) |
| Commande | Contrôler, ajouter une friandise, utiliser avoir et récompenses, payer | [#order](https://mik2a-coder.github.io/u-cinema/#order:0) |
| Page « Plus de réseau » (erreur) | Rassurer, laisser patienter avec le mini-jeu du chat, proposer « Réessayer » ou « Continuer hors ligne » | [Voir la page d'erreur](https://mik2a-coder.github.io/u-cinema/#x:0:off) |
| Billet | Présenter son QR code, même hors ligne | [#ticket](https://mik2a-coder.github.io/u-cinema/#ticket:0) |
| Compte | Réservations, rappels, suivis, films vus, points, avoir, récompenses | [#account](https://mik2a-coder.github.io/u-cinema/#account) |

## 4. Typographie et accessibilité

| Usage | Police | Détail |
|---|---|---|
| Titres | **Bebas Neue** | Capitales condensées « affiche de cinéma », tailles de 32 à 58 px |
| Textes courants | **Inter** | 16 px minimum, interligne 1,5, échelle réglable (100 / 115 / 130 %) |
| Option « Police lisible » | **Atkinson Hyperlegible** | Pensée pour la basse vision et la dyslexie |

Règles d'accessibilité : cibles tactiles ≥ 44 px ; focus visible (contour or) ; plan de salle utilisable au clavier ; annonces pour lecteurs d'écran ; **contraste élevé** ; **animations réductibles** (aucun mouvement imposé) ; vibrations désactivables ; extraits vidéo soumis à consentement ; mentions légales accessibles depuis le pied de page de chaque écran. Aucun défaut de débordement ou de chevauchement sur 6 largeurs testées (360 à 1440 px).

## 5. Prochaines étapes de validation et de passation

1. **Test avec 3 personnes** (grille `CHECKLIST-TESTS.md`) : à réaliser avec de vraies personnes, puis reporter les résultats dans `TESTS.md`. Aucun résultat n'a été inventé.
2. **Vérifier dans Safari** (Mac et iPhone) la vue depuis la place, l'en-tête et le fond de l'accueil : cela n'a pu être testé qu'avec Chrome.
3. **Extraits verticaux** : fournir les liens officiels des Shorts des 15 autres films (3 films en disposent déjà).
4. **Biographies** : relire les résumés (sources publiques) avant diffusion ; 15 noms n'ont qu'un rôle et une filmographie.
5. **Passation technique** : un seul fichier `index.html`, un `sw.js` (cache `cinelux2-vNN`), un manifeste ; `tools/` regroupe les scénarios de test et la fabrication des documents. La **page d'erreur réseau** (mascotte triste, mini-jeu, objets de cinéma) suit la même palette. Une version « autonome » (`CINELUX-autonome.html`) fonctionne sans réseau.
