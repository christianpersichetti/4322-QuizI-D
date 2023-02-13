'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile= open('employee_data.csv', 'r')


#create an empty dictionary
employees = []

#use a loop to iterate through the csv file

csvreader = csv.reader(infile, delimiter= (','))

next(csvreader)

#print(f"Manager Name: " + " " + "Current Salary: "+ '\n')
name = [1] + [2]
current_salary = int([5])
new_salary = 0.10*(current_salary) + current_salary

for row in infile:
    if current_salary == current_salary:
        print(f"Manager Name: ", name ,' ' , "Current Salary: ", current_salary, '\n')

for row in infile:
    if new_salary == new_salary:
        print(f"Manager Name: ", name, ' ', "New Salary: ", new_salary, '\n')


print()
print('=========================================')
print() 

infile.close()
    
    
    
#check if the employee fits the search criteria

    

#iternate through the dictionary and print out the key and value as per printout

    
        

        
    
