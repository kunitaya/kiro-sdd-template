---
inclusion: manual
description: Git worktree and Kiro Multi-root workspace isolation. Load with #workspace-isolation.
---

# Workspace Isolation

The portable execution identity for a task is the workspace root containing its Spec/working tree, resolved at runtime with `git rev-parse --show-toplevel`. Never commit an absolute filesystem path as a durable execution instruction.

Every Spec first artifact includes:

```text
STRICT WORKSPACE ISOLATION
Repository: <repository>
GitHub Issue: #<number>
Branch: <branch>
Allowed modification scope: <paths or repository-wide within this root>
Prohibited cross-root operations:
- edit files in another workspace root
- run repository-changing commands against another root
- use another worktree's uncommitted state as implementation truth
- copy uncommitted changes between worktrees
```

At task entry/resumption verify root, branch, and repository. Recheck after execution-context changes or uncertainty. A mismatch is a stop condition.

Git worktrees isolate working trees/indexes but do not guarantee AI-context isolation. Multi-root workspace surfaces may expose sibling roots' indexes, Specs, steering, hooks, or tool definitions. Treat sibling-root content as comparison context only, never implementation truth.

Use Multi-root primarily for overview, cross-Spec comparison, and dependency/ownership review. For genuine parallel implementation, prefer one IDE window per Issue/worktree unless the current Kiro version is known to provide the required independent task-execution concurrency.

If actual cross-root truth adoption, command execution against the wrong root, or cross-root file modification is observed, fall back to separate windows/workspaces for that scenario and record the operational limitation.