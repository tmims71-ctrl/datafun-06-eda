# Project Setup

## Prerequisites

- Python 3.11 or higher
- Git
- VS Code (recommended) or another editor
- uv package manager (or pip)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/tmims71-ctrl/datafun-06-eda.git
cd datafun-06-eda
```

### 2. Create and Activate Virtual Environment

Using **uv** (recommended):

```powershell
uv sync
```

Alternatively, using **pip and venv**:

```powershell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt --timeout 100
```

### 3. Verify Installation

Test that packages are installed correctly:

```powershell
uv run pytest --cov=src --cov-report=term-missing
```

### 4. Run Code Formatting

Format Python code with ruff:

```powershell
uv run ruff format .
```

## Working with Jupyter Notebooks

### Open the Notebook in VS Code

1. Open the notebook file: `notebooks/tmims_eda.ipynb`
2. Select the Python interpreter from your `.venv`
3. Select the kernel associated with your project virtual environment
4. Run cells individually or use "Run All"

### Run JupyterLab (Alternative)

To open JupyterLab in your browser:

```powershell
jupyter lab notebooks/tmims_eda.ipynb
```

Or with uv:

```powershell
uv run jupyter lab notebooks/tmims_eda.ipynb
```

## Building Documentation

### Build MkDocs Site

```powershell
uv run mkdocs build
```

### Serve Documentation Locally

```powershell
uv run mkdocs serve
```

Then open your browser to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Deploy to GitHub Pages

```powershell
uv run mkdocs gh-deploy
```

## Troubleshooting

### uv sync fails

If you encounter compiler errors, remove version pins and delete `uv.lock`:

```powershell
Remove-Item uv.lock
uv sync
```

### Kernel not found

Make sure you've selected the correct Python interpreter in VS Code and installed ipykernel in your virtual environment.

### Package import errors

Ensure your virtual environment is activated and all packages are installed:

```powershell
uv sync
```
