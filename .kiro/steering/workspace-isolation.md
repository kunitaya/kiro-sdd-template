---
inclusion: manual
description: Git worktree and Kiro Multi-root workspace isolation, runtime identity checks, contamination risks, and fallback rules. Load with #workspace-isolation.
---

# Workspace Isolation

This repository assumes a development model in which one change/Issue may own its own
Git worktree and Kiro root. Git worktrees isolate files/indexes, but that filesystem
isolation does not automatically imply AI-context, hook, task-execution, or tool-server
isolation. Keep those concerns distinct.

## Portable workspace declaration

A committed Spec must never record a machine-specific absolute filesystem path as its
durable execution identity. A Spec may later be opened from another clone, worktree,
machine, or IDE surface. Therefore workspace ownership is declared logically and
verified physically at runtime.

Every workflow's first Spec artifact contains a block equivalent to:

```text
STRICT WORKSPACE ISOLATION

This spec belongs exclusively to the workspace root containing this file
(resolved at runtime via `git rev-parse --show-toplevel`).

Repository: <repository name>
GitHub Issue: #<number>
Branch: <branch-name>
Allowed modification scope: <paths or repository-wide within this root>
Prohibited cross-root operations:
- edit files in another workspace root
- run repository-changing commands against another root
- use another worktree's uncommitted state as implementation truth
- copy uncommitted changes between worktrees

The main root may be referenced only for baseline comparison unless explicitly
authorized by this spec.
```

Do not replace the logical ownership sentence with `/home/...`, `C:\...`, or another
committed machine path.

## Runtime identity verification

At task entry/resumption, before file edits or project commands:

1. run `git rev-parse --show-toplevel` and treat the result as the owning physical root;
2. run `git branch --show-current` and confirm it matches the Spec's branch;
3. confirm repository identity from the actual root/remote;
4. confirm the requested operation is inside the Spec's allowed modification scope;
5. stop on mismatch instead of falling back to a path written elsewhere.

Reuse this verified identity only while the execution context remains unchanged. Repeat
checks after a root/branch/repository-context change, after an operation that may have
changed context, or whenever there is uncertainty. Before every commit/push, still apply
`AGENTS.md` branch safety checks even if root identity was verified earlier.

## Cross-root prohibitions

An agent working for one task must not:

- edit another worktree/root;
- execute repository-changing commands with another root as working directory/target;
- treat sibling-root uncommitted content as implementation truth;
- copy uncommitted changes from one worktree to another as a shortcut;
- use another root's generated environment as this root's mutable environment;
- broaden modification scope merely because another root is visible in Kiro indexing.

Committed sibling/main content may be used for baseline comparison when explicitly
allowed, but comparison context is not write authority.

## Worktree environment ownership

Mutable environments/caches that affect build or execution correctness must not be
silently shared between worktrees when cross-worktree mutation could break isolation.
The included Python/uv bootstrap therefore rejects symlinked or separately mounted
`.venv` directories and fingerprints the physical worktree root.

For another stack, apply the equivalent ownership rule to its generated environment,
package store, build output, or cache when mutation is not safely content-addressed or
otherwise isolated.

## Kiro Multi-root Workspace considerations

Multi-root Workspace is useful for review/overview because it can expose multiple roots
in one window. That convenience does not remove root discipline.

Treat these categories separately:

### Shared context surfaces

A Kiro window may expose code indexes, repository maps, Specs, steering entries, and
other context from multiple open roots. Same-named files from sibling worktrees can be
visible simultaneously. Root labels help a human but are not a safety boundary by
themselves.

Therefore:

- identify which root owns the current task before reasoning from same-named files;
- never treat sibling-root content as the active root's implementation truth;
- never let visibility expand the active Spec's allowed modification scope;
- prefer targeted references tied to the active root when ambiguity exists.

### Steering and hook scope

Steering/hook behavior may depend on Kiro version and inclusion/trigger type. Do not
assume every steering file or hook is root-scoped merely because file operations are.
When repository safety depends on a particular hook/inclusion behavior, verify the
installed Kiro version or keep an explicit repository-controlled check that does not
rely solely on that behavior.

### MCP / external tool definitions

Tool/MCP definitions can be workspace-scoped rather than root-scoped depending on Kiro
configuration. If multiple roots define same-named servers or tools, confirm which
configuration wins and which working directory/process context is used before treating
the tool as safe for root-bound mutation.

This generic template does not assume per-root MCP isolation.

## Multi-root versus separate windows

Use Multi-root primarily for:

- cross-Spec comparison;
- dependency/ownership review;
- roadmap/overview work;
- comparing sibling branches/worktrees without mutation.

For genuine parallel implementation, prefer one IDE window per Issue/worktree unless the
installed Kiro version has been verified to provide the independent task-execution
concurrency and root isolation the workflow needs. Multiple roots in one window do not
by themselves prove parallel Spec-agent execution.

This is an ergonomics/throughput choice, not a relaxation of workspace identity rules.

## Fallback condition

If actual operation reveals any of the following:

- sibling-root content is adopted as implementation truth;
- a project command runs against the wrong root;
- a hook/tool mutates the wrong root;
- cross-worktree file modification occurs;
- a workspace-scoped tool cannot be safely bound to the active root;

then stop using that Multi-root arrangement for the affected scenario and fall back to
separate windows/workspaces with one worktree per window until the behavior is understood
and corrected.

The existence of a safe fallback does **not** convert the original unsafe observation
into PASS. Record the actual failure truthfully and the fallback separately.

## Historical path evidence

A run-specific diagnostic or test report may record the actual absolute path observed
at that time when the path itself is relevant evidence. Such a recorded path is
historical observation, not a reusable execution instruction. Never copy it into a
Spec's durable workspace declaration.

## Finalization and archive scope

If a Spec declares a narrow allowed modification scope, include its eventual archive
path (`docs/spec-archive/<issue-number>-<slug>/`) from the start when final delivery is
expected to move the Spec there. The archive is a planned lifecycle transition, not an
excuse to discover and broaden scope only after final review.
