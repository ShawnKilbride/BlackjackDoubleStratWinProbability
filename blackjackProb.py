 #probability of losing n hands = p(winning 1 hand)^n
# n = number of hands
# p(losing a hand) = 50.4%
# p(tie) = 7.8%
# p(win) = 42.2%
# n number of lost hands in a row
# 2500
# 5000
# 10000
# 20000
# In order to have a 1 in 1,000,000 chance of losing n number of hands, how much money can we lose?
# money-loss potential = payroll
import math

startingBet = 2500
dep = int(input("Which dependent do you wish to use? Type 1 for number of rounds lost, 2 for money in the bank, or 3 for probability: "))

if dep == 1:
	n = int(input("How many times have you lost?: "))
	p = .504**n*100
	moneyLost = 0
	for i in range(n):
		moneyLost += startingBet*2**(i)
	print("With a starting bet of", startingBet, ", the probability of losing", n, "times is", "{:.10f}".format(p), "%, and you have lost $", moneyLost)
elif dep == 2:
	money = int(input("How much money do you have?:"))
	bet=startingBet
	n = -1
	while bet < money:
		bet*=2
		n+=1
	p = .504**n*100
	print("With a starting bet of", startingBet, ", and a total of $", money, ", you can lose up to", n, "times. The probability of this happening is", "{:.10f}".format(p), "%.")
elif dep == 3:
	p = float(input("What probability are you looking for in %?:"))
	p = p/100
	n = math.log(p, .504)
	n = math.floor(n)
	moneyLost = 0
	for i in range(n):
		moneyLost += startingBet*2**(i)
	print("With a starting bet of", startingBet, ", you have a probability of approximately", p*100, "% to lose", n, "times in a row and lose $", moneyLost, ".")
else:
	print("Error: Invalid option")
input("Press Enter to exit")