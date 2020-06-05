#Sears.py
#Determines how many days and dollar bills it would take to reach the height of the Sears Tower
#Each day, the double number of bills is placed on the previous stack

bill_Thickness = 0.11 * 0.001
sears_Height = 442
num_Bills = 1
num_Days = 1

while num_Bills * bill_Thickness < sears_Height:
    print (num_Days, num_Bills, num_Bills * bill_Thickness)
    num_Days = num_Days + 1
    num_Bills = num_Bills * 2


print ('Number of days', num_Days)
print ('Number of Bills', num_Bills)
print ('Final Height', num_Bills * bill_Thickness)