# from art import logo, vs
import game_data
import random
from replit import clear

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = game_data.data
data_length = len(data)
score = 0
print(logo)


def get_random_data():
  return random.choice(data)

def compare_data(first_data, second_data,guess):
  if guess == "A":
    return (first_data['follower_count'] > second_data['follower_count'])
  else:
    return (first_data['follower_count'] < second_data['follower_count'])


first_data = get_random_data()
second_data = get_random_data()

if first_data == second_data:
  second_data = get_random_data()
  
x= True 
while x:

  print(f"Compare A: {first_data['name']}, a {first_data['description']}, from {first_data['country']}.")
  print(first_data['follower_count']) ## 
  print(vs)
  
  print(f"Compare B: {second_data['name']}, a {second_data['description']}, from {second_data['country']}.")
  print(second_data['follower_count'])
  
  
  answer = input("Who has more followers? Type 'A' or 'B': ").upper()
  #compare_items = compare_data(first_data, second_data,answer)
  clear()
  print(logo)
  if compare_data(first_data, second_data,answer) and answer =="A":
    score += 1
    
    print(f"You're right! Current score: {score}.")
    second_data = get_random_data()
    
  elif compare_data(first_data, second_data,answer) and answer =="B":
    score += 1
    print(f"You're right! Current score: {score}.")
    first_data = second_data
    second_data = get_random_data()
    
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    
    x = False