dados = []
total = 0

produto = input ('O que quer produzir? ')

while True:
    print('-=-'*20)
    nome = input ('Ingrediente: ')
    
    try:
        preco = float(input('Preço R$: '))
        peso = float(input('Peso(kg/uni): '))
        usou = float(input('Quanto usou(kg/uni): '))
    except ValueError:
        print("Nessa parte digite apenas números")
        continue

    if peso == 0:
        print(f"Opa, peso não pode ser zero. Tenta de novo com o peso total do pacote.")
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
