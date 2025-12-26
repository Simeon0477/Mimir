from core.statistics import *

x = [1.25, 2, 11, 15, 7.5, 8]
y = [2.5, 12, 1.1, 8.8, 14, 8.2]

data = {
    "age" : [20, 17, 18, 25, 40],
    "taille" : [1.75, 1.65, 1.9, 1.55, 2.02],
    "poids" : [62.5, 53, 78.9, 48, 85]
}

#Test de la moyenne
print(f"Moyenne : {mean(x):.3f}", end="\n\n")

#Test de la variance
# - Sur tout la population
print(f"Variance sur toute la population : {variance(x, False):.3f}", end="\n")
# - Sur un échantillon
print(f"Variance sur un échantillon: {variance(x[1:-2]):.3f}", end="\n\n")

#Test de l'écart-type
# - Sur tout la population
print(f"Ecart-type sur toute la population : {std_dev(x, False):.3f}", end="\n")
# - Sur un échantillon
print(f"Ecart-type sur un échantillon: {std_dev(x[1:-2]):.3f}", end="\n\n")

#Test de la covariance
print(f"Covariance : {covariance(x, y):.3f}", end="\n\n")

#Test de la correlation
print(f"Correlation : {correlation(x, y):.3f}", end="\n\n")

#Test de la matrice de  correlation
corr_mat = correlation_matrix(data)
print("-----  Matrice de Correlation  ----- ")
for key in corr_mat.keys():
    print(f"Correlation {key} : {corr_mat[key]:0.2f}")
print("\n")