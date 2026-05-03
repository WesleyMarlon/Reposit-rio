# Calculadora de Custo de Salgados

Projeto feito pra minha mãe calcular o custo real de cada receita de salgado.

## Como usar
1. Coloque o nome do produto que quer produzir
2. Digite: ingrediente, preço, peso total e quanto usou
3. Exemplo: 
   - Ingrediente = Trigo
   - Preço = 14
   - Peso = 5 → 5kg de trigo por R$14
   - Usou = 0.3 → foram usadas 300g

## Tecnologias
Python 3.10+ | Sem bibliotecas externas

dados = []
total = 0

produto = input ('O que quer produzir? ')

while True:
    print('-=-'*20)
    nome = input ('Ingrediente: ')
    
    try:
        preco = float(input('Preço: '))
        peso = float(input('Peso(kg/uni): '))
        usou = float(input('Quanto usou(kg/uni): '))
    except ValueError:
        print("Erro: digite apenas números.")
        continue

    if peso == 0:
        print(f"Erro: Peso não pode ser zero. O produto: '{nome}' não será adicionado.")
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
