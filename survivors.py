import matplotlib.pyplot as plt
import csv
from collections import Counter
from titanic import load_data

def load_data(file_name: str, types: dict) -> dict:
    """Load Titanic dataset from CSV into a dictionary."""
    data = {key: [] for key in types}
    with open(file_name, 'r', encoding='utf8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key in types:
                data[key].append(types[key](row[key]))
    return data

def plot_survivors_by_category(data: dict, category: str):
    """Plot survivor counts and percentages by a given category."""
    category_counts = Counter(data[category])
    survivor_counts = Counter([data[category][i] for i in range(len(data['Survived'])) if data['Survived'][i] == 1])
    
    categories = list(category_counts.keys())
    total_counts = [category_counts[cat] for cat in categories]
    survived_counts = [survivor_counts.get(cat, 0) for cat in categories]
    
    survival_percentages = [s / t * 100 for s, t in zip(survived_counts, total_counts)]
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    axes[0].bar(categories, survived_counts, color='green', alpha=0.7, label='Survivors')
    axes[0].bar(categories, [t - s for t, s in zip(total_counts, survived_counts)], bottom=survived_counts, color='red', alpha=0.7, label='Non-Survivors')
    axes[0].set_title(f'Survivor Counts by {category}')
    axes[0].set_ylabel('Count')
    axes[0].legend()
    
    axes[1].bar(categories, survival_percentages, color='blue', alpha=0.7)
    axes[1].set_title(f'Survival Percentage by {category}')
    axes[1].set_ylabel('Survival Rate (%)')
    
    plt.savefig(f'survival_by_{category}.png')
    plt.show()

if __name__ == "__main__":
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int, 'Sex': str, 'Age': float,
                     'SibSp': int, 'Parch': int, 'Fare': float, 'Embarked': str, 'FamilySize': int, 'age_group': str}
    data = load_data('titanic_clean.csv', titanic_types)
    plot_survivors_by_category(data, 'Sex')  # Example: Plot survival by gender


'''
AI Use Documentation:

Used Chat GPT to find a faster way to count the occurences of the items in categories

My prompt: 
    what is the fastest way to return a dictionary with the number 
of occurrences of an item in a list?

Response: 
    The fastest way to return a dictionary with the number of 
occurrences of an item in a list is by using the Counter class from the 
collections module. Counter is optimized for this task and implemented in C,
 making it significantly faster than manual iteration.
 
'''