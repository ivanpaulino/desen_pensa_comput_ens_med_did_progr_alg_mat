import math

print("--- Explorador de Trigonometria ---")

angulo_graus = float(input("Digite o ângulo em graus: "))

angulo_rad = math.radians(angulo_graus)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)

print(f"\nÂngulo: {angulo_graus}° | em Radianos: {angulo_rad:.4f} rad")
print(f"Seno({angulo_graus}°) = {seno:.4f}")
print(f"Cosseno({angulo_graus}°) = {cosseno:.4f}")

# Demonstração da Relação Fundamental: sen² + cos² = 1
relacao_fundamental = seno**2 + cosseno**2
print(f"Verificação (sen² + cos²): {relacao_fundamental:.1f}")