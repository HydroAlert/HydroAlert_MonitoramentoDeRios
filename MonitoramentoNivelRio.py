# Monitoramento do nível do rio - Franco da Rocha (SP)
import numpy as np
import matplotlib.pyplot as plt

# 1. dados simulados do nível do rio ao longo de 10 dias consecutivos de chuva
dias = list(range(1, 11)) # domínio: dias inteiros de 1 a 10
nivel_rio = [1.0, 1.3, 1.8, 2.2, 2.6, 2.9, 3.1, 2.7, 2.3, 1.9] # níveis em metros (imagem aproximada entre 1 e 3.1m)

# 2. ajuste da função polinomial (grau 3 para curva suave)
coeficientes = np.polyfit(dias, nivel_rio, 3)
polinomio = np.poly1d(coeficientes)

# 3. análise do modelo
dominio = (dias[0], dias[-1])
imagem_min = min(nivel_rio)
imagem_max = max(nivel_rio)

print("=== Análise do Modelo de Monitoramento do Rio ===\n")
print(f"Domínio da função: dias de chuva consecutivos, de {dominio[0]} a {dominio[1]} (inteiros).")
print(f"Imagem da função: níveis do rio variando aproximadamente de {imagem_min:.2f}m a {imagem_max:.2f}m.\n")

# Encontrar o nível máximo e o dia correspondente
max_nivel = max(nivel_rio)
dia_max = dias[nivel_rio.index(max_nivel)]
print(f"Nível máximo registrado: {max_nivel:.2f} metros no dia {dia_max}.\n")

# identificar dias com risco de transbordamento (> 2.0 m)
limite_risco = 2.0
dias_risco = [dia for dia, nivel in zip(dias, nivel_rio) if nivel > limite_risco]
print("Dias com risco de transbordamento (nível > 2.0 m):")

for dia in dias_risco:
    print(f" - Dia {dia}: {nivel_rio[dia-1]:.2f} metros")

print("\nO modelo polinomial ajustado permite prever o comportamento do nível do rio para os dias entre 1 e 10,")
print("facilitando a emissão antecipada de alertas para planejamento de evacuação e ações preventivas.\n")


# 4. visualização gráfica
plt.figure(figsize=(10, 6))
plt.plot(dias, nivel_rio, 'bo', label='Dados simulados (nível real)')
plt.plot(dias, polinomio(dias), 'r-', label='Função polinomial ajustada (previsão)')
plt.axhline(limite_risco, color='orange', linestyle='--', label='Limite de segurança (2.0 m)')
plt.axhline(3.0, color='red', linestyle='--', label='Transbordamento crítico (3.0 m)')
plt.xlabel("Dias consecutivos de chuva")
plt.ylabel("Nível do Rio (m)")
plt.title("Monitoramento do Nível do Rio - Franco da Rocha (SP)")
plt.legend()
plt.grid(True)
plt.xticks(dias) # mostrar todos os dias no eixo x
plt.show()