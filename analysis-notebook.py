# Festival Data Analysis Project
# Part 2: Data Analysis and Visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go

# Load the cleaned data
df = pd.read_csv('festival_data_clean.csv')

# 1. Festival History Analysis
def analyze_festival_history():
    """
    Analyzes which festival has the longest history and identifies any gaps
    """
    festival_years = df.groupby('festival')['year'].agg(['min', 'max'])
    festival_years['duration'] = festival_years['max'] - festival_years['min']
    
    # Check for gaps in operations
    all_years = set(range(df['year'].min(), df['year'].max() + 1))
    festival_gaps = {}
    
    for festival in df['festival'].unique():
        festival_years = set(df[df['festival'] == festival]['year'])
        gaps = sorted(all_years - festival_years)
        if gaps:
            festival_gaps[festival] = gaps
    
    return festival_years, festival_gaps

# 2. Lineup Size Evolution
def analyze_lineup_evolution():
    """
    Analyzes how festival lineups have evolved over time
    """
    lineup_sizes = df.groupby(['festival', 'year']).size().reset_index(name='num_artists')
    
    # Create line plot
    plt.figure(figsize=(12, 6))
    for festival in lineup_sizes['festival'].unique():
        festival_data = lineup_sizes[lineup_sizes['festival'] == festival]
        plt.plot(festival_data['year'], festival_data['num_artists'], label=festival, marker='o')
    
    plt.title('Evolution of Festival Lineup Sizes')
    plt.xlabel('Year')
    plt.ylabel('Number of Artists')
    plt.legend()
    plt.grid(True)
    
    return lineup_sizes

# 3. Most Frequent Artists
def analyze_frequent_artists(min_appearances=5):
    """
    Identifies artists who have performed most frequently
    """
    artist_counts = df['artist'].value_counts()
    frequent_artists = artist_counts[artist_counts >= min_appearances]
    
    # Create bar plot
    plt.figure(figsize=(12, 6))
    frequent_artists.plot(kind='bar')
    plt.title(f'Artists with {min_appearances}+ Festival Appearances')
    plt.xlabel('Artist')
    plt.ylabel('Number of Appearances')
    plt.xticks(rotation=45)
    
    return frequent_artists

# 4. Cross-Festival Appearances
def analyze_cross_festival_appearances(year):
    """
    Analyzes artists who performed at multiple festivals in a given year
    """
    year_data = df[df['year'] == year]
    artists_by_festival = year_data.groupby('artist')['festival'].agg(list)
    multiple_festivals = artists_by_festival[artists_by_festival.str.len() > 1]
    
    return multiple_festivals

# 5. Artist Comebacks
def analyze_comebacks(min_gap_years=5):
    """
    Identifies artists with significant gaps between performances
    """
    comebacks = []
    
    for artist in df['artist'].unique():
        artist_years = sorted(df[df['artist'] == artist]['year'].unique())
        if len(artist_years) > 1:
            gaps = np.diff(artist_years)
            max_gap = gaps.max()
            if max_gap >= min_gap_years:
                comebacks.append({
                    'artist': artist,
                    'gap_years': max_gap,
                    'first_appearance': artist_years[0],
                    'comeback_year': artist_years[np.argmax(gaps) + 1]
                })
    
    comeback_df = pd.DataFrame(comebacks)
    return comeback_df.sort_values('gap_years', ascending=False)

# Main analysis
def main():
    print("Analyzing festival history...")
    festival_years, gaps = analyze_festival_history()
    print("\nFestival Duration:")
    print(festival_years)
    print("\nGaps in Operations:")
    for festival, gap_years in gaps.items():
        print(f"{festival}: {gap_years}")
    
    print("\nAnalyzing lineup evolution...")
    lineup_evolution = analyze_lineup_evolution()
    
    print("\nAnalyzing frequent artists...")
    frequent_artists = analyze_frequent_artists()
    
    print("\nAnalyzing cross-festival appearances for 2023...")
    cross_festival = analyze_cross_festival_appearances(2023)
    
    print("\nAnalyzing artist comebacks...")
    comebacks = analyze_comebacks()
    
    # Generate summary report
    generate_summary_report(festival_years, lineup_evolution, frequent_artists, cross_festival, comebacks)

def generate_summary_report(festival_years, lineup_evolution, frequent_artists, cross_festival, comebacks):
    """
    Generates a markdown summary report of the findings
    """
    report = """
# Festival Data Analysis Summary Report

## Key Findings

### 1. Festival History
- The longest-running festival is {longest_festival} with {longest_duration} years of operation
- {num_gaps} festivals had gaps in their operation during the analyzed period

### 2. Lineup Evolution
- The average number of artists per festival has {trend} over time
- {largest_festival} consistently features the largest lineups

### 3. Artist Frequency
- {top_artist} has made the most festival appearances ({num_appearances} times)
- {num_frequent} artists have performed 5 or more times

### 4. Cross-Festival Appearances
- In 2023, {cross_fest_count} artists performed at multiple Belgian festivals
- This suggests significant collaboration between festival organizers

### 5. Notable Comebacks
- {comeback_artist} made the most remarkable comeback, returning after {gap_years} years
- We identified {comeback_count} significant artist comebacks (gap of 5+ years)

## Recommendations
1. {rec1}
2. {rec2}
3. {rec3}

## Methodology
This analysis was conducted using Python, analyzing data scraped from festival websites. 
The data covers performances from {start_year} to {end_year}.
"""
    
    # Save report
    with open('festival_analysis_report.md', 'w') as f:
        f.write(report)

if __name__ == "__main__":
    main()