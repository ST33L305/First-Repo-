 # MATHEMATICAL SOLVING APP
question= input("what question do you want to solve? ") # e.g area of circle, value of pi.

# Equation to solve 
if question== "roots of equation":
    
    import math
    
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
 
    discriminant =(b * b)-(4 * (a * c))
    print(" the discriminant is " + str(discriminant))
    numerator1 = -(b) + math.sqrt(discriminant)
    print("numerator 1 is " + str(numerator1))
    numerator2 = -(b) - math.sqrt(discriminant)
    print("numerator 2 is " + str(numerator2))
 
    denominator= 2 * a;

    root1= (numerator1 / denominator)
    root2= (numerator2 / denominator)
    print(" root 1 is " + str(root1))
    print(" root 2 is " + str(root2))

if question== "area of trapezium":
    a = int(input("What is a? "))
    b = int(input("What is b? "))
    h = int(input("What is h? "))
    
    answer = ((a + b) / 2) * h
    print("The answer is " + str(answer))

if question== "nth term of GP":
    a = int(input("what is a? "))
    r = int(input("what is r? "))
    n = int(input("what is n? "))
        
    answer= a * (r ^ (n - 1))
    print("The answer is" + str(answer))

if question== "convert naira to pounds":
    naira=int(input("How much naira? "))
    pounds= (naira * 554.76) 
    print(str(naira) + " naira is " + str(pounds) + "pounds") 

if question== "cyclic permutation":
    number=int(input('What is n?'))
    answer=(n - 1)