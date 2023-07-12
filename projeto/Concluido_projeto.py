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
mostrar_premium = bool(input("Mostrar Cursos Premium (S/N)?"))

if mostrar_premium == "N" or mostrar_premium == "n":
    mostrar_premium = False
else:
    mostrar_premium = True

num_das_categorias = num_das_categorias.split(",") #vai separar na lista num valou de uma sty, quebra no espaço, no padrão.
ncategorias = []

for elemento in num_das_categorias:
    numero = int(elemento.strip()) #uma função que remove espaço, antes ou depois
    ncategorias.append(numero) #deixa colocar mais elemento na lista no final dela

print(ncategorias)
print(f"Nome {nome}")
print(f"ID das Categorias: {ncategorias}")
print(f"Tempo: {tempo}")
print(f"Mostrar Premium?: {mostrar_premium}")

cursos = ["Introdução ao Wordpress",
          "Criador de Sites",
          "Introdução ao WooCommerce",
          "Afiliado de Sucesso",
          "Venda mais com WhatsApp Business e Google Meu Negócio",
          "Introdução ao Google Ads",
          "E-commerce e Vendas Online",
          "Canva: Design Fácil para Empreendedores",
          "Youtube para Iniciantes: como criar e crescer o seu canal",
          "Rede de Display e Youtube",
          "Desenvolvimento de Plugins para WordPress"
          ]

tempo = [95,
          25,
          35,
          85,
          75,
          150,
          140,
          120,
          85,
          335,
          160]

categorias_do_curso = [['wordpress', 'criação de sites'],
  ['criação de sites'],
  ['e-commerce', 'criação de sites', 'wordpress'],
  ['marketing digital', 'vendas'],
  ['marketing digital', 'vendas', 'google ads', 'negócios'],
  ['marketing digital', 'google ads'],
  ['e-commerce', 'vendas', 'negócios'],
  ['design', 'negócios'],
  ['youtube', 'criação de conteúdo'],
  ['marketing digital', 'google ads', 'youtube'],
  ['programação', 'wordpress']
]

gratuidade = [True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,]

categorias_selecionada = []
for n in ncategorias:
    categorias_selecionada.append(categorias[n].upper()) #deixa a letra maiuscúlo

print(f"Olá, {nome}, com base no seu perfil, achamos que você iria gostar dos seguintes cursos:")

for cat in categorias_selecionada:
    print(f"{cat}:")
    for linha in range(len(cursos)):
        if gratuidade[linha] or mostrar_premium:
            if (cat.lower() in categorias_do_curso[linha]
                and tempo[linha] <= tempo):
                 print(f"-{cursos[linha]}({tempo[linha]} min)")#(lower.()) = deixa as palavras minuscúlo
