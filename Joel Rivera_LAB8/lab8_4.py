#lab8_4.py – Joel Rivera

#writing hello function
def hello():
    print(f'Hello World')

#writing helloNum function and adding a parameter
def helloNum(n):
    i = 0
    while i < n:
        i+=1
        hello()
        

#calling function
helloNum(3)