# Handoff protocol

Use the [packet template](../assets/packet.md) for Markdown or use JSON. A short handoff can stay in the conversation. Required fields in both kinds are `schema`, `kind`, `project_id`, `task_id`, and `scope`. Use schema `atlas-workflow/v1` for new packets.

| Kind | Fields in addition to the common identity |
| --- | --- |
| `context` | `constraints`, `decisions`, `evidence`, `unknowns`, `acceptance` |
| `result` | `changes`, `decisions`, `checks`, `findings`, `unresolved`, `next_action` |

Context evidence should identify the file or URL, the relevant finding, and any limit that changes its interpretation. A result should include each check’s `name`, `status`, `evidence`, and `observed` outcome when applicable. Use `pass`, `fail`, `unverified`, or `not-applicable`. A pass requires an observation and a pointer to the evidence. Keep build, runtime, visual, publication, and user acceptance results distinct.

Gather only the context the next phase needs. Keep credentials, authentication state, sensitive records, and whole transcripts out of packets. Use a single writer for an artifact or workspace. Current authorization governs edits and external changes. Before resuming interrupted work, inspect the latest evidence and the current target.

The optional [Python 3 checker](../scripts/check_packet.py) checks JSON structure and accepts the older `atlas-forge/v1` schema with the same fields. Use `--context` to check that a result has the same project ID, task ID, and scope as its context. Check the original evidence separately.
