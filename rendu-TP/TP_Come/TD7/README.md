# TD07 - Data Normalization + Comparison - Côme Leblois

## Objectif
Comparer un instrument (AAPL) à son benchmark (SP500) avec une couche
d'analyse réutilisable par tous les fournisseurs de données.

## Ce que j'ai fait
- `normalize_price_row()` dans `src/main.py` : conversion des champs CSV en `float` / `int`.
- Nouveau module `src/analytics.py` (sans aucun identifiant de fournisseur) :
  `index_by_date`, `align_series`, `calculate_period_return`,
  `calculate_relative_performance`, `calculate_base_100`.
- `src/main.py` aligne les deux séries sur les dates communes puis affiche les résultats.
- PR #4 relue par Aurélien puis mergée.

## Résultat (données locales)
- AAPL : +6.48 %
- SP500 : +2.15 %
- Performance relative : +4.33 points de pourcentage
- Base 100 : AAPL 100.00 -> 106.48, SP500 100.00 -> 102.15

## Fichiers
- Captures de la sortie et des vérifications (types, alignement, neutralité d'analytics.py).
- `analytics.py` et `main.py` : copie des fichiers tels qu'ils étaient à la fin du TD07
  (`src/main.py` a évolué ensuite aux TD08 et TD10).
