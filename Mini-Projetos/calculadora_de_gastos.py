dados = []
total = 0
print('-=-'*20)
produto = input ('O que quer produzir? ')

while True:
    print('-=-'*20)
    nome = input ('Ingrediente: ')
    if not nome:
        print("Nome não pode ser vazio")
        continue
    
    try:
        preco = float(input('Preço R$: '))
        peso = float(input('Peso(kg/uni): '))
        usou = float(input('Quanto usou(kg/uni): '))
    except ValueError:
        print("Nessa parte digite apenas números")
        continue

    if preco < 0 or peso <= 0 or usou < 0:
        print(f"Opa, usa só números positivos aqui. O '{nome}' não será adicionado.")
        continue
    if peso == 0:
        print(f"Opa, peso não pode ser zero. O '{nome}' não será adicionado.")
        continue

    media = (preco / peso)
    final = (media * usou)
    total += final


    lista = {
        'nome': nome,
        'final': final,
        'usou': usou
    }
    dados.append(lista)

    res = input ('Quer continuar? [S/N]: ').upper()
    while res not in ['S','N']:
        res = input ('Quer continuar? [S/N]: ').upper()
    if res == 'N':
        break


for lista in dados:
    print('-=-'*20)
    print(f"Usando {lista['usou']}(kg/uni) de {lista['nome']} custou no total R$ {lista['final']:.2f}")
print('-=-'*20)


print('-=-'*20)
print (f'O produto "{produto}" custou no total "{total:.2f}" para ser feito.')
print (f'Igredientes: ')
for lista in dados:
    print (f"• {lista['nome']}")
print('-=-'*20)

lucro = input('Quer calcular preço de venda? [S/N]: ').upper()
if lucro == 'S':
    margem = float(input('Qual % de lucro quer ter? Ex: 100 pra dobrar: '))
    rende = int(input('Quantos produtos a receita rende? '))
    
    preco_venda_total = total * (1 + margem/100)
    preco_unidade = preco_venda_total / rende
    total_unidade = total / rende
    
    print(f'\nCusto da receita: R$ {total:.2f}')
    print(f'Venda tudo por: R$ {preco_venda_total:.2f}')
    print(f'Preço por unidade: R$ {preco_unidade:.2f}')
    print(f'Lucro real total de R$ {preco_venda_total - total:.2f}')
    print(f'Lucro real por unidade de R$ {preco_unidade - total_unidade:.2f}')