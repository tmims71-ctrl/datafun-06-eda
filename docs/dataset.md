# Dataset Information

## Car Crashes Dataset

### Overview

The **car_crashes** dataset is a built-in dataset from the Seaborn library containing U.S. state-level statistics on fatal automobile accidents and related factors.

### Source

- **Origin**: Seaborn built-in datasets
- **GitHub**: [https://github.com/mwaskom/seaborn-data/blob/master/car_crashes.csv](https://github.com/mwaskom/seaborn-data/blob/master/car_crashes.csv)
- **Local Copy**: `data/car_crashes.csv`

### Dataset Statistics

| Property | Value |
|----------|-------|
| **Rows** | 51 |
| **Columns** | 8 |
| **Missing Values** | 0 |
| **Duplicate Rows** | 0 |

### Column Descriptions

| Column | Type | Description |
|--------|------|-------------|
| **abbrev** | string | State abbreviation (e.g., AL, AK, AZ) |
| **total** | float | Number of fatal collisions per billion miles driven |
| **speeding** | float | Percentage of fatal collisions where speeding was a factor |
| **alcohol** | float | Percentage of fatal collisions involving alcohol impairment |
| **not_distracted** | float | Percentage of fatal collisions where the driver was not distracted |
| **no_previous** | float | Percentage of drivers involved in fatal collisions with no previous accidents |
| **ins_premium** | float | Car insurance premiums (annual, in dollars) |
| **ins_losses** | float | Losses incurred by insurance companies for collisions per insured driver (annual, in dollars) |

## Data Quality

### Completeness

✅ **No missing values** - All 51 states have complete data across all 8 columns.

✅ **No duplicates** - Each state appears exactly once in the dataset.

### Data Types

All numeric columns are stored as `float64` types, while the state abbreviation is stored as `object` (string) type.

### Summary Statistics

**Total Fatal Collisions** (per billion miles):
- **Mean**: ~15.79
- **Std Dev**: ~4.12
- **Min**: ~5.90
- **Max**: ~23.90
- **Range**: ~18.00

These statistics show significant variability in crash rates across U.S. states.

## Usage in Analysis

This dataset is ideal for:

- **Exploratory Data Analysis (EDA)**: Understanding patterns and distributions
- **Correlation Studies**: Identifying relationships between crash factors
- **Comparative Analysis**: Comparing states on safety metrics
- **Visualization Practice**: Creating charts, plots, and heatmaps
- **Statistical Analysis**: Computing means, medians, standard deviations

## Why This Dataset?

The car_crashes dataset was chosen because:

1. ✅ **Clean**: No missing values or data quality issues
2. ✅ **Manageable Size**: 51 rows is perfect for learning
3. ✅ **Relevant**: Traffic safety is an important public policy topic
4. ✅ **Multiple Variables**: 8 columns provide rich analysis opportunities
5. ✅ **Pre-installed**: Available directly through Seaborn
6. ✅ **Well-documented**: Clear variable definitions and source

## Accessing the Data

### In Python

```python
import seaborn as sns
import pandas as pd

# Load from Seaborn
car_df = sns.load_dataset('car_crashes')

# Or load from local CSV
car_df = pd.read_csv('../data/car_crashes.csv')
```

### Preview

```python
# View first few rows
car_df.head()

# Get dataset info
car_df.info()

# View summary statistics
car_df.describe()
```
