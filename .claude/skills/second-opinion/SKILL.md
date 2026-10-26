---
name: second-opinion
description: Decide whether to get a cross-model second opinion (Codex/GPT, Gemini) before answering, and run it cheaply. Use when a task is high-stakes, irreversible, architectural, a disputed factual claim, or when two prior attempts have failed — not for routine work. Also use when the user asks to "check with", "get a second opinion", "ask Codex", "ask Gemini", or "have the agents collaborate".
---

# Second opinion

Default is solo. Escalate only when the cost of being wrong beats the cost of
asking. Most tasks are solo tasks.

## 1. Decide (10 seconds, no tools)

Escalate if **two or more** are true:

1. **Irreversible** — deletes data, force-pushes, spends money, sends to a
   real recipient, or is hard to walk back.
2. **Architectural** — a choice the next month of work is built on top of.
3. **Disputed or fast-moving fact** — API shape, pricing, a version's
   behaviour, anything where being confidently stale is the failure mode.
4. **Two attempts already failed** — the third try with the same assumptions
   is the expensive one. A fresh model breaks the loop.
5. **The user explicitly asked** — always honour it, skip the rest of this.

Do **not** escalate for: formatting, renames, single-file edits, anything with
a test that decides the answer, or a question you can settle by reading the
code. Reading the actual source beats any panel of models.

## 2. Pick the cheapest rung that works

| Rung | When | Cost |
|---|---|---|
| 0. Solo | Default. Everything above is false. | free |
| 1. Read the source / run the test | Anything checkable | ~free, most reliable |
| 2. One outside model | 2+ triggers true | one call |
| 3. Two outside models | Rung 2 came back split, and the stakes justify it | two calls |

Never start at rung 3. Stop the moment the answer converges — a matching
second opinion ends it; do not poll a third for a tiebreak you do not need.

**Who to ask for what:**
- **Codex / GPT** — code correctness, edge cases, "will this actually run".
- **Gemini** — long-context review, breadth, alternate framing of a design.
- **A Claude subagent** (`Agent` tool) — only when the user asked for one, or
  a fan-out search is genuinely needed. Each spawn re-derives context you
  already have, so it is the expensive option, not the free one.

## 3. Run it

Check availability first — these CLIs are on the user's Mac, not in cloud
containers:

```sh
command -v codex gemini
```

If neither is present, say so in one line and answer solo. Do not stall.

```sh
codex exec  "<question>"   # non-interactive
gemini -p   "<question>"   # non-interactive
```

Flags drift between releases; if a call errors, run `codex --help` /
`gemini --help` once, fix the invocation, and move on. Two failed invocations
means answer solo and note it.

**Write the question so one call is enough:**
- State the constraint, the code, and the specific decision. No conversation.
- Ask for a verdict plus the reasoning, not an essay.
- Never paste secrets, tokens, `.env` contents, or private customer data into
  another vendor's CLI. Redact first; if it cannot be redacted, do not ask.
- One round trip. Do not relay a debate between models.

## 4. Report

Three lines, then the work:

```
Asked: Codex — is this migration reversible?
Verdict: agrees / splits (what each said in one clause)
Doing: <the action you are now taking>
```

If they disagree and you cannot break the tie from the code, say which one you
are following and why in one sentence — then act. Do not hand the user an
unresolved debate as the deliverable.
