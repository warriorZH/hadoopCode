


print "M"+" %d %d %d" %(1,2,3)
m = [1,2,3]
n = [4,5,6]
for (x,y) in zip(m,n):
    result = x*y
    print result
print(lambda x,y: x*y for (x,y) in zip(m,n))
