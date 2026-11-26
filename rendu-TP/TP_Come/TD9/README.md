# TD09 - Bloomberg Introduction - Côme Leblois

## Objectif
Écrire le contrat de correspondance entre les données Bloomberg et le format MarketPulse.

## Ce que j'ai fait
- Mode d'accès : APPROVED_SAMPLE (pas de terminal Bloomberg, connexion live non démontrée).
- Inspection du fichier `data/sample/bloomberg_reference_sample.json`.
- Document `docs/BLOOMBERG_FIELD_MAPPING.md` :
  - `AAPL -> AAPL US Equity`, `SP500 -> SPX Index` ;
  - table des champs (`observation_date -> date`, `close_value -> close`...),
    en précisant que ce sont des clés pédagogiques et pas des champs Bloomberg réels ;
  - notes pour le TD10 (conversions, volume de SPX à 0, fichier de référence attendu).

## Fichiers
- `BLOOMBERG_FIELD_MAPPING.md` : copie du livrable.
- `inspection_bloomberg_sample.txt` : sortie de l'inspection du fichier d'exemple.
