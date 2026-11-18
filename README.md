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

## Fichiers
- `index.html` : l'application (fichier unique), `sw.js` : mode hors ligne, `manifest.webmanifest`
- `V2-NOTES.md`, `DESIGN.md`, `CONFORMITE.md`, `TESTS.md` : notes de conception, conformité et tests
- `deploy/` : déploiement sur Raspberry Pi


## Dossier de rendu (exercice « Prototyper en 2026 »)
| Pièce | Fichier |
|---|---|
| **Dossier à rendre (PDF, tout-en-un)** | `RENDU-U-CINEMA.pdf` |
| Barème (auto-évaluation avec preuves) | `BAREME.md` |
| Brief et persona | `BRIEF-PERSONA.md` |
| Parcours utilisateur | `PARCOURS.md` + `rendu/captures/` |
| Design system (variables, composants) | `DESIGN.md` |
| Tests (protocole, contrôles, revues) | `TESTS.md`, `tools/scenarios/` |
| **Checklist à utiliser pendant les 3 tests** | `CHECKLIST-TESTS.md` · `CHECKLIST-TEST-3-PERSONNES.pdf` (A4 paysage, à imprimer) |
| Journal (outils, prompts, choix) | `JOURNAL.md` |
| Notes de conception, grille Peaufiner | `V2-NOTES.md` |
| Conformité | `CONFORMITE.md` |

Régénérer le PDF : `python3 tools/build-rendu.py` (Chrome requis). Captures : `node tools/shoot.mjs …` (voir `TESTS.md`).
