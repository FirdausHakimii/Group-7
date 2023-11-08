a_int = int(input("Give a number: "))
b_int ,c_int = 1,0 
while b_int <= a_int :
        c_int = c_int + b_int
        b_int = b_int + 1 
print (a_int,b_int,c_int) 
print ("Result: ", float(c_int)/b_int - 1) 
        #CL03-1.py
