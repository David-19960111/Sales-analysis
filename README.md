# Sales Data Analysis

This project analyzes randomly generated fictitious sales data, applying cleaning and visualization techniques.

## Project Structure

- `datos/`: Contains the input data.

- `notebooks/`: Contains exploratory analyses.

- `scripts/`: Scripts to automate tasks such as generating data or performing analysis.

- `visualizations/`: Folder to store generated graphics 


## How to execute the project

1 - Install the dependecies.

```bash
pip install -r requirements.txt
```

2 - Generate dummy data

```
python scripts/crear_datos.py
```

3 - Run the analysis

```
python scripts/analisis.py
```

## Requisitos

- Python 3.8 or higher
- Necessary libraries included in requirements.txt 

If you work with virtual environments, you can activate your environment before installing:

```bash
source venv/bin/activate #Linux
.\venv\Scripts\activate #Windows
pip install - r requirements.txt
```