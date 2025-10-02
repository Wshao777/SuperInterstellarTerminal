#!/bin/bash

# --- Lightning Empire: Create Pull Request Script ---
# This script automates the process of creating a new branch,
# committing changes, and opening a pull request on GitHub using the 'gh' CLI.

# --- Colors for output ---
COLOR_RED='\033[0;31m'
COLOR_GREEN='\033[0;32m'
COLOR_BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 1. Check for required tools
if ! command -v gh &> /dev/null
then
    echo -e "${COLOR_RED}Error: 'gh' (GitHub CLI) is not installed.${NC}"
    echo "Please install it following the instructions at https://cli.github.com/"
    exit 1
fi

# 2. Check for a commit message argument
if [ -z "$1" ]; then
  echo -e "${COLOR_RED}Error: Please provide a commit message.${NC}"
  echo "Usage: ./tools/create_pr.sh \"Your commit message\""
  exit 1
fi

COMMIT_MESSAGE=$1
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BRANCH_NAME="feature/update-${TIMESTAMP}"

echo -e "${COLOR_BLUE}[*] Starting Pull Request process...${NC}"

# 3. Create and switch to a new branch
echo -e "[*] Creating new branch: ${BRANCH_NAME}"
git checkout -b ${BRANCH_NAME}

# 4. Add all changes to staging
echo -e "[*] Staging all changes..."
git add .

# 5. Commit the changes
echo -e "[*] Committing with message: '${COMMIT_MESSAGE}'"
git commit -m "$COMMIT_MESSAGE"

# 6. Push the new branch to the remote repository
echo -e "[*] Pushing branch to origin..."
git push --set-upstream origin ${BRANCH_NAME}

# 7. Create the pull request using GitHub CLI
echo -e "[*] Creating Pull Request on GitHub..."
gh pr create --title "$COMMIT_MESSAGE" --body "Automated PR created by create_pr.sh. Please review the changes." --base "main"

if [ $? -eq 0 ]; then
    echo -e "\n${COLOR_GREEN}[+] Successfully created Pull Request!${NC}"
else
    echo -e "\n${COLOR_RED}[-] Failed to create Pull Request. Please check your 'gh' authentication and repository permissions.${NC}"
    exit 1
fi