# Learning Git Branch Tutorial

This git tutorial followed [Learning git branch](https://learngitbranching.js.org/) interactive tutorial. It's more like a git learning note.

## Main

### Introduction To Git Commit

A commit in a git repository records a snapshot of all the (tracked) files in your directory. It's like a giant copy and paste, but even better!

Git wants to keep commits as lightweight as possible though, so it doesn't just blindly copy the entire directory every time you commit. It can (when possible) compress a commit as a set of changes, or a "delta", from one version of the repository to the next.

Git also maintains a history of which commits were made when. That's why most commits have ancestor commits above them -- we designate this with arrows in our visualization. Maintaining history is great for everyone working on the project!

Goal to reach:
![Goal To Reach](/Labs/img/2024-02-12-14-50-16.png)

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
![Goal To Reach](/Labs/img/2024-02-12-15-06-48.png)

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
![Goal to reach](/Labs/img/2024-02-12-15-14-39.png)

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
![Goal to reach](/Labs/img/2024-02-12-15-27-56.png)

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
![Goal to reach](/Labs/img/2024-02-12-15-41-13.png)

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
![Goal to reach](/Labs/img/2024-02-12-15-47-56.png)

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

`git branch -f `main` HEAD~3`

moves (by force) the `main` branch to three parents behind HEAD.

Note: In a real git environment git branch -f command is not allowed for your current branch.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-15-57-24.png)

Solution1:

```bash
git checkout c6
git branch -f `main` HEAD
git branch -f bugFix HEAD~4
git checkout c1
```

Explanation1:

- `git checkout c6` to point `HEAD` to commit `c6`.
- `git branch -f `main` HEAD` to move `main` branch to `HEAD`.
- `git branch -f bugFix HEAD~4` to move `bugFix` branch to the 4th ancestor of the `HEAD`. Note: 4 means 4 ancestors which include the commit that `HEAD` point to.
- `git checkout c1` to point `HEAD` to commit c1.

Solution2:

```bash
git branch -f `main` c6
git branch -f bugFix c0
git checkout c1
```

Explanation2：

- `git branch -f `main` c6`: You also can use the commit hash to move the branch to a specific commit.

### Reversing Changes in Git

There are many ways to reverse changes in Git. And just like committing, reversing changes in Git has both a low-level component (staging individual files or chunks) and a high-level component (how the changes are actually reversed). Our application will focus on the latter.

There are two primary ways to undo changes in Git -- one is using `git reset` and the other is using `git revert`.

`git reset` reverses changes by moving a branch reference backwards in time to an older commit. In this sense you can think of it as "rewriting history;" `git reset` will move a branch backwards as if the commit had never been made in the first place.

`git reset HEAD~1` is the most common way to undo the most recent commit. It works by moving the `main` branch backwards by one commit. The `--soft` option will move `main` back, but it will leave the index and working directory (your files on disk) as they were. This way you can re-commit the changes, but you'll have a chance to re-arrange them before doing so. The `--hard` option, on the other hand, will make your working directory match the state of the commit it moves back to. This is a great way to undo a commit, but it's also a great way to lose uncommitted work -- use it with care!

While resetting works great for local branches on your own machine, its method of "rewriting history" doesn't work for remote branches that others are using.

In order to reverse changes and share those reversed changes with others, we need to use `git revert`. Let's see it in action.

`git revert HEAD` will create a commit that inverses everything introduced by the last commit. This way you can push the new commit to the server and your colleagues can get it.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-16-16-11.png)

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
![Goal to reach](/Labs/img/2024-02-12-16-31-50.png)

Solution:

```bash
git cherry-pick c3 c4 c7
```

Explanation:

- `git cherry-pick c3 c4 c7` to copy a series of commits `c3`, `c4` and `c7` below `HEAD`.

### Git Interactive Rebase

Git cherry-pick is great when you know which commits you want (and you know their corresponding hashes) -- it's hard to beat the simplicity it provides.

But what about the situation where you don't know what commits you want? Thankfully git has you covered there as well! We can use interactive rebasing for this -- it's the best way to review a series of commits you're about to rebase.

All interactive rebase means Git is using the rebase command with the -i option.

If you include this option, git will open up a UI to show you which commits are about to be copied below the target of the rebase. It also shows their commit hashes and messages, which is great for getting a bearing on what's what.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-18-56-32.png)

Solution:

```bash
git rebase -i HEAD~4
```

Explanation:

- `git rebase -i HEAD~4` to open up a UI to show you which commits are about to be copied below the target of the rebase.

### Locally Stacked Changes

Here's a development situation that often happens: I'm trying to track down a bug but it is quite elusive. In order to aid in my detective work, I put in a few debug commands and a few print statements.

All of these debugging / print statements are in their own commits. Finally I track down the bug, fix it, and rejoice!

Only problem is that I now need to get my bugFix back into the `main` branch. If I simply fast-forwarded main, then `main` would get all my debug statements which is undesirable.

We need to tell git to copy only one of the commits over. This is just like the levels earlier on moving work around -- we can use the same commands:

- `git rebase -i`
- `git cherry-pick`

To achieve this goal.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-19-03-15.png)

Solution:

```bash
git checkout main
git cherry-pick c4
```

Explanation:

- `git checkout main` to switch to `main` branch, because we want to copy the bugFix commit to `main` branch, but we don't want to copy the debug commits that are the ancestors of the bugFix commit.
- `git cherry-pick c4` to copy the bugFix commit to `main` branch.

### Juggling Commits

Here's another situation that happens quite commonly. You have some changes (newImage) and another set of changes (caption) that are related, so they are stacked on top of each other in your repository (aka one after another).

The tricky thing is that sometimes you need to make a small modification to an earlier commit. In this case, design wants us to change the dimensions of newImage slightly, even though that commit is way back in our history!!

We will overcome this difficulty by doing the following:

- We will re-order the commits so the one we want to change is on top with git rebase -i
- We will git commit --amend to make the slight modification
- Then we will re-order the commits back to how they were previously with git rebase -i
- Finally, we will move `main` to this updated part of the tree to finish the level (via the method of your choosing)

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-19-13-23.png)

Solution:

```bash
git rebase -i HEAD~2
git commit --amend
git rebase -i HEAD~2
git branch -f `main` HEAD
```

Explanation:

- `git rebase -i HEAD~2` to re-order the commits so the one we want to change is on top.
- `git commit --amend` to make the slight modification.
- `git rebase -i HEAD~2` to re-order the commits back to how they were previously.
- `git branch -f `main` HEAD` to move `main` to this updated part of the tree.

### Juggling Commits II

As you saw in the last level, we used rebase -i to reorder the commits. Once the commit we wanted to change was on top, we could easily --amend it and re-order back to our preferred order.

The only issue here is that there is a lot of reordering going on, which can introduce rebase conflicts. Let's look at another method with git cherry-pick.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-19-28-07.png)

Solution:

```bash
git checkout main
git cherry-pick c2
git commit --amend
git cherry-pick c3
```

Explanation:

- `git checkout main` to switch the branch `main`
- `git cherry-pick c2` to copy the commit to `main` branch to do edit
- `git commit --amend` to make the slight modification
- `git cherry-pick c3` to copy the commit to `main` branch

### Git Tags

As you have learned from previous lessons, branches are easy to move around and often refer to different commits as work is completed on them. Branches are easily mutated, often temporary, and always changing.

If that's the case, you may be wondering if there's a way to permanently mark historical points in your project's history. For things like major releases and big merges, is there any way to mark these commits with something more permanent than a branch?

You bet there is! Git tags support this exact use case -- they (somewhat) permanently mark certain commits as "milestones" that you can then reference like a branch.

More importantly though, they never move as more commits are created. You can't "check out" a tag and then complete work on that tag -- tags exist as anchors in the commit tree that designate certain spots.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-19-34-13.png)

Solution:

```bash
git tag v0 c1
git tag v1 c2
git checkout c2
```

Explanation:

- `git tag v0 c1` to tag commit `c1` as `v0`.
- `git tag v1 c2` to tag commit `c2` as `v1`.
- `git checkout c2` to switch to commit `c2`.

### Git Describe

Because tags serve as such great "anchors" in the codebase, git has a command to describe where you are relative to the closest "anchor" (aka tag). And that command is called git describe!

Git describe can help you get your bearings after you've moved many commits backwards or forwards in history; this can happen after you've completed a git bisect (a debugging search) or when sitting down at the computer of a coworker who just got back from vacation.

Git describe takes the form of:

`git describe <ref>`

Where `<ref>` is anything git can resolve into a commit. If you don't specify a ref, git just uses where you're checked out right now (`HEAD`).

The output of the command looks like:

`<tag>_<numCommits>_g<hash>`

Where `tag` is the closest ancestor tag in history, `numCommits` is how many commits away that tag is, and `<hash>` is the hash of the commit being described.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-19-46-29.png)

Solution:

```bash
git describe main
git describe side
git commit
```

Explanation:

- `git describe main` to show `v0_2_gC2`, note: in the real git environment `--tags` option is needed to show the unannotated tag. To add annotated tag, use `git tag -a v0 c1 -m "v0"` to add an annotated tag.
- `git describe side` to show `v1_1_gC3`
- `git commit` to make a commit to move on to the next level.

### Rebasing Multiple Branches

Man, we have a lot of branches going on here! Let's rebase all the work from these branches onto main.

Upper management is making this a bit trickier though -- they want the commits to all be in sequential order. So this means that our final tree should have C7' at the bottom, C6' above that, and so on, all in order.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-19-59-04.png)

Solution:

```bash
git rebase bugFix
git checkout another
git rebase side
git rebase main
git branch -f `main` HEAD
```

Explanation:

- `git rebase bugFix` to rebase the current `side` branch onto `bugFix` branch.
- `git checkout another` to switch to `another` branch.
- `git rebase side` to rebase the current `another` branch onto `side` branch.
- `git rebase main` to rebase the current `another` branch onto `main` branch.
- `git branch -f `main` HEAD` to move `main` to `HEAD`.

### Specifying Parents

Like the ~ modifier, the ^ modifier also accepts an optional number after it.

Rather than specifying the number of generations to go back (what ~ takes), the modifier on ^ specifies which parent reference to follow from a merge commit. Remember that merge commits have multiple parents, so the path to choose is ambiguous.

Git will normally follow the "first" parent upwards from a merge commit, but specifying a number with ^ changes this default behavior.

The ^ and ~ modifiers can make moving around a commit tree very powerful:

```bash
git checkout HEAD~
git checkout HEAD^2
git checkout HEAD~2
```

Even crazier, these modifiers can be chained together! Check this out:

`git checkout HEAD~^2~2`

The same movement as before, but all in one command.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-21-15-20.png)

Solution:

```bash
git branch bugWork HEAD~^2~
```

Explanation:

- `git branch bugWork HEAD~^2~` to create a new branch `bugWork` and point it to the commit `HEAD~^2~`. Note: `HEAD~^2~` means the parent of the second parent of the first parent of `HEAD`.

### Branch Spaghetti

Here we have `main` that is a few commits ahead of branches one two and three. For whatever reason, we need to update these three other branches with modified versions of the last few commits on main.

Branch one needs a re-ordering of those commits and an exclusion/drop of C5. Branch two just needs a pure reordering of the commits, and three only needs one commit transferred!

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-21-24-20.png)

Solution:

```bash
git checkout one
git cherry-pick c4 c3 c2
git checkout two
git cherry-pick c5 c4 c3 c2
git branch -f three c2
```

Explanation:

- `git checkout one` to switch to `one` branch.
- `git cherry-pick c4 c3 c2` to copy the commits to `one` branch.
- `git checkout two` to switch to `two` branch.
- `git cherry-pick c5 c4 c3 c2` to copy the commits to `two` branch.
- `git branch -f three c2` to move `three` to `c2`.

## Remote

### Git Remotes

Remote repositories aren't actually that complicated. In today's world of cloud computing it's easy to think that there's a lot of magic behind git remotes, but they are actually just copies of your repository on another computer. You can typically talk to this other computer through the Internet, which allows you to transfer commits back and forth.

That being said, remote repositories have a bunch of great properties:

- First and foremost, remotes serve as a great backup! Local git repositories have the ability to restore files to a previous state (as you know), but all that information is stored locally. By having copies of your git repository on other computers, you can lose all your local data and still pick up where you left off.

- More importantly, remotes make coding social! Now that a copy of your project is hosted elsewhere, your friends can contribute to your project (or pull in your latest changes) very easily.

It's become very popular to use websites that visualize activity around remote repos (like GitHub), but remote repositories always serve as the underlying backbone for these tools. So it's important to understand them!

Up until this point, Learn Git Branching has focused on teaching the basics of local repository work (branching, merging, rebasing, etc). However now that we want to learn about remote repository work, we need a command to set up the environment for those lessons. `git clone` will be that command.

Technically, `git clone` in the real world is the command you'll use to create local copies of remote repositories (from github for example). We use this command a bit differently in Learn Git Branching though -- git clone actually makes a remote repository out of your local one. Sure it's technically the opposite meaning of the real command, but it helps build the connection between cloning and remote repository work, so let's just run with it for now.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-21-46-30.png)

Solution:

```bash
git clone
```

Explanation:

- `git clone` to make a remote repository out of your local one. Note: local branch "main" set to track remote branch "main" from "origin" i.e "o/main" in education system.

### Git Remote Branches

The first thing you may have noticed is that a new branch appeared in our local repository called o/main. This type of branch is called a remote branch; remote branches have special properties because they serve a unique purpose.

Remote branches reflect the state of remote repositories (since you last talked to those remote repositories). They help you understand the difference between your local work and what work is public -- a critical step to take before sharing your work with others.

Remote branches have the special property that when you check them out, you are put into detached HEAD mode. Git does this on purpose because you can't work on these branches directly; you have to work elsewhere and then share your work with the remote (after which your remote branches will be updated).

To be clear: Remote branches are on your local repository, not on the remote repository.

You may be wondering what the leading o/ is for on these remote branches. Well, remote branches also have a (required) naming convention -- they are displayed in the format of:

`<remote name>/<branch name>`

Hence, if you look at a branch named `o/main`, the branch name is `main` and the name of the remote is o.

Most developers actually name their `main` remote `origin`, not `o`. This is so common that git actually sets up your remote to be named origin when you git clone a repository.

Unfortunately the full name of origin does not fit in our UI, so we use o as shorthand :( Just remember when you're using real git, your remote is probably going to be named origin!

Goal to reach:
![Goal to reach](/Labs/img/
2024-02-12-21-59-40.png)

Solution:

```bash
git commit
git checkout o/main
git commit
```

Explanation:

- `git commit` to make a commit in `main` branch.
- `git checkout o/main` to switch to `o/main` branch.
- `git commit` to make a commit in `o/main` branch. Note: the `HEAD` is detached now, because you can't work on remote branches directly.

### Git Fetch

Working with git remotes really just boils down to transferring data to and from other repositories. As long as we can send commits back and forth, we can share any type of update that is tracked by git (and thus share work, new files, new ideas, love letters, etc.).

In this lesson we will learn how to fetch data from a remote repository -- the command for this is conveniently named `git fetch`.

You'll notice that as we update our representation of the remote repository, our remote branches will update to reflect that new representation. This ties into the previous lesson on remote branches.

`git fetch` performs two `main` steps, and two `main` steps only. It:

- downloads the commits that the remote has but are missing from our local repository, and...
- updates where our remote branches point (for instance, `o/main`)

`git fetch` essentially brings our local representation of the remote repository into synchronization with what the actual remote repository looks like (right now).

If you remember from the previous lesson, we said that remote branches reflect the state of the remote repositories since you last talked to those remotes. git fetch is the way you talk to these remotes! Hopefully the connection between remote branches and git fetch is apparent now.

`git fetch` usually talks to the remote repository through the Internet (via a protocol like http:// or git://).

`git fetch`, however, does not change anything about your local state. It will not update your `main` branch or change anything about how your file system looks right now.

This is important to understand because a lot of developers think that running `git fetch` will make their local work reflect the state of the remote. It may download all the necessary data to do that, but it does not actually change any of your local files. We will learn commands in later lessons to do just that :D

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-22-09-10.png)

Solution:

```bash
git fetch
```

Explanation:

- `git fetch` to download the commits that the remote has but are missing from our local repository, and update where our remote branches point.

### Git Pull

Now that we've seen how to fetch data from a remote repository with `git fetch`, let's update our work to reflect those changes!

There are actually many ways to do this -- once you have new commits available locally, you can incorporate them as if they were just normal commits on other branches. This means you could execute commands like:

- `git cherry-pick o/main`
- `git rebase o/main`
- `git merge o/main`
- etc., etc.

In fact, the workflow of fetching remote changes and then merging them is so common that git actually provides a command that does both at once! That command is `git pull`.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-22-13-23.png)

Solution:

```bash
git fetch
git merge o/main
```

or

```bash
git pull
```

Explanation:

- `git pull` to fetch remote changes and then merge them.

### Simulating collaboration

So here is the tricky thing -- for some of these upcoming lessons, we need to teach you how to pull down changes that were introduced in the remote.

That means we need to essentially "pretend" that the remote was updated by one of your coworkers / friends / collaborators, sometimes on a specific branch or a certain number of commits.

In order to do this, we introduced the aptly-named command git fakeTeamwork!

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-22-17-49.png)

Solution:

```bash
git clone
git fakeTeamwork `main` 2
git fetch
git commit
git merge o/main
```

Explanation:

- `git clone` to make a remote repository out of your local one.
- `git fakeTeamwork `main` 2` to simulate that the remote was updated by one of your collaborators on the `main` branch with 2 commits.
- `git fetch` to download the commits that the remote has but are missing from our local repository, and update where our remote branches point.
- `git commit` to make a commit in `main` branch.
- `git merge o/main` to merge the remote changes in `main` branch.

### Git Push

Well, the way to upload shared work is the opposite of downloading shared work. And what's the opposite of `git pull`? `git push`!

`git push` is responsible for uploading your changes to a specified remote and updating that remote to incorporate your new commits. Once `git push` completes, all your friends can then download your work from the remote.

You can think of `git push` as a command to "publish" your work. It has a bunch of subtleties that we will get into shortly, but let's start with baby steps...

note -- the behavior of `git push` with no arguments varies depending on one of git's settings called push.default. The default value for this setting depends on the version of git you're using, but we are going to use the upstream value in our lessons. This isn't a huge deal, but it's worth checking your settings before pushing in your own projects.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-22-23-57.png)

Solution:

```bash
git commit
git commit
git push
```

Explanation:

- Commit twice and push the commits in the local repo to the remote repo, `o/main` is changed to track the remote repo.

### Diverged Work

So far we've seen how to pull down commits from others and how to push up our own changes. It seems pretty simple, so how can people get so confused?

The difficulty comes in when the history of the repository diverges.

Imagine you clone a repository on Monday and start dabbling on a side feature. By Friday you are ready to publish your feature -- but oh no! Your coworkers have written a bunch of code during the week that's made your feature out of date (and obsolete). They've also published these commits to the shared remote repository, so now your work is based on an old version of the project that's no longer relevant.

In this case, the command git push is ambiguous. If you run git push, should git change the remote repository back to what it was on Monday? Should it try to add your code in while not removing the new code? Or should it totally ignore your changes since they are totally out of date?

Because there is so much ambiguity in this situation (where history has diverged), git doesn't allow you to push your changes. It actually forces you to incorporate the latest state of the remote before being able to share your work.

you already know git pull is just shorthand for a fetch and a merge. Conveniently enough, `git pull --rebase` is shorthand for a fetch and a rebase!

This workflow of fetching, rebase/merging, and pushing is quite common. In future lessons we will examine more complicated versions of these workflows, but for now let's try this out.

In order to solve this level, take the following steps:

- Clone your repo
- Fake some teamwork (1 commit)
- Commit some work yourself (1 commit)
- Publish your work via rebasing

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-22-35-22.png)

Solution:

```bash
git clone
git fakeTeamwork `main` 1
git commit
git pull --rebase
git push
```

Explanation:

- `git clone` to make a remote repository out of your local one.
- `git fakeTeamwork `main` 1` to simulate that the remote was updated by one of your collaborators on the `main` branch with 1 commit.
- `git commit` to make a commit in `main` branch.
- `git pull --rebase` to fetch the remote changes and then rebase your local changes on top of the remote changes.
- `git push` to push the commits in the local repo to the remote repo.

### Remote Rejected!

If you work on a large collaborative team it's likely that `main` is locked and requires some Pull Request process to merge changes. If you commit directly to `main` locally and try pushing you will be greeted with a message similar to this:

```bash
! [remote rejected] `main` -> `main` (TF402455: Pushes to this branch are not permitted; you must use a pull request to update this branch.)
```

The remote rejected the push of commits directly to `main` because of the policy on `main` requiring pull requests to instead be used.

You meant to follow the process creating a branch then pushing that branch and doing a pull request, but you forgot and committed directly to main. Now you are stuck and cannot push your changes.

Create another branch called feature and push that to the remote. Also reset your `main` back to be in sync with the remote otherwise you may have issues next time you do a pull and someone else's commit conflicts with yours.

Goal to reach:
![Goal to reach](/Labs/img/2024-02-12-22-40-20.png)

Solution:

```bash
git checkout -b feature
git branch -f `main` HEAD~
git push
```

Explanation:

- `git checkout -b feature` to create a new branch `feature` and switch to it.
- `git branch -f `main` HEAD~` to move `main` to the parent of `HEAD`. This step is important because resetting your `main` back to be in sync with the remote otherwise you may have issues next time you do a pull and someone else's commit conflicts with yours.
- `git push` to push the commits of `feature` branch in the local repo to the remote repo.

### Merging feature branches

It's common for developers on big projects to do all their work on feature branches (off of main) and then integrate that work only once it's ready. This is similar to the previous lesson (where side branches get pushed to the remote), but here we introduce one more step.

Some developers only push and pull when on the `main` branch -- that way `main` always stays updated to what is on the remote (o/main).

So for this workflow we combine two things:

- integrating feature branch work onto main, and
- pushing and pulling from the remote

his level is pretty hefty -- here is the general outline to solve:

- There are three feature branches -- side1 side2 and side3
- We want to push each one of these features, in order, to the remote
- The remote has since been updated, so we will need to incorporate that work as well

Goal to reach:
![Goal to reach](/Labs/img/2024-02-13-09-04-49.png)

Solution:

```bash
git fetch
git rebase `o/main` side1
git rebase side1 side2
git rebase side2 side3
git rebase side3 main
git push
```

Explanation:

- `git fetch` to download the commits that the remote has but are missing from our local repository, and update where our remote branches point.
- `git rebase `o/main` side1` to rebase `side1` branch onto `o/main` branch.
- `git rebase side1 side2` to rebase `side2` branch onto `side1` branch.
- `git rebase side2 side3` to rebase `side3` branch onto `side2` branch.
- `git rebase side3 main` to rebase `main` branch onto `side3` branch.
- `git push` to push the commits in the local repo to the remote repo.

### Why not merge?

In order to push new updates to the remote, all you need to do is incorporate the latest changes from the remote. That means you can either rebase or merge in the remote branch (e.g. o/main).

So if you can do either method, why have the lessons focused on rebasing so far? Why is there no love for merge when working with remotes?

here's a lot of debate about the tradeoffs between merging and rebasing in the development community. Here are the general pros / cons of rebasing:

Pros:

- Rebasing makes your commit tree look very clean since everything is in a straight line

Cons:

- Rebasing modifies the (apparent) history of the commit tree.

For example, commit C1 can be rebased past C3. It then appears that the work for C1' came after C3 when in reality it was completed beforehand.

Some developers love to preserve history and thus prefer merging. Others (like myself) prefer having a clean commit tree and prefer rebasing. It all comes down to preferences :D

Goal to reach:
![Goal to reach](/Labs/img/2024-02-13-09-21-41.png)

Solution:

```bash
git checkout main
git pull
git merge side1
git merge side2
git merge side3
git push
```

Explanation:

- `git checkout main` to switch to `main` branch.
- `git pull` to fetch the remote changes and then merge them.
- `git merge side1` to merge `side1` branch into `main` branch.
- `git merge side2` to merge `side2` branch into `main` branch.
- `git merge side3` to merge `side3` branch into `main` branch.
- `git push` to push the commits in the local repo to the remote repo.

### Remote-Tracking branches

One thing that might have seemed "magical" about the last few lessons is that git knew the `main` branch was related to `o/main`. Sure these branches have similar names and it might make logical sense to connect the `main` branch on the remote to the local `main` branch, but this connection is demonstrated clearly in two scenarios:

- During a pull operation, commits are downloaded onto `o/main` and then merged into the `main` branch. The implied target of the merge is determined from this connection.

- During a push operation, work from the `main` branch was pushed onto the remote's `main` branch (which was then represented by `o/main` locally). The destination of the push is determined from the connection between `main` and `o/main`.

Long story short, this connection between `main` and `o/main` is explained simply by the "remote tracking" property of branches. The `main` branch is set to track `o/main` -- this means there is an implied merge target and implied push destination for the `main` branch.

You may be wondering how this property got set on the `main` branch when you didn't run any commands to specify it. Well, when you clone a repository with git, this property is actually set for you automatically.

During a clone, git creates a remote branch for every branch on the remote (aka branches like `o/main`). It then creates a local branch that tracks the currently active branch on the remote, which is `main` in most cases.

Once git clone is complete, you only have one local branch (so you aren't overwhelmed) but you can see all the different branches on the remote (if you happen to be very curious). It's the best of both worlds!

This also explains why you may see the following command output when cloning:

> local branch `main` set to track remote branch `o/main`

Can I specify this myself?

Yes you can! You can make any arbitrary branch track o/main, and if you do so, that branch will have the same implied push destination and merge target as main. This means you can run git push on a branch named totallyNotMain and have your work pushed to the main branch on the remote!

There are two ways to set this property. The first is to checkout a new branch by using a remote branch as the specified ref. Running

`git checkout -b totallyNotMain o/main`

Creates a new branch named totallyNotMain and sets it to track o/main.

Another way to set remote tracking on a branch is to simply use the git branch -u option. Running

`git branch -u o/main foo`

will set the foo branch to track o/main. If foo is currently checked out you can even leave it off:

`git branch -u o/main`

Goal to reach:
![Goal to reach](/Labs/img/2024-02-13-09-49-49.png)

Solution:

```bash
git checkout -b side o/main
git commit
git pull --rebase
git push
```

Explanation:

- `git checkout -b side o/main` to create a new branch `side` and set it to track `o/main`.
- `git commit` to make a commit in `side` branch.
- `git pull --rebase` to fetch the remote changes and then rebase your local changes on top of the remote changes.
- `git push` to push the commits in the local repo to the remote repo.

### Push arguments

Great! Now that you know about remote tracking branches we can start to uncover some of the mystery behind how git push, fetch, and pull work. We're going to tackle one command at a time but the concepts between them are very similar.

First we'll look at `git push`. You learned in the remote tracking lesson that git figured out the remote and the branch to push to by looking at the properties of the currently checked out branch (the remote that it "tracks"). This is the behavior with no arguments specified, but git push can optionally take arguments in the form of:

`git push <remote> <place>`

What is a `<place>` parameter you say? We'll dive into the specifics soon, but first an example. Issuing the command:

`git push origin main`

translates to this in English:

Go to the branch named "main" in my repository, grab all the commits, and then go to the branch "main" on the remote named "origin". Place whatever commits are missing on that branch and then tell me when you're done.

By specifying main as the "place" argument, we told git where the commits will come from and where the commits will go. It's essentially the "place" or "location" to synchronize between the two repositories.

Keep in mind that since we told git everything it needs to know (by specifying both arguments), it totally ignores where we are checked out!

Goal to reach:
![Goal to reach](/Labs/img/2024-02-13-21-03-17.png)

Solution:

```bash
git push origin main
git push origin foo
```

Explanation:

- `git push origin main` to push the commits in the local repo to the remote repo, and place the commits on the branch `main` on the remote named `origin`.
- `git push origin foo` to push the commits in the local repo to the remote repo, and place the commits on the branch `foo` on the remote named `origin`.
- Note: because `main` and `foo` are not checked out, so the push arguments are needed.

### `<place>` argument details

Remember from the previous lesson that when we specified `main` as the place argument for git push, we specified both the source of where the commits would come from and the destination of where the commits would go.

You might then be wondering -- what if we wanted the source and destination to be different? What if you wanted to push commits from the `foo` branch locally onto the bar branch on remote?

In order to specify both the source and the destination of `<place>`, simply join the two together with a colon:

`git push origin <source>:<destination>`

This is commonly referred to as a colon refspec. Refspec is just a fancy name for a location that git can figure out (like the branch foo or even just `HEAD~1`).

Goal to reach:
![Goal to reach](/Labs/img/2024-02-13-21-10-31.png)

Solution:

```bash
git push origin foo:main
git push origin main^:foo
```

Explanation:

- `git push origin foo:main` to push the commits in the local repo to the remote repo, and source place is local branch `foo`, destination place is remote branch `main`.
- `git push origin main^:foo` to push the commits in the local repo to the remote repo, and source place is parent commits of local branch `main`, destination place is remote branch `foo`.

### Git fetch arguments

So we've just learned all about git push arguments, this cool `<place>` parameter, and even colon refspecs (`<source>:<destination>`). Can we use all this knowledge for git fetch as well?

You betcha! The arguments for git fetch are actually very, very similar to those for git push. It's the same type of concepts but just applied in the opposite direction (since now you are downloading commits rather than uploading).

If you specify a place with git fetch like in the following command:

git fetch origin foo

Git will go to the foo branch on the remote, grab all the commits that aren't present locally, and then plop them down onto the o/foo branch locally.

`git fetch origin foo` to download only the commits from foo and place them on o/foo.

You might be wondering -- why did git plop those commits onto the o/foo remote branch rather than just plopping them onto my local foo branch? I thought the <place> parameter is a place that exists both locally and on the remote?

Well git makes a special exception in this case because you might have work on the foo branch that you don't want to mess up!! This ties into the earlier lesson on git fetch -- it doesn't update your local non-remote branches, it only downloads the commits (so you can inspect / merge them later).

"Well in that case, what happens if I explicitly define both the source and destination with `<source>:<destination>`?"

If you feel passionate enough to fetch commits directly onto a local branch, then yes you can specify that with a colon refspec. You can't fetch commits onto a branch that is checked out, but otherwise git will allow this.

Here is the only catch though -- `<source>` is now a place on the remote and `<destination>` is a local place to put those commits. It's the exact opposite of git push, and that makes sense since we are transferring data in the opposite direction!

That being said, developers rarely do this in practice. I'm introducing it mainly as a way to conceptualize how fetch and push are quite similar, just in opposite directions.

`git fetch origin foo~1:bar`

Wow! See, git resolved foo~1 as a place on the origin and then downloaded those commits to bar (which was a local branch). Notice how foo and o/foo were not updated since we specified a destination.

What if the destination doesn't exist before I run the command? Git made the destination locally before fetching, just like git will make the destination on remote before pushing (if it doesn't exist).

If git fetch receives no arguments, it just downloads all the commits from the remote onto all the remote branches...

Goal to reach:
![Goal to reach](/Labs/img/
2024-02-13-21-26-42.png)

Solution:

```bash
git fetch origin foo:main
git fetch origin main~1:foo
git checkout foo
git merge main
```

Explanation:

- `git fetch origin foo:main` to download the commits from `foo` on the remote and place them on `main` locally.
- `git fetch origin main~1:foo` to download the parent commits of `main` on the remote and place them on `foo` locally.
- `git checkout foo` to switch to `foo` branch.
- `git merge main` to merge `main` branch into `foo` branch.

### Source of Nothing

Git abuses the `<source>` parameter in two weird ways. These two abuses come from the fact that you can technically specify "nothing" as a valid source for both git push and git fetch. The way you specify nothing is via an empty argument:

- `git push origin :side`
- `git fetch origin :bugFix`

What does pushing "nothing" to a remote branch do? It deletes it(the branch)!

`git push origin :foo`

There, we successfully deleted the `foo` branch on remote (and locally branch `o/foo`) by pushing the concept of "nothing" to it. That kinda makes sense...

`git fetch origin :bar`

Finally, fetching "nothing"(that branch doesn't exist locally) to a place locally actually makes a new branch.

This is a quick level -- just delete one remote branch and create a new branch with git fetch to finish!

Goal to reach:
![Goal to reach](/Labs/img/2024-02-13-21-37-13.png)

Solution:

```bash
git push origin :foo
git fetch origin :bar
```

Explanation:

- `git push origin :foo` to delete the `foo` branch on remote and locally.
- `git fetch origin :bar` to create a new branch `bar` locally.

### Git pull arguments

`Git pull` at the end of the day is really just shorthand for a fetch followed by merging in whatever was just fetched. You can think of it as running `git fetch` with the same arguments specified and then merging in where those commits ended up.

Here are some equivalent commands in git:

`git pull origin foo` is equal to:

```bash
git fetch origin foo
git merge o/foo
```

And...

`git pull origin bar~1:bugFix` is equal to:

```bash
git fetch origin bar~1:bugFix
git merge bugFix
```

See? git pull is really just shorthand for fetch + merge, and all git pull cares about is where the commits ended up (the destination argument that it figures out during fetch).

`git pull origin main`

See! by specifying main we downloaded commits onto o/main just as normal. Then we merged `o/main` to our currently checked out location which is not the local branch main. For this reason it can actually make sense to run git pull multiple times (with the same args) from different locations in order to update multiple branches.

`git pull origin main:foo`

Wow, that's a TON in one command. We created a new branch locally named `foo`, downloaded commits from remote's main onto that branch `foo`, and then merged that branch into our currently checked out branch bar. It's over 9000!!!

Goal to reach:
![Goal to reach](/Labs/img/2024-02-13-21-48-09.png)

Solution:

```bash
git pull origin bar:foo
git pull origin main:side
```

Explanation:

- `git pull origin bar:foo` to create a new branch `foo` locally, download the commits from `bar` on the remote and place them on `foo` locally, and then merge `foo` branch into the currently checked out branch.
- `git pull origin main:side` to create a new branch `side` locally, download the commits from `main` on the remote and place them on `side` locally, and then merge `side` branch into the currently checked out branch.
