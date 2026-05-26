#file handling
#write()
'''a=open("abbas.txt","w")
a.write("codegnan it solutions")
a.close()'''

'''a=open("abbas.txt","w")
a.write("python")
a.close()'''

#append()
'''a=open("abbas.txt","a")
a.write("\tabbas")
a.close()'''

#run_time()
'''a=open("abbas.txt","w")
a.write(input("data"))
a.close()'''

'''a=open("abbas.txt","w")
b=input("enter the data")
a.write(b)
a.close()'''

#read()
'''a=open("abbas.txt")
#print(a.read())#it will display entire content
#print(a.readline())#it will display first line
#print(a.readlines())#it will display with\n
print(a.read(9))#it will display no.of characters'''

#writelines()->it makes every object side by side
'''a=["abbas","khasim","akash","vishwa","pooja"]
b=open("abbas.txt","w")
b.writelines(a)
b.close()'''

'''a=["abbas","khasim","akash","vishwa","pooja"]
b=open("abbas.txt","w")
b.writelines("\n".join(a))
b.close()'''

'''a=open("dta.py")
print(a.read())'''


