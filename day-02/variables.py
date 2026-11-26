print("Assign multiple values to multiple variables")
num1, num2, num3 = 10,20,30
print("number1 value", num1)
print("number2 value", num2)
print("number3 value", num3)
print("All variable references are:", id(num1), id(num2), id(num3))


print("Assign single value to multiple variables")
num1 ,num2, num3 = 10, 10, 10
print("number1 value", num1)
print("number2 value", num2)
print("number3 value", num3)
print("All variable references are:", id(num1), id(num2), id(num3))


print("Tf more than 255")
print("Assign single value to multiple variables")
num1 ,num2, num3 = 350, 350, 350
print("number1 value", num1)
print("number2 value", num2)
print("number3 value", num3)
print("All variable references are:", id(num1), id(num2), id(num3))

print("Swapping two numbers")
a, b = 10, 20
print("before swapping")
print(a, b, id(a), id(b))
a, b = b, a
print("after swapping")
print(a, b, id(a), id(b))

      




      
