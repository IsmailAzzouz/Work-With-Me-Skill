---
name: work-with-me
description: >-
  Default collaboration workflow for non-trivial work. Keeps every task in its
  own working-sessions/ folder, reads the project's agent-journal/ first
  (learn-project), and runs fixed pragmatic phases: knowledge retrieval → scope
  → acceptance criteria → how → tests → refinements → fixes → coverage/issues.
  Use at the start of every non-trivial task, feature, bugfix, investigation,
  or when the user says "work with me", "session", or "follow the workflow".
license: MIT
---

# Work With Me

Default operating mode for all non-trivial work.

## Companion skills

Use these alongside this workflow for every substantive task (not one-line Q&A). Only `learn-project` ships with this skill; the rest are optional. If a companion is not installed, apply its principle inline (the "Fallback" column) and carry on.

| Skill | Role | Fallback if not installed |
|-------|------|---------------------------|
| `learn-project` | Ensure `agent-journal/` exists and is fresh; machine-only project truth | — (bundled) |
| `graphify` | Knowledge retrieval / codebase graph queries when `graphify-out/` exists or architecture relationships matter | Read manifests, entrypoints, and directory structure directly |
| `knowledge-base-builder` | Keep `agent-journal/` and large note trees navigable (`index.md` + summaries) | Every note gets a one-line `summary`; every folder gets an `index.md` |
| `karpathy-guidelines` | Think before coding, simplicity, surgical diffs, verifiable goals | Surface assumptions, smallest diff, define pass/fail before coding |
| `ponytail` | Laziness ladder: YAGNI, reuse, stdlib, minimal code (default **full**) | Question the need; reuse > stdlib > platform > new code |
| `caveman` | Terse communication (default **lite** unless the user asks for full/ultra); journal bodies may use ultra | Drop filler and hedging; keep technical detail exact |

Do not skip the stack because the task "seems simple" if it touches code, docs, or multiple files.

## Working sessions (mandatory)

Every project has a `working-sessions/` folder at the repo root. Create it if missing.

Each piece of work gets its own session folder named for the work, e.g.:

```text
working-sessions/
  Adding X feature/
  Fix auth token expiry/
```

**Session artifacts live in that folder**: task notes, logs, gotchas, research, debug scripts, seed data, and scratch docs. Product code, tests, and requested documentation changes stay in their normal project locations. Do not promote temporary session artifacts into the main codebase unless the user asks.

### Session bootstrap

At the start of work:

1. Ensure `working-sessions/` exists.
2. Create or reopen the session folder for this task.
3. Create/update `notes.md` (journal of record).
4. Capture context in `notes.md` early:
   - Goal (one sentence)
   - Repos / services involved
   - Branch name(s)
   - Key files (update via `git status` / `git diff` as work proceeds)
   - Open questions / assumptions
5. Add other files as needed (see [session-layout.md](references/session-layout.md)).

Keep `notes.md` current as you go: decisions, gotchas, commands run, links to logs.

## Pragmatic workflow (order is fixed)

Do phases in order. Write phase outcomes into the session (`notes.md` and/or dedicated files). Do not jump to implementation before 1–4 are clear enough to execute.

### 1. Knowledge retrieval

- First: read `agent-journal/index.md` if present (skill: `learn-project`). If missing or clearly stale for this work, run/refresh learn-project before deep coding.
- Then: the project's agent instructions file (`AGENTS.md` or your harness's equivalent), `graphify` queries, KB indexes, session notes, docs, prior sessions.
- Skim only what is needed; cite paths in session `notes.md`.
- If the map is missing and the codebase is unfamiliar, run/update learn-project (and graphify if available) before guessing.

### 2. What needs to be done

- State the problem and the smallest useful outcome.
- List out-of-scope items explicitly (YAGNI).
- Surface assumptions; ask if blocked.

### 3. Acceptance criteria

- Write verifiable checks (pass/fail). Prefer tests as criteria when code changes.
- Put them in `notes.md` under `## Acceptance criteria` (or `acceptance.md` if long).

### 4. How to do it

- Short plan: steps + how each step is verified.
- Prefer the laziness ladder; surgical changes only.
- Note repos/services/files/branch in the plan.

### 5. Tests

- Add or update tests that lock the acceptance criteria first when practical (red → green).
- Record how to run them in `notes.md`.

### 6. Refinements

- Tighten design/API/names only if needed to meet criteria. No drive-by refactors.

### 7. Fixes

- Fix failures from tests/review; keep diffs surgical; log gotchas.

### 8. Code coverage and issues

- Check coverage for touched code; note gaps.
- Scan for leftover issues (lints, TODOs you introduced, open risks).
- Update session notes with final status: done / blocked / follow-ups.

## Session hygiene

- One session per distinct goal; do not mix unrelated work.
- Promote durable docs into the real project docs/KB only when the user asks (then use `knowledge-base-builder` if organizing a notes tree).
- Durable project truth learned during the session goes to `agent-journal/` (learn-project); task detail stays in the session.
- Debug scripts and seeds stay under the session folder unless they become product assets.
- Before ending a session, leave `notes.md` readable by a cold agent: goal, branch, files touched, how to verify, leftovers.

## Trivial work exception

Skip full session scaffolding only for truly trivial asks (definition lookup, one-line answer, single obvious edit with no investigation). If unsure, open a session.

## Additional resources

- Session folder layout and templates: [session-layout.md](references/session-layout.md)
