# Committing the changes
When you previously used git commit for committing the first version to the repository, you included the `-m` flag that gives a comment on the command line. The commit command allows interactively editing comments for the commit. And now, let's see how it works.

If you omit the `-m` flag from the command line, Git will pop you into the editor of your choice from the list (in order of priority):

```
GIT_EDITOR environment variable;
core.editor configuration setting;
VISUAL environment variable;
EDITOR environment variable.
```