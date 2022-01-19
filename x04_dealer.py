#!python3

'''
In Blackjack, the dealer always must follow the same rules.

1. They will stand pat (not take new cards) if their score is over 16
2. They will automatically take a new card if their score is less than 17
'''
def cardvalue(x):
  if x == '2':
    return 2
  if x == '3':
    return 3
  if x == '4':
    return 4
  if x == '5':
    return 5
  if x == '6':
    return 6
  if x == '7':
    return 7
  if x == '8':
    return 8
  if x == '9':
    return 9
  if x == 'T' or x == 'J' or x == 'Q' or x == 'K':
    return 10
  if x == 'A':
    return 'ace'


def split(x):
  x = list(x)
  return x
def value(hand):
  finalvalue = 0
  for i in hand:
    i = split(i)
    score1 = cardvalue(i[0])
    if score1 == 'ace' and finalvalue + 11 > 21:
      score1 = 1
      finalvalue += score1
    elif score1 == 'ace' and finalvalue + 11 <= 21:
      score1 = 11
      finalvalue += score1
    else:
      finalvalue += score1
  return finalvalue




def dealer(deck):
  dealer = []
  score = 0
  
  for i in range(len(deck)):
    dealer.append(deck[i])
    score = value(dealer)
    if score > 16:
      break
  for i in dealer:
    deck.remove(i)
  return [dealer, score]
    
  
  ''' 
  inputs:
  list deck: contains a shuffled list of cards
  return:
  list of lists:
  list[0] : the dealer's hand
  list[1] : the dealer's count
  list[2] : the remaining deck
  
  function will keep drawing a card from the deck until they have a score > 16
  You may need to use the function in problem 2 to count the score
  it will then return a list
  '''
  
  return [ dealer , score , deck ]

def main():
  deck = ['3C', '3S', '8S', '3D', 'AC', '9H', 'QC', 'TD', 'TH', '8H', '8D', '7C', 'TS', '7D', 'AD', 'QD', 'KC', '6H', 'JH', 'KH', 'QS', '6C', '4H', '7H', '5S', '2S', 'AS', 'AH', '5C', '2D', '2H', '6D', 'TC', '4C', 'JS', 'JC', 'KD', '2C', '4S', '3H', '5H', '7S', 'KS', '5D', 'QH', '6S', '8C', '9D', 'JD', '9S', '9C', '4D']
  #run1 = dealer(deck)
  assert dealer(deck) == [['3C', '3S', '8S', '3D'], 17]
  #run2 = dealer( run1[2] )
  assert dealer(deck) == [['AC', '9H'], 20]



#deck = ['3C', '3S', '8S', '3D', 'AC', '9H', 'QC', 'TD', 'TH', '8H', '8D', '7C', 'TS', '7D', 'AD', 'QD', 'KC', '6H', 'JH', 'KH', 'QS', '6C', '4H', '7H', '5S', '2S', 'AS', 'AH', '5C', '2D', '2H', '6D', 'TC', '4C', 'JS', 'JC', 'KD', '2C', '4S', '3H', '5H', '7S', 'KS', '5D', 'QH', '6S', '8C', '9D', 'JD', '9S', '9C', '4D']
#print(dealer(deck))
deck = ['3C', '3S', '8S', '3D', 'AC', '9H', 'QC', 'TD', 'TH', '8H', '8D', '7C', 'TS', '7D', 'AD', 'QD', 'KC', '6H', 'JH', 'KH', 'QS', '6C', '4H', '7H', '5S', '2S', 'AS', 'AH', '5C', '2D', '2H', '6D', 'TC', '4C', 'JS', 'JC', 'KD', '2C', '4S', '3H', '5H', '7S', 'KS', '5D', 'QH', '6S', '8C', '9D', 'JD', '9S', '9C', '4D']
print(dealer(deck))
