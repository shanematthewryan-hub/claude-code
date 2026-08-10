# Working preferences

## Always use ADHD mode

Apply the `adhd-mode` skill to every response in this project, not only when it
is explicitly requested. Read `.claude/skills/adhd-mode/SKILL.md` at the start of
a session and follow it throughout.

The short version, so it holds even before the skill is loaded: answer first, one
next action rather than a menu of options, keep multi-step state in a visible
task list, and open any resumption with where-we-are / what's-next. This is a
formatting and pacing contract — never a reason to simplify substance, omit
detail, or do less of the actual work.

To make this apply everywhere rather than just this repository, copy this file to
`~/.claude/CLAUDE.md` and the skill to `~/.claude/skills/adhd-mode/`.
