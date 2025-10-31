'''
Author: Ashton Curl
Project 7 02/19/2024
Titanic
'''
import statistics
import matplotlib.pyplot as plt
import csv
# ============Functions================
# 3.1:
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

# data = load_data('titanic_clean.csv', types)
#----------------------
# 3.2:
def summarize(data: dict):
    '''
    Summarizes the data associated with each key of the data dictionary.
    '''
    for item in data:
        first_value = data[item][0]  # Directly get the first value to determine type

        print(f"Statistics for {item}:")
        
        # Numeric column
        if isinstance(first_value, (int, float)):
            #get all stats
            print(f"Min: {min(data[item])}")
            print(f"Max: {max(data[item])}")
            print(f"Mean: {statistics.mean(data[item]):.2f}")
            print(f"Standard deviation: {statistics.stdev(data[item]) if len(data[item]) > 1 else 'N/A'}")
            print(f"Mode: {statistics.mode(data[item])}")

        # String column    
        else:  
            #Find most frequent value
            frequency = {}
            for value in data[item]:
                frequency[value] = frequency.get(value, 0) + 1
            
            most_common_value = max(frequency, key=frequency.get)
            print(f"Number of unique values: {len(frequency)}")
            print(f"Most common value: {most_common_value}")

# print(summarize(data))
#----------------------
# 3.3:
def pearson_corr(x:list,y:list)->float:
    """
    Takes two lists of numerical values and returns the Pearson 
    correlation coefficient.
    """
    # Ensure inputs are lists of numbers
    if not all(isinstance(i, (int, float)) for i in x + y):
        raise ValueError("Both lists must contain only integers or floats.")

    # Ensure lists have the same length
    if len(x) != len(y):
        raise ValueError("Both lists must have the same length.")

    x_average            = statistics.mean(x)
    y_average            = statistics.mean(y)
    x_standard_deviation = statistics.stdev(x)
    y_standard_deviation = statistics.stdev(y)
    num   = 0.0
    for i in range(len(x)):
        num = num + (x[i] - x_average) * (y[i] - y_average)
    correlation = num / ((len(x) - 1) * x_standard_deviation * y_standard_deviation)
    return round(correlation, 2)
#----------------------
# 3.4:
def survivor_vis(data:dict,col_1:tuple,col_2:tuple)->plt:
    # Create a new figure with specified size
    figure = plt.figure(figsize=(8, 4))
    
    # Get the data for the specified columns
    x_data = data[col_1[0]]  # Column for x-axis
    y_data = data[col_2[0]]  # Column for y-axis

     # Get survival data
    survived = data['Survived']

    # survivors:
    plt.scatter(
        [x for i, x in enumerate(x_data) if survived[i] == 1],  # X values for survivors
        [y for i, y in enumerate(y_data) if survived[i] == 1],  # Y values for survivors
        color='green', label='Survivors', alpha=0.6, edgecolors='w', s=100, marker='o'
    )

    # Non-survivors:
    plt.scatter(
        [x for i, x in enumerate(x_data) if survived[i] == 0],  # X values for non-survivors
        [y for i, y in enumerate(y_data) if survived[i] == 0],  # Y values for non-survivors
        color='red', label='Nonsurvivors', alpha=0.6, edgecolors='w', s=100, marker='x'
    )

    #Labels
    plt.xlabel(col_1[0])
    plt.ylabel(col_2[0])

    #Title:
    plt.title('Survival Visualization in Titanic Dataset')

    #ledgend:
    plt.legend()

    # Show the plot
    plt.show()  # Display the plot
    return figure
# =================Don't modify main other than for the many bugs=================
def main():
    """Main program driver for Project 3."""

    # 3.1 Load the dataset
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('titanic_clean.csv', titanic_types)

    # 3.2 Print informative summaries
    print("\nPart 3.2")
    summarize(data)

    print("\nPart 3.3")
    # 3.3 Compute correlations between age and survival
    corr_age_survived = pearson_corr(data[('Age')],
                                     data[('Survived')])
    print(f'Correlation between age and survival is {corr_age_survived:3.2f}')

    # 3.3 Correlation between fare and survival
    corr_fare_survived = pearson_corr(data[('Fare')],
                                      data[('Survived')])
    print(f'Correlation between fare and survival is {corr_fare_survived:3.2f}')

    # 3.3 Correlation between family size and survival
    corr_fare_survived = pearson_corr(data[('FamilySize')],
                                      data[('Survived')])
    print(f'Correlation between family size and survival is'
          f' {corr_fare_survived:3.2f}')

    # 3.4 Visualize results
    fig = survivor_vis(data, ('Age', float), ('Fare', float))
    fig = survivor_vis(data, ('Age', float), ('Pclass', int))
    fig = survivor_vis(data, ('Age', float), ('Parch', int))


if __name__ == "__main__":
    main()
