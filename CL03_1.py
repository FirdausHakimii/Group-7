a_int = int(input("Give a number: "))                  #Input save into a_int
b_int ,c_int = 1,0                                     #Initial b_int and c_int values
while b_int <= a_int :                                 #The while loop - will compare b and a 
        c_int = c_int + b_int                          #if true, increment c with b
        b_int = b_int + 1                              #if true, increamnt b with 1
print (a_int,b_int,c_int)                              #Display a,b and c values
print ("Result: ", float(c_int)/b_int - 1)             #Diplay result
        #CL03-1.py
