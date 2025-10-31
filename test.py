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
                if key in row:  # Avoid KeyError if column is missing
                    value = row[key].strip()
                    data[key].append(datatype(value) if value else None)
    
    return data

data = load_data('titanic_clean.csv', types)

def summarize(data: dict):
    '''
    Summarizes the data associated with each key of the data dictionary.
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
            most_common_value = max(frequency, key=frequency.get) if frequency else "N/A"
            
            print(f"Number of unique values: {unique_count}")
            print(f"Most common value: {most_common_value}")
        
        else:
            numeric_values = [x for x in data[item] if x is not None]  # Remove None values
            
            if numeric_values:  # Check if list is not empty
                print(f"Min: {min(numeric_values)}")
                print(f"Max: {max(numeric_values)}")
                print(f"Mean: {statistics.mean(numeric_values)}")
                print(f"Standard deviation: {statistics.stdev(numeric_values) if len(numeric_values) > 1 else 'N/A'}")
                
                try:
                    print(f"Mode: {statistics.mode(numeric_values)}")
                except statistics.StatisticsError:
                    print("Mode: No unique mode found")
            else:
                print("No valid numeric data available")

summarize(data)  # Removed print(summarize(data))