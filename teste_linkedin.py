from linkedin import buscar_vagas

vagas = buscar_vagas()

print("\n========== RESULTADO ==========\n")

for vaga in vagas:

    print("Título      :", vaga["titulo"])
    print("Empresa     :", vaga["empresa"])
    print("Localização :", vaga["localizacao"])
    print("Link        :", vaga["link"])
    print("-" * 70)

print(f"\nTotal coletado: {len(vagas)}")