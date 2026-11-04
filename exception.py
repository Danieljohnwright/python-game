a = 10
b = 0

try:
 c = a / b
 print("code worked")
except Exception as e:
    print("exception")

finally:
    print("at last")