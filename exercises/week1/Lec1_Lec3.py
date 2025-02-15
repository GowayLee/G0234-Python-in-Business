# 1. print
CXX = "clang++"
print("CXX: ", CXX)

# 2. print_christmas_tree
print("\n-----------------------------\n")


print("        *        ")
print("       ***       ")
print("      *****      ")
print("     *******     ")
print("    *********    ")
print("   ***********   ")
print("  *************  ")
print(" *************** ")
print("*****************")
print("       |||       ")
print("       |||       ")
print("       |||       ")


# 3. print calendar
print("\n-----------------------------\n")

print("============================")
print("          Feb 2025          ")
print("============================")
print(" SUN MON TUE WED THU FRI SAT")
print("                          1")
print("  2   3   4   5   6   7   8")
print("  9  10  11  12  13  14  15")
print(" 16  17  18  19  20  21  22")
print(" 23  24  25  26  27  28")

# 4. calculate BMI
print("\n-----------------------------\n")

weight = 60
height = 1.7
BMI = weight / (height**2)
print("BMI:", BMI)


# 5. perform summation
print("\n-----------------------------\n")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
print("Sum:", sum)

# 6. print type
print("\n-----------------------------\n")

a = 1
b = 1.1
c = 2 + 4j

print("Type of a", type(a))
print("Type of b", type(b))
print("Type of c", type(c))

# 7. calculate company budget
print("\n-----------------------------\n")

company_name = "my-company"
total_budget = 814916.06
rent_expense = 70200.06
salary_expense = 3185.767
marketing_expense = 42357.99
remaining_budget = total_budget - (rent_expense + salary_expense + marketing_expense)
print("Remaining Budget:", remaining_budget)
