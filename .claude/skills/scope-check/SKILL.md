---
name: scope-check
description: Cut a build request down to the smallest version that solves the real problem before writing anything. Use when the ask is to build, automate, centralise, integrate or set up a system, hub, dashboard, pipeline or workflow — especially when it names several tools at once, or when scope has grown mid-conversation.
---

# Scope check

Run this before writing code or config for anything system-shaped. It takes
about two minutes and it is not a request for permission — do the work after,
in the same turn.

## 1. Name the recurring cost

One sentence, concrete: *what does this cost right now, per week?*

"Ten minutes every Monday reconciling two lists." "Missed a renewal twice."
"Re-typing the same reply four times a day."

If that sentence cannot be written, there is no problem to build for yet —
say so and stop. A system built for an anticipated cost is a hobby, which is
fine, but it should be called one.

## 2. Find the one-hour version

What is the smallest thing that removes most of that cost?

Usually one of these, and usually enough:

1. A single file or page — one list, one table, one note.
2. A recurring calendar entry or reminder.
3. One script run by hand.
4. One integration between exactly two things.
5. A checklist.

An hour of build for a weekly ten minutes pays back in six weeks. A weekend
of build for the same ten minutes pays back in a year, if it survives.

## 3. Test the difference

Ask what the elaborate version does that the one-hour version does not, and
whether that difference is worth its maintenance. Say the answer out loud in
the reply.

Rule of thumb: **every extra moving part must remove a recurring decision.**
If it adds a dashboard to check, a sync to watch, or an agent to supervise, it
has moved the work rather than removed it. Multi-tool architectures fail here
most often — each connector is a thing that breaks quietly while being trusted.

## 4. Deliver, and state the cut

Build the small version now. Then, in two or three lines:

```
Built: <the small thing>
Left out: <the parts deferred> — add when <the concrete trigger>
```

Naming the trigger matters. "Add SMS when you've missed something the calendar
reminder didn't catch" is a real condition. "Add SMS later" is scope waiting to
return.

## When to skip this

- The larger build is the point — the reader is building it to learn or enjoy
  it, and has said so.
- The reader has already been through this and reaffirmed the bigger scope.
  Once is a check; twice is nagging. Build what was asked.
- The request is a single bounded task, not a system.
