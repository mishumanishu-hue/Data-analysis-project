import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
    "Student": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Math":    [85, 72, 90, 65, 88],
    "Science": [78, 80, 85, 70, 92],
    "English": [88, 65, 75, 80, 85]
}

# Create table from data
df = pd.DataFrame(data)

# Show data on screen
print("===== Student Marks =====")
print(df)

print("\n===== Average Marks =====")
print(df.mean(numeric_only=True))

print("\n===== Highest Math Scorer =====")
print(df.loc[df["Math"].idxmax()])

# Draw bar chart
df.set_index("Student").plot(
    kind="bar",
    figsize=(8, 5),
    color=["#4C72B0", "#DD8452", "#55A868"]
)

plt.title("Student Marks Analysis")
plt.ylabel("Marks")
plt.xlabel("Students")
plt.tight_layout()
plt.savefig("marks_chart.png")
plt.show()

print("\nChart saved successfully!")