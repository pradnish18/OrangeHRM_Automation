import random
import time

def generate_employee_list(count=4):
    """Generates unique test employee names to avoid duplicate collisions."""
    timestamp = int(time.time()) % 10000
    first_names = ["Alex", "Bella", "Charlie", "Diana", "Evan", "Fiona", "George", "Hannah"]
    last_names = ["Turner", "Smith", "Davis", "Evans", "Miller", "Wilson", "Taylor", "Anderson"]
    
    employees = []
    selected_firsts = random.sample(first_names, count)
    selected_lasts = random.sample(last_names, count)
    
    for i in range(count):
        emp_id = f"9{timestamp}{i+1:02d}"
        employees.append({
            "first_name": selected_firsts[i],
            "middle_name": "QA",
            "last_name": f"{selected_lasts[i]}{i+1}",
            "emp_id": emp_id
        })
    return employees
