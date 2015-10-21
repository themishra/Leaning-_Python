import random
def random_num(val2):
	min=1
	max=val2
	return(random.randint(min,max))
response =input("\tDo you want to Roll a dice!! \n\n \t Enter response:\t")
while (response == 'y') or (response =='yes'):
	num=int(input("\nEnter the no of faces in a dice:\t"))
	face = random_num(num)
	print("\n\n\t\t_________")
	print("\t\t|-------|\n\t\t|  ",face,"\t|\n\t\t|_______|")
	response = input("\n\n Do u want to roll it again? \n \n Enter response:\t")