#inital setup/commit is left blank on purpose for start of project 

# Project Scope:
# Project is filled with a data sample of medical insurance participates
# Step 0: What is the problem? Understand various attributes inside data about patient information
# Step 1: Goals - Complete all necessary pieces and answer any questions about dataset
# Step 2: Actions - No actions needed
# Step 3: Data - Data provided. Needed a larger sample size for analysis
# Step 4: Analysis - Description and detection
# Additional Considerations - 

import csv

# numerical and categorical values these are the variables, create empty lists to store data
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

# import data from csv with helper function

def load_list_data(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst
    
load_list_data(ages, "insurance.csv", 'age')
# print(ages)
load_list_data(sexes, "insurance.csv", 'sex')
# print(sexes) 
# tests successful continue to load other csv information
load_list_data(bmis, "insurance.csv", 'bmi')
load_list_data(num_children, "insurance.csv", 'children')
load_list_data(smoker_statuses, "insurance.csv", 'smoker')
load_list_data(regions, "insurance.csv", 'region')
load_list_data(insurance_charges, "insurance.csv", 'charges')

#analysis can begin

def average_age(list):
    age_counter = 0
    
    for age in list:
        age_counter += int(age)
    print(f"Average age is {round(age_counter/len(ages), 2)} years")

average_age(ages)
