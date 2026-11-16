# U CINEMÀ — Conformité (RGPD, consommation, accessibilité)

> Ce document décrit ce que **l'application fait techniquement**. Ce n'est **pas un avis juridique** :
> avant toute mise en service réelle, faire valider les textes par un juriste / le DPO.
> Dernière mise à jour des règles consultées : novembre 2026.

## Ce qui est en place

| Sujet | Mesure dans l'application |
|---|---|
| Minimisation | Aucun nom, e-mail, téléphone, compte ni numéro de carte n'est demandé. Paiement simulé. Réservation en mémoire seulement (effacée à la fermeture). |
| Données de santé (art. 9 RGPD) | Le tarif « personne en situation de handicap » et l'emplacement fauteuil roulant déclenchent une **demande de consentement explicite** (finalité, ce qui est enregistré, retrait). Refuser n'empêche pas de réserver. Justificatif contrôlé à l'entrée, jamais téléversé. |
| Retrait du consentement | « Données et confidentialité › Mes données › Retirer mon consentement » : supprime tarif et emplacement handicap. |
| Droits d'accès / portabilité | « Exporter mes données » (fichier JSON). |
| Droit à l'effacement (local) | « Effacer toutes mes données sur cet appareil » (réglages, cache hors ligne, service worker, réservation). Demande une confirmation. |
| Information (art. 13) | Politique de confidentialité, cookies, mentions légales, CGV, déclaration d'accessibilité, accessibles depuis l'accueil, l'intro, les réglages d'accessibilité et l'écran de commande. |
| Cookies / traceurs | **Aucun** cookie ni traceur publicitaire ou de mesure d'audience. Seul stockage : réglages d'accessibilité choisis par l'utilisateur (`cinelux-a11y`) → pas de bannière nécessaire. Si de l'audience ou de la pub est ajoutée : bannière avec « Tout refuser » aussi visible que « Tout accepter ». |
| Pas de fuite vers des tiers | Polices, affiches, images servies par l'application. En-têtes serveur : CSP stricte (aucune ressource externe), `Referrer-Policy: no-referrer`, `Permissions-Policy` (géolocalisation, caméra, micro, paiement interdits), `nosniff`. Fichier `deploy/security-headers.conf`. |
| Vente à distance (Code de la consommation) | Bouton de validation « **Commande avec obligation de paiement** » (art. L.221-14). Prix **TTC** et frais de service affichés avant la commande. **Case CGV obligatoire**. Information claire : **pas de droit de rétractation** pour les loisirs à date déterminée (art. L.221-28 12°). |
| Accessibilité (directive (UE) 2019/882, applicable depuis le 28/06/2025) | Réglages (texte, contraste, police lisible, animations), lecture vocale, annonces lecteurs d'écran, audiodescription / sous-titres, emplacements PMR. **Déclaration d'accessibilité : « non évalué »** (aucun audit RGAA). |

## À compléter (champs `[À COMPLÉTER]` dans l'application)
- Identité du responsable du traitement, contact, DPO éventuel.
- Vendeur : raison sociale, adresse, SIRET, n° de TVA.
- Éditeur, directeur de la publication, hébergeur.
- Conditions de report / annulation / remboursement.
- Médiateur de la consommation (nom, adresse, site) — obligatoire pour un professionnel.
- Contact accessibilité.

## À prévoir pour un vrai service (hors périmètre du prototype)
- **Serveur de réservation** : registre des consentements (date, version du texte, preuve), durées de conservation (pièces comptables), journalisation sécurisée, sauvegardes.
- **Registre des traitements** ; **analyse d'impact (AIPD)** à évaluer si des données de santé sont traitées à grande échelle.
- **Contrat de sous-traitance** (art. 28) avec l'hébergeur et le prestataire de paiement ; vrai paiement via un prestataire certifié PCI-DSS (ne jamais stocker les numéros de carte).
- **Droits de diffusion** des affiches, photos et images de scène (actuellement : usage de démonstration) ; sous-titres/audiodescription réels.
- **Audit RGAA** et mise à jour de la déclaration d'accessibilité.
- HTTPS obligatoire (Tailscale Serve ou certificat), mises à jour de sécurité du serveur.

## Sources consultées
CNIL (cookies et traceurs, données de santé), DGCCRF (e-commerce, accessibilité), Code de la consommation L.221-14 et L.221-28, directive (UE) 2019/882.


## Ajouts novembre 2026
- **Extraits vidéo (YouTube)** : contenu tiers. Aucune requête vers YouTube avant le choix de l'utilisateur (feuille de consentement, « Activer » et « Non merci » de même poids). Domaine `youtube-nocookie.com` uniquement ; CSP : `frame-src https://www.youtube-nocookie.com` (voir `deploy/security-headers.conf`). Réglage modifiable à tout moment ; refus conservé sur l'appareil. À mentionner dans la politique de confidentialité : YouTube peut recevoir l'adresse IP lorsque la vidéo est chargée.
- **Compte et fidélité** : données (points, réservations, notes, rappels) conservées **uniquement dans le navigateur** (`localStorage`), incluses dans « Exporter mes données », supprimées par « Tout effacer ». Un vrai programme de fidélité côté serveur demandera : base légale (contrat / consentement), durée de conservation, information sur le profilage éventuel, droit d'accès et d'effacement.
- **Rappels de sortie** : enregistrés sur l'appareil, aucune notification envoyée.
- **Assistant U Ghjattu-Volpe** : règles locales (aucun appel réseau, aucun service d'IA externe). Les phrases saisies ne quittent pas l'appareil et ne sont pas conservées ; les goûts utilisés sont les notes du compte (`localStorage`). À indiquer dans la politique de confidentialité.
