# U CINEMÀ V2 — Design System

Application de réservation de places de cinéma (PWA), pour mobile **et** grands écrans. Ambiance « salle obscure » : fonds sombres chauds, un seul signal lumineux, titres condensés façon affiche.
Thème par défaut : **Noir & Or** (quatre autres palettes interchangeables) ; **version claire** déduite de la palette. Marque : **U CINEMÀ**, logo « chat aux lunettes 3D » et mascotte *U Ghjattu-Volpe*.
Prototype en ligne : https://mik2a-coder.github.io/u-cinema/
Cette version 2 applique le cours *Prototyper en 2026* (voir `V2-NOTES.md` pour la correspondance idée → écran).

---

## 1. Principes

| Principe | Ce que ça veut dire dans U CINEMÀ |
|---|---|
| **Le premium se sent** | Le soin vient des décisions : dates humaines (« Aujourd'hui », « Demain »), prix en euros TTC, libellés précis (« Commande avec obligation de paiement »). |
| **Salle obscure, affiche d'abord** | Les visuels de films sont les héros ; l'interface reste en retrait (verre dépoli, dégradés sobres). |
| **Une intention par écran** | Une action principale visible (accueil : « Voir les séances » ; fiche : « Réserver » ; places : « Acheter » ; commande : le bouton légal). |
| **Un seul signal** | L'or est la seule couleur d'accent. L'emplacement PMR n'introduit pas de 2ᵉ teinte : contour crème pointillé + pictogramme. |
| **Le mouvement aide, il ne décore pas** | Il répond (appui), guide (carrousel qui suit le doigt) ou pousse (un seul « coup de coude » sur *Réserver* après 2,5 s sans action). Plus d'animation infinie. |
| **Échouer avec grâce** | Paiement refusé : la commande est conservée, on dit ce qui s'est passé et on propose la suite. Hors ligne : bandeau rassurant. |
| **Accessible dès le départ** | Cibles ≥ 44 px (sièges : jusqu'à 44 px de large), focus visible, plan de salle au clavier, échelle de texte, contraste élevé, vibrations désactivables, animations réduites. |

---

## 2. Tokens

### Couleurs (Noir & Or)
| Token | Valeur | Rôle |
|---|---|---|
| `--bg` | `#0B0A08` | Fond |
| `--bg2` | `#241C0C` | Halo en haut d'écran |
| `--surface` / `--surface2` | `#181510` / `#27231B` | Cartes, créneaux / éléments sur carte |
| `--text` / `--muted` | `#F8F3E8` / `#B3AA98` | Texte principal / secondaire |
| `--accent` / `--accent2` | `#F0C05A` / `#B98322` | Signal (dégradé `--grad`) |
| `--accent-text` | `#F0C05A` | Accent utilisé comme texte |
| `--on-accent` | `#1A1204` | Texte sur accent |
| `--paper` / `--ink` / `--ink-muted` | `#F3EAD3` / `#16120A` / `#5F5642` | Billet (seul élément clair) |
| `--line` | `rgba(255,255,255,.12)` | Bordures fines |

Autres palettes (Rouge cinéma, Violet néon, Bleu nuit, Émeraude) : mêmes 15 clés, voir `PALETTES` dans `index.html`.

### Contrastes mesurés (WCAG 2.2, seuil 4,5 : 1 pour le texte)
| Paire | Noir & Or | Pire cas des 5 palettes |
|---|---|---|
| Texte / fond | 17,9 | 17,9 |
| Texte secondaire / fond | 8,6 | 8,6 |
| Texte secondaire / surface | 7,9 | 7,9 |
| Texte secondaire / surface 2 | 6,8 | 6,6 |
| Accent en texte / fond | 11,7 | 7,8 |
| Texte sur bouton (début / fin du dégradé) | 10,9 / 5,6 | 4,6 / 5,6 |
| Texte du billet | 15,6 | 15,5 |
| Texte secondaire du billet | 6,0 | 5,8 |

Toutes les paires dépassent 4,5 : 1 (minimum mesuré : 4,6 avec la palette Rouge cinéma).

### Mode clair (Réglages › Affichage et accessibilité › Apparence : Sombre · Clair · Auto)
Le mode **Auto** suit l'appareil (clair ou sombre) ; la palette par défaut est Noir & Or. Le mode clair n'est pas une 6ᵉ palette : il se **déduit de la palette active**, donc les 5 thèmes ont leur version claire.
| Jeton | Règle |
|---|---|
| `--bg` / `--surface` / `--surface2` | le « papier » de la palette éclairci à 55 % / 80 % / 25 % (ivoire chaud pour Noir & Or) |
| `--bg2` | papier teinté d'accent à 14 % (halo en haut d'écran) |
| `--text` / `--muted` | `--ink` de la palette / `--ink-muted` assombri jusqu'à 4,9 : 1 |
| `--accent` / `--accent2` | **inchangés** : l'or reste le signal dans les deux modes (les boutons principaux, eux, passent en encre foncée en clair : voir § 7) |
| `--accent-text` | `--accent2` assombri jusqu'à 4,9 : 1 sur le fond (bronze ≈ `#8A5A00` pour Noir & Or) |
| `--paper` | blanc : le billet reste l'élément le plus clair, cerné d'un filet |
| `--line`, `--wr` | filets et voiles en brun foncé (`60,44,16`) au lieu de blanc |
Règles : les zones qui posent du texte **sur une image** (affiches du carrousel, haut de fiche, scène de la salle, photo du billet) restent des « îlots » sombres ; sièges libres en sable avec bord et ombre ; emplacement fauteuil = contour **encre** pointillé (crème en sombre) ; « Contraste élevé » devient noir sur blanc ; `color-scheme: light` et `theme-color` suivent le mode. Contrastes mesurés : texte 17 : 1, secondaire ≥ 6,5 : 1, texte d'accent ≥ 5,1 : 1 sur les 5 palettes.

### Typographie — échelle modulaire (base 16 px, ratio 1,125)
Chaque niveau découle du précédent ; toutes les tailles sont multipliées par `--ts` (échelle de texte de l'utilisateur : 1 / 1,15 / 1,3).
| Token | Valeur | Usage |
|---|---|---|
| `--fs-micro` | 11,24 | Badges, numéros de sièges |
| `--fs-xs` | 12,64 | Légendes, étiquettes, chips |
| `--fs-sm` | 14,22 | Texte courant dense, boutons secondaires |
| `--fs-md` | **16** | Corps |
| `--fs-lg` | 18 | Prix, titres de carte |
| `--fs-xl` / `--fs-2xl` | 20,25 / 22,78 | Titres de section |
| `--fs-3xl` / `--fs-4xl` | 25,63 / 28,83 | Titre d'écran (Bebas) |
| `--fs-5xl` … `--fs-14xl` | 32,44 … 93,7 | Titres film, héros |

Polices : **Bebas Neue** (titres, MAJUSCULES, `line-height .95`), **Inter** (texte), **Atkinson Hyperlegible** (option lisibilité).

### Rayons (imbriqués)
`--r-xs 8` siège · `--r-sm 12` · `--r-md 16` vignette, créneau · `--r-lg 24` carte · `--r-xl 32` feuille, panneau · `--r-pill 99` pilule · `50 %` bouton rond.

### Espacements (grille de 4 pt)
`--sp-1 4` · `--sp-2 8` · `--sp-3 12` · `--sp-4 16` · `--sp-5 20` · `--sp-6 24` · `--sp-8 32` · `--sp-10 40` · `--sp-12 48` · `--sp-16 64`. Tous les `padding` / `margin` / `gap` de la feuille de style sont alignés sur cette grille (valeurs ≥ 8 px).

### Points de rupture (grille 4 / 8 / 12 colonnes)
| Largeur | Mise en page |
|---|---|
| ≤ 599 px | **Téléphone** plein écran, barre de navigation flottante qui se rétracte au défilement |
| 600 – 1023 px | **Tablette** : barre du haut (icônes seules < 760 px), grille d'affiches 3 colonnes, fiche en 2 colonnes, parcours centré |
| ≥ 1024 px | **Bureau** : carrousel agrandi, grille d'affiches auto (≥ 4 colonnes), fiche 2 colonnes, plan de salle centré |

### Autres variables
`--ts` échelle de texte · `--top` / `--bot` marges de sécurité (encoche, barre d'accueil) · `--sw` largeur d'un siège (`clamp(34px, (100vw − 76px) / 8, 44px)`) · `--glow` lueur du bouton principal.

---

## 3. Composants

| Composant | Classe | Spécification |
|---|---|---|
| **Bouton primaire** | `.btn` | Pilule h 56 ; **sombre : `--grad` or, texte `--on-accent`, lueur `--glow`** ; **clair : encre `#1E1810`, texte crème `#F4E4B6`** (§ 7). `:active` scale .95, `:disabled` désaturé |
| **Bouton secondaire (verre)** | `.btn.alt`, `.vfs`, `.pill`, `.qchip`, `.hslot`, `.fchip` | Verre dépoli : blanc 72 % + flou + filet fin (clair) ou blanc 10 % (sombre) ; texte encre / crème |
| **Bouton Réserver** | `.cta.gold` | Même règle que le primaire ; l'onde au toucher est contenue dans le bouton |
| **Suivre (réalisateur / film)** | `.follow`, `.ff2` | Repos : verre. **Suivi : plein** (encre en clair, or en sombre) + coche ou cloche pleine + animation de cloche ; le film se suit à côté de « Réserver » |
| **Acheter (partagé)** | `.split` | Pilule dégradée « Acheter · séparateur · prix · pastille flèche » ; grisé tant que le choix n'est pas complet |
| **Hero d'accueil** | `.ftitle` + `.hero-cta` | Année · genre · durée, titre, le jour et 4 horaires en pastilles, **une** action « Toutes les séances » |
| **Progression du parcours** | `.stp` | 4 segments (Séance · Places · Paiement · Billet), segment courant déjà à 55 % (on part avec de l'avance), `role="progressbar"` |
| **Séances rapides** | `.qchip` | Pastilles d'horaires sur la fiche film : un tap → réservation avec ce créneau |
| **Tarifs** | `.trow` + `.redtog` | Plein tarif visible ; « J'ai droit à un tarif réduit » déplie les 4 autres |
| **Siège** | `.seat` | Zone tactile `--sw` × 40 (jusqu'à 44 px) ; libre gris ; occupé hachuré ; choisi = or ; PMR = contour crème pointillé + pictogramme (choisi : or + pastille ✓) ; focus visible ; flèches du clavier |
| **Menu duo** | `.upsell` | Même carte : « Ajouter » → « Ajouté ✓ · Retirer » (transformation, pas de remplacement) |
| **Toast** | `.toast` | Message + action **Annuler** (5,5 s) : ce qui s'est passé, ce que je peux annuler |
| **Erreur de paiement** | `.payerr` | Encadré rouge doux : cause, « rien n'a été débité », commande conservée, [Changer de moyen] [Réessayer] |
| **Hors ligne** | `.net` | Bandeau pilule « Connexion instable · le chargement peut être lent » / « De retour en ligne » (le détail est dans la page « Plus de réseau ») |
| **Squelette d'affiche** | `.poster` | Reflet animé tant que l'image charge, fondu à l'arrivée (désactivé en animations réduites) |
| **Modale** | `.sheet` + `.sheet-back` | Fenêtre **centrée** (largeur max 560 px, rayon `--r-xl`), bouton fermer en haut à droite, Échap ou clic sur le voile pour fermer ; **voile adapté au thème** : sombre `rgba(6,4,2,.80)`, clair `rgba(32,22,8,.62)`, contraste élevé `.90` ; apparition en fondu + légère mise à l'échelle ; sans animation en mode « Réduire les animations » ; utilisée sur tout le site (billet, accessibilité, consentement vidéo, mentions légales, choix de cinéma…) |
| **Barre haute (bureau)** | `#dtop` | Verre progressif : opaque à hauteur du logo et du menu, flou et teinte qui s'estompent sur ~40 px ; pas de ligne ; le contenu démarre sous la barre |
| **Logo** | `.lg-mark` + `.lg-word` | Pastille du chat (image à fond transparent, sans filtre) + « **U** CINEMÀ » : U ambre, mot en encre, lettres espacées ; proportions du dessin d'origine (§ 6) |
| **Bannière de petite faim** | `.bn` | Photo, accroche, bouton « Commander · prix » ; carrousel à défilement doux ; repliée par défaut |
| **Carte de fidélité** | `.lcard` | Carte or qui s'incline et se retourne (QR au dos), niveau, points, progression |
| **Mes suivis** | `.acc-row .acc-open` | Films, acteurs et réalisateurs suivis, avec photo ; « Ne plus suivre » à droite ; ordre de la page Compte : réservations · rappels de sortie · suivis · films vus |
| **Assistant** | `.muv-*` | Chat-renard cliquable, yeux qui suivent la souris, panneau de conversation local (rien n'est envoyé) |
| **Chip / Pill / Stepper / Onglets / Nav / Ticket / QR** | — | Inchangés (voir V1) ; nav flottante en verre, se rétracte au défilement |

---

## 4. Patterns

- **Parcours** : Intro → Accueil → Fiche → Séance (jour/heure/tarifs) → Places → Commande → Billet, avec progression 1/4 → 4/4.
- **États du système** : chargement (squelette), vide (recherche : suggestions de genres + « Effacer »), erreur (paiement refusé), hors ligne, **séance annulée** (grisée, « voir 23:15 »), **séance terminée / complète** (désactivée avec raison).
- **Retour d'information** : après chaque action légère, un toast dit ce qui s'est passé et propose **Annuler** ; la suite est visible dans l'écran (total, « Encore 1 place à choisir »).
- **Haptique** (Android) : tic léger à chaque choix, séquence courte pour le succès, double impulsion pour l'erreur ; réglable dans Accessibilité.
- **Mouvement** : transitions 0,15–0,5 s, courbe `cubic-bezier(.2,.8,.2,1)` ; le carrousel suit le doigt ; la barre de navigation se rétracte en descendant ; tout est neutralisé avec `prefers-reduced-motion` ou le réglage « Réduire les animations ».
- **Nudge sans dark pattern** : pas de fausse urgence, pas de case précochée, refus aussi simple que l'acceptation, prix TTC complet avant paiement, case CGV non cochée par défaut. La jauge « bonbons offerts » est factuelle (seuil de 10 €).
- **Accessibilité** : voir `CONFORMITE.md` (RGPD, consommation, directive d'accessibilité) et les 4 tests du cours : daltonisme (états jamais portés par la couleur seule : icône, hachures, texte), zoom (échelle 130 % sans coupure), sans souris (Tab + flèches), animations réduites.

---

## 5. De la V1 à la V2

| V1 | V2 | Idée du cours |
|---|---|---|
| Dates figées | « Aujourd'hui », « Demain », séances passées désactivées | Par défaut ou décidé |
| Accueil sans action explicite | Hero + prochaine séance + un seul CTA | Anatomie d'un hero header |
| Parcours sans repère | Progression en 4 étapes | Goal-gradient, progression visible |
| 5 tarifs visibles | Plein tarif + « tarif réduit » replié | Loi de Hick |
| Sièges 38 px | Jusqu'à 44 px + clavier + 1 arrêt de tabulation | Loi de Fitts, test « sans souris » |
| Bleu PMR | Crème pointillé (un seul signal) | Moins de couleurs, plus de nuances |
| Animation dorée infinie | Statique + coup de coude unique | Bouger seulement là où ça aide |
| Toasts simples | Toasts avec Annuler, vibrations | Trois réponses, faire sentir le toucher |
| Carrousel par saut | Suit le doigt | L'animation suit le doigt |
| Menu duo qui disparaît | Se transforme en « Ajouté » | Transformer plutôt que remplacer |
| Billet sobre | Coche animée, mot de fin | Règle peak-end |
| Pas d'états d'erreur | Paiement refusé, séance annulée, hors ligne, recherche vide, squelettes | États du système, échouer avec grâce |
| Fiche texte d'abord | Image, séances rapides, synopsis replié | L'image avant le paragraphe |
| Tailles/rayons/espaces libres | Échelle 1,125, rayons imbriqués, grille de 4 | Échelle typographique, design system |
| Téléphone ou « petit iPhone » | Téléphone / tablette / bureau pensés | Grille responsive 4-8-12 |


---

## 6. Logo et mascotte
- **Logo** : pastille ronde du chat aux lunettes 3D (dessin de l'auteur) + mot-symbole « U CINEMÀ ». Proportions du fichier d'origine, exprimées par rapport à la pastille (`--lm`) : U à 3 % de la pastille, grand blanc, lettres espacées de .3 em ; taille de police = 52 % de la pastille.
- **Couleurs** : « CINEMÀ » `--text` ; « U » ambre soutenu en clair (`#B06F06`), or en sombre.
- **Règle des images** : aucune ombre portée ni filtre CSS sur une image à fond transparent (sinon un cadre apparaît sous Safari).
- **Mascotte** *U Ghjattu-Volpe* : image du chat à fond transparent, yeux animés par l'app ; ne bouge qu'à l'action de l'utilisateur (regard, clignement à l'ouverture) ; aucune animation en boucle.

## 7. Boutons — règles (clair / sombre)
| Rôle | Sombre | Clair |
|---|---|---|
| Primaire (`.btn`, `.split`, `.cta.gold`, « + » des quantités) | Or `--grad`, texte `--on-accent` | **Encre `#1E1810`**, texte crème `#F4E4B6`, ombre douce, sans bordure ni dégradé ; survol `#2C2316` |
| Secondaire (verre) | Blanc 10 %, filet blanc | Blanc 72 %, flou, filet brun 16 %, texte encre |
| Suivi / sélectionné | Or plein | Encre pleine |
| Désactivé | Désaturé, 62 % | idem |
| Sur image | Verre sombre | Verre sombre (îlot) |
Règle d'or : **un seul bouton principal par écran**, les autres en verre.

## 8. Mouvement — règles
- Transitions d'écran **séquentielles** : l'ancien écran s'efface en 160 ms, le nouveau arrive en 340 ms (jamais deux écrans visibles ensemble) ; la transition d'affiche (accueil ↔ fiche) n'est utilisée que sur grand écran.
- Pas de boucle décorative. Les seules animations continues sont fonctionnelles : cercle de chargement, reflet des affiches qui chargent.
- Tout est neutralisé par « Réduire les animations » ou `prefers-reduced-motion`.

## 9. Variables CSS ↔ ce document (réponse « Variables et composants »)
| Famille | Variables | Où |
|---|---|---|
| Couleurs | `--bg --bg2 --surface --surface2 --text --muted --accent --accent2 --accent-text --on-accent --paper --ink --ink-muted --line --glow --grad` | § 2 |
| Typographie | `--fs-micro … --fs-14xl`, `--ts` | § 2 |
| Rayons | `--r-xs --r-sm --r-md --r-lg --r-xl --r-pill` | § 2 |
| Espacements | `--sp-1 … --sp-16` | § 2 |
| Mise en page | `--top --bot --sw --lm` | § 2, § 6 |
| Composants | `.btn .cta .split .qchip .trow .seat .upsell .bn .toast .payerr .net .poster .sheet .lcard .ff2 .follow` | § 3 |
Principe : couleurs, tailles, rayons et espaces passent par des variables ; une palette ou un mode se change en redéfinissant ces variables. **Exception connue** : les boutons du mode clair utilisent deux valeurs écrites directement (`#1E1810`, `#F4E4B6`) ; elles devraient devenir des jetons (`--btn-ink`, `--btn-ink-text`).


## 10. Accueil : fond en ovale, barre transparente, liste des films
- **Fond en ovale** : la couleur de l'affiche en cours forme un ovale doux centré sur le carrousel (masque `radial-gradient(ellipse 92% 54%)`), qui **déborde des deux côtés de l'écran** ; opacité **55 % en clair, 90 % en sombre** ; bord en fondu progressif, **aucun flou sur les boutons ni les textes**.
- **Barre du haut sur l'accueil** : transparente en haut de page (l'ovale passe derrière), elle se remplit en fondu au défilement.
- **Liste « À l'affiche »** : grille alignée sur le titre de section (colonnes de 210 px minimum, toutes les affiches en 2:3 sur la même ligne de base) ; pas de décalage au survol (anneau et ombre seulement) ; résultats de recherche centrés.
- **Plan de salle** : depuis la v91, toute la salle est visible d'un coup (voir § 12) ; les trois zones (`ZONES` : Avant A–C, Centre D–F, Fond G–H) ne servent plus qu'à l'assistant.
- **Téléphone** : le logo de l'app en haut à gauche de l'accueil ; le compte est dans le menu du bas.
- **Vue depuis la place** : scène en couches 2D (sans 3D CSS, fiable sous Safari) : fond rouge sombre uni sans détails (ni rayures ni rideau visible) et écran 16:9 (la vidéo y passe, seul point clair), rangées de fauteuils en velours rouge devant soi, de plus en plus petites et floues vers l'écran, spectateurs à peine visibles (opacité 38 %), fauteuils voisins au premier plan, lumière chaude ; ambiance sombre mais lisible (rouges profonds, vignettage doux) ; léger parallaxe à la souris ; arrivée en zoom, changement de place en fondu.
- **Vue depuis la place (version immersive)** : écran presque pleine largeur (la bande-annonce y passe), salle très sombre en rouge profond avec vignettage fort, lumière de l'écran qui retombe sur les premières rangées, fauteuils voisins de notre rangée visibles de chaque côté en bas de l'image, têtes à peine visibles.


## 11. Version 82 : nouveaux composants et règles
- **Barre d'étapes** (`.stp-bar`) : segments atteints pleins (or), étape en cours épaissie avec un point lumineux, étapes à venir en gris. « Étape 2 sur 4 » = 2 segments sur 4.
- **Barre de défilement** (grands écrans à la souris) : 10 px, pouce arrondi de 4 px, transparent au repos (22 %), plus marqué au survol (42 %), or sur le pouce survolé. Aucune barre sur écran tactile.
- **Fiche personne** (`#s-person`) : photo ronde cerclée d'or (initiales si absente), rôles en puces, bouton « Suivre », biographie (résumé indicatif), filmographie en lignes `.acc-row`, lien « Voir ses films dans la liste », pied de page légal.
- **Interrupteurs** (`.sw2`) : activé = **or profond** (`--accent2`), plus de bleu étranger à la palette.
- **Avoir et récompenses** : carte « Avoir disponible » cerclée d'or (`.acc-credit`), cartes `.rw` (nom, description, bouton « Débloquer · N pts »), bloc « Mes avantages » de la commande (`.rwbox`, interrupteurs).
- **Pied de page légal** : lien texte souligné `.textlink` « Confidentialité et mentions légales », présent sur tous les écrans ; ce n'est plus un bouton dans les préférences.
- **Barre du haut (bureau)** : fondu limité à 94 px (`#dtop::before`) pour ne jamais recouvrir un titre placé dessous ; les en-têtes d'écran commencent à `--top` (96 px) ou plus.
- **Vue depuis la place** : écran sans cadre (lueur seule), format 2,3 : 1 (2,05 : 1 sur téléphone), vidéo recadrée pour supprimer les bandes noires ; au premier et deuxième rang, les fauteuils voisins se réduisent aux bords.
- **Introduction** : à chaque « Continuer », les trois affiches changent (glissement décalé de 60 ms, fondu) en même temps que le texte ; bouton de 264 px ; sans animation si « Réduire les animations ».
- **Identité de l'onglet** : favicon, icône d'écran d'accueil (180, 192, 512, maskable) et image d'aperçu de lien 1200×630 générés à partir de `img/logo-mark3.png` (`tools/make-icons.mjs`).

- **Mini-jeu (v86)** : poses du chat en `img/chat/` (assis au départ, course en 5 images, saut en 3 temps, glissade, chute sur le dos), objets de cinéma dessinés au trait (pop-corn, claquette, bobine, gobelet, projecteur), ligne d'arrivée à 260 m ; mouvement indépendant de la fréquence de l'écran, saut mémorisé, collisions indulgentes.
- **Page « Plus de réseau »** (`#off`) : plein écran, mascotte triste, titre Bebas, message, zone de jeu `.off-game` (canvas, couleurs lues dans les variables du thème), boutons « Réessayer » (primaire) et « Continuer hors ligne » (secondaire). Le jeu ne démarre qu'à l'action de l'utilisateur ; Échap ferme la page.

## 12. Version 91 : plan de salle complet, personnages, deux réalisateurs
- **Plan de salle** : toute la salle est visible d'un coup, sans zoom par zone ni bouton « Voir toute la salle ». Les zones (Avant, Centre, Fond) ne servent plus qu'à l'assistant (« au fond »).
- **Personnage du compte** : 10 portraits (depuis la v99 ; dessins vectoriels en secours) (mascotte, astronaute, guerrier, héros masqué, héroïne à cape, chasseur casqué, plombier moustachu, aventurier, shérif, navigatrice), choix dans une fenêtre centrée (`.avgrid`, `.avp`), pastille ✎ sur la photo ; l'initiale reste possible.
- **Deux réalisateurs** : chaque nom est un lien vers sa fiche ; « Suivre » ouvre « Qui voulez-vous suivre ? » (un interrupteur par personne, ou « Suivre les deux ») ; le bouton indique « Suivi 1/2 » si un seul est suivi.
- **Bande-annonce dans la salle** : lancement automatique si les extraits sont acceptés ; sinon, ou si la vidéo n'apparaît pas au bout de 7 s, bouton « Lancer la bande-annonce » (un toucher, qui demande l'accord si besoin) ; la vidéo repart quand on change de place.

## 13. Version 92 : onglet Enfants, boutons de l'introduction
- **Onglet Enfants** (4ᵉ onglet de l'accueil, marqué d'une étoile dorée) : films dont les genres contiennent « Animation » ou « Famille ». Un bandeau `.kidsbar` (mascotte assise, titre Bebas, une phrase) accompagne la liste ; le titre de section devient « Pour les enfants ».
- **Introduction** : bouton principal « Suivant » (puis « Commencer »), bouton secondaire plein « Passer l'intro » (verre clair), tous deux de 264 px, l'un sous l'autre.
- **Bande-annonce** : lien discret « Ouvrir sur YouTube » dans la fenêtre vidéo, en secours.

## 14. Version 93 : règles du cinéma affichées
- **Une seule source** : l'objet `POL` (annulation 2 h, 45 min entre films, fermeture des réservations 10 min avant, avoir 12 mois, horaires) alimente le code **et** les textes affichés.
- **Où l'utilisateur les voit** : phrase d'information sous les tarifs (étape Séance) et sous le total (Commande), avec liens « Règles d'annulation » et « Horaires du cinéma » ; fenêtre « Règles et informations légales » (pied de page) avec les sections annulation, horaires, règlement, CGV ; horaires dans le choix du cinéma ; avoir daté dans Compte et à la commande.
- **Champs « À COMPLÉTER »** (surlignés) : uniquement les informations que seul un exploitant réel connaît (raison sociale, médiateur, jours fériés, délai de remboursement).

## 15. Version 96 : bureau, historique, états
- **Bureau** : le conteneur qui défile occupe toute la largeur (la barre de défilement est au bord de la fenêtre) ; la colonne centrale est obtenue par un remplissage latéral (`padding-inline: max(0, (100% − largeur)/2)`).
- **Plan de salle** : la fonction `fitSeats()` réduit le plan (et l'écran) juste assez pour que tout tienne dans le panneau, sans cacher la légende.
- **Historique du navigateur** : chaque écran est une entrée (`history.pushState`) ; l'application revient en arrière avec `history.back()` quand la cible est l'écran précédent, pour garder la pile cohérente.
- **États sélectionnés** : un filtre ou une option choisie change de fond (or), reçoit une coche et un halo ; le survol seul ne suffit pas.
- **Pied de page** : le lien légal est le dernier élément du contenu de chaque écran, avec une marge basse égale à la hauteur des barres de boutons.
