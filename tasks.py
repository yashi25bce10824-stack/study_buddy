from storage import load_data, save_data

# This file deals with tasks (adding, showing and marking done).

def add_task(title, subject, due):
    data = load_data()

    # Creating a simple task dictionary
    task = {
        "title": title,
        "subject": subject,
        "due": due,
        "done": False
    }

    data["tasks"].append(task)
    save_data(data)
    print("Task added successfully!")

def list_tasks():
    data = load_data()
    all_tasks = data.get("tasks", [])

    if len(all_tasks) == 0:
        print("No tasks yet.")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(all_tasks, start=1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['title']} ({t['subject']}) - Due: {t['due']} - {status}")

def mark_task_done(number):
    data = load_data()
    number = number - 1  # converting to 0 index

    # simple validation
    if number < 0 or number >= len(data["tasks"]):
        print("Invalid task number.")
        return

    data["tasks"][number]["done"] = True
    save_data(data)
    print("Task marked as done!")