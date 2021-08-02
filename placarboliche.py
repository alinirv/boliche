def strik(lista,x):
    i = 0
    j = x
    soma = 0
    while i < 3:
        soma = soma +lista[j]
        i += 1
        j += 1
    return soma
#---------------------------------------
def spare(lista,x):
    i = 0
    j = x
    soma = 0  
    while i <= 2:
        soma = soma +lista[j]
        i += 1
        j += 1
    return soma
#---------------------------------------
pinos = [int(i) for i in input().split()]
jogadas = 10
placar = []
pontos = 0
soma_pontos = 0
soma_total = 0
i = 0
j = 1

for a in range(jogadas):

    if pinos[i] == 10:
        soma_pontos = strik(pinos,i)        
        if a == 9:
            cont = 0
            x = i
            while cont < 3:
                if pinos[x] == 10:
                    placar.append('X')
                else:
                    placar.append(pinos[x])
                x += 1
                cont += 1                
        else:    
            placar.append('X')
            placar.append('_')
            placar.append('|')
        i += 1
        j += 1 
    else:
        pontos = pinos[i] + pinos[j]
        if pontos == 10:
            soma_pontos = spare(pinos,i) 
            if a == 9:
                placar.append(pinos[i])
                placar.append('/')
                placar.append(pinos[j+1])
            else:
                placar.append(pinos[i])
                placar.append('/') 
                placar.append('|') 
        else:
            soma_pontos = pontos
            if a == 9:
                placar.append(pinos[i])
                placar.append(pinos[i+1])   
            else:
                placar.append(pinos[i])
                placar.append(pinos[i+1]) 
                placar.append('|') 
        i += 2
        j += 2  
    
    soma_total = soma_total + soma_pontos
        
j=0
for i in range(len(placar)):
    print(placar[j],'',end="")
    j = j + 1

print('\n{}'.format(soma_total))
