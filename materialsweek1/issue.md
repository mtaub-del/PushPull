# "Git commit" and VIM
To commit every change made in a session you need "git commit -m "-" .
It is important to not write just "git commit" such that we dont end in the text editor VIM

# Problem: 
You used "git commit"
# Result: 
VIM text editor is opened
# Solution: 
use: "git commit -m "description of change" and to leave VIM press escape and use :q! to leave the editor
# Result: 
git saves every change that was added to the stage