# TD08 - Yahoo Finance - Côme Leblois

## Objectif
Remplacer les fichiers locaux par des données de marché récentes,
sans modifier la couche d'analyse.

## Ce que j'ai fait
- Installation de `yfinance`, ajouté dans `requirements.txt`.
- Nouveau module `src/providers/yahoo_provider.py` :
  `fetch_yahoo_prices()` renvoie des lignes canoniques (date, ticker, open, high, low, close, volume).
- Correspondance `AAPL -> AAPL` et `SP500 -> ^GSPC` : `^GSPC` reste dans le provider,
  le ticker canonique reste `SP500`.
- `src/main.py` récupère AAPL et SP500 (period=1mo, interval=1d) et réutilise
  `align_series()` et les fonctions du TD07. `src/analytics.py` n'a pas changé.

## Résultat (exécuté le 2026-11-26, dépend du moment de l'exécution)
- 23 observations alignées, du 2026-10-26 au 2026-11-25
- AAPL : +3.39 %
- SP500 : -6.43 %
- Performance relative : +9.83 points de pourcentage

## Captures
Sortie de `python src/main.py` avec "Provider : Yahoo Finance via yfinance"
(aussi utilisée pour le Checkpoint B : `evidence/checkpoint-b/sawee4/`).
