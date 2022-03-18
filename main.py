from game_data import data
import random
from art import vs
from art import logo
from replit import clear
  

option_a = random.choice(data)
option_b = random.choice(data)
higher = ""
pontos = 0
option_player = ""
game_over = False
while not game_over:

  while option_a == option_b:
    option_b = random.choice(data)
  
  print (logo)

  print (f" Name: {option_a['name']}. Famous for: {option_a['description']}. From: {option_a['country']}")

  print (vs)
  
  print (f" Name: {option_b['name']}. Famous for: {option_b['description']}. From: {option_b['country']}\n")
  

  # Definir qual das duas opções tem mais seguidores
  if option_a['follower_count'] > option_b['follower_count']:
    higher = option_a
  else:
    higher = option_b

  # Perguntar qual das duas opções o jogador acha que tem mais seguidores


  option_player= input("Qual das duas opções voce acha que tem a maior quantidade de inscritos? A ou B: \n").lower()

  if option_player == "a":
    option_player = option_a
  else:
    option_player = option_b
  # Comparar resposta do jogador com a correta
  if option_player == higher:
    pontos += 1
    clear()
    print (f"Acertou! Voce tem {pontos} pontos")
    option_a = option_player
    option_b = random.choice(data)
  else:
    if pontos == 1:
      print(f"Errrrou! Voce fez {pontos} ponto!")
    else:
      print(f"Errrrou! Voce fez {pontos} pontos!")
    game_over=True
  
  
  



# Caso o jogador acerte, acrecentar um ponto na pontuação e gerar novas duas opções de comparativo utilizando a opção escolhida pelo jogador como uma das opções e outra opção aleatória da lista diferente da anterior
# Caso o jogador erre, encerrar a rodada e entregar a pontuação final