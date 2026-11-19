---
name: planning
description: Route urban, regional, master-planning and site-planning requests to suitable GIS analysis, maps, terrain models, parametric design and visualisation tools. Use for planning projects needing figure-ground maps, accessibility, constraints, OD flows, terrain, massing, environmental diagrams or architectural renders, including combinations. Excludes daily task planning and scheduling.
---

# Planning

Select tools from the requested planning question and deliverable, not repository popularity. Combine analysis, modelling and presentation tools when each adds a necessary capability. This skill is a routing workflow, not an installation of its catalogue or evidence that a connector is live.

## Start with the project

Read the selected project's AGENTS.md, PROJECT_CONTEXT.md, REQUIREMENTS.md, decision log and next actions when present. Reuse confirmed inputs. Resolve only material gaps: site/boundary, study extent, required figure, decision it supports, output format, scale, available data and deadline. Do not confuse a place name with a verified parcel. If boundaries are missing, produce explicitly indicative regional context, not parcel-specific conclusions.

For a simple map, proceed directly. For a multi-output commission, state a short chain of inputs → computation → drawings/models → checks. Ask for missing critical inputs while continuing independent work. Preserve originals; save versioned derivatives in the selected project. This skill contains methods, not client data or machine-specific paths.

## Choose and run the route

1. Read [output-routes.md](references/output-routes.md) and select the row matching each requested output. Multiple rows may share a single data preparation stage. Prefer existing working tools and the smallest sufficient chain.
2. Consult only the relevant entries in [tool-catalogue.md](references/tool-catalogue.md). The catalogue includes all 19 named resources: 9 AI-oriented candidates, 7 core libraries/plugins, Ladybug, a discovery index and a commercial service. A reference URL is not a callable tool.
3. Inspect available tool schemas, installed packages and relevant local skills. Record capability state as candidate / installed / configured / reachable / task-tested. For desktop MCPs use a read-only scene/layer/document inspection before editing. Do not confuse a similarly named installed connector with the catalogue's implementation.
4. If usable, execute the route. If unavailable, use the route's equivalent fallback and disclose differences. Do not fabricate tool calls or deliver a plan instead of an achievable output. An unavailable imagery service does not prevent vector analysis. Stop retrying an unchanged failure after a bounded diagnostic attempt.
5. Do not install the entire catalogue, add credentials, enable paid services or upload private datasets merely because a route mentions them. If required setup is outside the request, explain the specific dependency and request the needed action; continue feasible local work.
6. Read any selected companion skill before using it. If installed, aleph-geospatial supports authorised Aleph capture; datacenter-site-planning supports data-centre site requirements; site-context-encyclopedia supports background research; site-terrain-blender supports terrain production; site-scan-report supports evidence-based site comparisons; dc-planning supports data-centre planning; diagram-design/consulting-diagram support conceptual diagrams; script-to-slides or sj-script-to-slides supports the requested presentation. These are optional: use available equivalent tools otherwise. Never add company branding by default.

## Data and interchange contract

Keep one shared data basis across outputs: source/date/licence, site boundary version, horizontal CRS, vertical datum, units, study extent and transformations. Use an appropriate projected CRS for distances and areas; exchange web GeoJSON as longitude/latitude WGS84. Avoid assigning a CRS to coordinates that actually require transformation. Check raster resolution, alignment and nodata. Record any China-specific coordinate conversion explicitly; do not blindly offset data.

Prefer GeoPackage for analysis layers, GeoTIFF for DEM, and GeoJSON/CSV for web exchange. For Blender/Rhino record model units, local origin, axis orientation and the transform back to world coordinates. Use suitable editable native files plus GLB/glTF or another supported exchange format. Preserve stable feature IDs across maps, models and schedules. Confirm actual importer/exporter support before promising a format.

Keep analytical results distinct from illustrative images. OSM is dated screening data, not cadastral evidence or confirmed utility capacity. Heights inferred from levels are assumptions. Generated renders cannot establish parcel geometry, setbacks, shadow compliance or engineering performance. Do not infer legal reuse rights from API-free access or a repository's code licence.

## Review and deliver

Check numerical basis, geometry and appearance separately. Recompute a representative area/distance; inspect extent, joins, missing attributes, legend units and classification. For networks verify travel mode, connectivity and travel-time assumptions. For 3D verify unit scale, origin, terrain datum, water/land relationship and camera framing. For environmental outputs state weather file, time zone, date and simulation method.

Render/open the actual output and inspect labels, clipping, layers and source credits. For interactive deliverables exercise a relevant filter/layer/time control, not just source syntax. If an inspection is unavailable, state it. A successful install, exported file or hash is not end-to-end validation.

Deliver the requested figures and editable source where feasible, with concise sources/assumptions, tool route, checks performed and unresolved inputs. Save a small project-local run record containing selected routes, tool versions/status, inputs/CRS, transformations, output paths and validation results. Do not publish project data or mark a professional decision approved without explicit authority.

## Invocation examples

- “用 planning 做场地周边 2 km 图底图，再加 15 分钟步行等时圈。”
- “用 planning 把 DEM 和建筑轮廓做成可编辑地形体块，输出鸟瞰图。”
- “用 planning 分析 OD 数据，做流向图和可筛选的时间动画。”
- “用 planning 比较三个总图方案：指标表、约束图和概念效果图分别生成。”
