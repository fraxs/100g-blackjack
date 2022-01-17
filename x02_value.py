def cardvalue(a):
  if a == '2':
    return 2
  elif a == '3':
    return 3
  elif a == '4':
    return 4
  elif a == '5':
    return 5
  elif a == '6':
    return 6
  elif a == '7':
    return 7
  elif a == '8':
    return 8
  elif a == '9':
    return 9
  elif a == 'T' or a == "J" or a == "Q" or a == "K":
    return 10
  if a == "A":
    return [1,11]
def split(word):
  return list(word)
def value(hand):
  list1 = []
  for i in hand:
    i = split(i)
    final = cardvalue(i[0])
  if final == [1,11]:
    list1[0][0] += list1[1] + list1[2]
    list1[0][1] += list1[1] + list1[2]
    list1.pop()
    list1.pop()
    finallist = [list1[0][0],list1[0][1]]
    return finallist
  else:
    list1.append(final)
    return sum(list1)
def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26
if __name__ == "__main__":
  main()