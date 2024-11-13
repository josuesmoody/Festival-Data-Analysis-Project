# Festival Data Analysis Project

## Overview
This project analyzes lineup data from major Belgian music festivals including Rock Werchter, Pukkelpop, Graspop Metal Meeting, and Tomorrowland. The analysis includes historical trends, artist appearances, and festival evolution over time.

## Project Structure
- `notebooks/`: Jupyter notebooks for data collection and analysis
- `data/`: Raw and processed data files
- `src/`: Source code for scraping, cleaning, and analysis
- `tests/`: Unit tests
- `results/`: Output figures and reports

## Setup
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Chrome WebDriver for Selenium (required for web scraping)

## Usage
1. Run data collection:
```bash
jupyter notebook notebooks/01_data_collection.ipynb
```

2. Run analysis:
```bash
jupyter notebook notebooks/02_data_analysis.ipynb
```

## Data Sources
- Rock Werchter: https://www.rockwerchter.be
- Pukkelpop: https://www.pukkelpop.be
- Graspop Metal Meeting: https://www.graspop.be
- Tomorrowland: https://www.tomorrowland.com

## Analysis Features
- Festival timeline analysis
- Lineup size evolution
- Artist frequency analysis
- Cross-festival appearances
- Artist comeback analysis
- Genre evolution analysis
- Interactive visualizations

## Results
Results are stored in the `results/` directory, including:
- Visualization figures
- Analysis reports
- Data summaries

## Contributing
This is a student project for the Data Science course 2024-2025.

## License
This project is created for educational purposes.