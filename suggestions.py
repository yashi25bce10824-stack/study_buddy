from storage import load_data

# This file gives small study suggestions
# based on what the student has studied so far.

def give_suggestion():
    data = load_data()
    sessions = data.get("sessions", [])

    if len(sessions) == 0:
        print("You haven't studied anything yet. Start with any subject for at least 20 minutes.")
        return

    # Count minutes studied for each subject
    subject_time = {}
    for s in sessions:
        subj = s["subject"]
        mins = s["minutes"]
        subject_time[subj] = subject_time.get(subj, 0) + mins

    # Find the subject with least study time
    weakest = min(subject_time, key=subject_time.get)

    print(f"You should focus more on: {weakest}.")
    print("Try to study it for at least 30 minutes today.")