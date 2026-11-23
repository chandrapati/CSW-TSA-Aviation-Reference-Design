# Diagram tools

Regenerates the diagrams in `../assets/` so they stay in step with the
reference design rather than drifting from it.

```bash
cd .diagram-tools && python3 build.py ../assets
```

Requirements: Python 3 with Pillow, and Google Chrome at the path in
`render.py`. Rendering happens at `deviceScaleFactor=2` and downsamples to the
logical size, which keeps text sharp at a file size reasonable to commit.

## Files

| File | Purpose |
|---|---|
| `theme.py` | Palette and base CSS. Colours were sampled from the Cisco CSW workflow infographics, so everything sits in the Cisco blue family with light-green success callouts and amber for the boundary column. |
| `diagrams.py` | Layout builders: `evidence_workflow` and `scope_boundary`. |
| `spec_tsa_aviation.py` | The content. Every string is lifted from the reference design so the diagram and the prose cannot disagree. |
| `render.py` | Headless Chrome render and downsample. |
| `build.py` | Renders the set. |

## Conventions

Diagrams are committed as PNG rather than Mermaid for two reasons. PNGs embed
in the pandoc-generated DOCX and PDF exports, which Mermaid does not, and they
render identically wherever the markdown is read.

Edit `spec_tsa_aviation.py` and re-run rather than editing the PNGs. If a
statement changes in the reference design, change it here too.

`scope_boundary` sizes its columns from the row count and asserts the column
can hold every row it was given, because a diagram that silently drops a row
of in-scope estate is worse than no diagram.

Keep these diagrams free of competitive comparison. This is a public,
customer-facing repository, so positioning belongs on Cisco capability and the
evidence boundary; competitive material belongs in internal battle cards.
