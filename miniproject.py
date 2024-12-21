import pandas as pd
import matplotlib.pyplot as plt

class StudentPerformanceAnalyzer:
    def __init__(self):
        self.data = pd.DataFrame(columns=['Name', 'Grade'])

    def add_student(self, name, grade):
        self.data = self.data.append({'Name': name, 'Grade': grade}, ignore_index=True)

    def analyze_performance(self):
        if self.data.empty:
            print("No student data available.")
            return
        
        print("Student Performance Analysis:")
        print(f"Total Students: {len(self.data)}")
        print(f"Average Grade: {self.data['Grade'].mean():.2f}")
        print(f"Highest Grade: {self.data['Grade'].max()}")
        print(f"Lowest Grade: {self.data['Grade'].min()}")
        
        grade_distribution = self.data['Grade'].value_counts().sort_index()
        print("\nGrade Distribution:")
        print(grade_distribution)

        self.visualize_performance(grade_distribution)

    def visualize_performance(self, grade_distribution):
        plt.figure(figsize=(10, 5))
        grade_distribution.plot(kind='bar', color='skyblue')
        plt.title('Grade Distribution')
        plt.xlabel('Grades')
        plt.ylabel('Number of Students')
        plt.xticks(rotation=0)
        plt.grid(axis='y')
        plt.show()

def main():
    analyzer = StudentPerformanceAnalyzer()
    
    while True:
        name = input("Enter student name (or 'exit' to finish): ")
        if name.lower() == 'exit':
            break
        try:
            grade = float(input(f"Enter grade for {name}: "))
            analyzer.add_student(name, grade)
        except ValueError:
            print("Invalid grade. Please enter a numeric value.")

    analyzer.analyze_performance()

if __name__ == "__main__":
    main()