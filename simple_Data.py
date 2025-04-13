import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Kathmandu', 'Pokhara', 'Lalitpur']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic operations
print("\nAverage Age:", df['Age'].mean())
print("\nPeople from Kathmandu:")
print(df[df['City'] == 'Kathmandu'])
