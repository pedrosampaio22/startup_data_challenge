import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Read the data
df = pd.read_parquet('dados_sensores_5000.parquet')

def analyze_sector_consumption():
    # Previous sector analysis code remains the same
    sector_analysis = df.groupby('setor').agg({
        'energia_kwh': 'mean',
        'agua_m3': 'mean',
        'co2_emissoes': 'mean'
    }).round(2)
    
    print("\n=== Average Consumption by Sector ===")
    print(sector_analysis)
    
    for metric in ['energia_kwh', 'agua_m3', 'co2_emissoes']:
        fig = px.bar(sector_analysis, 
                    y=metric, 
                    title=f'Average {metric} by Sector',
                    labels={metric: metric.replace('_', ' ').title()})
        fig.show()

def identify_top_consumers():
    # Previous top consumers code remains the same
    metrics = ['energia_kwh', 'agua_m3', 'co2_emissoes']
    top_n = 5
    
    print("\n=== Top Consumers Analysis ===")
    for metric in metrics:
        print(f"\nTop {top_n} companies by {metric}:")
        print(df.nlargest(top_n, metric)[['empresa', 'setor', metric]])

def analyze_correlations():
    # New correlation analysis
    correlation_matrix = df[['energia_kwh', 'agua_m3', 'co2_emissoes']].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Between Consumption Metrics')
    plt.show()

def detect_outliers():
    # New outlier detection
    metrics = ['energia_kwh', 'agua_m3', 'co2_emissoes']
    
    for metric in metrics:
        df[f'{metric}_zscore'] = (df[metric] - df[metric].mean()) / df[metric].std()
        
        outliers = df[abs(df[f'{metric}_zscore']) > 3]
        print(f"\nOutliers in {metric}:")
        print(outliers[['empresa', 'setor', metric]].head())

def compare_sectors():
    # New statistical comparison
    sectors = df['setor'].unique()
    metrics = ['energia_kwh', 'agua_m3', 'co2_emissoes']
    
    for metric in metrics:
        print(f"\nKruskal-Wallis H-test for {metric}:")
        sector_groups = [group[metric].values for name, group in df.groupby('setor')]
        h_stat, p_value = stats.kruskal(*sector_groups)
        print(f'H-statistic: {h_stat:.2f}')
        print(f'p-value: {p_value:.4f}')

if __name__ == "__main__":
    # Execute all analyses
    print("=== Original Analysis ===")
    analyze_sector_consumption()
    identify_top_consumers()
    
    print("\n=== Correlation Analysis ===")
    analyze_correlations()
    
    print("\n=== Outlier Detection ===")
    detect_outliers()
    
    print("\n=== Statistical Comparison of Sectors ===")
    compare_sectors()