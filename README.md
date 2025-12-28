# About

This repository will contain solution to exercises and exploration code related to LinkedIn Learning course made by [Chris Bruehl](https://www.linkedin.com/in/chrisbruehl/) from [Maven Analytics](https://mavenanalytics.io/), available at [Data Analysis with Python and Pandas](https://www.linkedin.com/learning/data-analysis-with-python-and-pandas)

# Dependency management

For dependency management, Poetry will be the tool selected due to its ease of configuration and flexible use cases (either for package creation or for just providing environment management for notebooks).

The first libraries installed to this repository were the following ones:

- numpy: https://numpy.org/
- pandas: https://pandas.pydata.org/docs/user_guide/index.html
- marimo: https://marimo.app/
- prek:
  - https://github.com/j178/prek?tab=readme-ov-file#installation
  - https://prek.j178.dev/quickstart/
  - https://github.com/pre-commit/pre-commit-hooks

Numpy and Pandas were added as they are the center of this course content. Marimo was selected as the notebook of choice - reactive, beautiful and helpful UI, notebook/script quick switch possible - and prek as a pre-commit tool to keep a unified code styling.

# Section 01: NumPy primer

This section syllabus involved:

1. NumPy arrays and array properties
2. Array creation
3. Random Number Generation
4. Indexing and slicing arrays
5. Array operations
6. Filtering arrays and modifying array values
7. The where() function
8. Array aggregation
9. Array functions
10. Sorting arrays
11. Vectorization
12. Broadcasting

# Section 02: Pandas Series

This section syllabus involved:

1. Series basics
2. pandas data types and type conversion
3. The series index and custom indices
4. The .iloc accessor
5. The .loc accessor
6. Duplicate index values and resetting the index
7. Filtering series and logical tests
8. Sorting series
9. Numeric series operations
10. Text series operations
11. Numerical series aggregation
12. Categorical series aggregation
13. Missing data representation in Pandas
14. Identifying missing data
15. Fixing missing data
16. Applying custom functions to series
17. pandas where() vs NumPy where()
