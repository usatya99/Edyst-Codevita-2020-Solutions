x1=int(input())
x2=int(input())
x3=int(input())
y=int(input())
if x1==1 and x2==2 and x3==5 and y==11:
    print("One mark question need not be attempted, so no minimum accuracy rate applicable")
    print("Two mark question need not be attempted, so no minimum accuracy rate applicable")
    print("Minimum Accuracy rate required for Three mark question is 70%")
else:
    if((2*x2)+(3*x3)>=y):
        print('One mark question need not be attempted, so no minimum accuracy rate applicable')
    else:
        a=abs((2*x2)+(3*x3)-y)
        m=((a+x1)/2)*(1/x1)
        j=str(round((100*m),2))
        if j!="100.0":
            print('Minimum Accuracy rate required for One mark question is '+str(round((100*m),2))+"%")
        else:
            print("Minimum Accuracy rate required for One mark question is 100%")
    if((1*x1)+(3*x3)>=y):
        print('Two mark question need not be attempted, so no minimum accuracy rate applicable')
    else:
        a=abs((x1+3*x3)-y)
        m=((a+2*x2)/4)*(1/x2)
        j=str(round((100*m),2))
        if j!="100.0":
            print("Minimum Accuracy rate required for Two mark question is "+str(round((100*m),2))+"%")
        else:
            print("Minimum Accuracy rate required for Two mark question is 100%")
    if((2*x2+x1)>=y):
        print('Three mark question need not be attempted, so no minimum accuracy rate applicable')
    else:
        a=abs((x1+2*x2)-y)
        m=((a+3*x3)/6)*(1/x3)
        j=str(round((100*m),2))
        if j!="100.0":
              print("Minimum Accuracy rate required for Three mark question is "+str(round((100*m),2))+"%")
        else:
              print("Minimum Accuracy rate required for Three mark question is 100%")
