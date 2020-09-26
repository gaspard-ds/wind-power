# Wind Power

## Set up
- Create a venv : `python3.7 -m venv venv`
- Install requirements (requirements.txt)
- Install `jupyter-lab` (or jupyter notebooks)
- Install `windrose` (for wind maps plots)
- Create a jupyter kernel for the venv : 
```python
pip install ipykernel
ipython kernel install --user --name=wind_power
```

## Open Data Sources : 
- [French Power production (30 minutes granularity)](https://opendata.reseaux-energies.fr/explore/dataset/eco2mix-regional-cons-def/information/?disjunctive.libelle_region&disjunctive.nature)
- [Installed Wind Power (Yearly granularity)](https://www.data.gouv.fr/fr/datasets/parc-regional-annuel-de-production-eolien-et-solaire-2001-a-2019/)
- [French Weather Data (3hour granularity)](https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/table/?sort=date)
