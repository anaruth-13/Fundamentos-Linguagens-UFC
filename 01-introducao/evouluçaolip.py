import matplotlib.pyplot as plt

# Dados dos tópicos e anos aproximados
topicos = [
    "Pseudocódigos", "Fortran", " Lisp",
    "ALGOL 60", "COBOL", "Basic", "PL/I", "APL e SNOBOL", "SIMULA 67", "ALGOL 68",
    "Descendentes de ALGOLs", "Prolog", "Ada", "Smalltalk", "C++", "Python", "Java", "Linguagens de scripting",
    "C#", "Linguagens híbridas de marcação-programação"
]
anos = [
    1950, 1954, 1958, 
    1960, 1960, 1964, 1964, 1966, 1967, 1968, 
    1970, 1972, 1980, 1983, 1990, 1991, 1994, 1995, 
    2000, 2005
]

# Criar o gráfico
plt.figure(figsize=(12, 6))
plt.plot(anos, range(len(topicos)), marker='o', linestyle='-', color='b')

# Adicionar rótulos
for i, topico in enumerate(topicos):
    plt.text(anos[i], i, topico, fontsize=8, ha='right')

# Configurar o gráfico
plt.title("Evolução das Linguagens de Programação", fontsize=16)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Linguagens", fontsize=12)
plt.yticks(range(len(topicos)), [])
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

# Mostrar o gráfico
plt.show()


