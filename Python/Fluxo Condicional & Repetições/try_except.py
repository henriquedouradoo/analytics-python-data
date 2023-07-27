preco = 132.85
pessoas = 2

try:
  valor_por_pessoa = preco / pessoas
  print(valor_por_pessoa)
except ZeroDivisionError:
  print('Número de pessoas inválido. Espera-se um valor maior que 0 e obteve-se um valor igual a ' + str(pessoas))
except Exception as exc:
  print(exc)
  print('Erro Genérico.')

nome = 'Henrique Dourado'
idade = 19

try:
  apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
  print(apresentacao)
except TypeError:
  idade = str(idade)
finally:
  print('Segunda chance')
  apresentacao = 'Fala pessoal, meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
  print(apresentacao)


 