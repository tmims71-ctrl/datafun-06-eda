# Notebook Analysis

## tmims_eda.ipynb

The main analysis notebook is located at: `notebooks/tmims_eda.ipynb`

## Notebook Structure

The notebook is organized into 10 main sections that guide you through a complete exploratory data analysis workflow.

### Section 0: Introduction

**Intro to Jupyter Notebooks**
- Basic notebook usage and keyboard shortcuts
- Cell types (Markdown vs Code)
- Kernel selection guidance

**Intro to EDA**
- Purpose and goals of exploratory data analysis
- Understanding data structure, quality, and relationships

### Section 1: Project Setup and Imports

All necessary libraries are imported at the top:

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

Display options are configured for optimal data viewing.

### Section 2: Load the Data

The car_crashes dataset is loaded from the local CSV file:

```python
car_df = pd.read_csv("../data/car_crashes.csv")
```

Initial data preview with `.head()` displays the first few rows.

### Section 3: Inspect Data Shape and Structure

Key checks performed:
- **Shape**: 51 rows × 8 columns
- **Data Types**: `.info()` shows column types and non-null counts
- **Column Names**: List all variable names

### Section 4: Data Quality Checks

Quality validation includes:
- **Missing Values**: Check for null values per column
- **Duplicates**: Verify uniqueness of records

Result: ✅ No missing values or duplicates found

### Section 5: Create Clean View

A clean DataFrame is created by removing any rows with missing values (though none exist in this dataset):

```python
car_clean = car_df.dropna()
```

This ensures downstream analysis uses only complete records.

### Section 6: Descriptive Statistics

Statistical summary generated using:
- **Pandas**: `.describe()` for all numeric columns
- **NumPy**: Manual calculation of mean, std dev, min, max, and range for specific columns

Key findings:
- Mean total crashes: ~15.79 per billion miles
- Significant variation across states (std dev ~4.12)

### Section 7: Correlation Matrix

**Correlation Analysis:**
- Compute correlation matrix between all numeric variables
- Visualize with Seaborn heatmap showing correlation coefficients

**Key Insights:**
- Identifies which factors are most strongly associated with total crashes
- Reveals relationships between contributing factors (speeding, alcohol, distraction)

### Section 8: Visualizations

**Scatter Plot**: Speeding vs Total Crashes
- Shows relationship between speeding percentage and crash rates
- Helps identify if speeding is a major factor

**Histogram**: Alcohol-Related Crash Distribution
- Displays frequency distribution of alcohol involvement
- Includes KDE (kernel density estimate) curve for smooth distribution

### Section 8b: Additional Charts

**Pairplot:**
- Matrix of scatter plots between all numeric variables
- Diagonals show distributions
- Reveals multivariate relationships at a glance

**Bar Chart**: Top 15 States by Total Crashes
- Ranks states with highest fatal collision rates
- Highlights geographic variations in traffic safety

**Boxplot**: Distribution of Numeric Metrics
- Shows spread, median, quartiles, and outliers for all variables
- Useful for identifying unusual states or extreme values

### Section 9: Reminder

A note to ensure all cells are executed before saving and pushing to GitHub, ensuring outputs are captured.

### Section 10: Conclusion

**Key Findings:**
1. Dataset is clean and reliable (no missing values/duplicates)
2. Significant state-to-state variability in crash rates
3. Correlation analysis reveals relationships between factors
4. Visual analysis identifies patterns and outliers

**Implications:**
- Region-specific traffic safety interventions may be more effective
- High-risk states could benefit from targeted programs

**Next Steps:**
- Incorporate additional variables (population density, infrastructure, weather)
- Deeper analysis of state-level traffic safety laws
- Predictive modeling for crash risk factors

## Execution Results

All 26 code cells have been successfully executed with outputs including:

- ✅ Text output (print statements, statistics)
- ✅ DataFrames (tables with data)
- ✅ Visualizations (PNG images of plots)

## Running the Notebook

### In VS Code
1. Open `notebooks/tmims_eda.ipynb`
2. Select the `.venv` Python interpreter
3. Click "Run All" or execute cells individually

### In JupyterLab
```powershell
uv run jupyter lab notebooks/tmims_eda.ipynb
```

## Best Practices Demonstrated

✅ **Single Imports Section** - All libraries imported at the top  
✅ **Markdown Documentation** - Each section has explanatory text  
✅ **Logical Flow** - Analysis proceeds from basic to complex  
✅ **Multiple Visualizations** - Various chart types for different insights  
✅ **Statistical Rigor** - Descriptive stats and correlation analysis  
✅ **Data Quality Checks** - Explicit validation of data integrity  
✅ **Clear Conclusions** - Summary of findings and implications  
✅ **Professional Presentation** - Clean code, clear narratives  

## Analysis Highlights

### Visualizations Created

1. **Correlation Heatmap** - Shows relationships between all variables
2. **Scatter Plot** - Speeding vs total crashes
3. **Histogram with KDE** - Distribution of alcohol-related crashes
4. **Pairplot** - Comprehensive multivariate view
5. **Bar Chart** - Top states by crash rate
6. **Boxplot** - Distribution comparison across metrics

### Statistical Methods Applied

- Descriptive statistics (mean, median, std dev, min, max, range)
- Correlation analysis (Pearson correlation coefficients)
- Distribution analysis (histograms, KDE)
- Outlier detection (boxplots)

### Data Story

The notebook tells a coherent story about U.S. traffic safety:

1. **Setup**: Introduce the problem and data
2. **Validate**: Ensure data quality
3. **Explore**: Examine distributions and relationships
4. **Visualize**: Create informative plots
5. **Conclude**: Summarize findings and suggest actions

This demonstrates professional data analysis skills and effective communication.
