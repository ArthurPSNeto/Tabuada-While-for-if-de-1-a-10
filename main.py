#Tabuada laço em while e for complexa
print("Tabuada de 0 a 10")
n=0
while n>=-1 or n<=10:
    n=(int(input("Digite um número de 0 a 10: ")))
    for x in range(0,11):
        if n>=11 or n<=-1:
          print("\nOs numeros são de 0 a 10, tente novamente.\n")
          print("-"*60)
          break
        print(n,"x",x,"=",n*x) 
      
