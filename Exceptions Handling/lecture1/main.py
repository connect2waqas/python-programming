try:
    print("code that may rise the error!")
    a = 10
    b = 0
    division = a / b
    dict = {"name": "waqas"}
    print(dict["key"])
    
except ZeroDivisionError:
    print("The denomenoter should not be Zero")
except KeyError:
    print("enter the correct key")