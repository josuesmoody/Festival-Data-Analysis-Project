# Festival Data Analysis Project

## Overview
This project focuses on analyzing data from Belgian music festivals, exploring trends, artist participation, and the evolution of festivals over the years. The project is implemented using Python and organized into scripts for web scraping, data cleaning, and analysis, along with Jupyter Notebooks for interactive visualizations.

The results provide valuable insights into the growth of music festivals and the patterns of artist participation over time.

---

## Project Objectives
1. Scrape and clean data from well-known Belgian festivals such as:
   - **Rock Werchter**
   - **Pukkelpop**
2. Answer the following key questions:
   - Which festival has the longest-running history?
   - Who are the most frequent artists?
   - How has the number of artists evolved over the years?
   - Which artists appear in multiple festivals in the same year?
   - How have the headliners changed over time?
3. Present the findings with visualizations and concise summaries.

---

## Folder Structure
      ```bash
   . ├── data/ # Contains raw and cleaned data files 
   │ ├── festivals_data.json # Raw data scraped from festival websites 
   │ ├── cleaned_festivals_data.json # Cleaned and processed data 
   │ ├── werchter_data.json # Additional data specific to Rock Werchter 
   ├── notebooks/ # Jupyter Notebooks for data analysis 
   │ ├── analysis_festivals.ipynb # Main notebook for data analysis 
   │ ├── werchter_start.ipynb # Initial scraping and exploration 
   ├── scripts/ # Python scripts for scraping and cleaning 
   │ ├── scraping_festivals.py # Script for web scraping 
   │ ├── cleaning_data.py # Script for data cleaning 
   ├── results/ # Contains final output files 
   │ ├── festival_analysis_summary.md # Markdown file summarizing insights 
   ├── venv/ # Python virtual environment 
   ├── .gitignore # Git ignore file 
   ├── requirements.txt # Python dependencies 
   └── README.md # Project documentation


---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage

1. Scraping Data:
   - Run the scraping script to collect raw festival data:
   ```bash
   python scripts/scraping_festivals.py

2. Cleaning Data:
   - Process and clean the scraped data:
   ```bash
   python scripts/cleaning_data.py

3. Data Analysis:
   - Open the main analysis notebook:
   ```bash
   jupyter notebook notebooks/analysis_festivals.ipynb

4. Review Results:
   - View the insights and visualizations directly in the notebook or check the markdown summary:
   ```bash
   results/festival_analysis_summary.md

## Results

The results of the analysis are saved in:

- Visualizations: Available in notebooks/analysis_festivals.ipynb.
- Summary: Detailed markdown summary in results/festival_analysis_summary.md.

## Contact

For further inquiries or feedback:

- Name: Josué Elías Santana
- Email: r1035131@student.thomasmore.be
- GitHub: https://github.com/josuesmoody