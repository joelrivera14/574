fi='new.txt'

with open(fi, 'r+') as f:
    p=['h','e','y']
    for i in p:
        l=f.readlines()
        f.write(f'{i}\n')
        print(i)
    
        
    