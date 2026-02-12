# datafun-06-eda

## README.md
- Author: Tammy Mims
  
- Purpose: Create a custom exploratory data analysis (EDA) project using GitHub, Jupyter, pandas, Seaborn, and other popular data analytics tools.

## Commands
```
py -m venv .venv
```

```
.\.venv\Scripts\activate
```

```
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt --timeout 100
```

```
jupyter lab notebooks/tmims_eda.ipynb
```

## Process
- Created .gitignore, requirements.txt, and pyproject.toml.
- Added a starter script (mims.py) that prints the author and module on two lines.
- Added a project log to capture work notes.
- Enabled required packages (jupyterlab, pandas, pyarrow, matplotlib, seaborn).
- Added seaborn car_crashes dataset to data/car_crashes.csv.
- Created data and notebooks folders.
- Built EDA notebook at notebooks/tmims_eda.ipynb with dataset info, workflow sections, and plots.
- Added additional charts (pairplot, bar chart, boxplot) for the car_crashes dataset.

## Files
- [notebooks/tmims_eda.ipynb](notebooks/tmims_eda.ipynb)
- [data/car_crashes.csv](data/car_crashes.csv)

## Dataset

| Item | Description |
| --- | --- |
| Name | Car Crashes (Seaborn dataset) |
| Source | [https://github.com/mwaskom/seaborn-data/blob/master/car_crashes.csv](https://github.com/mwaskom/seaborn-data/blob/master/car_crashes.csv) |
| Records | 51 rows, 8 columns |

| Column | Description |
| --- | --- |
| abbrev | State abbreviation |
| total | Total drivers involved in fatal collisions per billion miles |
| speeding | Percentage of drivers involved in fatal collisions who were speeding |
| alcohol | Percentage of drivers involved in fatal collisions who were alcohol-impaired |
| not_distracted | Percentage of drivers involved in fatal collisions who were not distracted |
| no_previous | Percentage of drivers involved in fatal collisions with no previous accidents |
| ins_premium | Car insurance premium (annual, dollars) |
| ins_losses | Insurance losses per insured driver (annual, dollars) |

## Notes
- Use the local .venv interpreter in VS Code.
- Select the .venv kernel when working in notebooks.
