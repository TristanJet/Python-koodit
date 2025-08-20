while 1:
    inch = float(input("Enter inches: "))
    if inch < 0:
        break
    cm = inch * 2.54
    print(f"{round(inch, 3)} inches == {round(cm, 3)} centimetres")
