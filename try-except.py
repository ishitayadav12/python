while(True):
    print("Press q to quit")
    a = input("Enter a number:")

    if a == 'q'or "Q":
        break
    try:
        a=int(a)
        if a>10:
            print("Geater than 10")
        elif a==10:
            print("Equal to 10")
        else:
            print("Less than 10")   
    except Exception as e:
        print(e) 

print("***THANKS****")