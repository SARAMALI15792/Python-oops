#calculate the sum of sequence:
num=int(input("enter the number u want:"))
fact=1
sum=0
for i in range(1,num+1):
    fact*=i
    sum=sum+i/fact
   
print("the sequence is:",sum)   