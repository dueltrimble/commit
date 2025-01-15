# | ---------------------------------------------------------- |
# | Commits to the git repository and enforces the 50/72 rule. |
# | ---------------------------------------------------------- |

import os
import json
import subprocess as sp

# The commit dictionary that is saved and loaded as JSON.
commit_obj = {

    'Title':        'Hello, world!',
    'Description':  'This is the default commit message!'
}

# The path that the dictionary should be saved to.
commit_json_path = '../.git/commit.json'

# If the file exists, delete it.
if os.path.exists(commit_json_path):
    os.remove(commit_json_path)

# Converts the dictionary into JSON.
commit_json = json.dumps(commit_obj, indent=2)

# Saves the dictionary as a file.
with open(commit_json_path, 'w') as file:
    file.write(commit_json)

# Opens the dictionary in Notepad++ and waits for it to close.
sp.call(['C:/Program Files/Notepad++/notepad++.exe', commit_json_path])

# Loads the dictionary that was presumably edited while 
# Notepad++ was open.
with open(commit_json_path) as file:
    commit_obj = json.load(file)

# Limit the title to 50 characters.
new_commit_title = commit_obj['Title'][:50]
if len(new_commit_title) > 50:
    print('The following characters were removed from the title: ' 
    + commit_obj['Title'][50:])

# Limit each line in the description to 72 characters.
new_commit_desc = ''
for i in range(0, len(commit_obj['Description']), 72):
    new_commit_desc += (commit_obj['Description'][i:i+72]).strip() + '\n'

# Execute the git commit command.
sp.run(['git.exe', 'commit', 
'-m', new_commit_title,
'-m', new_commit_desc], cwd="../")

# If the file exists, delete it again.
if os.path.exists(commit_json_path):
    os.remove(commit_json_path)
