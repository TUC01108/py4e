
smallest = 10000
print('Before',smallest)
for value in [9,41,12,3,74,15]:
    if value < smallest:
        smallest = value
    print(smallest,value)
print('After', smallest)
