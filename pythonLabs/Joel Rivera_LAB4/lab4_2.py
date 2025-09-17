#lab4_2.py – Joel Rivera

#create an empty list
grades=[]
grades.extend([56,65,100,58,87])
print(f'Current List: {grades}')

#calculating grades
total=sum(grades)
average=total/len(grades)
print(f'Average: {average:.2f}')

#using two different methods to remove failing grades
grades.remove(56)
grades.pop(2)
total2=sum(grades)
average2=total2/len(grades)
print(f'Updated list: {grades} \nUpdated Average: {average2:.3f}')