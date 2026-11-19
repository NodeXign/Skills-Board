# Output routes

Routes are recommendations conditional on data and runtime availability. Do not download or configure every listed tool. Use the catalogue for source links and limitations.

| Requested output | Inputs | Preferred route and useful combinations | Fallback and acceptance check |
|---|---|---|---|
| Context / POI / satellite reference | Boundary or verified location, extent, date | Authorised source data or Aleph → QGIS; Mapbox for geocoding/POI when configured | Supplied vector/raster sources → GIS. Credit imagery and distinguish observation dates; no parcel inference from a place-name search |
| Figure-ground / street hierarchy / urban morphology | Building footprints, road network, extent | OSMnx extraction/graph analysis → QGIS layout; geoai skills for relevant checks | Existing GeoPackage/OSM extract → QGIS or GeoPandas. Check completeness, projection and area denominator; graph centrality is not automatically space syntax |
| Isochrone / service catchment / accessibility | Origins, travel mode, network, speeds or service API | Mapbox isochrones OR OSMnx weighted routing → QGIS; deck.gl for exploration | Local routable graph with explicit speeds. A circular buffer is only a distance catchment, never label it travel time; test a known route |
| Constraints / suitability / land-use map | Parcel, dated planning/flood/ecology layers, rules | QGIS overlay, buffering and raster calculations + geoai checks | Local GIS libraries with the same methods. Separate statutory exclusions from assumed weights; missing constraint layers mean unknown, not unconstrained |
| OD / heatmap / mobility animation | Authorised trajectories or OD table, time fields | TransBigData cleaning/aggregation → Kepler.gl exploration; deck.gl for custom interaction | Aggregated flow lines and static time slices in GIS. Check totals, time zone, bins and disclosure risk; arcs show flows, not travelled routes |
| Contours / slope / terrain sections | DEM, resolution, CRS/vertical datum, boundary | QGIS terrain analysis → BlenderGIS or site-terrain-blender → Blender | GeoTIFF-derived analytical map/section. Document resolution and vertical exaggeration; never invent a flat DEM |
| Georeferenced context / editable 3D massing | Footprints/heights, DEM, origin, units | BlenderGIS or Blosm import → Blender MCP for scene/render; Aleph where source rights permit | Local mesh generation or Rhino from supplied geometry. Record estimated heights, datum and georeferencing transform |
| Parametric masterplan / option comparison | Boundary, setbacks, land use, height/area assumptions | Rhino/Grasshopper via a verified connector or Archigen → metric checks → Blender render | Scripted editable geometry with explicit inputs. Check site coverage/GFA independently; preserve prior option geometry |
| Regional 3D globe / 3D Tiles viewer | Authorised terrain/tiles and GeoJSON, intended audience | CesiumJS guided by cesiumjs-skills; deck.gl for thematic overlays where integration is verified | Local 3D model or 2D map. Check browser loading, tile access/attribution and coordinate alignment; library alone supplies no global dataset |
| Wind rose / sun path / climate chart | EPW weather file, location, time zone | Ladybug core; Grasshopper ecosystem for spatial context | Explicitly documented weather analysis. Core library alone is not a CFD or whole-building energy engine; verify simulation extensions for shading/radiation claims |
| Architectural / landscape day-night render | Approved geometry, camera, depth/linework, style | Blender MCP geometry render → AI Architect/ComfyUI OR Grasshopper-ComfyUI nodes for controlled styling | Direct Blender render or available image generation using reference geometry. Compare silhouette, openings, access and boundaries; mark AI output indicative |
| Concept / phasing / infrastructure diagram | Confirmed relationships, spatial or conceptual basis | GIS for spatial base + diagram-design/consulting-diagram if installed | Editable SVG or presentation shapes. Explicitly separate a schematic from a scaled plan |
| Planning report / slide set | Verified outputs, sources, decision, duration | Routes above → site-scan-report or script-to-slides if available | Available document/presentation tools. Reconcile legends, site IDs, quantities and notes; preserve source references |

## Combination examples

**Site analysis board:** one boundary and CRS → OSMnx buildings/roads + QGIS constraints → figure-ground/accessibility/constraints sheets. Share the same extent, feature IDs and source register; keep different analytical legends explicit.

**Masterplan and atmosphere:** QGIS boundary/DEM → Rhino massing options → checked area schedule → Blender camera/lighting → optional ComfyUI imagery. Analytical geometry remains the master; an AI image never edits the area schedule.

**Mobility story:** TransBigData cleans and aggregates → Kepler filters and time slices → deck.gl only if custom interaction adds value → static export for the report. Do not rebuild the same viewer in two engines without need.

## Preflight examples for maintainers

1. Missing Mapbox token + supplied road graph: choose local weighted routing, disclose speeds; do not block all work or call buffers isochrones.
2. “Make a night render”: preserve geometry/camera; do not start network/traffic analysis.
3. “Wind comfort”: distinguish an EPW wind rose from a validated pedestrian-wind simulation; request or identify an appropriate solver.
4. “Plan my week”: this skill does not apply.
5. “List all tools”: return catalogue and status, not an installation command for every repository.
6. “Produce parcel compliance with no boundary”: request the boundary; proceed only with labelled regional context.
