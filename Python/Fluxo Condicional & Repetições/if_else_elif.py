print('---------Sistema de Verificação----------')

cartao_cvv = '812'
cartao_cvv_cadastrado = '812'

senha = '0010'
senha_cadastro = '0010'

if (cartao_cvv == cartao_cvv_cadastrado):
  print('Seu cartão atende os requisitos.')
else:
  print('Seu cartão não atende os requisitos.')

if (senha == senha_cadastro):
    print('Sua senha atende os requisitos')
else:
   print('Sua Senha não atende os requisitos.')

if (cartao_cvv == cartao_cvv_cadastrado) & (senha == senha_cadastro):
   print('Pagamento Concluido!')
elif (cartao_cvv != cartao_cvv_cadastrado) & (senha == senha_cadastro):
   print('erro: Seu cartão não atende os requisitos.')
elif (cartao_cvv == cartao_cvv_cadastrado) & (senha != senha_cadastro):
   print('erro: Sua senha não atende os requisitos.')
else:
   print('erro: Pagamento não pode ser concluido.')