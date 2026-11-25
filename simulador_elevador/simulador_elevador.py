import random
import time
andar_atual = random.randint(-2, 8)
while True:
    print(f'andar atual: {andar_atual}')
    andar_escolhido = int(input('andar escolhido [-2 -1 0 1 2 3 4 5 6 7 8]:'))
    if andar_escolhido < -2 or andar_escolhido > 8:
         print('Andar não existe') 
    elif andar_escolhido == '':
          break
    elif andar_atual == andar_escolhido:
                print('O elevador já está no seu andar...')
    else:
        while andar_atual != andar_escolhido:  
            if andar_atual > andar_escolhido:
                time.sleep(1)
                print(f'{andar_atual}...')
                andar_atual -= 1
            else:
                time.sleep(1)
                print(f'{andar_atual}...')
                andar_atual += 1
        time.sleep(1)
        print(andar_atual)
        time.sleep(1)
                    
#limpar andar q ja passou
#musica de elevador


