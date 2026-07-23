from engine import calcular_score

titulo = "Assistente de Qualidade"

empresa = "Taurus Armas"

score, palavras = calcular_score(titulo, empresa)

print()

print("Título:", titulo)

print("Empresa:", empresa)

print()

print("Score:", score)

print()

print("Palavras encontradas:")

for p in palavras:
    print(p)