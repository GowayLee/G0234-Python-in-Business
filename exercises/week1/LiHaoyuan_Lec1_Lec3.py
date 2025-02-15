# 1. print
language="python"
print("I am learning",language)

# 2. print_christmas_tree
print("\n=============================\n")

def print_christmas_tree(height=5):
    # 树的顶部
  for i in range(height):
    print((' ' * (height - i - 1)) + ('*' * (2 * i + 1)))
    
    # 树干
  for i in range(height // 2):
    print((' ' * (height - 1)) + '|')

print_christmas_tree()

# 3. print calendar
print("\n=============================\n")

print(" =============================")
print("        Feb 2025 ")
print(" =============================")
print("   SUN MON TUE WED TUR FRI SAT  \n")
print("   \n")
print("    ***    ")
print("    ***    ")

# 4. calculate BMI
print("\n=============================\n")

weight=60
height=1.7
BMI=weight/(height**2)
print("BMI:",BMI)


# 5. perform summation
print("\n=============================\n")

# 6. print type
print("\n=============================\n")

a=1
b=1.1
c=2+4j

print("Type of a",type(a))
print("Type of b",type(b))
print("Type of c",type(c))

# 7. calculate company budget
print("\n=============================\n")

company_name = "my-company"
total_budget = 814916.06
rent_expense = 70200.06
salary_expense = 3185.767
marketing_expense = 42357.99
remaining_budget = total_budget - (rent_expense + salary_expense + marketing_expense)