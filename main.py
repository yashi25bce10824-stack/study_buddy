from subjects import add_subject, show_subjects
from tasks import add_task, list_tasks, mark_task_done
from study_sessions import add_session, show_sessions
from suggestions import give_suggestion
from reports import weekly_report
from utils import get_input, line

# Main menu for the Study Planner application

def main():
    while True:
        line()
        print("STUDY PLANNER MENU")
        line()
        print("1. Add Subject")
        print("2. View Subjects")
        print("3. Add Task")
        print("4. View Tasks")
        print("5. Mark Task as Done")
        print("6. Add Study Session")
        print("7. View Study Sessions")
        print("8. Study Suggestion")
        print("9. Weekly Report")
        print("0. Exit")

        choice = get_input("Enter your choice: ")

        if choice == "1":
            name = get_input("Enter subject name: ")
            add_subject(name)

        elif choice == "2":
            show_subjects()

        elif choice == "3":
            title = get_input("Task title: ")
            subject = get_input("Subject: ")
            due = get_input("Due date: ")
            add_task(title, subject, due)

        elif choice == "4":
            list_tasks()

        elif choice == "5":
            num = int(get_input("Enter task number: "))
            mark_task_done(num)

        elif choice == "6":
            subject = get_input("Subject: ")
            mins = int(get_input("Minutes studied: "))
            add_session(subject, mins)

        elif choice == "7":
            show_sessions()

        elif choice == "8":
            give_suggestion()

        elif choice == "9":
            weekly_report()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()