# TD02 - Python + CSV / JSON - Côme Leblois

## Objectif
Lire les fichiers locaux `data/sample/instruments.json` et `data/sample/prices.csv`
et afficher un premier résumé de marché.

## Ce que j'ai fait
- Chargement de `instruments.json` (instrument AAPL, benchmark SP500).
- Chargement de `prices.csv` avec `csv.DictReader`.
- Séparation des lignes AAPL et SP500 (21 observations chacune).
- Affichage du premier et du dernier cours de clôture, convertis en `float`.

## Captures
5 captures du code et de la sortie de `python src/main.py` (2026-10-07).
