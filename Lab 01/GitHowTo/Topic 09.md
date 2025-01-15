# History

Getting a list of changes made is a function of the git log command.

```bash
git log
```

## There are some parameters which can be used along it:
```bash
git log --oneline
git log --oneline --max-count=2
git log --oneline --since="10 minutes ago"
git log --oneline --until="10 minutes ago"
git log --oneline --author="Kanich"
git log --oneline --all
git log --all --pretty=format:"%h %cd %s (%an)" --since="7 days ago"
```

Some tools like `gitx` (for Mac) and `gitk` (for any platform) can help to explore log history.