first_ten = [[0,0,1],[0,0,2],[0,1,1],[0,1,2],[0,2,1],[0,2,2],[0,3,1],[0,3,2],[1,1,2],[1,2,1]] 
def print_config(config):
    total = config[0]+config[1]+config[2];
    print(str(total) + " " + str(config[0])+" "+str(config[1])+" "+str(config[2]))
n=int(input())
if(n<10):
    print_config(first_ten[n-1]);
else:
    config=[0]*3
    counter_five = 0;
    remainder = 0;
    if(n%10 == 0):
        counter_five = (n-10)//5
        config = first_ten[9]
        config[0]+= counter_five
    elif(n%10 < 5):
        counter_five = (n-(n%10)-5)//5
        config = first_ten[n%10+5-1]
        config[0]+= counter_five
    elif(n%10>=5):
        counter_five = (n-(n%10))//5
        config = first_ten[n%10-1]
        config[0]+= counter_five
    print_config(config)
