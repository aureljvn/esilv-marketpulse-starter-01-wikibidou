# TD06 - Code Review - Côme Leblois

## Objectif
Relire le travail d'un autre étudiant avant intégration.

## Ma review : PR #2 d'Aurélien "feat: display data provider label"
- J'ai récupéré la branche et lancé `python src/main.py` : la ligne
  `Provider: Local sample files (data/sample)` s'affiche bien.
- Le diff ne touche que `src/main.py` (+2 lignes) et n'entre pas en conflit avec ma PR #1.
- Point bloquant signalé : la description de la PR ne correspondait pas au diff
  (elle parlait d'une section README, alors que seul `src/main.py` changeait).
- Suggestion non bloquante : utiliser "CSV" comme label pour rester cohérent
  avec `config/settings.yml` (`provider: csv`).

## Review reçue sur ma PR #1
Aurélien a testé la branche, vérifié que le marché s'affiche pour AAPL et SP500
et que la valeur vient de `instruments.json`, puis a confirmé son approbation.

## Comment / Request changes / Approve
- Comment : remarque sans décision.
- Request changes : un problème doit être corrigé avant le merge.
- Approve : la PR peut être mergée.

## Liens
- https://github.com/aureljvn/esilv-marketpulse-starter-01-wikibidou/pull/2
- https://github.com/aureljvn/esilv-marketpulse-starter-01-wikibidou/pull/1
