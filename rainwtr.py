inches_str=input("How many inches of rain have fallen:")
inches_int=int(inches_str)
volume=(inches_str/12)*43560
gallons=volume*7.48051945
print(inches_int,"in. rain on 1 acre is",gallons,"gallons")