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
Sombre reste le défaut. Le mode clair n'est pas une 6ᵉ palette : il se **déduit de la palette active**, donc les 5 thèmes ont leur version claire.
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
| **Hero d'accueil** | `.ftitle` + `.hero-cta` | Année · genre · durée, titre, « Prochaine séance · aujourd'hui, 20:30 », **une** action « Voir les séances » |
| **Progression du parcours** | `.stp` | 4 segments (Séance · Places · Paiement · Billet), segment courant déjà à 55 % (on part avec de l'avance), `role="progressbar"` |
| **Séances rapides** | `.qchip` | Pastilles d'horaires sur la fiche film : un tap → réservation avec ce créneau |
| **Tarifs** | `.trow` + `.redtog` | Plein tarif visible ; « J'ai droit à un tarif réduit » déplie les 4 autres |
| **Siège** | `.seat` | Zone tactile `--sw` × 40 (jusqu'à 44 px) ; libre gris ; occupé hachuré ; choisi = or ; PMR = contour crème pointillé + pictogramme (choisi : or + pastille ✓) ; focus visible ; flèches du clavier |
| **Menu duo** | `.upsell` | Même carte : « Ajouter » → « Ajouté ✓ · Retirer » (transformation, pas de remplacement) |
| **Toast** | `.toast` | Message + action **Annuler** (5,5 s) : ce qui s'est passé, ce que je peux annuler |
| **Erreur de paiement** | `.payerr` | Encadré rouge doux : cause, « rien n'a été débité », commande conservée, [Changer de moyen] [Réessayer] |
| **Hors ligne** | `.net` | Bandeau pilule « Hors ligne · vos choix sont conservés » / « De retour en ligne » |
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
- **Plan de salle en zones** : trois zones (`ZONES` : Avant A–C, Centre D–F, Fond G–H) ; arrivée en vue d'ensemble puis zoom de la caméra sur la zone des places proposées (`#sgrid.ov` → `.zf`, 0,8 s) ; les autres rangées s'estompent ; « Voir toute la salle » bascule ; animations réduites : pas de zoom.
- **Téléphone** : le logo de l'app en haut à gauche de l'accueil ; le compte est dans le menu du bas.
- **Vue depuis la place** : scène en couches 2D (sans 3D CSS, fiable sous Safari) : rideau rouge et écran 16:9 (la vidéo y passe), rangées de fauteuils en velours rouge devant soi, de plus en plus petites et floues vers l'écran, spectateurs en silhouette, fauteuils voisins au premier plan, lumière chaude ; ambiance claire (rouges profonds, pas de noir) ; léger parallaxe à la souris ; arrivée en zoom, changement de place en fondu.
