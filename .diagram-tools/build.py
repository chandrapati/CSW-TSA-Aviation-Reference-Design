"""Render the TSA Aviation diagram set."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import diagrams
import render
from theme import base_css
import spec_tsa_aviation as s

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/diagrams/out")

JOBS = [
    ("evidence_workflow", s.EVIDENCE_WORKFLOW, "csw-evidence-workflow",
     96 + 22 + 382 + 16 + 58 + 92),
    # scope_boundary sizes its own columns from the row count; height comes back
    # on the spec so the sheet always fits every row rather than clipping some.
    ("scope_boundary", s.SCOPE_BOUNDARY, "csw-scope-boundary", None),
]

for kind, spec, name, height in JOBS:
    body = diagrams.BUILDERS[kind](spec)
    if height is None:
        height = int(96 + 18 + 126 + spec["_col_h"] + 34 + 92)
    p = render.render(render.page(body, base_css(), diagrams.W, height),
                      OUT / f"{name}.png", diagrams.W, height)
    print(f"  {name}.png  {diagrams.W}x{height}  {os.path.getsize(p) // 1024} KB")


# The scope-architecture graphic lives in its own script, so run it from here too.
import os as _os
import runpy as _runpy

_runpy.run_path(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "build_tree.py"),
                run_name="__main__")
