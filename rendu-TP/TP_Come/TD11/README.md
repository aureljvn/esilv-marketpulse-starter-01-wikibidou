# TD11 - Dash Dashboard - Côme Leblois

## Objectif
Afficher la comparaison dans un tableau de bord web, à partir du même résultat que le terminal.

## Ce que j'ai fait
- Installation de `dash` et `plotly`, ajoutés dans `requirements.txt`.
- Nouveau fichier `src/dashboard.py` :
  - appelle `build_market_snapshot()` une seule fois ;
  - affiche le contexte (provider + mode d'accès, instrument, benchmark, période, intervalle) ;
  - affiche 3 indicateurs : rendement AAPL, rendement SP500, performance relative ;
  - trace un graphique base 100 avec les deux séries.
- Aucun appel à Yahoo ou Bloomberg et aucune formule dans `dashboard.py`.

## Lancer
```text
python src/dashboard.py
```
puis ouvrir http://127.0.0.1:8050

## Résultat
Mêmes valeurs que le terminal : +6.48 %, +2.15 %, +4.33 pts.

## Captures
Page du dashboard.
