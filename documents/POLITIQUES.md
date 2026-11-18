# Politiques d'achat, d'annulation et règles du cinéma

*Version du prototype : v93 (18 novembre 2026). Ces règles sont **codées dans l'application** (une seule source : `POL` dans `index.html`) et **affichées** dans « Règles, confidentialité et mentions légales » (lien en bas de chaque page), sur la page « Séance » et sur la page « Commande ». Textes-types : à faire valider par un juriste avant toute mise en service réelle.*

## 1. Les règles retenues
| Règle | Valeur | Où elle est appliquée dans l'app |
|---|---|---|
| Réservation en ligne | jusqu'à **10 minutes avant** la séance | Les séances commencées ou sur le point de l'être sont grisées « Terminée » |
| Annulation par le client | jusqu'à **2 heures avant** la séance | Bouton « Annuler la réservation » sur la page du billet et dans Compte › Mes réservations › Mon billet, ou message « Annulation impossible » |
| Contrepartie de l'annulation | **avoir** du montant payé (frais de service compris), **jamais un remboursement en argent** | Avoir visible dans Compte et activable à la commande |
| Validité de l'avoir | **12 mois** à partir de l'annulation | Date affichée dans Compte et à la commande ; un avoir périmé n'est plus proposé |
| Séance annulée par le cinéma | **remboursement intégral** (ou autre séance) | Créneau « Annulée · voir 23:15 » ; règle écrite dans les conditions |
| Absence ou retard | billet ni remboursé ni échangé | Règle écrite |
| Même séance deux fois | impossible | Créneau « Déjà réservé », refus au paiement et à l'étape « Places » |
| Deux films qui se chevauchent | impossible ; **45 minutes minimum** entre deux films | Créneau « Séance déjà prévue », message « Vous avez déjà une séance… » |
| Droit de rétractation | **exclu** (activité de loisirs à date déterminée) | Case CGV non précochée qui le rappelle |
| Frais de service | 1,20 € par billet, affichés avant la commande et compris dans le total | Page Commande |
| Points | 1 point par euro ; les points d'une commande annulée sont retirés | Compte |

## 2. Horaires de démonstration (identiques dans les quatre cinémas)
| Élément | Horaire |
|---|---|
| Accueil et caisses | tous les jours de **16 h 30 à 1 h 00**, et jusqu'à la fin de la dernière séance |
| Séances | de **17 h 15 à 23 h 15** (les films longs peuvent finir après minuit) |
| Ouverture des salles | 15 minutes avant la séance |
| Retrait comptoir (friandises) | 30 minutes avant la première séance, jusqu'au début de la dernière |
| Début de séance | l'horaire est celui du début des publicités ; le film commence environ 15 minutes plus tard |
| Jours fériés, fermetures exceptionnelles | à renseigner par l'exploitant (champ « À COMPLÉTER ») |

## 3. Règles de la salle (règlement intérieur type)
Billet contrôlé à l'entrée (QR code) · justificatif pour les tarifs réduits · films interdits aux moins de 12, 16 ou 18 ans (classification du CNC) avec pièce d'identité possible · entrée possible après le début sans remboursement, places numérotées gardées · téléphones silencieux · interdiction de filmer ou photographier · restauration vendue sur place, boissons alcoolisées extérieures interdites · sacs pouvant être contrôlés, consignes d'évacuation, capacité de la salle (64 places) · emplacements fauteuil roulant et accompagnant, chiens guides et d'assistance acceptés, autres animaux non admis · objets trouvés à l'accueil · le personnel peut refuser l'accès ou exclure une personne qui gêne les autres.

## 4. Références juridiques à valider
| Sujet | Référence |
|---|---|
| Pas de droit de rétractation pour une séance à date déterminée | Code de la consommation, art. L.221-28, 12° |
| Bouton « Commande avec obligation de paiement » | Code de la consommation, art. L.221-14 |
| Prix toutes taxes comprises, frais annoncés avant la commande | Code de la consommation, art. L.112-1 et L.111-1 |
| Médiateur de la consommation | Code de la consommation, art. L.612-1 (nom à renseigner) |
| Données personnelles, cookies | RGPD ; CNIL (aucun cookie ni traceur dans l'application) |
| Accessibilité | Directive européenne 2019/882, applicable depuis le 28 juin 2025 |
| Droit d'auteur (interdiction de filmer) | Code de la propriété intellectuelle |

## 5. Ce qui reste à renseigner par un exploitant réel
Raison sociale, SIRET, TVA, coordonnées · médiateur de la consommation · délai de remboursement en cas d'annulation par le cinéma · liste des jours fériés et fermetures · durée de conservation des objets trouvés · classification de chaque film (non affichée dans le prototype). Ces champs sont signalés « À COMPLÉTER » dans l'application.
