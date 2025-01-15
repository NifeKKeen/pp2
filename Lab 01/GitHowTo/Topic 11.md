# Tagging versions

You could easily check out to a specific version of the project by its tag name rather than by its hash. For this reason, Git has a feature called "tags".

## Creating a tag for the first version
```bash
git tag v1
git log

commit a0ab0624f7f598c6793b1f0518f85670c4824905 (HEAD -> main, tag: v1)
Author: [name] [email]
Date:   Wed Jan 15 09:01:44 2025 +0500

    Modify
```


## Tags for previous versions
Let's tag the version prior to the current version with the name `v1-beta`. First of all we will check out the previous version. Instead of looking up the hash of the commit, we are going to use the `^` notation, specifically `v1^`, indicating the commit previous to `v1`.

You can also try `v1~1`, which will reference the same version. The `V~[N]` notation means "the N-th version prior to `V`", or in case of `v1~1`, first version prior to `v1`.

```bash
git checkout v1^
git tag v1-beta
git switch main
git log

commit a0ab0624f7f598c6793b1f0518f85670c4824905 (HEAD -> main, tag: v1)
Author: [name] [email]
Date:   Wed Jan 15 09:01:44 2025 +0500

    Modify

commit 84ac51cb01c97c22614e20e1df5d096a1ce1194c (tag: v1-beta)
Author: [name] [email]
Date:   Mon Jan 13 10:30:42 2025 +0500

    Create helloWorld.py

```
