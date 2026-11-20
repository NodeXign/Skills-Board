# Skills-Board
Reusable AI skills for design, research, and everyday workflows. Practical instructions and templates can adapt to work.

## Available skills

- [planning](skills/planning/SKILL.md): output-driven routing for GIS maps, accessibility, terrain, massing, environmental diagrams and renders. Includes 13 output routes and 19 referenced resources; combines available tools without assuming they are installed. Version 0.1.0. Structural checks completed; runtime workflows remain task-dependent.

- [consultant](skills/consultant/SKILL.md): bilingual executive problem solving with a McKinsey CEO-level strategic lens and Barbara Minto-inspired pyramid communication; includes 30-second key lines, SCQA, MECE, hypothesis testing and innovation under constraints. Version 1.1.0. An independent advisory persona, not an affiliated product.

- [script-to-slides](skills/script-to-slides/SKILL.md): narrative-first presentations with linked slide maps, timed speaker notes and reusable components. Version 0.1.0. Uses your supplied template; no company branding assets are included.

- [site-scan-report](skills/site-scan-report/SKILL.md): evidence-based site screening and modular site-selection reports. Version 0.1.0. Requires an authorised presentation template and research/presentation tools; full runtime testing is pending.

- [datacenter-site-planning](skills/datacenter-site-planning/SKILL.md): data centre site surveys, infrastructure planning requirements, facility checks and evidence-based trade-offs for planners and infrastructure engineers. Includes capacity/space arithmetic, power/cooling/decarbonisation strategy, a project workbook and source digest. Version 2.0.0. Unit calculations and desk scenarios checked; real-project validation pending.

- [aleph-geospatial](skills/aleph-geospatial/SKILL.md): Aleph geospatial capture setup and site-context workflow for OSM buildings, terrain and supported imagery; requires Python 3.11+ and a separate Aleph installation. Data licensing and survey-accuracy limits apply.

- [j7-diagram](skills/j7-diagram/SKILL.md): personal Notion black-and-white illustrations, hairline logic diagrams and editable infographics. Includes a personal visual preset and upstream source manifest. Requires separately installed `diagram-design`, `hairline-create`, `hairline-adopt`, `niyam-notionaly-illustrations` and `niyam-notionaly-infographic` as siblings in your skills directory; load only the components needed for the task. Upstream components are not bundled.

## Install and update

Clone this repository, then copy the selected folder from `skills/` into your tool's skills directory. For Codex on this machine, the selected destination is `~/.codex/skills/`. Keep the entire skill folder together. Check the destination supported by other tools before installing; cross-platform execution is not yet verified.

For updates, pull this repository, review differences, and back up any existing local skill before replacing it. GitHub updates do not automatically update installed copies. See each package's notes for dependencies and changes.
