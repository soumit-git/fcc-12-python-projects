import random

def play():
  user = input("'r' for rock, 'p' for paper, 's' for scissor, what's your choice : ").lower()
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    return "It\'s a tie!"
  
  if is_win(user, computer):
    return "You won!"
  
  return "You lose"

def is_win(u, c):
  if (u == 'r' and c == 's') or (u == 'p' and c == 'r') or (u == 's' and c == 'p'):
    return True
  return False

print(play())