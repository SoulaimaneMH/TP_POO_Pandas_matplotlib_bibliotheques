import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv(r"C:\Users\HP\Downloads\A_0\POO\Numpy-Matplot-Pandas\qualite_industrielle.csv")
print(df)
print(df.columns)
print(df["Cout_Non_Qualite_DH"])
print(df.shape)
print(df.head(5))
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

#-------------------Coût de Non-Qualité par Ligne---------------------------------------

cout_par_ligne = df.groupby('Ligne_Production')['Cout_Non_Qualite_DH'].sum()
lignes = cout_par_ligne.index
couts = cout_par_ligne.values

plt.figure(figsize=(8, 5))
bars = plt.bar(lignes, couts, color='#4682B4', edgecolor='black', alpha=0.85)


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 100, f'{int(yval)} DH', ha='center', va='bottom', fontsize=9)

plt.title('1. Coût Total de Non-Qualité par Ligne de Production (DH)', fontsize=12, fontweight='bold')
plt.xlabel('Ligne de Production', fontsize=10)
plt.ylabel('Coût Total (DH)', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

#----------------------------------Température vs Taux de Défauts--------------------------------
conforme = df[df['Resultat'] == 'Conforme']
non_conforme = df[df['Resultat'] == 'Non conforme']

plt.figure(figsize=(8, 5))
plt.scatter(conforme['Temperature_C'], conforme['Taux_Defauts_pct'], color='green', marker='o', label='Conforme', s=60, alpha=0.8)
plt.scatter(non_conforme['Temperature_C'], non_conforme['Taux_Defauts_pct'], color='red', marker='x', label='Non conforme', s=60, alpha=0.8)

plt.title('2. Corrélation entre la Température (°C) et le Taux de Défauts (%)', fontsize=12, fontweight='bold')
plt.xlabel('Température (°C)', fontsize=10)
plt.ylabel('Taux de Défauts (%)', fontsize=10)
plt.legend(title='Résultat')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


#------------------------------Distribution du Poids par Produit---------------------------------------
produits = np.sort(df['Produit'].unique())
data_poids = [df[df['Produit'] == p]['Poids_g'].to_numpy() for p in produits]

plt.figure(figsize=(8, 5))
box = plt.boxplot(
    data_poids, 
    tick_labels=produits, 
    patch_artist=True,
    boxprops=dict(facecolor='#A6C8E0', color='black'),
    medianprops=dict(color='red', linewidth=2)
)

# Ligne cible de référence à 500g
plt.axhline(500, color='gray', linestyle='--', label='Poids cible (500g)')

plt.title('3. Distribution et Dispersion du Poids par Produit (g)', fontsize=12, fontweight='bold')
plt.xlabel('Produit', fontsize=10)
plt.ylabel('Poids (g)', fontsize=10)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
