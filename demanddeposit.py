principal = 85033.59
interest_rate = 0.045

for i in range(1, 31):
  principal *= 1 + interest_rate / 365
  
  print(i, " day: ", principal)