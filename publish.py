"""
publish.py - sends your latest PianoMind Studios changes to GitHub.
GitHub Pages then updates the live site in a minute or two.

How to use: double-click this file, or run  python publish.py
"""
import subprocess
import os
from datetime import datetime

# Always work inside the folder this file lives in.
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def run(cmd):
    """Run one git command, show what it says, and return its result."""
    print("\n> " + " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    print((result.stdout + result.stderr).strip())
    return result


print("=== Publish PianoMind Studios ===")

# 1. Is there anything new to send?
status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
if status.returncode != 0:
    print("\nThis folder is not a git project, or git is not installed.")
    print(status.stderr)
elif not status.stdout.strip():
    print("\nNothing changed since the last publish. Nothing to send.")
else:
    print("\nChanged files:")
    print(status.stdout)

    # 2. A short note about what changed. Press Enter to use a date instead.
    message = input("What did you change? (press Enter to skip): ").strip()
    if not message:
        message = "Update " + datetime.now().strftime("%Y-%m-%d %H:%M")

    # 3. Stage, commit, push.
    run(["git", "add", "."])
    commit = run(["git", "commit", "-m", message])
    if commit.returncode == 0:
        push = run(["git", "push"])
        if push.returncode == 0:
            print("\nDone! The live site updates in about 1-2 minutes.")
            print("Then press Ctrl+Shift+R on the site to see it.")
        else:
            print("\nPush failed. Read the message above, or copy it to Claude.")
    else:
        print("\nCommit failed. Read the message above, or copy it to Claude.")

input("\nPress Enter to close this window.")
