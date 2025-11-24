def average_marks(*marks):
    if len(marks) == 0:
        print("No marks provided.")
        return
    total = sum(marks)
    average = total / len(marks)
    print("Average marks of", len(marks), "students is:", average)

# Example usage:
average_marks(75, 82, 91, 68, 89)  # You can pass any number of student marks