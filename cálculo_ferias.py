import math



#Essas duas váriaveis recebem o valor inteiro.
diaria_da_casa = int(input('Digite o valor da diária: '))
taxa_de_limpeza = int(input('Digite o valor da taxa de limpeza: '))

#Criando uma lista para receber os valores das notas do mercado e derivados de alimentação e armazena dentro dela esses valores.
gasto_com_alimentacao = []

#Enquanto não finalizar as notas escrevendo 'Fim' deverá colocar todos os valores em sequência.
while True:
  gasto_com_mercado = input('Digite os valores das compras do mercado, após finalizar, encerre digitando "Fim" ')
  if gasto_com_mercado == 'fim':
    break
  gasto_com_alimentacao.append(float(gasto_com_mercado))

#recebe a quantidade de pessoas na casa.
pessoas_na_casa = int(input('Quantidade de pessoas na casa? '))

#somará o total gasto, e armazenará na variável essa soma.
total_gasto_com_alimentacao = sum(gasto_com_alimentacao) / pessoas_na_casa

#essas variáveis irão receber e fazer os cálculos com base nas informações colocadas pelo usuário.
valor_total_das_diarias = diaria_da_casa * pessoas_na_casa
valor_por_pessoa = ((diaria_da_casa * pessoas_na_casa) / pessoas_na_casa) 
valor_taxa_de_limpeza_por_pessoa = taxa_de_limpeza / pessoas_na_casa
valor_total_por_pessoa_com_taxa_de_limpeza = valor_por_pessoa + valor_taxa_de_limpeza_por_pessoa
valor_1_pessoa = total_gasto_com_alimentacao + valor_total_por_pessoa_com_taxa_de_limpeza
valor_2_pessoas = (total_gasto_com_alimentacao + valor_total_por_pessoa_com_taxa_de_limpeza) * 2
valor_3_pessoas = (total_gasto_com_alimentacao + valor_total_por_pessoa_com_taxa_de_limpeza) * 3 
valor_4_pessoas = (total_gasto_com_alimentacao + valor_total_por_pessoa_com_taxa_de_limpeza) * 4

#retorna os valores ao usuário já com a solução.

#Custo total das diárias.
print(f'Valor total de diarias é: {valor_total_das_diarias:.2f}')

#Custo da taxa limpeza.
print(f'Valor da taxa de limpeza é: {taxa_de_limpeza}')

#Custo Total gasto com alimentação.
print(f'Valor total do mercado ficou: R$ {total_gasto_com_alimentacao:.2f}')

#Valor já divido entre os inquilinos.
print(f'Sendo o valor por pessoa referente a taxa de limpeza R$ {valor_taxa_de_limpeza_por_pessoa:.2f}')

#valor da diária.
print(f'O valor somente da diaria por pessoa é: R$ {valor_por_pessoa:.2f}')

#Custo total que todos deverão pagar unitariamente.
print(f'Cada pessoa de férias na casa, deverá pagar ao Locador R$ {valor_1_pessoa:.2f}')

#Custo pra uma pessoa.
print(f'O valor fica definido pela quantidade de pessoas da sua família na casa.\n"Uma" pessoa pagará R$: {valor_1_pessoa:.2f}')

#Custo para duas pessoas.
print(f'A família com "duas" pessoas deverá pagar R$ {valor_2_pessoas:.2f}')

#Custo para três pessoas.
print(f'A família com "três" pessoas deverá pagar R$ {valor_3_pessoas:.2f}')

#Custo para quatro pessoas.
print(f'A família com "quatro" pessoas deverá pagar R$ {valor_4_pessoas:.2f}')
