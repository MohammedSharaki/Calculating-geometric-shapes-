# import turtle
# tools=turtle.Turtle()
''' 
    نعمل مثلث نظريه فيثاغورث 
    نعمل المربع محيط ومساحه وحجم 
    لازم نفرق بين المربع والمكعب
    نعمل مستطيل محيط مساحه حجم 
    نعمل معين محيط مساحه حجم
    نعمل متوازي اضلاع محيط مساحه حجم برضو
    نعمل معادلات للاشكال الهندسيه دي
'''
# from bidi.algorithm import get_display
def triangel():
    print("find the\n       1- find Side\n       2- find corner\n please enter number to slove : ")

    l=input("enter your problem : ")

    if l=="2":

        ab=int(input("enter the  AB : "))

        bc=int(input("enter the  BC : "))

        ac=int(input("enter the  AC : "))

        if (ab*ab + bc*bc) ==ac*ac:
            print("this is Qaemeh Angle in B")

        elif (bc*bc + ac*ac) ==ab*ab:
            print("this is Qaemeh Angle in C")


        elif (ac*ac + ab*ab) ==bc*bc:
            print("this is Qaemeh Angle in A")

        else:

            print("please return")

    elif l=="1":

        ab=float(input("enter the frist Side : "))

        bc=float(input("enter the sec Side : "))

        ab1=ab*ab
        bc1=bc*bc

        a=ab1+bc1
        print(a**(1.0/2))
pass

def Box():
    ab=int(input("enter one sides : "))
    ad=ab
    bc=ab
    cd=ab
    
    print(f"{cd} cem")
    mean=input("enter what are you want \n 1-Space (sp)\n 2-Perimeter(per)\n 3-Box size(size): ")
    if mean=="sp":
        print(f"{ab*bc} cem")
    elif mean=="per":
        print(f"{ab*4} cem")
    elif mean=="size":
        print(f"{ab*bc*cd} cem")
pass

def Rectangle():

    mean=input("enter what are you want \n 1-Space (sp)\n 2-Perimeter(per)\n 3-Box size(size): ")
    if mean=="sp":
        height=int(input("enter the heigth : "))
        width=int(input("enter widt here : "))
        print(width+height*2)


    elif mean=="per":
        height=int(input("enter the heigth : "))
        width=int(input("enter widt here : "))
        print(height*width)


    elif mean=="size":
        height=int(input("enter the heigth : "))
        width=int(input("enter widt here : "))
        high=int(input("enter the high of Parallel rectangles"))
        print(width*height*high)
pass
def Rhombus():
    ab=int(input("enter the side : "))
    bc=int(input("enter the side : "))
    cd=int(input("enter the side : "))
    ad=int(input("enter the side : "))
pass 

if __name__ == "__main__":
    print("your language is 'english'")
    
    sides=int(input("Enter the number of sides : "))

    if sides==3:
        triangel()
    
    elif sides==4:
        mean=input("enter what are you want\n 1-Rectangle (rec)\n 2-box ")
    
        if mean=="rec":

            Rectangle()
        
        elif mean=="box":
            Box()
else:
    print("nooooooooooo")
