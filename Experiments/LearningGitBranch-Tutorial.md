# Learning Git Branch Tutorial

This git tutorial followed [Learning git branch](https://learngitbranching.js.org/) interactive tutorial. It's more like a git learning note.

## Main

### Introduction To Git Commit

A commit in a git repository records a snapshot of all the (tracked) files in your directory. It's like a giant copy and paste, but even better!

Git wants to keep commits as lightweight as possible though, so it doesn't just blindly copy the entire directory every time you commit. It can (when possible) compress a commit as a set of changes, or a "delta", from one version of the repository to the next.

Git also maintains a history of which commits were made when. That's why most commits have ancestor commits above them -- we designate this with arrows in our visualization. Maintaining history is great for everyone working on the project!

Goal to reach:
![Goal To Reach](/Experiments/img/2024-02-12-14-50-16.png)

Solution:

```bash
git commit
git commit
```

Explanation:

- Just `git commit` twice to reach the goal.

### Git Branches

Branches in Git are incredibly lightweight as well. They are simply pointers to a specific commit -- nothing more. This is why many Git enthusiasts chant the mantra:

> branch early, and branch often

Because there is no storage / memory overhead with making many branches, it's easier to logically divide up your work than have big beefy branches.

Goal to reach:
![Goal To Reach](/Experiments/img/2024-02-12-15-06-48.png)

Solution:

```bash
git checkout -b bugFix
```

Explanation:

- Use `git checkout -b bugFix` to create a new branch `bugFix` and switch to it.
- It's equivalent to `git branch bugFix` and `git checkout bugFix`.

### Branches and Merging

The first method to combine work that we will examine is git merge. Merging in Git creates a special commit that has two unique parents. A commit with two parents essentially means "I want to include all the work from this parent over here and this one over here, and the set of all their parents."

Goal to reach:
![Goal to reach](/Experiments/img/2024-02-12-15-14-39.png)

Solution:

```bash
git checkout -b bugFix
git commit
git checkout main
git commit
git merge bugFix
```

Explanation:

- `git checkout -b bugFix` to create a new branch `bugFix` and switch to it.
- `git commit` to make a commit in `bugFix` branch.
- `git checkout main` to switch to `main` branch.
- `git commit` to make a commit in `main` branch.
- `git merge bugFix` to merge `bugFix` branch into `main` branch.

### Git Rebase

The second way of combining work between branches is rebasing. Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.

While this sounds confusing, the advantage of rebasing is that it can be used to make a nice linear sequence of commits. The commit log / history of the repository will be a lot cleaner if only rebasing is allowed.

Goal to reach:
![Goal to reach](/Experiments/img/2024-02-12-15-27-56.png)

Solution:

```bash
git checkout -b bugFix
git commit
git checkout main
git commit
git checkout bugFix
git rebase main
```

Explanation:

- `git checkout -b bugFix` to create a new branch `bugFix` and switch to it.
- `git commit` to make a commit in `bugFix` branch.
- `git checkout main` to switch to `main` branch.
- `git commit` to make a commit in `main` branch.
- `git checkout bugFix` to switch back to `bugFix` branch. Note: you must switch back to `bugFix` branch before rebasing according to the goal.
- `git rebase main` to rebase `bugFix` branch onto `main` branch.

### Moving around in Git

Before we get to some of the more advanced features of Git, it's important to understand different ways to move through the commit tree that represents your project.

First we have to talk about "HEAD". HEAD is the symbolic name for the currently checked out commit -- it's essentially what commit you're working on top of.

HEAD always points to the most recent commit which is reflected in the working tree. Most git commands which make changes to the working tree will start by changing HEAD.

Normally HEAD points to a branch name (like bugFix). When you commit, the status of bugFix is altered and this change is visible through HEAD.

Detaching HEAD just means attaching it to a commit instead of a branch. Detaching HEAD means your HEAD no longer points to a branch -- it points directly to a commit instead. This has some interesting side effects. For one, if you commit while HEAD is detached, the commit won't belong to any branch and will be completely unreachable (except by commit hash). This is great for scribbling down a quick note to yourself, but not something you'd normally want to do in the middle of working on a feature.

Goal to reach:
![Goal to reach](/Experiments/img/2024-02-12-15-41-13.png)

Solution:

```bash
git checkout c4
```

Explanation:

- `git checkout c4` to detach `HEAD` and point it to commit `c4`.

### Relative Refs

With relative refs, you can start somewhere memorable (like the branch bugFix or HEAD) and work from there.

Relative commits are powerful, but we will introduce two simple ones here:

- Moving upwards one commit at a time with ^
- Moving upwards a number of times with ~num

Goal to reach:
![Goal to reach](/Experiments/img/2024-02-12-15-47-56.png)

Solution:

```bash
git checkout bugFix^
```

Explanation:

- `git checkout bugFix^` to detach `HEAD` and point it to the parent of the branch `bugFix`.

### The "~" operator

Say you want to move a lot of levels up in the commit tree. It might be tedious to type ^ several times, so Git also has the tilde (~) operator.

The tilde operator (optionally) takes in a trailing number that specifies the number of parents you would like to ascend.

One of the most common ways I use relative refs is to move branches around. You can directly reassign a branch to a commit with the -f option. So something like:

`git branch -f main HEAD~3`

moves (by force) the main branch to three parents behind HEAD.

Note: In a real git environment git branch -f command is not allowed for your current branch.

Goal to reach:
![Goal to reach](/Experiments/img/2024-02-12-15-57-24.png)

Solution1:

```bash
git checkout c6
git branch -f main HEAD
git branch -f bugFix HEAD~4
git checkout c1
```

Explanation1:

- `git checkout c6` to point `HEAD` to commit `c6`.
- `git branch -f main HEAD` to move `main` branch to `HEAD`.
- `git branch -f bugFix HEAD~4` to move `bugFix` branch to the 4th parent of the `HEAD`. Note: 4 parents include the `HEAD` itself.
- `git checkout c1` to point `HEAD` to commit c1.

Solution2:

```bash
git branch -f main c6
git branch -f bugFix c0
git checkout c1
```

Explanation2：

- `git branch -f main c6`: You also can use the commit hash to move the branch to a specific commit.

### Reversing Changes in Git

There are many ways to reverse changes in Git. And just like committing, reversing changes in Git has both a low-level component (staging individual files or chunks) and a high-level component (how the changes are actually reversed). Our application will focus on the latter.

There are two primary ways to undo changes in Git -- one is using `git reset` and the other is using `git revert`.

`git reset` reverses changes by moving a branch reference backwards in time to an older commit. In this sense you can think of it as "rewriting history;" `git reset` will move a branch backwards as if the commit had never been made in the first place.

`git reset HEAD~1` is the most common way to undo the most recent commit. It works by moving the `main` branch backwards by one commit. The `--soft` option will move `main` back, but it will leave the index and working directory (your files on disk) as they were. This way you can re-commit the changes, but you'll have a chance to re-arrange them before doing so. The `--hard` option, on the other hand, will make your working directory match the state of the commit it moves back to. This is a great way to undo a commit, but it's also a great way to lose uncommitted work -- use it with care!

While resetting works great for local branches on your own machine, its method of "rewriting history" doesn't work for remote branches that others are using.

In order to reverse changes and share those reversed changes with others, we need to use `git revert`. Let's see it in action.

`git revert HEAD` will create a commit that inverses everything introduced by the last commit. This way you can push the new commit to the server and your colleagues can get it.

Goal to reach:
![Goal to reach](/Experiments/img/2024-02-12-16-16-11.png)

Solution:

```bash
git reset HEAD~1
git checkout pushed
git revert HEAD
```

Explanation:

- `git reset HEAD~1` to move `local` branch backwards by one commit.
- `git checkout pushed` to switch to `pushed` branch.
- `git revert HEAD` to create a commit that inverses everything introduced by the last commit.

### Moving Work Around

The next concept we're going to cover is "moving work around" -- in other words, it's a way for developers to say "I want this work here and that work there" in precise, eloquent, flexible ways.

The first command in this series is called `git cherry-pick`. It takes on the following form:

`git cherry-pick <Commit1> <Commit2> <...>`

It's a very straightforward way of saying that you would like to copy a series of commits below your current location (`HEAD`). I personally love `cherry-pick` because there is very little magic involved and it's easy to understand.

Goal to reach:
![Goal to reach](/Experiments/img/2024-02-12-16-31-50.png)

Solution:

```bash
git cherry-pick c3 c4 c7
```

Explanation:

- `git cherry-pick c3 c4 c7` to copy a series of commits `c3`, `c4` and `c7` below `HEAD`.


## Remote
