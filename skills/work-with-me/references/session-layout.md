# Session layout

Canonical layout for `working-sessions/<Session name>/`. Create files as needed; do not invent empty boilerplate.

```text
working-sessions/
  <Session name>/
    notes.md           # required: journal of record
    acceptance.md      # optional: long acceptance criteria
    plan.md            # optional: how-to plan if notes.md gets crowded
    gotchas.md         # optional: pitfalls discovered
    thoughts.md        # optional: study / design thoughts
    logs/              # command output, failing test dumps, traces
    study/             # excerpts, links, research notes
    debug/             # one-off debug scripts (not product code)
    seeds/             # local seed data / fixtures for this work
    docs/              # scratch docs only for this session
```

## `notes.md` template

````markdown
# <Session name>

## Goal
<one sentence>

## Context
- Repos:
- Services:
- Branch:
- Related PRs/issues:

## Knowledge retrieved
- <path or graph query> — <what it told us>

## What needs to be done
-

## Out of scope
-

## Acceptance criteria
- [ ] ...

## How
1. ... → verify: ...

## Files touched
| Path | Change |
|------|--------|
| | |

## Commands / tests
```bash
# how to run verification
```

## Journal
- YYYY-MM-DD: ...

## Gotchas
-

## Coverage / issues / follow-ups
-
````

## Naming

- Session folder names: human-readable goal, e.g. `Adding X feature`, `Fix auth token expiry`.
- Prefer Title Case or sentence case; avoid slug-only names unless the user asks.
- Keep names stable once work starts; rename only if the goal truly changes.

## Git hygiene for sessions

- Session folders may be gitignored by the project; still maintain them locally.
- Keep secrets and private data out of notes and logs, whether or not the project tracks `working-sessions/`.
- When recording files touched, prefer real paths from `git status` / `git diff --name-only`.
