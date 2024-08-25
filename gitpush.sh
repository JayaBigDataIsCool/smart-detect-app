#!/bin/bash

# Navigate to the project directory
# cd /path/to/your/project   # Uncomment and replace with your project directory if needed

# Stage all changes (new, modified, deleted files)
git add .

# Commit changes with a message
git commit -m "Updating project with latest changes"

# Push to the current branch (HEAD) on the remote repository (origin)
git push origin HEAD

# Output message for confirmation
echo "Changes have been pushed to the remote repository."

