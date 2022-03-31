a=10                       #global variable

def func():
    global a              #overwrites value of global variable with new value
    print(a)
    a=8                  #local variable
    print(a)                
func()                   #function calling
print(a)                 #prints global var

