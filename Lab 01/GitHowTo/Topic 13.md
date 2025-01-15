# Cancel staged changes (before committing)

## Change `helloWorld.py`

```helloWorld.py
print("Hello, Kanich!")
```

## Stage the modified file.

```bash
git add hello.html
```

## Reset the staging area
The `reset` command resets the staging area to `HEAD`. This clears the staging area from the changes that we have just staged.

```bash
git reset HEAD hello.html
```

The `reset` command (default) does not change the working directory. Therefore, the working directory still contains unwanted comments. We can use the `checkout` command from the previous tutorial to remove unwanted changes from working directory.

