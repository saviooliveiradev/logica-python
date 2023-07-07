cursos = ["Introdução ao  Wordpress", 
          "Criador de Sites",
          "Afiliado de Sucesso",
          "Introdução ao Google Ads",
          "E-commerce e Vendas Online",
          "Desenvolvimento de Plugins para Wordpress"] #a contagem da lista começa em zero 

print(cursos)

print(f"A lista de cursos tem {len(cursos)} cursos")  
indice = int(input("Digite um número:\n"))

if indice < len(cursos):
    # estamos seguros
    print(f'O curso no índice {indice} é o "{cursos[indice]}"')
else:
    print(f"O índide {indice} não é váçido")

print(cursos)
print(f"A lista de cursos tem {len(cursos)} cursos")  
