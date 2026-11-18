# U CINEMÀ — Brief et persona (une page)

## Brief
**Sujet.** L'énoncé propose « Ciné Lumière, multiplexe de 12 salles ». J'ai gardé le même parcours (film → séance → places → paiement → billet) mais je l'ai adapté en **U Cinemà, un réseau de 4 cinémas fictifs en Corse** (Aiacciu, Bastia, Corti, Portivechju) avec une mascotte, *U Ghjattu-Volpe*, symbole de la classe. *(Adaptation à faire valider par le formateur.)*

**Problème.** Choisir un film, une séance et ses places prend trop d'étapes et d'hésitations sur les applis de cinéma : tarifs en liste interminable, plan de salle minuscule, frais découverts à la fin, erreurs de paiement qui font tout recommencer.

**Objectif mesurable.** Réserver 2 places en **moins de 60 secondes**, d'une main, sans erreur, sur téléphone comme sur grand écran.

**Périmètre.** Films à l'affiche, fiche film, séances, choix des places sur le plan de salle (et vue depuis la place), paiement, billet dans le téléphone, compte (carte d'abonné, historique). **Imprévus** : séance complète ou annulée, paiement refusé, hors ligne, double réservation.

**Contraintes.** Accessible (WCAG 2.2, emplacements fauteuil roulant, audiodescription, texte agrandi), respectueux des données (RGPD, tout reste sur l'appareil), prix TTC clairs, pas de fausse urgence.

**Mesure de réussite.** Temps de réservation ≤ 60 s · 0 aide demandée · tarif adapté retrouvé · billet retrouvé hors ligne.

## Persona principal
**Mika, 27 ans, graphiste à Ajaccio.** Va au cinéma deux fois par mois, souvent le samedi avec un ami. Réserve dans le bus ou le train, d'une main, avec peu de patience.
- **Veut** : savoir vite s'il reste des places ce soir, choisir deux sièges côte à côte, avoir son billet même sans réseau (les tunnels du train et les zones blanches de l'intérieur de l'île coupent la connexion).
- **Frustrations** : formulaires longs, tarifs incompréhensibles, frais au dernier écran, billet introuvable à l'entrée.
- **Contexte** : téléphone, une main, trajet, réseau instable.

## Persona d'accessibilité
**Ghjuvana Maria, 34 ans, de Bastia, se déplace en fauteuil roulant.** Prend le train ou le bus pour aller au cinéma. Besoin d'emplacements dédiés, du tarif adapté et d'un accompagnant ; veut savoir combien d'emplacements restent **avant** de se déplacer.

## Ce que l'app répond
| Besoin | Réponse dans l'app |
|---|---|
| Voir vite ce soir | Accueil : affiche + **4 séances du jour** + un seul bouton |
| Deux sièges côte à côte | Places proposées d'office, plan de salle jusqu'à 44 px par siège |
| Pas de mauvaise surprise | Total TTC et frais visibles avant le paiement, case CGV non précochée |
| Carte refusée | « Rien n'a été débité », commande conservée, [Changer de moyen] |
| Billet sans réseau | Billet QR conservé hors ligne (mode avion) |
| Accessibilité | Emplacements PMR comptés, texte jusqu'à 130 %, contraste élevé, clavier, animations réduites |
