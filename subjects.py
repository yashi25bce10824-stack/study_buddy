from storage import load_data, save_data

# This file handles adding subjects and showing the list of subjects.

def add_subject(name):
    data = load_data()

    # Just add the name of the subject to the list
    data["subjects"].append({"name": name})

    save_data(data)
    print(f"Subject '{name}' added.")

def show_subjects():
    data = load_data()
    subs = data.get("subjects", [])

    if len(subs) == 0:
        print("No subjects found. Add some first!")
        return

    print("\nYour Subjects:")
    for i, s in enumerate(subs, start=1):
        print(f"{i}. {s['name']}")