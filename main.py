import subprocess
import sys

# Read the content from the txt file
with open('repository_branches.txt', 'r') as file:
    lines = file.readlines()

# Iterate over each line
for line in lines:
    # Split the line to get repository, branch, and commit information
    repository, branch, commit = line.strip().split()

    print(f"Repository: {repository}")
    print(f"Branch: {branch}")
    print(f"Commit: {commit}")

    try:
        # Change to the specified repository directory and switch to the specified branch
        subprocess.run(f'cd /D "{repository}" && git checkout {branch}', shell=True, check=True)

        # Reset to the specified commit
        subprocess.run(f'cd /D "{repository}" && git reset --hard {commit}', shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing Git command in repository: {repository}")
        sys.exit(1)

# Print success message and add two newlines
print("\n\n")
print("****************************************")
print("All repositories processed successfully.")
print("****************************************")
print("\n\n")