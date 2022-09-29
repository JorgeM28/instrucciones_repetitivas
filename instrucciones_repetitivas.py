print("-----------------------------------------------------")
print("----------SUMA DE N PRIMEROS NUM POSITIVOS-----------")
print("-----------------------------------------------------")


#input
N=int(input("Digite N:"))

#procesing
i=1
sum=0

while i<=N:
    sum=sum + i 
    i=i+1

#output
print("La suma es: "+ str(sum))