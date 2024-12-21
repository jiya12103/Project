class StudentPerformanceAnalyzer:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append({'Name': name, 'Grade': grade})

    def analyze_performance(self):
        if not self.students:
            print("No student data available.")
            return
        
        total_students = len(self.students)
        grades = [student['Grade'] for student in self.students]
        average_grade = sum(grades) / total_students
        highest_grade = max(grades)
        lowest_grade = min(grades)

        print(f"\nTotal Students: {total_students}")
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Highest Grade: {highest_grade}")
        print(f"Lowest Grade: {lowest_grade}")
        
        self.display_grade_distribution(grades)

    def display_grade_distribution(self, grades):
        # Display grade distribution as simple text
        grade_counts = {}
        for grade in grades:
            grade_counts[grade] = grade_counts.get(grade, 0) + 1
        
        print("\nGrade Distribution:")
        for grade, count in sorted(grade_counts.items()):
            print(f"Grade {grade}: {count} student(s)")

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
