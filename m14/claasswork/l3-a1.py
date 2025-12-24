import matplotlib.pyplot as plt

# Student data
students_names = ["Sanjay", "Rahul", "Karan", "Wasim", "Ramesh", "Ajay", "Sartaj", "Priya"]
students_marks = [35, 50, 20, 45, 25, 40, 25, 40]

# Calculate percentage (assuming total marks = 50)
marks_perc = [(marks / 50) * 100 for marks in students_marks]

# Line chart for raw marks
def marks_line_chart():
    plt.plot(students_names, students_marks, marker='o', linestyle='-', color='blue')
    plt.title("Students Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Marks out of 50")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Bar chart for percentage
def percentage_bar_chart():
    plt.bar(students_names, marks_perc, color='green')
    plt.title("Students Percentage Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run both charts
marks_line_chart()
percentage_bar_chart()