# Getting older versions

```bash
$ git log
commit a0ab0624f7f598c6793b1f0518f85670c4824905 (HEAD -> main)
Author: [name] [email]
Date:   Wed Jan 15 09:01:44 2025 +0500

    Modify

commit 84ac51cb01c97c22614e20e1df5d096a1ce1194c
Author: [name] [email]
Date:   Mon Jan 13 10:30:42 2025 +0500

    Create helloWorld.py

```

## Going back to the first version

```bash
git switch a0ab0624f7f598c6793b1f0518f85670c4824905
cat hello.html

```

## Returning to the latest version in the `main` branch

```bash
git switch main
cat hello.html

print("Hello, world!")
```