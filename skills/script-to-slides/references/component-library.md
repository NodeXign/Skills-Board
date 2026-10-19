# Reusable PPT component library

## Location and boundaries

Use the user-selected project-local library destination. If none exists, propose `PPT_Component_Library/catalogue.v01.json` relative to the project root; do not assume a particular machine path or skill installation directory. Read the latest catalogue version; preserve previous versions when updating it.

Inspect any existing library first; a newly created library starts empty. Category definitions are not finished assets. Collect useful generic candidates locally when the user requests library maintenance or reusable component extraction. Do not harvest unrelated folders or copy an entire client deck into the general library.

Separate three kinds of reusable material:

1. **Narrative modules**: openings, transitions, problem/evidence/recommendation structures, closing questions. Replace names, dates and project facts with explicit parameters.
2. **Visual components**: covers, section dividers, image/text layouts, process diagrams, comparisons, charts/tables, case-study cards, source/appendix pages. Preserve editable originals, aspect ratio and a preview when feasible.
3. **Source assets**: approved templates, images, icons and data-reference links, with provenance, usage restrictions and freshness. Do not treat historical business content as evergreen.

## Candidate capture and promotion

After a meaningful deck iteration, identify only genuinely reusable additions or improvements. Store candidate files under `candidates/<component-id>/<version>/` when a real asset exists; retain a source link instead of copying where permissions or confidentiality are unclear. Generalise project-specific details before proposing cross-project reuse.

Each record includes:

```json
{
  "id": "layout-comparison-001",
  "version": "1.0",
  "name": "Two-option comparison",
  "kind": "visual-component",
  "category": "comparison",
  "status": "Candidate",
  "purpose": "Compare two alternatives against the same criteria",
  "source": {"path_or_url": "", "slide_page_or_range": "", "source_date": null},
  "files": {"editable": null, "preview": null},
  "aspect_ratio": null,
  "template_version": null,
  "editable": null,
  "parameters": [],
  "reuse_scope": "project-only",
  "rights_or_restrictions": "unverified",
  "fact_refresh_required": true,
  "qa": [],
  "accepted_by": null,
  "accepted_at": null,
  "supersedes": null
}
```

Use stable IDs. The example is a schema illustration, not a catalogue entry. Fields irrelevant to a narrative module may remain null; do not fabricate preview files, source dates or approvals.

Status flow: **Candidate → Reviewed → Accepted**; use Retired for superseded assets without deleting source versions. Reviewed means recorded checks completed. Accepted requires explicit human acceptance. A rendered preview, successful file copy or use in a draft does not establish acceptance or reuse rights.

Before reuse, check purpose, template compatibility, size, editability, permission scope and factual freshness. Project-only candidates may support drafts within that project; cross-project reuse requires appropriate rights and removal of confidential content. Brand changes should create a new version, not silently modify accepted assets.

## Updating the catalogue

Write the next `catalogue.vNN.json` only when real entries or status changes exist; include source, change reason and checks. Preserve previous catalogue and asset versions. Report the small set of new candidates and proposed promotions at delivery instead of forcing approval for every extraction. Do not promote automatically or add fabricated ready-made components merely to populate the library.
