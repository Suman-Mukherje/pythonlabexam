
def enqueue(lst,value):
    lst.append(value)
    print(str(value)+" inserted in queue!")
    
def dequeue(lst):
    if len(lst)<1:
        print("Queue is empty")
    else:
        a=lst.pop(0)
        print("Poped element is: "+str(a))
    
def display(lst):
    i = len(lst)
    if len(lst)<1:
        print("Queue is empty")
        
    else:
        print("Queue elements are")
        for l in lst:
            print(l)
        
        
queue=[]
loop='Y'
while(loop=='Y'):
    choice=input("Enter 1 for enqueue,2 for dequeue and 3 for display :: ")
    if choice=='1':
        val=int(input("Enter the value :: "))
        enqueue(queue,val)
    elif choice=='2':
        dequeue(queue)
    elif choice=='3':
        display(queue)
    else:
        print("Bad Choice")
        
    loop=str(input("Do you want to continue Y/N:"))
    if(loop!='Y'):
        print("Ok ! Exited from this program")


