#!/usr/bin/env sh
# Install the i-have-adhd plugin (github.com/ayghri/i-have-adhd) and turn on
# always-on mode, then verify every piece actually landed.
#
# Safe to re-run: each step is idempotent.

set -u

claude_dir="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
flag_path="$claude_dir/.i-have-adhd-always"
fail=0

say() { printf '%s\n' "$*"; }

if ! command -v claude >/dev/null 2>&1; then
  say "FAIL: 'claude' is not on your PATH. Install Claude Code first."
  exit 1
fi

say "==> Adding marketplace"
claude plugin marketplace add ayghri/i-have-adhd || say "    (already added, continuing)"

say "==> Installing plugin"
claude plugin install i-have-adhd@i-have-adhd || say "    (already installed, continuing)"

say "==> Enabling always-on flag at $flag_path"
mkdir -p "$claude_dir" && touch "$flag_path"

# The SessionStart hook injects the ruleset into main sessions only — subagents
# spawned via the Task tool start with fresh context and never see it. A
# user-level CLAUDE.md does propagate to subagents, so it covers that gap, and
# it applies in every repository rather than just this one. The repo's own
# CLAUDE.md is the source, so there is one copy of the ruleset to maintain.
say "==> Extending CLAUDE.md to cover subagents"
src="$(dirname -- "$0")/CLAUDE.md"
memory="$claude_dir/CLAUDE.md"
marker="ADHD mode — always on"
if [ ! -f "$src" ]; then
  say "    skipped: CLAUDE.md not found next to this script"
elif [ ! -f "$memory" ]; then
  cp "$src" "$memory" && say "    created $memory"
elif grep -qF "$marker" "$memory" 2>/dev/null; then
  say "    already present, left unchanged"
else
  # Append rather than overwrite: an existing CLAUDE.md holds your own notes.
  { printf '\n'; cat "$src"; } >> "$memory" && say "    appended to existing $memory"
fi

say "==> Installing the second-opinion skill"
# Skills under ~/.claude/skills are available in every local session and to
# subagents, so the escalation rules apply wherever work happens — not just in
# this repository. The repo copy is the source; this is a copy, not a link.
skill_src="$(dirname -- "$0")/.claude/skills/second-opinion/SKILL.md"
skill_dst="$claude_dir/skills/second-opinion/SKILL.md"
if [ ! -f "$skill_src" ]; then
  say "    skipped: SKILL.md not found next to this script"
else
  mkdir -p "$(dirname -- "$skill_dst")" && cp "$skill_src" "$skill_dst" \
    && say "    installed $skill_dst"
fi

say ""
say "==> Verifying"

# 1. Plugin registered.
if claude plugin list 2>/dev/null | grep -q "i-have-adhd@i-have-adhd"; then
  say "  ok   plugin installed"
else
  say "  FAIL plugin not listed by 'claude plugin list'"
  fail=1
fi

# 2. Opt-in flag present where the hook looks for it.
if [ -f "$flag_path" ]; then
  say "  ok   always-on flag present"
else
  say "  FAIL flag missing at $flag_path"
  fail=1
fi

# 3. The hook that reads the flag is on disk. Without this the flag is inert,
#    which is the exact failure mode this script exists to rule out.
hook=$(find "$claude_dir/plugins" -path '*i-have-adhd*' -name 'always-on.mjs' 2>/dev/null | head -1)
if [ -n "$hook" ]; then
  say "  ok   SessionStart hook found"
else
  say "  FAIL hook always-on.mjs not found under $claude_dir/plugins"
  fail=1
fi

# 4. Dry-run the hook's own logic: it prints the ruleset only when the flag is
#    set, so non-empty output here means a real session will get it too.
if [ -n "$hook" ] && command -v node >/dev/null 2>&1; then
  if [ -n "$(node "$hook" 2>/dev/null)" ]; then
    say "  ok   hook emits the ruleset"
  else
    say "  FAIL hook ran but emitted nothing"
    fail=1
  fi
fi

# 5. Subagent coverage.
if [ -f "$memory" ] && grep -qF "$marker" "$memory" 2>/dev/null; then
  say "  ok   subagent coverage via CLAUDE.md"
else
  say "  WARN CLAUDE.md missing the ruleset - subagents will not inherit it"
fi

# 6. Second-opinion skill on disk where sessions and subagents will see it.
if [ -f "$skill_dst" ]; then
  say "  ok   second-opinion skill installed"
else
  say "  WARN second-opinion skill missing at $skill_dst"
fi

say ""
if [ "$fail" -eq 0 ]; then
  say "All checks passed. Restart Claude Code — the hook runs at session start,"
  say "so an already-open session will not pick it up. You will see a banner"
  say "beginning 'ADHD MODE ACTIVE (always-on)'."
else
  say "Something above failed. Re-run, or paste the output for help."
  exit 1
fi
