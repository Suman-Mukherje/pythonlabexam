
def my_push(lst,value):
    lst.append(value)
    print(str(value)+" inserted in stack!")
    
def my_pop(lst):
    if len(lst)<1:
        print("Stack is empty")
    else:
        a=lst.pop()
        print("Poped element is: "+str(a))
    
def display(lst):
    i = len(lst)
    if len(lst)<1:
        print("Stack is empty")
        
    else:
        print("Stack elements are")
        for l in lst:
            print(l)
        
        
stack=[]
loop='Y'
while(loop=='Y'):
    choice=input("Enter 1 for push,2 for pop and 3 for display :: ")
    if choice=='1':
        val=int(input("Enter the value :: "))
        my_push(stack,val)
    elif choice=='2':
        my_pop(stack)
    elif choice=='3':
        display(stack)
    else:
        print("Bad Choice")
        
    loop=str(input("Do you want to continue Y/N:"))
    if(loop!='Y'):
        print("Ok ! Exited from this program")


