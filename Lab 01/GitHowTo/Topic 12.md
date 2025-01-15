# Discarding local changes (before staging)

## Change `helloWorld.py`

```helloWorld.py
print("Hello, Kanich!")
```

## Undoing the changes in the working directory
Use the `checkout` command in order to check out the repository's version of the `helloWorld.py` file.

```bash
git checkout helloWorld.py
cat helloWorld.py
print("Hello, world!")
```