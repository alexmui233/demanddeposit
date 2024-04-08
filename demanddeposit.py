principal = input("principal: ")
interest_rate = input("interest_rate: ")
days = int(input("days: "))

principal = float(principal)
interest_rate = float(interest_rate)
interest = 0
for i in range(1, days + 1):
  interest += principal * (interest_rate / 365)
  principal *= 1 + interest_rate / 365
  print(i, " day: ", principal)

print("\ntotal interest: ", interest)