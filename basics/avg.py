sum=0
count=0
print('Before', sum)
for value in [9,41,12,3,74,15]:
    count+=1
    sum+=value
    print(sum/count,value)
print('After',sum/count)
