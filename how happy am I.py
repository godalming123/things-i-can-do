#all values ar between 1 and 0 except happiness
#happiness varies from 0 to 2
def ObjectTree (tree, **inputs):
 #for self, question in inputs.iteritems():
 pass   
#ObjectTree ("money", "how much money do you have (from 1 to 0): ", "SocialSkills" "social skills (from 1 to 0): ", "HomeGrownFood", "how many crops did you grow (from 1 to 0): ")
money = eval (input ("how much money do you have (from 1 to 0): ")) / 1
SocialSkills = eval (input ("social skills (from 1 to 0): ")) / 1
#
food = money + eval (input("how many crops did you grow (from 1 to 0): ")) / 2
friends = SocialSkills + eval (input ("friend help (from 1 to 0): ") ) / 2
excersize = friends + eval (input ("excersize gotten(from 1 to 0): ")) / 2
sleep = eval (input ("sleep (from 1 to 0): ") ) / 1
#
PhysicalHealth = excersize + food / 2
MentalHealth = friends + sleep + excersize / 3
#
happiness = MentalHealth + PhysicalHealth/2
print (happiness)
