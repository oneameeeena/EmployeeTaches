# Employee Task Management System

This project is a simple Python program that manages employee tasks and assignments.  
It allows adding tasks, searching for them, and assigning them to employees with deadlines.

---

## 📁 Project Features

### ✅ 1. Task Categories
The system contains predefined task categories:
- Administrative  
- Technical  
- Managerial  
- Support  

---

## 📝 2. Task Management

Each task contains:
- **ID**
- **Description**
- **Deadline**
- **Category**

### Implemented functions:
| Function | Description |
|----------|-------------|
| `add_task()` | Adds a new task to the task list |
| `remove_task()` | Deletes a task by ID |
| `display_task()` | Shows information about a single task |
| `show_all_tasks()` | Displays all stored tasks |
| `search_by_description()` | Searches for a task by exact description |
| `search_by_substring()` | Searches for tasks that match part of a description |

---

## 👨‍🔧 3. Employee Assignments

Each assignment contains:
- **ID**
- **Date**
- **Employee ID**
- **List of assigned task IDs**

### Implemented functions:
| Function | Description |
|----------|-------------|
| `add_assignment()` | Adds a new assignment |
| `remove_assignment()` | Deletes an assignment |
| `assign_task_to_employee()` | Assigns a task to an employee |
| `remove_task_from_employee()` | Removes a task from an employee’s assignment |
| `display_employee_assignments()` | Shows tasks assigned to a specific employee |
| `count_employee_tasks()` | Counts the number of tasks assigned to an employee |
| `show_all_assignments()` | Displays all assignments |
| `count_all_tasks()` | Returns the total number of assigned tasks |

---

## 🖥️ 4. Interactive Menu

The program includes a simple menu system that allows you to:
- Add/Delete tasks  
- Search for tasks  
- Assign tasks to employees  
- Display and manage assignments  
- Count tasks per employee or globally  

To run the menu, uncomment the following line at the bottom of the script:

```python
menu()
