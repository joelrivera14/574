#lab7_5.py - Joel Rivera
import random

#requesting an integer
number = int(input('Enter the number of grades in the list: '))

#use a loop to generate random grades 
grades = []
for num in range(number):
    r=random.randint(1,100)
    grades.append(r)

#requesting the passing grade
passingNum=int(input('Enter the passing grade: '))

passGrades=[]
for n in grades:
    if n >= passingNum:
        passGrades.append(n)
print(f'Updated List: {passGrades}\nOriginal List: {grades}')