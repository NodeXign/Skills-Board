# Planning tool catalogue

Source review: 2026-11-19. Upstream pages were consulted for scope; no third-party runtime was installed or tested as part of authoring this skill. Recheck version-specific APIs, licences and prerequisites before execution. Stars are deliberately omitted: popularity is not a routing criterion or reliability guarantee.

The supplied list's count was inconsistent. Preserve all named resources: 9 AI-oriented entries + 7 core libraries/plugins + Ladybug + one discovery index + Cadmapper = 19. “AI-oriented” does not mean every entry is an MCP server.

## A. AI-oriented candidates (9)

| Resource / primary source | Role | Prerequisites / boundaries |
|---|---|---|
| [Belluxx/Aleph](https://github.com/Belluxx/Aleph) | CLI/dashboard for imagery, terrain, buildings and street-view capture | Upstream advertises no API keys; verify individual source access and reuse terms. Concept screening, not authoritative survey. Not inherently a live MCP |
| [mapbox/mcp-server](https://github.com/mapbox/mcp-server) | Geocoding, POI and route/isochrone services | Requires Mapbox access token; inspect current schema, entitlement and costs. Do not expose tokens in project output |
| [CesiumGS/cesiumjs-skills](https://github.com/CesiumGS/cesiumjs-skills) | Agent guidance for CesiumJS development | Skills are not the engine or a global terrain dataset. Verify CesiumJS, hosting, tiles and access credentials separately; migration history not relied upon |
| [jjsantos01/qgis_mcp](https://github.com/jjsantos01/qgis_mcp) | MCP connection to QGIS Desktop | Verify plugin/server compatibility and live layer inspection. Existing QGIS connector may be a different implementation; use actual exposed schema |
| [muend/geoai-skills](https://github.com/muend/geoai-skills) | Geospatial reasoning and quality guidance | Read relevant current SKILL.md only; not a computational runtime and not a guarantee of correctness |
| [ArchiGenio/archigen-connect](https://github.com/ArchiGenio/archigen-connect) | Bridge to Rhino/Grasshopper, ComfyUI and Revit workflows | Upstream describes public beta, with version-specific target support. Check software licences and configured connection; do not assume production stability |
| [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | Community Blender control, scene/model/render workflow | Blender + compatible add-on/server and live scene check. Material/HDRI access and licences are separate; not an official Blender Foundation plugin |
| [fullydigital-design/ai-architect](https://github.com/fullydigital-design/ai-architect) | ComfyUI workflow generation/validation and MCP operations | Requires running ComfyUI, models/nodes and provider setup. It is a general workflow builder, not proof of architectural accuracy |
| [awesome-genmedia ai-building-visualization](https://github.com/awesome-genmedia/skills/tree/main/categories/architecture/ai-building-visualization) | User-supplied candidate for architectural image guidance | Parent [repository](https://github.com/awesome-genmedia/skills) accessible; exact module content not verified in this review. Do not install or rely on this path until resolved; use available image-generation guidance as fallback |

## B. Libraries, engines and plugins (8 including Ladybug)

| Resource / primary source | Role | Prerequisites / boundaries |
|---|---|---|
| [domlysz/BlenderGIS](https://github.com/domlysz/BlenderGIS) | GIS/geographic data bridge for Blender | Check compatible Blender version and source-service availability; datum, scale and attribution remain necessary |
| [gboeing/osmnx](https://github.com/gboeing/osmnx) | OSM feature retrieval and street-network modelling/analysis | Requires Python environment/data access. Network centrality does not establish a full space-syntax method; specify graph representation and metric |
| [vvoovv/blosm](https://github.com/vvoovv/blosm) | Blender import of buildings, terrain and city context | Feature tiers and source licences vary; do not assume all services/data are free or redistributable |
| [ni1o1/transbigdata](https://github.com/ni1o1/transbigdata) | Transportation spatial-temporal processing and visualisation | Needs appropriately authorised mobility data. Explicit coordinate conventions, time zone and aggregation rules |
| [visgl/deck.gl](https://github.com/visgl/deck.gl) | Custom GPU/web geospatial visualisation | Requires application/data implementation and browser QA. It renders supplied data; it is not itself a GIS analysis engine or data provider |
| [keplergl/kepler.gl](https://github.com/keplergl/kepler.gl) | Interactive geospatial layers, filters and time exploration | Upstream documents AI/MCP through local bridge + open map tab. Check that runtime separately; do not infer connectivity from installing a library |
| [seghier/Grasshopper-ComfyUI-Nodes](https://github.com/seghier/Grasshopper-ComfyUI-Nodes) | Grasshopper-to-ComfyUI workflow integration | Requires compatible Rhino/Grasshopper, running ComfyUI and referenced models/nodes; no guarantee that image geometry matches the source |
| [ladybug-tools/ladybug](https://github.com/ladybug-tools/ladybug) | Core Python weather/EPW analysis, sun-path and climate visualisation | Distinguish core library from Grasshopper and simulation extensions; radiation, shading, energy or CFD claims require the actual corresponding engine and inputs |

## C. Discovery and commercial reference (2)

- [sparkgeo/geo-mcp-servers](https://github.com/sparkgeo/geo-mcp-servers): discovery catalogue, not an executable server. Use only when an unmet capability warrants finding a candidate. Entry count is not pinned.
- [Cadmapper](https://cadmapper.com/): commercial web service for CAD context downloads. Not an open-source GitHub project; respect service terms, extent limits and purchasing authority.

## Status recording

Record runtime status in the project, not this shared catalogue: tool/repository, installed version, configured endpoint (without secrets), read-only connection check, small task check, date, result and fallback. Keep these stages separate. A source page being reachable proves only that the reference could be read.
