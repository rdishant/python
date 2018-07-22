#1
'''a=int (input('Enter a number'))
l=(lambda x:x**3)(a)
print(l)
'''
#3
'''l1=[1,2,3]
l2=[2,3,4]
l3=[4,6,7]
l4=[7,8,9]
L=[x for x in map(lambda a,b,c,d:a+b+c+d,l1,l2,l3,l4)]
print(L)
'''
#2
'''l1=[1,3,5,10,12,15,18,20,21,30]
L=[x for x in filter(lambda a:True if a%3==0 and a%5==0 else False,l1)]
print(L)'''
#4
'''l1=[7,6,4]
l2=[2,3,5]
L={k:v in k,v in map(lambda a,b:(a,b**2) if a>b else (b,a**2),l1,l2)}
print(L)   
'''
