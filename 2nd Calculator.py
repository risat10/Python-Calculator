#2nd a calculator

a=float(input("Enter the number")) #just add input here  #add datatype
b=float(input("Enter the number"))                       #if you don't add datatype the addition of 2 and 2 will come 22
                                                         #run and see 
ans1=a+b
ans2=a-b
ans3=a*b
ans4=a/b
ans5=a//b
ans6=a**b
ans7=a%b

print("1.the addition of",a,"and",b,"is",ans1) 
print("2.The Substraction of",a,"and",b,"is",ans2)
print("3.The multification of",a,"and",b,"is",ans3)
print("4.The division of",a,"and",b,"is",ans4)
print("5.The Floor division of",a,"and",b,"is",ans5)
print("6.The exponential of",a,"and",b,"is",ans6)
print("7.The modulus of",a,"and",b,"is",ans7)

ans8=(ans1+ans2+ans3+ans4+ans5+ans6+ans7)/7

print("Total average of (1to7) is",ans8)
