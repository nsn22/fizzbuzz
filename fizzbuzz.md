# Git Script Demo
git clone https://github.com/yourname/fizzbuzz-10-sol.git

## Fizzbuzz Solution 1
```python
for i in range(1,101):
    if(i % 5 == 0 and i % 3 == 0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)
```

## Fizzbuzz Solution 2
```python
for i in range(1,101):
    output = ""
    if(i % 3 == 0):
        output += "Fizz"
    if(i % 5 == 0):
        output += "Buzz"
    if(output == ""):
        output = i;
    print(output)
```

## Fizzbuzz Solution 3-10
```python

```

## Log Terminal for git session
```bash

$cd fizzbuzz-10-sol/
$ls README.md
$touch sol-1.py
$nano sol-1.py

$git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	sol-1.py

nothing added to commit but untracked files present (use "git add" to track)

$git log
commit 5f4bf2c47b26aed3ddd39462354a3619c8e400ec (HEAD -> main, origin/main, origin/HEAD)
Author: Your Name <yourname@users.noreply.github.com>
Date:   Wed Feb 24 11:48:27 2021 +0700

    Initial commit

$git config --global user.name "Your Name"
$git config --global user.email "yourname@gmail.com"

$git config -l
user.name=Your Name
user.email=yourname@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
remote.origin.url=https://github.com/yourname/fizzbuzz-10-sol.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main

$git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	sol-1.py

nothing added to commit but untracked files present (use "git add" to track)

$git log
commit 5f4bf2c47b26aed3ddd39462354a3619c8e400ec (HEAD -> main, origin/main, origin/HEAD)
Author: Your Name <yourname@users.noreply.github.com>
Date:   Wed Feb 24 11:48:27 2021 +0700

    Initial commit

$git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	sol-1.py

nothing added to commit but untracked files present (use "git add" to track)

$git add sol-1.py
$git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   sol-1.py


$git commit -m "sol 1: fizzbuzz using if else"
[main fdde024] sol 1: fizzbuzz using if else
 1 file changed, 9 insertions(+)
 create mode 100644 sol-1.py

$git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

$git push origin main
Username for 'https://github.com': yourname
Password for 'https://yourname@github.com': 
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 384 bytes | 384.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/yourname/fizzbuzz-10-sol.git
   5f4bf2c..fdde024  main -> main

$git branch sol-2
$git branch
* main
  sol-2
$git checkout sol-2
Switched to branch 'sol-2'
$git branch
  main
* sol-2
$ls
README.md  sol-1.py
$touch sol-2.py
$nano sol-2.py
$git status
On branch sol-2
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	sol-2.py

nothing added to commit but untracked files present (use "git add" to track)
$git log
commit fdde024df2f2017c59dbc21c051f8085e4795efb (HEAD -> sol-2, origin/main, origin/HEAD, main)
Author: Your Name <yourname@gmail.com>
Date:   Wed Feb 24 12:09:04 2021 +0700

    sol 1: fizzbuzz using if else

commit 5f4bf2c47b26aed3ddd39462354a3619c8e400ec
Author: Your Name <yourname@users.noreply.github.com>
Date:   Wed Feb 24 11:48:27 2021 +0700

    Initial commit
$git status
On branch sol-2
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	sol-2.py

nothing added to commit but untracked files present (use "git add" to track)
$git add sol-2.py
$git status
On branch sol-2
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   sol-2.py

$git commit -m "sol 2: fizzbuzz using string concatenation"
[sol-2 742ca53] sol 2: fizzbuzz using string concatenation
 1 file changed, 9 insertions(+)
 create mode 100644 sol-2.py
$git status
On branch sol-2
nothing to commit, working tree clean

$ls
README.md  sol-1.py  sol-2.py
$git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
$ls
README.md  sol-1.py

$git merge sol-2
Updating fdde024..742ca53
Fast-forward
 sol-2.py | 9 +++++++++
 1 file changed, 9 insertions(+)
 create mode 100644 sol-2.py

$ls
README.md  sol-1.py  sol-2.py

$git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

$git log
commit 742ca5309da107d960a14966f80d19bf25033d3c (HEAD -> main, sol-2)
Author: Your Name <yourname@gmail.com>
Date:   Wed Feb 24 12:20:57 2021 +0700

    sol 2: fizzbuzz using string concatenation

commit fdde024df2f2017c59dbc21c051f8085e4795efb (origin/main, origin/HEAD)
Author: Your Name <yourname@gmail.com>
Date:   Wed Feb 24 12:09:04 2021 +0700

    sol 1: fizzbuzz using if else

commit 5f4bf2c47b26aed3ddd39462354a3619c8e400ec
Author: Your Name <yourname@users.noreply.github.com>
Date:   Wed Feb 24 11:48:27 2021 +0700

    Initial commit

$git branch -d sol-2
Deleted branch sol-2 (was 742ca53).

$git branch
* main
$git push origin main
Username for 'https://github.com': yourname
Password for 'https://yourname@github.com': 
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 422 bytes | 422.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/yourname/fizzbuzz-10-sol.git
   fdde024..742ca53  main -> main
$
```

## Log Terminal for git pull request
```bash
$git config --global user.name "Friend Name"
$git config --global user.email "friendname@gmail.com" 

$git clone https://github.com/friendname/fizzbuzz-10-sol.git
Cloning into 'fizzbuzz-10-sol'...
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 9 (delta 1), reused 5 (delta 0), pack-reused 0
Unpacking objects: 100% (9/9), done.

$cd fizzbuzz-10-sol/

$git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

$ls
fizzbuzz-sol-1.py  fizzbuzz-sol-2.py  README.md

$git checkout -b sol-3
Switched to a new branch 'sol-3'

$touch fizzbuzz-sol-3.py
$nano fizzbuzz-sol-3.py
$git add fizzbuzz-sol-3.py

$git commit -m "sol 3: fizzbuzz cycle of 15"
[sol-3 8671055] sol 3: fizzbuzz cycle of 15
 1 file changed, 8 insertions(+)
 create mode 100644 fizzbuzz-sol-3.py

$git status
On branch sol-3
nothing to commit, working tree clean

$git push origin sol-3
Username for 'https://github.com': friendname
Password for 'https://friendname@github.com': 
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 432 bytes | 432.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: 
remote: Create a pull request for 'sol-3' on GitHub by visiting:
remote:      https://github.com/friendname/fizzbuzz-10-sol/pull/new/sol-3
remote: 
To https://github.com/friendname/fizzbuzz-10-sol.git
 * [new branch]      sol-3 -> sol-3
$
```



