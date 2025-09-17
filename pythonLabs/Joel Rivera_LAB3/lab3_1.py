#lab3_1.py - Joel Rivera

#prompt the request input for bill and percentage and storing in a variable
bill = float(input('Enter the amount of the bill: '))
percentage = int(input('Enter the percentage of tip: '))

#calculate the result
markdown = percentage/100
total = bill * markdown

#print the result
print('Tip: $%.2f' % total, sep='')