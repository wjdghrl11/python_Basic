# 파이썬 사용자 입력
# input 사용법
# 기본 타입(str)

# 예제 1
name = input("Enter Your Name :")
grade = input("Enter Your Grade :")
company = input("Enter Your Company Name :")

print(name, grade, company)

# 예제 2
number = int(input("Enter number : "))
name = input("Enter Name")

print("type of number", type(number))
print("type of number", type(name))

# 예제 3
float_number = float(input("Enter float number"))

print("input float : ", float_number)
print("input float type : ", type(float_number))

# 예제 4
print("FirstName - {0}, LastName - {1}".format(input("Enter First Name : "), input("Enter Second Name : ")))