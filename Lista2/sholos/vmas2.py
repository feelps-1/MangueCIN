quantidadeAlunos = int(input())
beyonce = 0
taylor = 0

for c in range(1, quantidadeAlunos + 1):
    if input() == 'beyonce':
        print(f'Aluno {c} votou na Beyoncé.')
        beyonce += 1
    else:
        print(f'Aluno {c} votou na Taylor Swift.')
        taylor += 1

print('Contagem de votos:')
print(f'Taylor Swift: {taylor} votos')
print(f'Beyoncé: {beyonce} votos')

if beyonce == taylor:
    print('Empate! Iniciando rodada de debate.')
    print('Alunos, agora é a sua chance de convencer os outros a mudar de voto!')
    
    for c in range(1, quantidadeAlunos + 1):
        if input() == 'sim':
            if input() == 'beyonce':
                print(f'Aluno {c} mudou seu voto para Beyoncé.')
                beyonce += 1
            else:
                print(f'Aluno {c} mudou seu voto para Taylor Swift.')
                taylor += 1
        else:
            print(f'Aluno {c} não mudou seu voto.')
            
    print('Nova contagem de votos após o debate:')
    print(f'Taylor Swift: {taylor} votos')
    print(f'Beyoncé: {beyonce} votos')

    if beyonce == taylor:
        print('Aldo, como presidente do evento, tem o voto decisivo.')
        if input() == 'beyonce':
            print('Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?')
        else:
            print('Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso.')
    elif beyonce > taylor:
        print(f'Beyoncé venceu com {beyonce} votos! Será que Kanye West estava certo?')
    else:
        print(f'Taylor Swift venceu com {taylor} votos! Kanye West tá irritado com isso.')
elif beyonce > taylor:
    print(f'Beyoncé venceu com {beyonce} votos! Será que Kanye West estava certo?')
else:
    print(f'Taylor Swift venceu com {taylor} votos! Kanye West tá irritado com isso.')
