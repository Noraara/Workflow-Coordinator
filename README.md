# Workflow Coordinator Skill

**Carry the brief, constraints, and evidence from one skill to the next.** Workflow Coordinator helps Codex and Claude Code handle tasks that span project knowledge and delivery. It passes the relevant context to the right specialist, collects the checks that actually ran, and can return useful findings to your project notes.

For example, [Atlas’ Notes](https://github.com/Noraara/Atlas-Notes) can find the size constraint for a Blender asset. [Blender Production](https://github.com/Noraara/Blender-Production) can build and verify the export. The coordinator keeps the size requirement and verification result tied to the same task.

## Quick start

Use [GitHub CLI](https://cli.github.com/) with support for [`gh skill install`](https://cli.github.com/manual/gh_skill_install).

```sh
# Codex
gh skill install Noraara/Workflow-Coordinator workflow-coordinator --agent codex --scope user

# Claude Code
gh skill install Noraara/Workflow-Coordinator workflow-coordinator --agent claude-code --scope user
```

Use `--scope project` from your project’s Git checkout for a project-only install. For a local checkout, replace `Noraara/Workflow-Coordinator` with its path and add `--from-local`. For manual setup, copy the entire [`skills/workflow-coordinator`](skills/workflow-coordinator) folder into a skills directory.

| Agent | One project | All projects |
| --- | --- | --- |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |

## Try a read-only handoff

Open a checkout of this repository and try the following in a fresh Codex session.

> Use $workflow-coordinator to read the cable guide brief under examples/cable-guide and prepare the handoff for Blender Production. Tell me what must be verified. Keep this read-only.

In Claude Code, start the request with `/workflow-coordinator`. Expect the task scope, the measurements from the brief, and the checks the delivery phase would need to run. The [worked cable guide example](examples/cable-guide/README.md) includes context and result packets, a Blender source, a GLB, and observed round-trip checks.

Try the [ordinary-files handoff](examples/cable-guide/standalone-handoff.md) for a route that uses the project brief directly and records partial progress when Blender is unavailable.

## How it works

| Task | What the coordinator does |
| --- | --- |
| Find an earlier project decision | Uses Atlas’ Notes if available, or reads the supplied notes and sources directly. |
| Deliver a focused change | Uses the named or best-fit installed workflow and the relevant task context. |
| Retrieve, deliver, and capture evidence | Passes scoped context to the delivery workflow, reviews the results, and returns verified findings for an authorized knowledge update. |

The [handoff protocol](skills/workflow-coordinator/references/protocol.md) uses a stable project ID, task ID, and scope. You can keep a small handoff in the conversation or save JSON for repeatable exchanges. An [optional Python checker](skills/workflow-coordinator/scripts/check_packet.py) checks the structure and can match a result to its context.

## Optional companion skills

| Skill | What it contributes |
| --- | --- |
| [Atlas’ Notes](https://github.com/Noraara/Atlas-Notes) | Source-backed project context and authorized updates to project notes. |
| [Blender Production](https://github.com/Noraara/Blender-Production) | Blender asset delivery and export verification. |
| [Forge OutSystems 11](https://github.com/Noraara/Forge-OutSystems-11) | Service Studio changes and verification of OutSystems 11 features. |
| [Tokenwise](https://github.com/Noraara/Tokenwise) | Focused retrieval and smaller verification output. |

The coordinator can also use other installed project skills. When one is missing, it reports which phase is affected and continues with the work it can do safely.

## Help and contributing

For an issue or pull request, include the host and version, the skills available, the request, the route you expected, and what happened. Use fictional or redacted context and evidence. For a protocol change, include a packet that exercises the change.

## License

Released under the [MIT license](LICENSE).

## Credit

Made by [Noraara](https://github.com/Noraara).
