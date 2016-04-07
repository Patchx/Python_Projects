#      Author:  Robert Anderson
#        Date:  April 7th, 2016
#     Purpose:  Display average grade of a student to 2 decimal places
# Inspiration:  https://www.hackerrank.com/challenges/finding-the-percentage?h_r=next-challenge&h_v=legacy

print(chr(27) + "[2J") #Clears the terminal screen on Unix-like systems
print("\n-------------- Gradebook --------------------")

# Global Variables
# ----------------
studentNum = 0
usrIn = []
studentList = {}
yesNo = ""

# Functions
# ---------
def toNumDefault(inStr):
	try:
		return abs(float(inStr))
	except ValueError: # type(user_input) != number
		return 0

def findName(inputList):
	name = raw_input('\n> Please choose a record to access: \n%(listIn)s \n' % {'listIn': inputList.keys()})
	if (name in inputList):
		return([name, inputList[name]])
	else:
		yesNo = raw_input("> Student record not found. Try again?: ").lower()
		if (yesNo in ['yes','y']):
			return findName(inputList)

def avgGrade(studentIn):
	return float(sum(studentIn[1]) / len(studentIn[1]) )

# Main
# ----
while (studentNum < 2):
	studentNum = raw_input("\n> Please enter the number of students in the class:  ")
	studentNum = int(toNumDefault(studentNum))
	if (studentNum < 2): print("  Sorry, try again")

print("\nEnter student records in the following format: ")
print("  Name Grade Grade Grade")

for i in range(studentNum):
	usrIn = raw_input("> ").split()
	if (len(usrIn) == 0): usrIn.append("noName")
	for x in range(1,len(usrIn)):
		usrIn[x] = toNumDefault(usrIn[x])
	while (len(usrIn) < 4):
		usrIn.append(0)
	studentList[usrIn[0]] = usrIn[1:]

student = findName(studentList)
print("Student's average = %.2f" % avgGrade(student)) # formatted to 2 decimal places
