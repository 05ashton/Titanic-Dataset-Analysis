'''
Authors: Carter Gladden and Ashton Curl
Project 7 02/19/2024
Titanic
'''
import statistics
import matplotlib.pyplot as plt
import csv

types = {
    'PassengerId': int,
    'Survived': int,
    'Pclass': int,
    'Sex': str,
    'Age': float,
    'SibSp': int,
    'Parch': int,
    'Fare': float,
    'Embarked': str,
    'FamilySize': int,
    'age_group': str
}


def load_data(file_name: str, types: dict) -> dict:
    """
    Loads Titanic data from a CSV file and converts columns based on the provided types.
    """
    data = {key: [] for key in types}
    
    with open(file_name, 'r', encoding='utf8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key, datatype in types.items():
                value = row[key].strip()
                data[key].append(datatype(value) if value else None)
    
    return data

#load_data('titanic_clean.csv', types)

data = load_data('titanic_clean.csv', types)


def summarize(data: dict):
    '''
    Summarizes the data associated with each key of the data dictionary
    For Integer and float type values, prints the min, max, mean, 
    standard deviation and mode
    For string type values, prints the number of unique values and the
    most common value
    '''
    
    for item in data:
        print(f"Statistics for {item}:")
        if types[item] == str:
            frequency = {}  
    
            for value in data[item]:
                if value in frequency:
                    frequency[value] += 1
                else:
                    frequency[value] = 1
            unique_count = len(frequency)
            print(f"Number of unique values: {unique_count}")
            most_common_value = max(frequency, key = frequency.get)
            print(f"Most common value: {most_common_value}")
        else:
            print(f"Min: {min(data[item])}")
            print(f"Max: {max(data[item])}")
            print(f"Mean: {statistics.mean(data[item])}")
            print(f"Standard deviation: {statistics.stdev(data[item])}")
            print(f"Mode: {statistics.mode(data[item])}")

print(summarize(data))
