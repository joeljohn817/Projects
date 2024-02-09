import csv

# list of ages, regions, and insurance_costs
ages = []
regions = []
insurance_costs = []

#opening insurance.csv
with open('insurance.csv') as insurance_csv:
    insurance_dict = csv.DictReader(insurance_csv)

# appending data to lists
    for row in insurance_dict:
        insurance_costs.append(row['charges'])
        ages.append(row['age'])
        regions.append(row['region'])
       
        
def medical_data_analysis():
    # Initialize total age and total insurance cost
    total_age = 0
    total_insurance_cost = 0
    
    # total number of records
    num_records = len(ages)
    
    # calculating total, average, max and min ages
    for age in ages:
        total_age+= int(age)

    average_age = total_age / num_records
    max_age = max(ages)
    min_age = min(ages)

    
    # calculating total and average insurance costs
    for cost in insurance_costs:
        total_insurance_cost += float(cost)

    average_cost = round(total_insurance_cost/ num_records, 2)
   

    #individuals by region
    location_southwest = 0
    location_southeast= 0
    location_northwest = 0
    location_northeast = 0

    for region in regions:
        if region == 'southwest':
            location_southwest += 1
        elif region == 'southeast':
            location_southeast +=1
        elif region == 'northwest':
            location_northwest +=1
        elif region == 'northeast':
            location_northeast +=1
    
   
    
    # Print  Results
    print('There are {} records in the inusurance csv file'.format(num_records))
    print('The total insurance cost is $ {} and the average cost is $ {}'.format(round(total_insurance_cost,2), average_cost))
    print('The average age is {}.'.format(average_age))
    print('The maximum age is {} and the minimum age is {}.'.format(max_age, min_age))
    print('There are {} people from southwest, {} people from southeast, {} people for northwest and {} people from northeast'.format(location_southwest, location_southeast, location_northwest, location_northeast))            
   
medical_data_analysis()
