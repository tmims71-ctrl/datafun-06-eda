# datafun-06-eda

## README.md
- Author: Tammy Mims
  
- Purpose: Create a custom exploratory data analysis (EDA) project using GitHub, Jupyter, pandas, Seaborn, and other popular data analytics tools.

## Setup Commands (Using uv - Recommended)

### Install Dependencies
```powershell
uv sync
```

### Run Tests
```powershell
uv run pytest --cov=src --cov-report=term-missing
```

### Format Code
```powershell
uv run ruff format .
```

### Build Documentation
```powershell
uv run mkdocs build
```

### Serve Documentation Locally
```powershell
uv run mkdocs serve
```
Visit: http://127.0.0.1:8000

### Deploy Documentation to GitHub Pages
```powershell
uv run mkdocs gh-deploy
```

## Alternative Setup (Using pip/venv)

If you prefer the traditional approach:

```powershell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt --timeout 100
```

## Open Notebook

In VS Code, open `notebooks/tmims_eda.ipynb` and select the `.venv` kernel, or use:

```powershell
jupyter lab notebooks/tmims_eda.ipynb
```

## Process
- Created .gitignore, requirements.txt, and pyproject.toml.
- Added a starter script (mims.py) that prints the author and module on two lines.
- Added a project log to capture work notes.
- Set up project with uv and pyproject.toml (recommended approach).
- Enabled required packages (jupyterlab, pandas, pyarrow, matplotlib, seaborn, pytest, ruff, mkdocs).
- Added seaborn car_crashes dataset to data/car_crashes.csv.
- Created data and notebooks folders.
- Built EDA notebook at notebooks/tmims_eda.ipynb with dataset info, workflow sections, and plots.
- Added additional charts (pairplot, bar chart, boxplot) for the car_crashes dataset.
- Executed all notebook cells with outputs.
- Added conclusion section summarizing key findings and implications.
- Created comprehensive MkDocs documentation site.

## Files
- [notebooks/tmims_eda.ipynb](notebooks/tmims_eda.ipynb)
- [data/car_crashes.csv](data/car_crashes.csv)

## Dataset Description

| Item | Description |
| --- | --- |
| Name | Car Crashes (Seaborn) |
| Source | [https://github.com/mwaskom/seaborn-data/blob/master/car_crashes.csv](https://github.com/mwaskom/seaborn-data/blob/master/car_crashes.csv) |
| Records | 51 rows, 8 columns |

| Column | Description |
| --- | --- |
| abbrev | State abbreviation |
| total | Fatal collisions per billion miles |
| speeding | % of fatal collisions involving speeding |
| alcohol | % of fatal collisions involving alcohol impairment |
| not_distracted | % of fatal collisions with no distraction |
| no_previous | % of fatal collisions with no prior accidents |
| ins_premium | Insurance premium (annual, dollars) |
| ins_losses | Insurance losses per insured driver (annual, dollars) |

## Notes
- Use the local .venv interpreter in VS Code.
- Select the .venv kernel when working in notebooks.
