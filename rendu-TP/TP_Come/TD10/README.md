# TD10 - Bloomberg Provider - Côme Leblois

## Objectif
Brancher l'étape Bloomberg sur la même chaîne que CSV et Yahoo, sans réécrire l'application.

## Ce que j'ai fait
- Nouveau module `src/providers/bloomberg_provider.py` :
  - `fetch_raw_bloomberg_history()` : lecture de l'entrée (fichier d'exemple en APPROVED_SAMPLE) ;
  - `normalize_bloomberg_history()` : conversion en lignes canoniques ;
  - correspondance `AAPL -> AAPL US Equity`, `SP500 -> SPX Index`.
- Les lignes produites sont identiques aux 42 lignes de `bloomberg_reference_expected.json`.
- `src/main.py` : nouvelle fonction `build_market_snapshot()` qui renvoie le résultat
  partagé (provider, access_mode, période, rendements, performance relative, base 100).
  `main()` affiche ce snapshot, et `main.py` peut être importé sans lancer le terminal.
- `src/analytics.py` n'a pas changé.

## Résultat
Provider : Bloomberg stage, Access mode : APPROVED_SAMPLE.
AAPL +6.48 %, SP500 +2.15 %, +4.33 points de pourcentage.
Ce n'est pas une preuve de connexion Bloomberg réelle (mode échantillon).

## Captures
Sortie de `python src/main.py`.
