import random
while(True):
    n=random.randint(1,100)
    i=1
    while(True):
        h=0
        while(True):
            h=input("hads bezan : ")
            if h.isdigit():
                h=int(h)
                break
            else:
                print("dobare vard kon : ")
        i+=1
        if i==6:
            print("bakhti! javab ",n," bood")
            break
        if h>n:
            print("Too high!")
        elif h<n:
            print("Too low!")
        else:
            print("Congratulations! You guessed it!")
            print ("adad mored nazar ",n," bood va to ba ",i," talash movafagh shodi!")
            break
    print("aya ghast edame dadan dari ?")
    print("age ghast khoroj dari no vard kon")
    print("dar gheir in sorat har chi vard kardi")
    q=input()
    if q=="no":
        print("good bye")
        break