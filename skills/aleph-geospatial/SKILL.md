---
name: aleph-geospatial
description: Use Aleph to gather geospatial context for site research, including OpenStreetMap buildings, terrain and supported imagery. Use for map-area capture and site-context collection, not survey-grade or legally verified site assessment.
---

# Aleph geospatial capture

Upstream: https://github.com/Belluxx/Aleph (MIT). This is an integration guide, not a bundled copy of Aleph.

## Setup

Requires Python 3.11+. In a user-selected tools directory:

```sh
git clone https://github.com/Belluxx/Aleph.git
cd Aleph
python3.11 -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/alephgeo --help
```

Use the virtual environment executable; do not change system Python. Inspect the upstream README and `alephgeo --help` before choosing flags; commands can change. Never store credentials or captured datasets in this skill folder.

## Workflow

1. Establish location, area boundary, requested layers, output directory and intended use. Do not infer a project boundary from a place name. Confirm ambiguous geocoding before capture.
2. Prefer OpenStreetMap and open terrain sources for reusable planning material. Upstream warns Google imagery, Street View and 3D mesh downloading violates Google terms. Do not default to these sources or represent downloaded material as cleared for client publication; use authorised alternatives.
3. Run `alephgeo dashboard -o <output-directory>` for user-controlled polygon or rectangle selection. Dashboard defaults to http://127.0.0.1:8100. Use CLI only after checking current command help. Keep captures outside version control.
4. Record source, capture date, bounding area, coordinate reference and units where available, licence/attribution, missing layers and errors. Keep original files; derive analyses separately.
5. Report what was actually downloaded and validated. Imagery and OSM are context evidence, not confirmation of ownership, utilities, capacity, planning permission or survey accuracy. Do not claim Rhino readiness without checking exported formats, coordinates and units.

No API keys are required according to upstream. Undocumented endpoints may fail or be rate limited. Do not repeatedly retry large captures; retain partial results and report the failed source.
