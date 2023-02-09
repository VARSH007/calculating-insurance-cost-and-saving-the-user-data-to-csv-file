import pandas as pd

def estimate_insurance_cost(age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    return estimated_cost

customer_data = pd.DataFrame(columns=["Name","Age","Sex","BMI","Children","Smoker","Estimated Cost"])


count = 0
max_users = int(input("Enter the number of users you want to enter data for: "))

while count < max_users:
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    sex = int(input("What is your sex?(Enter 0 for Female, 1 for Male) "))
    bmi = float(input("What is your BMI? "))
    num_of_children = int(input("How many children do you have? "))
    smoker = int(input("Do you smoke?(Enter 0 for No, 1 for Yes) "))

    estimated_cost = estimate_insurance_cost(age, sex, bmi, num_of_children, smoker)
    print("{}'s Estimated Insurance Cost: {} dollars.".format(name, estimated_cost))

    customer_data.loc[len(customer_data)] = [name,age,sex,bmi,num_of_children,smoker,estimated_cost]
    count +=1

print(customer_data)
customer_data.to_csv("customer_data.csv")
