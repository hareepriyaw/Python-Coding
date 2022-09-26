"""
my_dic={"name": "hari", "age":"47"}
print(my_dic)

my_list=list(my_dic.keys())
print(my_list)
our_dic=my_dic.items()
print(our_dic)



my_fd={"name":"balaji", "place": "Henrico"}
my_fd1={"name":"haripriya","place": "Virginia"}
my_lis=[my_fd,my_fd1]
print(my_lis)


my_str={"haripriya":1,"is":2, "my":3, "name":4}
my_str1={"Balaji":5,"is":6, "my":7,"name":8}
my_lis_str=[my_str,my_str1]
#print(my_str[0])

for i in my_lis_str:
    if "name" in i:
        if i["name"]==4:
            lis_ap=i
            print(lis_ap)

for x in range(1,10):
    for i in my_lis_str:
        if i["name"]==x:
            print(i)
"""
list_st=[1,2,3,4,5]
even_num=[]
odd_num=[]
for i in list_st:
    if i%2 == 0:
        even_num=i
        print("THis is even:",even_num)
    else:
        odd_num=i
        print("This is odd:",odd_num)