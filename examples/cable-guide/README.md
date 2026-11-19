# Cable guide handoff

This fictional task follows a desk cable guide from a project brief through delivery and back to a project note. It uses ordinary Markdown for the brief and JSON for two reviewable handoffs.

## Try the flow

1. Read the [brief](brief.md). If Atlas’ Notes is available, ask it to retrieve the constraints and point to their source. The [context packet](context.json) records what delivery needs.
2. Give the packet to Blender Production in an empty or disposable scene. Build an editable guide and export only the asset. Use the [source](cable-guide.blend) and [GLB](cable-guide.glb) as sample outputs.
3. Reimport the GLB into a clean Blender scene. Compare the evaluated dimensions, mesh count, and triangle count with the source. The [result packet](result.json) reports the observed checks, and [measurements.json](measurements.json) contains the underlying measurements.
4. If the request authorizes saving durable findings, pass the result back for a note update. The [sample note](handoff-note.md) records a compact outcome and points to the evidence.

The sample measurements came from an isolated Blender 5.2.2 LTS run. It covered the editable source and GLB round trip. No publication, visual acceptance, or engine runtime check was part of the fixture.

## Check the handoff

With Python 3, run this from the repository root.

```sh
python skills/workflow-coordinator/scripts/check_packet.py examples/cable-guide/context.json
python skills/workflow-coordinator/scripts/check_packet.py examples/cable-guide/result.json --context examples/cable-guide/context.json
```

You can also try the example without Atlas’ Notes. Use the brief directly. If Blender or its integration is unavailable, return the context and leave the delivery and export checks pending.
