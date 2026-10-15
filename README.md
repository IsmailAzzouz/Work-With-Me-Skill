# Work With Me

Two Markdown skills for coding agents: a structured workflow for each task and a persistent journal for project knowledge.

**Work With Me** keeps scope, acceptance criteria, decisions, and verification together. **Learn Project** records the context an agent needs to resume work without rediscovering the repository.

No application, runtime dependencies, or account setup. Install the folders and connect them to your agent's instructions.

## The skills

| Skill | Purpose | Writes to your project |
| --- | --- | --- |
| [work-with-me](skills/work-with-me/SKILL.md) | Work through context, scope, acceptance criteria, approach, tests, refinements, fixes, and remaining issues. | `working-sessions/<Session name>/` |
| [learn-project](skills/learn-project/SKILL.md) | Build and maintain a concise map of architecture, stack, product, conventions, and gotchas. | `agent-journal/` |

Install both. Work With Me uses Learn Project to retrieve context and preserve durable lessons. Simple questions and trivial edits do not need a full working session.

## Install

Download and extract `work-with-me-v0.1.0.zip` from [GitHub Releases](https://github.com/IsmailAzzouz/Work-With-Me-Skill/releases), or clone the repository. Run the commands below from the extracted folder or repository root containing `skills/`.

### 1. Choose a skills directory

| Agent | Personal installation | Project installation | Documentation |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/` | `.agents/skills/` | [Skills](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` | [Skills](https://code.claude.com/docs/en/skills) |
| Cursor | `~/.cursor/skills/` | `.cursor/skills/` | [Skills](https://cursor.com/docs/skills) |

The examples use a personal Codex installation. Change the destination for your agent, or use the skills directory inside your target project. These are documented installation locations, not a claim of end-to-end testing across every agent or version.

**macOS / Linux**

```bash
skills_dir="$HOME/.agents/skills"
mkdir -p "$skills_dir"
cp -R skills/work-with-me skills/learn-project "$skills_dir/"
```

**Windows (PowerShell)**

```powershell
$skillsDir = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Force $skillsDir | Out-Null
Copy-Item -Recurse -Path skills\work-with-me, skills\learn-project -Destination $skillsDir
```

Copy the complete folders, including `references/` and `LICENSE`. For updates, back up any local customizations and replace the two installed folders with the new release; do not rely on merging old and new files.

### 2. Connect the workflow

Merge [templates/AGENTS.md](templates/AGENTS.md) into your target project's agent instructions. Replace `<skills-dir>` with the installed location; for a project-local Codex installation, use `.agents/skills`.

If your agent reads a different instructions file, such as `CLAUDE.md`, add the same guidance there or explicitly instruct it to read `AGENTS.md`. Preserve any existing project instructions.

### 3. Try it

Start a new agent session and ask:

```text
Use learn-project to map this repository and create agent-journal/index.md.
```

Then start a task:

```text
Use work-with-me to investigate this bug. Record the scope and acceptance
criteria before changing code, then verify the fix.
```

Check that the agent can read both `SKILL.md` files and their references. The expected result is a project journal and a task folder containing `notes.md`. Skill discovery and automatic selection depend on the agent; naming the skill explicitly helps verify the installation.

## What gets created

```text
your-project/
  AGENTS.md
  agent-journal/
    index.md
    architecture.md
    stack.md
    ...
  working-sessions/
    Fix auth token expiry/
      notes.md
```

The skills instruct the agent to create and maintain these files. Project source code stays in its normal location; session folders hold task notes and temporary artifacts.

Decide whether to commit generated journals and sessions in each project. Keep credentials and private data out of both, even when ignored by Git. Review generated notes before making them public.

## Optional integrations

The workflows include fallbacks for `graphify`, `knowledge-base-builder`, `karpathy-guidelines`, `ponytail`, and `caveman`. None is required or distributed here. Their names refer to optional external skills; availability, installation, and licensing are managed by their respective projects.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for reporting issues, proposing focused changes, and checking skill behavior. Release history is in [CHANGELOG.md](CHANGELOG.md).

## License

MIT — Copyright (c) 2026 Ismail Azzouz. See [LICENSE](LICENSE). Each installable skill includes a copy of the license.
