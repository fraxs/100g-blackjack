#!python3

'''
In Blackjack, having a score over 21 is an automatic loss.
Create a function that determines if the score is a bust
'''

def busts(score):
  if score > 21:
    return True
  else:
    return False
  


def main():
  assert busts(22) == True
  assert busts(20) == False
  assert busts(21) == False
  assert busts(17) == False
  assert busts(30) == True
  
if __name__ == "__main__":
  main()
