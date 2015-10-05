import random
import sys
import os
import time
response=''
welcome_text="*******Welcome to the dice Simulator*******"
def animation():
		for i in range(5):
			time.sleep(0.5)
			print(".",end="",flush=True)

def cube(val2):
	min=1
	max=val2
	print("Rolling Dice",end='')
	animation()
	os.system('cls')
	print("\n\n\t\t", welcome_text,"\n\n")
	print("\n\n\t\t_________")
	print("\t\t|-------|\n\t\t|  ",random.randint(min,max),"\t|\n\t\t|_______|")

def cube_roll(response,num):
	while (response == 'y') or (response =='yes'):
		os.system('cls')
		print("\n\n\t\t", welcome_text,"\n\n")
		cube(num)
		response =input("\n\n Do u want to roll it again? \n \n Reply with Either Y or yes in order to Confirm \
			\n\n Or you may press X to exit:\t")
		if(response=="X") or (response=="x"):
			sys.exit()

print("\t\t", welcome_text,"\n\n\n")
if __name__ == "__main__":
	ex=input("\tDo you want to Roll a dice!! \n\n \t Enter yes to Continue...\t")
	if (ex =='y') or (ex =='yes'):
		num=int(input("\nEnter the no of faces you would like to have in your dice:\t"))
		cube_roll(ex,num)
