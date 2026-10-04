try:
    num=int(input("enter a number"))
    num2=int(input("enter a number"))
    print(num/num2)
except ZeroDivisionError:
    print("there is a ZeroDivisionError")
except ValueError:
    print("there is a ValueError")
except Exception as e:
    print("there was an issue")
finally:
    print("i strongly hate python")