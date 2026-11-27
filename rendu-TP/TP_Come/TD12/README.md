# TD12 - Integration + Release - Côme Leblois

## Objectif
Obtenir une version de MarketPulse qu'une autre personne peut installer et lancer.

## Ce qui a été fait dans l'équipe
- Release finale de l'équipe : PR #9 "chore: prepare MarketPulse final release"
  (Aurélien, relue par Gabin) : chemins `data/sample` rendus indépendants du dossier
  de lancement, README d'équipe avec les commandes d'installation et de lancement.

## Ce que j'ai fait
- Mise à jour de mon `main` local puis validation sur le `main` final mergé :
  - `python src/main.py` : Bloomberg stage / APPROVED_SAMPLE, +6.48 %, +2.15 %, +4.33 points ;
  - `python src/dashboard.py` : mêmes valeurs, graphique base 100.
- Test de reproductibilité sur un clone neuf, dans un dossier séparé :
  ```text
  git clone https://github.com/aureljvn/esilv-marketpulse-starter-01-wikibidou.git marketpulse-repro
  cd marketpulse-repro
  python -m venv .venv
  .venv\Scripts\python -m pip install -r requirements.txt
  .venv\Scripts\python src/main.py
  ```
  Installation réussie (yfinance, dash, plotly) et même résultat que sur mon poste.
- Checkpoint C : `evidence/checkpoint-c/sawee4/`.

## Mode d'accès final
Bloomberg stage - APPROVED_SAMPLE : connexion Bloomberg réelle non démontrée.
