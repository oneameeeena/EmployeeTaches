# =======================
#   EMPLOYEE TASK SYSTEM
# =======================

task_categories = ["Administrative", "Technical", "Managerial", "Support"]

tasks = []   # each task = {"id":.., "description":.., "deadline":.., "category":..}

def add_task(task_id, description, deadline, category):
    task = {
        "id": task_id,
        "description": description,
        "deadline": deadline,
        "category": category
    }
    tasks.append(task)

def remove_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]

def display_task(task):
    print(f"\nID: {task['id']}")
    print(f"Description: {task['description']}")
    print(f"Deadline: {task['deadline']}")
    print(f"Category: {task['category']}")

def show_all_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return
    print("\n--- ALL TASKS ---")
    for task in tasks:
        display_task(task)

def search_by_description(desc):
    for task in tasks:
        if task["description"] == desc:
            return task
    return None

def search_by_substring(sub):
    return [task for task in tasks if sub.lower() in task["description"].lower()]



assignments = []  # each assignment = {"id":.., "date":.., "employee_id":.., "tasks":[task_ids]}

def add_assignment(assign_id, date, emp_id, task_list):
    assignment = {
        "id": assign_id,
        "date": date,
        "employee_id": emp_id,
        "tasks": task_list
    }
    assignments.append(assignment)

def remove_assignment(assign_id):
    global assignments
    assignments = [a for a in assignments if a["id"] != assign_id]

def assign_task_to_employee(assign_id, task_id):
    for a in assignments:
        if a["id"] == assign_id:
            a["tasks"].append(task_id)
            return
    print("Assignment not found.")

def remove_task_from_employee(assign_id, task_id):
    for a in assignments:
        if a["id"] == assign_id:
            if task_id in a["tasks"]:
                a["tasks"].remove(task_id)

def display_employee_assignments(emp_id):
    print(f"\n--- TASKS FOR EMPLOYEE {emp_id} ---")
    for a in assignments:
        if a["employee_id"] == emp_id:
            print(f"Assignment ID: {a['id']}, Date: {a['date']}, Tasks: {a['tasks']}")

def count_employee_tasks(emp_id):
    total = 0
    for a in assignments:
        if a["employee_id"] == emp_id:
            total += len(a["tasks"])
    return total

def show_all_assignments():
    print("\n--- ALL ASSIGNMENTS ---")
    for a in assignments:
        print(f"\nID: {a['id']}, Date: {a['date']}, Employee: {a['employee_id']}, Tasks: {a['tasks']}")

def count_all_tasks():
    return sum(len(a["tasks"]) for a in assignments)



def menu():
    while True:
        print("""
===========================
     TASK MANAGEMENT
===========================
1. Add Task
2. Remove Task
3. Show All Tasks
4. Search Task by Description
5. Search Task by Substring
6. Add Assignment
7. Assign Task to Employee
8. Remove Task From Employee
9. Show Employee Assignments
10. Count Employee Tasks
11. Show All Assignments
12. Count All Tasks
0. Exit
""")
        choice = input("Enter choice: ")

        if choice == "1":
            i = input("Task ID: ")
            d = input("Description: ")
            dl = input("Deadline: ")
            c = input("Category: ")
            add_task(i, d, dl, c)
        elif choice == "2":
            i = input("Task ID to remove: ")
            remove_task(i)
        elif choice == "3":
            show_all_tasks()
        elif choice == "4":
            d = input("Description: ")
            t = search_by_description(d)
            print("Found:" if t else "Not found.")
            if t: display_task(t)
        elif choice == "5":
            sub = input("Substring: ")
            result = search_by_substring(sub)
            for t in result:
                display_task(t)
        elif choice == "6":
            i = input("Assignment ID: ")
            date = input("Date: ")
            emp = input("Employee ID: ")
            add_assignment(i, date, emp, [])
        elif choice == "7":
            aid = input("Assignment ID: ")
            tid = input("Task ID: ")
            assign_task_to_employee(aid, tid)
        elif choice == "8":
            aid = input("Assignment ID: ")
            tid = input("Task ID: ")
            remove_task_from_employee(aid, tid)
        elif choice == "9":
            emp = input("Employee ID: ")
            display_employee_assignments(emp)
        elif choice == "10":
            emp = input("Employee ID: ")
            print("Total tasks:", count_employee_tasks(emp))
        elif choice == "11":
            show_all_assignments()
        elif choice == "12":
            print("Total tasks in all assignments:", count_all_tasks())
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# <-- uncomment to run the menu when executing the file
