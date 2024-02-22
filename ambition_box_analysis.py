import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('companies.csv')

# Análise do dataset:
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

# Ajuste de colunas númericas (NÃO COMENTAR!)
columns_to_adjust = ['Total_reviews', 'Avg_salary', 'Interviews_taken', 'Total_jobs_available', 'Total_benefits']
def adjust_column_values(value):
    if 'k' in value:
        return float(value.replace('k', '')) * 1000
    elif value == '--':
        return np.nan
    else:
        return float(value)

for column in columns_to_adjust:
    df[column] = df[column].apply(adjust_column_values)

# Verificar se os valores foram ajustados corretamente
"""print(df.head())""" # Ultilize somente se necessário verificar se foi corretamente ajustado os valores!


# DESAFIOS:

# Desafio 1: Qual é a distribuição das classificações (ratings) das empresas? Existe algum padrão notável?

"""plt.figure(figsize=(10, 6))
plt.hist(df['Ratings'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribuição das Classificações das Empresas')
plt.xlabel('Classificação')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(df['Ratings'], shade=True, color='skyblue')
plt.title('Distribuição de Densidade das Classificações das Empresas')
plt.xlabel('Classificação')
plt.ylabel('Densidade')
plt.grid(True)
plt.show()"""


# Desafio 2: Quais são as áreas ou aspectos mais frequentemente destacados como altamente avaliados (Highly_rated_for) e criticamente avaliados (Critically_rated_for)?

"""highly_rated_counts = df['Highly_rated_for'].value_counts()
critically_rated_counts = df['Critically_rated_for'].value_counts()

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
highly_rated_counts.head(10).plot(kind='barh', color='skyblue')
plt.title('Áreas Altamente Avaliadas')
plt.xlabel('Número de Empresas')
plt.ylabel('Área')

plt.subplot(1, 2, 2)
critically_rated_counts.head(10).plot(kind='barh', color='salmon')
plt.title('Áreas Criticamente Avaliadas')
plt.xlabel('Número de Empresas')
plt.ylabel('Área')

plt.tight_layout()
plt.show()"""


# Desafio 3: Qual é a distribuição dos valores nas colunas Total_reviews, Interviews_taken, Total_jobs_available e Total_benefits?

"""columns_to_analyze = ['Total_reviews', 'Interviews_taken', 'Total_jobs_available', 'Total_benefits']
# histogramas
for column in columns_to_analyze:
    plt.figure(figsize=(8, 6))
    plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Distribuição de {column}')
    plt.xlabel('Valor')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()
print(df[columns_to_analyze].describe())"""


# Desafio 4: Analisar as correlações com matriz de correlação

"""numeric_columns = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_columns.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Matriz de Correlação')
plt.show()"""


# Desafio 5: Quais são as empresas com as melhores e piores avaliações médias?

"""ratings_mean = df.groupby('Company_name')['Ratings'].mean().reset_index()
ratings_mean_sorted = ratings_mean.sort_values(by='Ratings', ascending=False)

print("Empresas com as melhores avaliações médias:")
print(ratings_mean_sorted.head())
print("\nEmpresas com as piores avaliações médias:")
print(ratings_mean_sorted.tail())"""

# Desafio 6: Existe uma diferença significativa entre o número total de avaliações para as empresas mais bem avaliadas e as menos avaliadas?

"""ratings_mean = df.groupby('Company_name')['Ratings'].mean().reset_index()
ratings_mean_sorted = ratings_mean.sort_values(by='Ratings', ascending=False)

mean_total_reviews_top = df[df['Company_name'].isin(ratings_mean_sorted.head()['Company_name'])]['Total_reviews'].mean()
mean_total_reviews_bottom = df[df['Company_name'].isin(ratings_mean_sorted.tail()['Company_name'])]['Total_reviews'].mean()

print("Média do número total de avaliações para as empresas mais bem avaliadas:", mean_total_reviews_top)
print("Média do número total de avaliações para as empresas menos avaliadas:", mean_total_reviews_bottom)"""
