python function

1)in-build function2)user defiend function

#function is a block of code.when the function is call block of code will be executed..
##different between parameter and arguments 1)we passing a parameter in the form of variable in a parentisis when the function is defiend 2)and when the function is call we passing a arguments in the fome of a value.....


#without passing a value 

#function definition...
def printinfo():
    print("my name is rumit")
    
#function call.... 
printinfo() 


#passing a parameter and argument in function

def showinfo(name,age):
    print('my name is "{}" and my age is "{}". '.format(name,age))
a =showinfo('rumit',21)

##type of function objects...
print(type(a))



#function insided function...
def first():
    a =int(input("enter a number: "))
    newfun(a)
def newfun(number):
    i =0
    while number>i:
        print(i)
        i =i+1
        
        
 # Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

#This way the function will receive a tuple of arguments, and can access the items accordingly:
#example
def print_data(*args):
    print('my name is "{}" and my age is "{}". '.format(args[0],args[1]))
    
    
#keyword argument:
def print_data1(name,age,mobile):
    print("my name is [{}] and age is [{}] and mobile nu is [{}].".format(name,age,mobile))
print_data1(name ="rumit",age =21,mobile =9925881941)    



#Arbitrary Keyword Arguments, **kwargs

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

#This way the function will receive a dictionary of arguments, and can access the items accordingly:

def print_data2(**rumit):
    print("my name is [{}] and age is [{}]".format(rumit['name'],rumit['age']))
    
print_data2(name ='rumit',age =21)    



#default parameter
def print_data3(default ='rumit'):
    print("my name is "+ default)
print_data3("vishal")
print_data3()
print_data3("jay")


#Passing a List or any ... as an Argument

#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

a =['rumit','21']
def print_data4(a):
    for i in a:
        print(i)
print_data4({1:'rumit',2:'vishal'}) 



#function inside other function creation.....
def myname():
    print("hi")
    
    def hello():
        print("hey")
        
myname()


#make a calcualter using function .....
#what ever value you wont to perfome to do operations...
l1 =[]
l2 =[]
def calculater():
    print("welcome bro..")
    value()
def value():
    a =int(input("how many value you wont to perfom the arthmetics operations: "))
    choise =int(input("1 for add 2  for mul 3 for sub 4 for div: "))
    l2.append(choise)
    take_value(a)
    
def take_value(a):
    for i in range(a):
        values =int(input("enter a valur one by one: "))
        if l2[0]==1:
            Add(values)
            if len(l1)==a:
                total =0   
                for j in l1:
                    total =total+j
                print(total)
            else:
                continue
        elif l2[0]==2:
            Mul(values)
            if len(l1)==a:
                mul =1
                for j in l1:
                    mul =mul*j
                print(mul)
            else:
                continue
        elif l2[0]==3:
            Sub(values)
            if len(l1)==a:
                sub =0
                for j in l1:
                    if sub==0:
                        sub =j-sub
                    else:
                        sub =sub-j
                print(sub)
            else:
                continue
        elif l2[0]==4:
            Div(values)
            if len(l1)==a:
                div =1
                for j in l1:
                    if div==1:
                        div =j/div
                    else:
                        div =div/j 
                print(div)
            else:
                continue  
                
def Add(values):
    l1.append(values) 
    
def Mul(values):
    l1.append(values)    

def Sub(values):
    l1.append(values) 

def Div(values):
    l1.append(values) 
