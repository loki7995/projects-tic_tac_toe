import pandas as pd
import plotly.express as px

# Load dataset
file_path = input("Enter CSV file path: ")
data = pd.read_csv(file_path)

print("\nDataset Preview:")
print(data.head())

print("\nAvailable Columns:")
print(list(data.columns))

# User input for visualization
chart_type = input("\nEnter chart type (line/bar/scatter/hist): ").lower()

if chart_type == "hist":
    column = input("Enter column name for histogram: ")
    fig = px.histogram(data, x=column, title=f"Histogram of {column}")

else:
    x_col = input("Enter X-axis column: ")
    y_col = input("Enter Y-axis column: ")

    if chart_type == "line":
        fig = px.line(data, x=x_col, y=y_col, title=f"Line Chart: {x_col} vs {y_col}")

    elif chart_type == "bar":
        fig = px.bar(data, x=x_col, y=y_col, title=f"Bar Chart: {x_col} vs {y_col}")

    elif chart_type == "scatter":
        fig = px.scatter(data, x=x_col, y=y_col, title=f"Scatter Plot: {x_col} vs {y_col}")

    else:
        print("Invalid chart type")
        exit()

# Show interactive plot
fig.show()
#OUTPUT
'''
Enter CSV file path: cognify_tasks\Level 3\student.csv

Dataset Preview:
   RollNo    Name  Marks
0       1  Lokesh     85
1       2    Ravi     78
2       3   Anita     92
3       4   Sneha     88

Available Columns:
['RollNo', 'Name', 'Marks']

Enter chart type (line/bar/scatter/hist): line
Enter X-axis column: RollNo
Enter Y-axis column: Marks
'''
