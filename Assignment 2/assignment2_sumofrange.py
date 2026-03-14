#Task 2: Sum of Integers from 1 to 50 Using a Loop

#Intialize a variable of type int with 0
sum_of_elements=0

#Start a for loop to run from 1to 50
for i in range(1,51):
    sum_of_elements= sum_of_elements + i          #add each element in the loop to the prev element

print("The sum of numbers from 1 to 50 is ", sum_of_elements)