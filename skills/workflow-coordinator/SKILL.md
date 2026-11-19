---
name: workflow-coordinator
description: Coordinate installed skills when a project task needs a handoff between research, delivery, or evidence capture. Use when a user requests workflow routing or asks to apply prior project decisions, verify the result, and return findings.
license: MIT
---

# Workflow Coordinator

Choose the route from the current request. Use the workflow the user names, or pick an installed skill whose declared scope fits. Read its instructions before using it. Keep routine single-workflow work local to that workflow.

- **Knowledge only.** Use Atlas’ Notes if available, or retrieve the answer directly from the selected project’s notes and sources.
- **Delivery only.** Use the requested or clearly applicable delivery skill and the relevant context. Blender Production and Forge OutSystems 11 are examples.
- **Mixed work.** Follow the [handoff protocol](references/protocol.md). Gather scoped knowledge, pass it to the delivery workflow, assess its evidence, and return verified results for any authorized knowledge update.

For Atlas or Forge, resolve the public skill names or the corresponding earlier local names using [routing guidance](references/routing.md). Tokenwise can guide retrieval and verification without a separate phase. If a skill or tool is unavailable, identify the affected capability and complete authorized work that can still be verified. One agent can carry out all phases.

Keep one project ID, task ID, and scope throughout the handoff. Current task authorization governs edits, publishing, and knowledge writes. Preserve unrelated work. Report delivery, verification, and note updates separately, and have each workflow return control to the coordinator.
