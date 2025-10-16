'''pessoas = [['João',10], ['Pedro',15], ['José',18]]

print(pessoas)

print(pessoas[0][0])

print(pessoas[1][0])

print(pessoas[2])

teste=list()

teste.append('lindolfo')
teste.append(43)

print(teste)

galera=list()
galera.append(teste[:]) #cópia

print(galera)

teste[0]='Maria'
teste[1]=22

print(teste)
print(galera)
'''
turma = [['Ana',15],['João',20],['Pedro',32],["Raul",44]]

'''print(turma)
print(turma[0])
print(turma[1][1])

for p in turma:
    print(p)

for p in turma:
    print(p[0])


for p in turma:
    print(f'{p[0]} tem {p[1]} anos de idade')
'''

turma2=list()
dados=list()
totmaior = totmenor = 0

for c in range(0,6):
    dados.append(str(input("Nome:")).upper().strip())
    dados.append(int(input("Idade:")))
    turma2.append(dados[:])
    dados.clear()
print(turma2)

for p in turma2:
    if p[1]>= 18:
        print(f'{p[0]} é maior de idade , ele tem {p[1]} anos de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade , ele tem {p[1]}anos de idade')
        totmenor += 1 

print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade')
