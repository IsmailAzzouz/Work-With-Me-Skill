---
name: learn-project
description: >-
  Build and maintain project-root agent-journal/: machine-only notes
  (architecture, stack, product, philosophy, gotchas, map), graph-first when
  graphify is available. Caveman-ultra token-cheap prose ok. Use when learning
  a new project, onboarding, "learn this repo", refreshing agent context, or
  before non-trivial work when agent-journal/ is missing or stale.
license: MIT
---

# Learn Project

Create + maintain `agent-journal/` at the **project root**. Audience = agents only. Humans never the target. Token-cheap writing ok (caveman **ultra**): drop fluff, articles, punctuation if meaning stays clear. Keep paths, symbols, APIs, package names exact.

## Companion skills (optional)

| Skill | Use | Fallback if not installed |
|-------|-----|---------------------------|
| `graphify` | Build/query project knowledge graph; prefer `graphify-out/` + `query` before raw sprawl | Scan manifests, entrypoints, imports, top dirs by hand |
| `knowledge-base-builder` | Keep `agent-journal/` navigable: every note `summary` frontmatter + `index.md` tree | Follow [conventions.md](references/conventions.md) directly |

Also align with `work-with-me`: knowledge retrieval should read this journal first when it exists.

## Goal

After learn: cold agent opens `agent-journal/index.md` → picks 1–3 notes via summaries → enough context to work without re-discovering stack/architecture/product from scratch.

## Layout

```text
agent-journal/
  index.md              # nav protocol + map (machine)
  architecture.md
  stack.md
  product.md
  philosophy.md
  map.md                # entrypoints, key dirs, god nodes
  gotchas.md
  services.md           # optional mono/multi-service
  workflows.md          # optional build/test/deploy
  glossary.md           # optional project terms
  ...                   # agent may add more notes as needed
```

Agent chooses links (`[[wikilinks]]`, relative md links, or bare paths). Consistency inside one journal > matching human docs style.

Full note schemas: [conventions.md](references/conventions.md).

## Workflow

### 1. Assess

- If `agent-journal/` exists: read `index.md`, check note dates/summaries, decide refresh vs full rebuild.
- Scan repo: README, agent instructions file (`AGENTS.md` or harness equivalent), package manifests, docker/compose, CI, top dirs.
- If graphify available and `graphify-out/` missing or stale → run graphify on project (or `--update`). Prefer graph queries for architecture/map over reading everything.

Tell user briefly: found X / will create or refresh journal. Then proceed (do not wait unless destructive moves needed; journal is additive).

### 2. Extract (graph-first when available)

Pull facts into notes:

- **architecture**: components, boundaries, data flow, critical paths
- **stack**: languages, frameworks, datastores, infra, versions if known
- **product**: what it does, users, non-goals
- **philosophy**: conventions, patterns the codebase already follows, "how we build here"
- **map**: entrypoints, important dirs, god modules (from graphify when available)
- **gotchas**: traps, footguns, "do not"
- add other notes only if they earn a summary slot (auth, domain model, etc.)

Use graph reports and queries to navigate. Verify conclusions against current code and configuration; when sources disagree, current implementation takes precedence over generated graphs or descriptive documentation. Record intended behavior separately when it differs.

### 3. Write machine notes

- Caveman ultra ok in body. Frontmatter still structured (YAML) so indexes work.
- Every note: `title` + one-line `summary` (summary = decide-to-open signal).
- Link heavily between notes; point to real repo paths.
- No secrets (tokens, passwords). Point to secret *locations* only.

### 4. Index

- Apply knowledge-base-builder conventions (or [conventions.md](references/conventions.md)) to `agent-journal/`.
- Root `index.md` = navigation protocol + list of notes with summaries.
- If subfolders appear later, each gets `index.md`.

### 5. Maintain

Refresh when:

- user says learn/refresh
- stack or architecture clearly drifted
- agent repeatedly rediscovers facts not in journal
- after large features land (merge key learnings; leave session detail in `working-sessions/`)

Update only stale notes. Keep summaries honest. Re-run graphify `--update` when structure shifted.

## Read protocol (any agent)

1. Open `agent-journal/index.md`
2. Pick notes by `summary`
3. Open only those
4. If gap → investigate code/graph → **write back** into journal (compounding knowledge)

## Anti-patterns

- Human-polished essays / marketing tone
- Dumping whole files into journal
- Duplicating `working-sessions/` task logs here (promote only durable project truth)
- Skipping index/summaries
- Inventing architecture not evidenced in repo

## Additional resources

- Note schemas + style: [conventions.md](references/conventions.md)
