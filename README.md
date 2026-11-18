# U CINEMÀ

Prototype d'application de réservation de cinéma (PWA), réalisé dans le cadre d'un projet de classe.

**Démo en ligne :** https://mik2a-coder.github.io/u-cinema/

> **Maquette pédagogique.** Les cinémas, adresses, séances, prix et notes sont fictifs. Les affiches, photos de personnes et de produits servent uniquement à la démonstration, sans but commercial ; leurs droits appartiennent à leurs auteurs et ayants droit.

## Fonctions
- Catalogue de films (à l'affiche, nouveautés, prochainement), recherche avec suggestions (films, acteurs, cinémas)
- Fiche film, extrait de bande-annonce (YouTube sans cookie, uniquement après accord)
- Réservation : cinéma, date, séance, tarifs, choix des places avec vue depuis la place
- Petite faim (menus, pop-corn, boissons), paiement simulé, billet
- Compte local : carte de fidélité, historique, notes
- Assistant « U Ghjattu-Volpe » pour choisir un film
- Mode clair / sombre, accessibilité (taille du texte, contraste, animations réduites)
- Données conservées uniquement sur l'appareil

## Lancer en local
```bash
python3 -m http.server 8731
```
puis ouvrir http://localhost:8731/index.html (les extraits vidéo demandent un serveur http).

## Organisation du dossier
| Où | Quoi |
|---|---|
| `index.html`, `sw.js`, `manifest.webmanifest`, `icons/`, `img/`, `fonts/` | **Le site** (publié tel quel sur GitHub Pages ; ne pas déplacer) |
| `A-RENDRE/` | **Les deux PDF à remettre** : `RENDU-U-CINEMA.pdf` (dossier complet) et `CHECKLIST-TEST-3-PERSONNES.pdf` |
| `documents/` | Tous les textes sources : direction artistique, brief et persona, parcours, design system, tests, journal, **journal des versions**, conformité, notes, barème |
| `U-CINEMA-autonome.html` | Version en un seul fichier, utilisable sans réseau |
| `Ouvrir U CINEMA.command` | Double-clic : ouvre le prototype dans Chrome (serveur local) ; la variante « tests appareils » sert aux essais sur téléphone |
| `tools/` | Outils : captures (`shoot.mjs`), contrôles (`scenarios/`), fabrication des PDF et de la version autonome, icônes, poses du chat |
| `rendu/captures/` | Captures d'écran du parcours (utilisées dans le PDF) |
| `deploy/` | Déploiement sur Raspberry Pi |
| `archives/` | Anciens essais (études de logos, page de test), non publiés |

## Liens
- Prototype : https://mik2a-coder.github.io/u-cinema/
- **Page d'erreur réseau (mini-jeu)** : https://mik2a-coder.github.io/u-cinema/#x:0:off
- Code : https://github.com/mik2a-coder/u-cinema

## Dossier de rendu (exercice « Prototyper en 2026 »)
| Pièce | Fichier |
|---|---|
| **Dossier à rendre (PDF, tout-en-un)** | `A-RENDRE/RENDU-U-CINEMA.pdf` |
| Direction artistique et palette (60-30-10) | `documents/DIRECTION-ARTISTIQUE.md` |
| Journal des versions (v82 à v86, fichiers modifiés, historique complet) | `documents/VERSIONS.md` |
| Critères et preuves | `documents/BAREME.md` |
| Brief et persona | `documents/BRIEF-PERSONA.md` |
| Parcours utilisateur | `documents/PARCOURS.md` + `rendu/captures/` |
| Design system (variables, composants) | `documents/DESIGN.md` |
| Tests (protocole, contrôles, revues) | `documents/TESTS.md`, `tools/scenarios/` |
| **Checklist à utiliser pendant les 3 tests** | `documents/CHECKLIST-TESTS.md` · `A-RENDRE/CHECKLIST-TEST-3-PERSONNES.pdf` (format vertical 3:4) |
| Journal (outils, prompts, choix) | `documents/JOURNAL.md` |
| Notes de conception | `documents/V2-NOTES.md` |
| Conformité | `documents/CONFORMITE.md` |

Régénérer les PDF : `python3 tools/build-rendu.py` (Chrome requis). Version autonome : `python3 tools/build-autonome.py`. Captures : `node tools/shoot.mjs …` (voir `documents/TESTS.md`).
