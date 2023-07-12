nome = str(input("Como gostaria de ser chamado(a):\n"))
categorias = ["Wordpress",
              "Criação de Site",
              "E-commerce",
              "Marketing Digital",
              "Vendas",
              "Google Ads",
              "Design",
              "Negócios",
              "Youtube",
              "Criação de Conteúdo",
              "Programação"]
for i in range (len(categorias)):
    print(f"{i}. {categorias[i]}")

num_das_categorias = float(input("Digite o número dos assuntos do seu interesse(use vírgulas):\n"))
tempo = float(input("Quanto tempo gostaria de estudar? (min)\n"))
gratuidade = bool(input("Mostrar apenas gratuitos (S/N)?"))

if gratuidade == "N" or gratuidade == "n":
    gratuidade = False
else:
    gratuidade = True

num_das_categorias = num_das_categorias.split(",") #vai separar na lista num valou de uma sty, quebra no espaço, no padrão.
ncategorias = []

for elemento in num_das_categorias:
    numero = int(elemento.strip()) #uma função que remove espaço, antes ou depois
    ncategorias.append(numero) #deixa colocar mais elemento na lista no final dela

print(ncategorias)
print(f"Nome {nome}")
print(f"ID das Categorias: {ncategorias}")
print(f"Tempo: {tempo}")
print(f"Gratuidade?: {gratuidade}")