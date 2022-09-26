'''
class _init_():
    def priya(self):
        a=int(self)
        b[a]=0
        b[a]=[a,a+2,a+4,a+8,a+10]
    for x in range(b[a:a+10]):
            x=b[a]
            print("the number is:{x}")
            continue
            


st='I am a woman.\n I am a teacher.\n I am a devotee.\n  I am a traveler.\n  I am a programmer'

st1=st.splitlines(False)

st2=''.join(st1)
print(st2)

bol=st2.startswith("AM")
print(bol)

st3=st2.swapcase()
print(st3)

#print("My name is: %('name')s and my age is %(age)03d" %{'name':"hari", 'age':47})
my_lis=[1,2,3,4,5,6,7,8,9,10]
lis1=[]
lis1=list(map(lambda x: x**2, my_lis))
print(lis1)
'''



dict1={'flowers':['rose','jasmine','lily'],'fruits':['mango', 'orange','kiwi']}

df=list(dict1.fromkeys('flowers','fruits'))
print(df)