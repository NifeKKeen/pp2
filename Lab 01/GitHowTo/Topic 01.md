# Topic 1 - Git Credentials

## Setting up name and email address
When git was installed in your machine, you should identify yourself:
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@whatever.com"
```

Now when you commit changes, in the commit history it is logged like this:
```
Author: Kanat <kanich@kidalovich.com>
```
also...
- Ensures your commits are correctly attributed.
- Helps avoid commit mismatches on GitHub/GitLab (especially if email privacy is enabled).
- Necessary for signing commits or using GPG keys.


## Default branch name
```bash
git config --global init.defaultBranch main
```

## Line endings treatment

Also, Unix/Mac users (LF - \n):
```bash
git config --global core.autocrlf input
git config --global core.safecrlf warn
```

For Windows users (CRLF - \r\n):
```bash
git config --global core.autocrlf true
git config --global core.safecrlf warn
```
