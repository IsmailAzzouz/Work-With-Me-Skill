# Contributing

This repository distributes two Markdown skills and their supporting references. Keep changes focused on agent behavior, clear instructions, or installation and packaging.

## Report an issue

Open an issue in this repository with:

- The agent and version you used.
- The skill version and installation method.
- A minimal prompt that reproduces the problem.
- Expected and observed behavior.
- A short, sanitized excerpt if it helps explain the result.

Do not include credentials, private project contents, or complete agent transcripts containing sensitive information. For a security issue, use the repository's private vulnerability reporting feature if enabled; do not post exploitable details or secrets in a public issue.

## Propose a change

1. Describe the concrete problem and the resulting behavior.
2. Edit the relevant skill or reference. Preserve the separation between task sessions and durable project knowledge.
3. Update installation examples or documentation when behavior changes.
4. Explain what you verified and what remains untested in your pull request.

Keep optional integrations optional. Avoid introducing dependencies or universal workflow rules to solve a single project's problem. Contributions are made under the repository's MIT license.

## Verify your changes

Check that both `SKILL.md` files have valid YAML frontmatter, matching folder names, useful descriptions, and working relative links. Render edited Markdown, including fenced examples, and keep the root and per-skill licenses identical.

For behavior changes, use a disposable project and record the agent and version. Check that Learn Project produces an index pointing to real project facts, and that Work With Me records task scope, acceptance criteria, and verification without moving product files into the session folder. Repeat without optional companion skills when changing fallback behavior.

There is no application build or runtime test suite. Static checks do not establish agent behavior; report live checks separately.
