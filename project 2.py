import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load COVID-19 dataset
covid_data = pd.read_csv('covid19_data.csv')

# Load World Bank Education dataset
education_data = pd.read_csv('world_bank_education.csv')
# Clean COVID-19 data
covid_data = covid_data.dropna(subset=['total_cases', 'total_deaths'])
covid_data['mortality_rate'] = covid_data['total_deaths'] / covid_data['total_cases'] * 100

# Clean Education data
education_data = education_data.dropna(subset=['tertiary_education_rate'])

# Merge datasets
merged_data = pd.merge(covid_data, education_data, on='country', how='inner')
plt.figure(figsize=(12, 8))
sns.scatterplot(data=merged_data, x='tertiary_education_rate', y='mortality_rate', 
                hue='continent', size='total_cases', sizes=(20, 500), alpha=0.7)

plt.title('COVID-19 Mortality Rate vs. Tertiary Education Rate by Country')
plt.xlabel('Tertiary Education Rate (%)')
plt.ylabel('COVID-19 Mortality Rate (%)')
plt.legend(title='Continent', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()

top_10_mortality = merged_data.nlargest(10, 'mortality_rate')

plt.figure(figsize=(12, 6))
sns.barplot(data=top_10_mortality, x='country', y='mortality_rate')
plt.title('Top 10 Countries with Highest COVID-19 Mortality Rates')
plt.xlabel('Country')
plt.ylabel('Mortality Rate (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()