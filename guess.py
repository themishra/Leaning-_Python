import random
import time
import os
def animation():
	for i in range(5):
		time.sleep(0.5)
		print("\t.",end="",flush=True)

def random_num():
	x=random.randint(0,1000)
	return x

def equlity_chk(unum, rnum):
	print("\t\t\tPLAY AND GUESS IT...")
	print("\t\t\t[\t]\n\t\t\t  ", rnum,"\n\t\t\t[\t]\n\n\n")
	if unum == rnum:
		print("\tBINGO...Hey your guess is correct")
	else:
		diff = ((int)(unum) - rnum)
		if diff > 0:
			print("\tSorry...You have entered a greator values--[",unum,"]")
		else:
			print("\tsorry...you have entered a smaller value--[",unum,']')
response='yes'			
while (response == 'y') or (response == 'yes'):
	os.system('cls')
	print("\t\t\tPLAY AND GUESS IT...")
	print("\t\t\t[\t]\n\t\t\t     ?\n\t\t\t[\t]\n")
	animation()
	num=input("\n\n\n\tGuess the number? \t")
	a=(random_num())
	print(a)
	os.system('cls')
	equlity_chk(num,a)
	response = input("\n\tDo u want to repeat it again.. Reply with either yes or y   ")