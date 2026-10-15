# agent-journal conventions

Machine-only. Token-cheap body ok. Frontmatter stays valid YAML.

## Frontmatter (required)

```yaml
---
title: architecture
summary: Bounds + dataflow + critical paths; open before large structural change.
updated: 2026-07-20
tags: [architecture, graphify]
---
```

| Field | Rule |
|-------|------|
| `title` | short slug-like or words |
| `summary` | one line; enough to decide open/skip |
| `updated` | ISO date when last materially changed |
| `tags` | optional |

## Body style (caveman ultra ok)

Allowed:

- Fragments, drop articles, sparse punctuation
- Arrows for flow: `api → service → db`
- Abbreviate prose (`auth`, `cfg`, `svc`) — never mangle real symbols/paths
- Dense bullets over paragraphs

Required exact:

- file paths, package names, class/fn names, env var names, API routes
- version pins when stating constraints

Example body:

```text
# architecture

entry: `apps/api/src/main.ts`
req → gateway → domain svc → repo → pg

god: `packages/domain/` (graphify)
ui: `apps/web` talk api only; no db

boundaries:
- domain no import ui
- infra adapters at edges

see: [[stack]] [[map]] [[gotchas]]
```

## index.md

Root index must include:

1. One-line purpose: agent journal; machine nav
2. Read protocol (open index → summaries → few notes → write back gaps)
3. Note list with summaries (and links)

Example:

```markdown
---
title: agent-journal
summary: Machine nav map for project truth; start here.
updated: 2026-07-20
---

# agent-journal

machine-only. read protocol: scan summaries → open 1-3 → write gaps back.

## notes
- [architecture](architecture.md) — Bounds + dataflow + critical paths
- [stack](stack.md) — langs frameworks datastores versions
- [product](product.md) — what/who/non-goals
- [philosophy](philosophy.md) — how this repo builds
- [map](map.md) — entrypoints dirs god nodes
- [gotchas](gotchas.md) — footguns do-nots
```

## Linking

Any scheme fine if stable inside journal:

- `[[architecture]]`
- `[architecture](architecture.md)`
- bare `` `architecture.md` ``

Prefer links to repo paths for code: `` `src/foo/bar.ts` ``

## Suggested starter notes

Create if evidence exists; skip empty shells.

| Note | Capture |
|------|---------|
| architecture | components, flows, boundaries |
| stack | runtime, libs, data, infra |
| product | purpose, users, non-goals |
| philosophy | conventions, testing bar, PR norms seen in repo |
| map | entrypoints, dirs, graphify god nodes |
| gotchas | traps, flaky tests, local setup pitfalls |
| services | multi-service ownership + ports |
| workflows | build/test/lint/deploy commands that actually work |
| glossary | project jargon |

## Relation to other folders

| Folder | Role |
|--------|------|
| `agent-journal/` | durable project truth for agents |
| `working-sessions/` | ephemeral task work |
| `graphify-out/` | graph artifacts; journal cites, does not replace |
| human docs (`README`, `docs/`) | source input; journal may compress, never "fix" human docs unless asked |
