"""
The program is trying to analyze the grades on a final exam.
The program will point to a file, Final.txt, and analyze it and display 3 items to the user.
The first item that it will display is the number of grades.
The second item that will display is the average grade.
The third item it will display is the percentage of grades that are above the average grade.


There will be 5 functions, the first will point the program to a file
The second will read the file in a loop then close the file
The third will output the number of grades
The fourth will output the average grade 
The fifth will output the percentage of grades above the average grade
"""


"""
# Function1
 infile = open("File name", 'r')
 point to file

# Function2
 varibale= [line.rstrip() for line in infile]
 infile.close()
 read file in loop and close

# Function3
for i in range(len(variable)):
    Variable[i] = int(variable[i])
 output is read number of grades

# Function4
 average = sum(variable) / len(variable)
 output is average the grades

# Function5
num = 0 # number of grades above average
 for variable in variable:
 if variable > average:
 num += 1
 output is the percentage of grades above the average grade

main
"""