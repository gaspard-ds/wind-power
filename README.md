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


## Modules :
- `wind_constants.py` : contains constants like regions, region_code and model features
- `data_processing.py` : summary of data manipulation shown in the notebooks. Can be run as a script to processed new data.
- `main.py` : contains functions to train one model and output predictions for production in MWH. Can be used as a script to train a linear regression, print the scores and save the model.

## Notebooks :
`1.Capacity_Exploration.ipynb` & `2.Weather_Exploration.ipynb` & `3.Production_Exploration.ipynb` : 
- Data exploration and selection of useful columns for capacity, weather and production data. </br>
- Functions were added later to `data_processing` to replicate the results and provide a executable script.</br>
- Notebooks left here to show the steps taken and the interim results/plots.</br>

#### `4.Exploration_and_plots.ipynb` :
- Experimented on different ways to merge the data and reconcile the date indexes.
- Also use this notebook for `WindRose` plots displayed in the results
- Notebook left here to show how the plots were generated.</br>

#### `5.Data_Merge.ipynb` :
- Shows actual steps taken to merge the data
- Functions were added later to `data_processing` to replicate the results and provide a executable script.</br>
- Notebook left here to show the steps taken and the interim results/plots.</br>

#### `6.Model_Benchmark.ipynb` :
- Target : `relative production = (Production (MW)/ Capacity (MW))`
- Features : different lists were testes, mainly weather data (speed, direction, pressure, temperature)
- Benchmarking model results using a private library
- Displays detailed table with results and model parameters
- Plots : results per model type, difference between train and test scores for all models

#### `7.Model_Benchmark.ipynb` :
- Twist on the first benchmark : the goal is to see if the production could be used directly as a target, having installed capacity as a feature. </br>
- Same models as before, but interesting results, as they validate one hypothesis.