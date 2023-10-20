# STACK 
# -> linear data-structure
# -> working manner - LIFO/FILO

# Operations

l=[]
while True:
    c= int(input('''ENTER THE NUMBER OF OPERATION TO PERFORM
                    1 - PUSH STACK
                    2 - POP STACK
                    3 - PEEK
                    4 - DISPLAY STACK
                    5 - EXIT :- ''')
    )
    # PUSH
    if c==1:
        n = input("ENTER THE VALUE:-")
        l.append(n)                                                        
        print(l)
    #POP
    elif c==2:
         if len(l)==0:
              print("EMPTY STACK")
         else:
          print(l.pop())
         print(l)
    #PEAK     
    elif c==3:
         if len(l)==0:
              print("EMPTY STACK")
         else:
             print("LAST STACK VALUE:-", l[-1])
    #DISPLAY
    elif c==4:
         print("DISPLAY STACK",l)
    #EXIT     
    elif c==5:                
         break;
    else:
        print("INVALID INPUT")

# QUEUE
# -> Working manner - FIFO

#OPERATIONS

l=[]
while True:
    c= int(input('''ENTER THE NUMBER OF OPERATION TO PERFORM
                    1 - ENQUEUE
                    2 - DEQUEUE
                    3 - FIRST ELEMENT
                    4 - LAST ELEMENT
                    5 - DISPLAY QUEUE
                    6 - EXIT :- ''')
    )
    # ENQUEUE
    if c==1:
        n = input("ENTER THE VALUE:-")
        l.append(n)                                                        
        print(l)
    #DEQUEUE
    elif c==2:
         if len(l)==0:
              print("EMPTY QUEUE")
         else:
          print(l.pop())
         print(l)
    #FIRST    
    elif c==3:
         if len(l)==0:
              print("EMPTY QUEUE")
         else:
             print("LAST FIRST VALUE:-", l[0])
    #LAST
    elif c==4:
         if len(l)==0:
              print("EMPTY QUEUE")
         else:
             print("LAST LAST VALUE:-", l[-1])
    #DISPLAY
    elif c==5:
         print("DISPLAY QUEUE",l)
    #EXIT     
    elif c==6:                
         break;
    else:
        print("INVALID INPUT")

