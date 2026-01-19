student = { 
    "id": "2025-001", 
    "name": "Juan Dela Cruz", 
    "grades": [88, 90, 85] 
} 

# Manipulation
student["grades"].append(95)  # Add grade
student["name"] = "Juan Q. Dela Cruz"  # Update info

# Logic
avg = sum(student["grades"]) / len(student["grades"])

# Output
print("--- Student Record System ---")
print(f"ID:      {student['id']}")
print(f"Name:    {student['name']}")
print(f"Grades:  {student['grades']}")
print(f"Average: {avg:.2f}")