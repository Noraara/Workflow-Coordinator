# Hand off a project brief with ordinary files

Open the cable guide example and ask the coordinator to use its [project brief](brief.md), prepare the Blender delivery, and record only observed results. The coordinator can read the brief with ordinary file tools. Use the [context packet](context.json) to keep the 50 × 24 × 15 mm envelope, 8 mm opening, and round-trip criteria attached to the same task. Pass it to Blender Production or an installed asset delivery skill that owns those checks.

If Blender is available, compare the resulting measurements against the brief and return the [completed result](result.json). If the required tool is unavailable, the brief and acceptance criteria still stand. Return the [partial result](partial-result.json) to the caller. Resume by opening the permitted Blender scene, confirming the bridge and the current file, and continuing with the same identity and scope. Keep the project note at brief status until there is observed delivery evidence.

```sh
python skills/workflow-coordinator/scripts/check_packet.py examples/cable-guide/partial-result.json --context examples/cable-guide/context.json
```
