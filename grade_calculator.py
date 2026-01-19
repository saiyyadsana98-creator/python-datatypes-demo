
try:
    marks = float(input("Enter your marks (0-100): "))

    if marks < 0 or marks > 100:
        print("❌ Invalid marks! Marks must be between 0 and 100.")

    else:
       
        if marks >= 90 and marks <= 100:
            grade = "A+"
            message = "Excellent performance"

        elif marks >= 75 and marks < 90:
            grade = "A"
            message = "Very good performance"

        elif marks >= 60 and marks < 75:
            grade = "B"
            message = "Good performance"

        elif marks >= 40 and marks < 60:
            grade = "C"
            message = "Average performance"

        else:
            grade = "F"
            message = "Fail - Needs improvement"

    
        print("✅ Grade:", grade)
        print("📢 Message:", message)

except ValueError:
    print("❌ Invalid input! Please enter numeric values only.")
