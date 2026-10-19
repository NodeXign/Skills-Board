---
name: "site-scan-report"
description: "Run a verified, sourced site scan for one or more candidate land parcels (data centre, industrial, logistics, energy, mixed use) and deliver or extend an English site selection report on the SJ PowerPoint template, built as mergeable per-site modules with numbered sources on every page and speaker notes. Use whenever the user asks to assess, screen, scan, compare or due-diligence a site or parcel, add a new site to an existing site selection deck, update or regenerate the site selection report, or produce site selection / 选址 / 场地筛选 slides, even if they never say the words site scan."
---

# Site Scan Report

## Dependencies and portability

This package contains instructions only. The SJ template and sj-ppt-template skill are external dependencies and are not distributed here. Use SJ branding only with permission; if unavailable, ask for an authorised template and record the substitution. Research access, geospatial processing, PowerPoint authoring and rendering must be supplied by the host tool. Codex and Claude Code runtime execution has not yet been tested. Paths below are relative to the user-selected project. Sample records are placeholders, not project facts.

Produce a decision grade scan of one or more candidate sites and deliver it as one English PowerPoint report on the SJ template. Every site becomes a self-contained module built from a structured site record, so a later run can scan a new site and merge it into the same report without rebuilding what already exists. Every page carries numbered sources, every figure carries a status tag, and every slide carries speaker notes.

The value of this skill is verification discipline and repeatability, not breadth. A fluent report full of unsourced numbers is worse than a short one that separates what is known from what is assumed, because the unsourced version gets quoted back by the client months later.

## Operating rules

1. **English is the deliverable language.** Slides, tables, map labels, source strips and speaker notes are written in English. If the briefing audience needs a second language, add it as a twin page after each content page (same figures, same reference numbers) or as a second notes block. Never mix two languages inside one text frame or one page.
2. **The SJ template governs the look.** Follow the `sj-ppt-template` skill for canvas, colours, fonts, logo, footer and type sizes. Source precedence: the official `sj_template.potx` if available in the working context; otherwise the most recent SJ-branded site selection deck already in the project (open it, drop its slides, add new slides on its content layout so master, logo and theme are inherited); otherwise rebuild the fixed elements from the spec. Never restyle the master.
3. **One site, one record, one module.** All content for a site lives in a site record (section 2). Pages are generated from the record, never typed directly into slides. This is what makes merging possible.
4. **The project is the memory.** Save the register, the site records, the build script and the map script to the project (section 6) at the end of every run. Do not assume temporary session storage persists; save durable outputs to the chosen project folder.
5. **Facts and judgement stay on separate pages.** Comparison tables carry facts with sources; the scorecard and recommendation carry judgement and say so.

## Phase 0. Fix what is actually being assessed

Do this before any research. Getting it wrong wastes the entire scan, and it has gone wrong before: a candidate site was mapped on the wrong side of the island for two revisions because its coordinate was inferred rather than supplied.

1. Establish the exact identity of each site. A name is not an identity; estates share brands across separate parcels.
2. Obtain, in this order of preference: a boundary file (KMZ, KML, shapefile), a title document with area and parcel number, a client-supplied coordinate. Record which one you have in the site record under `identity.coordinate_source`. If only a coordinate exists, say so on every page that depends on it and treat areas, setbacks and buffers as provisional.
3. Check every coordinate against a land polygon before drawing anything (for example, inspect an appropriate geoBoundaries coastline dataset and verify its resolution and access in the current environment). A point in the sea is a transcription error until proven otherwise.
4. Recompute the area from the boundary file in a projected CRS and compare it with the registered area. State both.
5. Restate the sites, their IDs, coordinates and areas back to the user and ask for confirmation before building. Name any mismatch between the sources supplied. Existing sites keep their letters; a new site takes the next free letter.
6. Confirm the intended use and the capacity phases, because they set the thresholds (plot ratio, redundant feeds, tenure longer than asset life, water at full build-out).

## Phase 1. The ten dimensions

Scan these in order. The first four decide feasibility, the next three decide cost and programme, the last three decide risk and commercial terms.

1. **Land tenure and control.** Title type and number, holder, issue and expiry dates, extension mechanism, underlying right, controlling authority, registered conditions, transfer route and fee, change-of-use route. Normalise price by remaining tenure year, never by area alone.
2. **Planning parameters.** Spatial plan status, zone code, conformity route, plot ratio, coverage, height, setbacks, permitted use, uplift or change-of-use procedure and duration.
3. **Power.** Nearest substation and voltage, firm capacity available to the site as distinct from installed, independent feeders, energisation date, contracted competing loads in the same corridor, projected allocation, system supply and peak, self generation rules, gas, green power route, tariff class.
4. **Water, cooling and discharge.** Local plant capacity, firm allocation, source and connection, island or regional balance, policy on developer-funded desalination, wastewater coverage, demand at each capacity phase for at least two cooling assumptions (state the WUE used).
5. **Connectivity.** Cable landing stations with coordinates and distance, carriers, cable systems and ready-for-service dates, latency to the hub market, physically diverse routes. Two routes in one corridor are one route.
6. **Site physical conditions.** Boundary and CRS, corner coordinates, topography and grading state, water bodies, existing structures, vegetation, flood exposure, geotechnical knowns.
7. **Infrastructure delivery interface.** Where each utility reaches the boundary, who delivers it, by when, road reserve width, abnormal load access.
8. **Permits and programme.** Environmental approval route and duration, each gating approval in sequence, earliest construction start, the programme condition that would switch to the fallback site.
9. **Aviation, defence and security.** Height surfaces and the limit in metres at the site, military installations, radar, construction crane limits.
10. **Surroundings and commercial terms.** Adjacent uses by compass direction, hazard sources and required buffers, distances to ports, airports, city and the other candidate sites, land price bands from official schedules, offered price, acquisition taxes and fees, incentives.

## Phase 2. The site record

Write one record per site before any slide exists. Store it in the project as `site-scan/sites/<ID>_<slug>.json`. Every value carries a source, a date and a status tag.

```json
{"id":"A","slug":"candidate-a","name":"Candidate A","role":"candidate",
 "identity":{"centroid_lonlat":null,"boundary_file":null,
   "area_ha_registered":null,"area_ha_computed":null,"crs":null,"coordinate_source":"TBC"},
 "dimensions":{"tenure":{"value":null,"source":null,"date":null,"status":"TBC"},
   "power":{"value":null,"source":null,"date":null,"status":"TBC"}},
 "distances_km":{},"corrections":[],
 "open_items":[{"item":"Confirm parcel boundary","owner":"TBC","route":"request boundary file","when":"TBC"}],
 "assets":{"photos":[],"scans":[],"maps":[]}}
```

Status vocabulary, used verbatim on slides: `verified` (issuing agency, utility, title document), `operator` (estate, carrier, developer statement), `press` (named outlet and date), `calculated` (your own computation, method stated), `indicative` (position or figure approximated, precision stated), `unverified`, `TBC` (not provided by the counterparty).

Distances are computed once from the site centroid to a point-of-interest list, written to `distances_km`, and read from there by every page and map. Never type a distance into a slide by hand; a cluster and its cable landing station have different coordinates and will otherwise be given the same distance.

## Phase 3. Verification discipline

This is the part that must not be skipped.

- Search for every current-state figure rather than recalling it. Grid capacity, tariffs, land fee schedules, cable dates and office holders all go stale.
- Prefer sources in this order: issuing agency, utility or operator, national news agency, market aggregator, estate brochure. Brochures are claims, not facts, until dated.
- Record the publisher and date of every source and carry both onto the slide's source strip.
- Run an internal consistency check: recompute distances from coordinates, recompute areas from boundaries, reconcile capacity against peak and reserve, reconcile a renewable claim against its footprint. Discrepancies inside one document are the fastest way to find which half is wrong.
- Keep a corrections register in the record and present it plainly on the open items page. The client usually needs to know that their own document is wrong.
- Mark derived content as yours. Programme quarters, risk ratings, scorecards and USD conversions are SJ analysis and are labelled as such on the page and in the sources strip.

## Phase 4. Visuals

Every substantive page carries a visual sized to fill its box, beside the text it supports.

**Maps.** Check whether licensed tile and satellite services are available in the current environment. If unavailable, draw maps in matplotlib from real coastline data (geoBoundaries gbOpen ADM2 for the country, ADM0 for neighbouring states, via `media.githubusercontent.com`; Natural Earth via `raw.githubusercontent.com`). Fixed style: sea `#D6E4F5`, land `#F3F4F0`, site polygon Impact Red at 50% fill, Impact Blue for points, numbered circular tags on every point of interest, scale bar, north arrow, facility positions marked `indicative` when not taken from a published coordinate. Generate each map at the exact aspect ratio of its slide box (axes fill the figure, limits expanded to the box ratio) so it inserts without gaps or cropping. The standard set per site: regional (all candidates, distances), vicinity (2 and 5 km rings), power corridor, water, connectivity to the hub market, parcel plan with corner labels and segment lengths, and a height-envelope diagram where an airport surface applies. The tag numbers on a map are repeated in the page text so the reader can match them.

**Photographs.** Use the client's own survey photographs. Cover-crop into the box; never letterbox. Produce an annotated bird's-eye image with compass-direction labels for the surroundings page, and crops for each direction. Official satellite imagery belongs to its publisher; if the client supplies screenshots, georeference them against the coastline, overlay the boundary, and credit the source on the strip.

**Charts.** Native PowerPoint charts (python-pptx), Impact Blue primary series, grey comparison, blue tints for further series, data labels on, no legend for a single series. Typical: demand at full build-out under two WUE assumptions against the local plant; land price bands as a floating bar.

**Diagrams.** Native shapes: chevron sequences for approvals and programme, traffic-light scorecard, three-card verdict. Where a spatial question is live, also build a Leaflet overlay tool (range rings, bearing spokes, measure, GeoJSON export, slot for the authority's own WMS endpoint) and deliver it as a downloadable file.

## Phase 5. The deck

### Page grammar (every content page)

Header: title in Impact Blue, one-line subtitle in grey, one bold summary line that states the conclusion and carries reference markers. Body: solid-fill blocks only, no left accent bars and no outlined cards; KPI tiles in navy with white value, panels in light grey `#F1F4F9`, callouts in Impact Blue with white text, tables with a navy header row and alternating rows. Bottom: a `Sources` strip listing `[1] publisher, document, date` for every marker used on the page (two columns when more than three), then the SJ footer and page number. Empty table cells are written as a non-breaking space, otherwise LibreOffice renders them at 18 pt. Reference markers `[n]` appear in the body text next to the figure they support and are numbered per page.

Type: follow the `sj-ppt-template` targets and never go below the official minimums (body 14 pt, captions, tables and strips 10 pt, footer 8 pt). When a page does not fit at the floor, split it into a facts page and an evidence page rather than shrinking type. Sentence case throughout. Fonts Aptos (Söhne where installed).

Speaker notes on every slide, in English, with three labelled parts: key points to brief, the conclusion that matters for site selection, and what still needs verifying. The notes are what the presenter reads; the page is what the client reads.

### Deck skeleton

| Position | Page | SJ layout |
|---|---|---|
| 1 | Cover: project, report title, revision, sites in scope | 1 or 2 |
| 2 | Contents with section numbers | 3 |
| 3 | Executive summary: recommendation callout, one card per site, programme condition | content |
| 4 | Criteria and method: the ten dimensions, evidence hierarchy, candidate list | content |
| 5 | Candidate sites overview: regional map and thumbnails | content |
| 6+ | One section divider and one module per site, in ID order | 4 then content |
| after modules | Summary at a glance: one column per site, facts only, status colours for TBC | 8 |
| | Qualitative scorecard: traffic lights on the five screening groups, labelled unweighted | content |
| | Recommendation: anchor site card, alternate site card, deprioritised sites with reasons, programme condition | content |
| | Open items and next steps: item, owner, route, when, reference | 8 |
| | Sources and data notes appendix: official, operator, press, calculated, indicative, unverified | content |
| last | Closing | 19 |

### Site module

Full module, for the anchor and alternate sites: parcel overview (vicinity map, facts table, status tile list, SWOT); land title and legal basis (KPI tiles, title scans, certificate chain, steps before permit); existing site condition (survey photographs, parcel plan, corner coordinates, observations); surroundings and neighbouring land use (annotated bird's-eye, direction crops); location and key distances (regional map, distance table with relevance); power; water; connectivity; planning and regulatory (instrument table, height envelope, approval sequence); land cost and tenure (KPI tiles, cost elements, negotiation frame, price band chart); programme (phase chevrons, programme condition); risk register (rating, mitigation, reference).

Snapshot module, for sites screened out early: one overview page (image, dimension table, read-across callout) and, where the site is being deprioritised, one page listing the enabling works it would need and the reasons for the decision.

## Phase 6. Merge, version and save

The report is cumulative. A run scans one or more sites and merges them into the existing report rather than starting a new one.

1. Read `site-scan/register.md` from the project. It lists every site with ID, slug, role, module type, record path, and the revision log. If it does not exist, create it on the first run.
2. Add the new site record. Keep existing IDs and records untouched unless the user supplies a correction, in which case update the record, add a line to its `corrections`, and note it in the revision log.
3. Regenerate the whole deck from all records with the build script. Per-site modules are deterministic from their records, so unchanged sites render identically; the comparison table, scorecard, recommendation, open items and sources appendix are rebuilt from all records so a new column or row appears everywhere it should.
4. Recompute distances between all candidate sites from their centroids and refresh the regional map.
5. Name the file `<Project>_Site_Selection_Report_rev_<MonYYYY>_EN.pptx`, bump the revision on the cover, and add a revision line to the register (date, sites added or changed, pages affected).
6. Save to the project: the register, the site records, `site-scan/build.py` and `site-scan/maps.py`. If the project includes an authorised existing implementation, inspect and reuse its compatible helpers. Otherwise create the build and map scripts in the project; no private reference implementation is bundled with this skill.

## Phase 7. QA and delivery

- Use an available presentation validator after checking its documented interface. If no validator is available, record that limitation and inspect structure, template use, rendering and notes. Fix issues in the generator, not the packed XML.
- Render to PDF and look at every page as an image: no overflow, no gaps beside images, no empty frames, strips and footers not colliding, every `[n]` in the body present in that page's strip.
- Confirm every slide has notes, no placeholder text remains, the page count matches the register, and the cover revision matches the register.
- Deliver the `.pptx` and a PDF export, then write the project files in Phase 6.

## Phase 8. Close the loop

End by telling the user, in plain terms, which sites you could not confirm, which supplied figures disagreed with each other and what you did about them, which content is SJ analysis rather than evidence, and the single next action that would resolve the most uncertainty. Usually that action is a confirmation from the counterparty or a spatial overlay against the authority's own layers rather than more desktop research.