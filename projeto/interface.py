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
