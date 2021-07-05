gabarito = []
respostas = []

for i in range(10):
  gabarito.append(input('Resposta do gabarito:'))

print('\n---------------')
for i in range(30):
  respostasN = []
  acertos = 0
  for e in range(10):
    respostasN.append(input('Resposta do aluno:'))
    if respostasN[e] == gabarito[e]:
      acertos +=1
  respostas.append(respostasN)
  respostas[i].append(acertos)
  if acertos >= 5: print('Aluno classificado!')
  else: print('Aluno desclassificado!')
  print('\n---------------')

print('lista G',gabarito)

print('lista R',respostas)
