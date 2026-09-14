# AGENTS.md

## Scope

This repository is an under-construction template for Kiro-based spec-driven
development. These instructions currently define command selection only; the
remaining shared development and review guidance is still being prepared.
Follow the language and contribution policy in README.md.

## Permission-aware command selection

Choose an execution form from the applicable permissions before composing a new
command. This rule applies to all shell operations, not just a particular tool.

### Establish the permission context

At task start, before shell execution, inspect the applicable permissions exposed
by the environment and any accessible active `permissions.yaml` files. Use an
available file-reading capability for this inspection. Identify the active user,
workspace, and other policy scopes from the environment; do not assume a file
with that name is active or search unrelated workspaces.

Use this information throughout the task. Do not reread unchanged policy before
every command. Refresh it when policy, workspace, execution environment, or
session context changes, or when an unexpected approval prompt contradicts the
known policy. If the policy cannot be read or its effective state is unknown,
state that limitation; do not infer permission from missing information.

### Select and reuse an allowed execution form

Before submitting a command:

1. Identify the required operation, target, working directory, runtime,
   arguments, and side effects.
2. If an explicitly allowed execution form meets all of those requirements and
   no applicable ASK or DENY overrides it, use that form. Do not choose a new
   spelling or invocation merely out of habit or stylistic preference.
3. Preserve its executable name, relative or absolute path form, launcher,
   argument structure, and required environment setup unless a concrete
   technical need requires a change. Supply task-specific arguments only
   within the applicable permission rules.
4. Set the intended working directory through the execution tool when supported.
   Avoid unnecessary directory-change commands, wrappers, shell nesting, or
   compound commands that alter permission matching.
5. Reuse a form that has already worked under the same applicable conditions.
   Successful execution alone is not proof of lasting permission: a one-time
   approval does not authorize subsequent operations.

Equivalent-looking commands may select different runtimes, targets, or side
effects. Permission matching never substitutes for checking correctness.
Derive eligible forms from active policy and established project guidance;
do not maintain a duplicate per-command allowlist in this document.

### Handle necessary exceptions

When selecting a form that requires new approval, explain the concrete reason
the known allowed forms cannot satisfy the task. If none is known or policy is
unavailable, say so instead of inventing a justification.

After an unexpected ASK, inspect the cause rather than submitting successive
aliases or invocation variants. Continue only under the effective policy and
the required approval for the intended operation. An authorization boundary is
not an execution error to work around.

### Preserve authorization boundaries

The runtime permission system remains authoritative. An ALLOW in one file does
not override an applicable ASK or DENY from another policy scope.

Never conceal an operation behind an allowed executable, alias, script, wrapper,
or compound command to evade ASK or DENY. Do not edit permission files, broaden
allow rules, disable safeguards, or change security settings merely to avoid an
approval prompt. Permission changes require a separate explicit instruction.

These instructions guide command selection; they do not grant execution rights
or guarantee that the runtime will execute a command without prompting.
