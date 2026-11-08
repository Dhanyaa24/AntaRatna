Antaratna --- AI-Driven Archaeological Discovery
Antaratna is a prototype for non-invasive archaeological intelligence.
It combines satellite imagery, terrain/elevation context, and anomaly
scoring to highlight areas around Hampi, Karnataka that may warrant
archaeological investigation---before any excavation takes place.
Important: Antaratna identifies potential anomaly zones. It does
not confirm the presence of buried archaeological structures. All
candidate areas require expert review and field validation.

Project Overview
The prototype focuses on the Discover stage of a three-stage
concept:
1. Discover (prototype): Visualizes potential anomaly zones using a
   map, heat layer, category filters, and zone-level explanations.
2. Reconstruct (planned): Intended to create confidence-labelled,
   AI-assisted visual reconstructions from available imagery and
   historical references.
3. Fragments (planned): Intended to use computer vision to propose
   matches between damaged artifact fragments for conservator review.
Demonstration Area and Prototype Metrics
The supplied prototype is configured for an Area of Interest (AOI)
around Hampi, Karnataka.

  Item                                                       Value shown in prototype
  AOI centre                                                     15.335° N, 76.462° E
Detection zones displayed                                                       168
Candidate zones                                                                 155
Zones near known sites                                                           13
Known monuments correctly flagged in the demonstration                          6/6
Satellite source identified in UI                                    Sentinel-2 L2A
Elevation source identified in UI                             Copernicus DEM GLO-30
Sentinel-2 ground resolution stated in UI                                      10 m

These are prototype/demo figures shown by the application, not
independently verified archaeological discoveries or a field-validation
accuracy claim.
Features
- Interactive satellite map centred on the Hampi AOI.
- Heat layer showing the spatial distribution of potential scores.
- Individual anomaly-zone markers sized and coloured by category and
  score.
- Filters for all zones, candidate zones, and
  validated/near-known-site zones.
- Zone list showing zone ID, category, and potential score.
- Detail panel with coordinates, proximity to known monuments, and a
  potential score.
- Explanatory terrain-style visualization with selectable layers:
  - Detection boundary
  - Vegetation anomaly
  - Soil anomaly
  - ML cross-check
- Responsive page layout and navigation between the project stages.
Technology
The supplied frontend uses:
- HTML5 for page structure
- CSS3 for layout and visual styling
- JavaScript for application interactions
- Leaflet for interactive mapping
- Leaflet.heat / simpleheat for the heatmap layer
- Esri World Imagery as the map tile layer
- Google Fonts --- Fraunces, IBM Plex Sans, and IBM Plex Mono
The Discover page reads zone records from an embedded JSON data block in
discover.html. The supplied files do not include a separate backend,
API service, model-training pipeline, or raw Sentinel-2 / DEM processing
scripts. The interface presents the outputs and explanatory signals for
the prototype.
Repository Structure
.
├── index.html          # Landing page and project overview
├── discover.html       # Interactive Hampi anomaly map and zone explorer
├── reconstruct.html    # Planned reconstruction stage (placeholder page)
└── fragments.html      # Planned artifact-fragment matching stage (placeholder page)
Run Locally
This is a static website. No package installation or build step is
required.
Option 1: Open directly
1. Download or clone the repository.
2. Open index.html in a modern browser.
3. Use the navigation to open Discover.
Option 2: Run a local HTTP server
If Python is installed, open a terminal in the project folder and run:
python -m http.server 8000
Then visit:
http://localhost:8000
Using a local server is recommended for consistent browser behaviour.
Using the Discover Map
1. Open Discover from the navigation.
2. Use the category filters to switch between all zones, candidates,
   and zones near known monuments.
3. Select a marker on the map or a zone in the list.
4. Review the zone ID, coordinates, category, distance to a known
   monument (where applicable), and potential score.
5. Select the terrain visualization labels to inspect the boundary,
   vegetation, soil, and ML cross-check explanations.
6. Drag the terrain visualization to rotate it.
Understanding the Zone Categories
- Candidate: A potential anomaly with no known monument within the
  configured nearby-distance check. It is a candidate for further
  investigation, not a confirmed archaeological site.
- Validated / near known site: An anomaly located near a
  documented monument. This acts as a demonstration sanity check that
  the method can respond around known structures; it does not
  independently validate every nearby anomaly.
The potential score is a ranking signal in the prototype. It should not
be interpreted as a probability that archaeological remains are present
unless it has been calibrated and validated for that purpose.
Limitations and Responsible Use
- The current repository is a frontend prototype with embedded
  demonstration data.
- The included files do not contain the complete geospatial
  preprocessing or model-training workflow.
- Reconstruct and Fragments are concept pages marked as in
  development.
- Map tiles are loaded from Esri services and require an internet
  connection.
- The displayed anomaly scores and counts should be treated as
  prototype outputs.
- Archaeological interpretation requires domain-expert review, ground
  truth, and appropriate permissions.
- The system is intended to support non-invasive research and
  prioritization, not replace archaeologists or authorize excavation.
Future Work
- Connect a reproducible satellite and elevation-data preprocessing
  pipeline.
- Document feature engineering and anomaly-scoring methodology.
- Add model evaluation against independently verified archaeological
  and non-archaeological locations.
- Provide provenance for every input layer and generated score.
- Implement expert feedback and field-validation workflows.
- Develop the planned reconstruction and artifact-fragment matching
  stages.
Credits and Data Sources
- Sentinel-2 L2A --- satellite source identified by the prototype UI.
- Copernicus DEM GLO-30 --- elevation source identified by the
  prototype UI.
- Esri World Imagery --- basemap tiles used by the interactive map.
- Leaflet --- interactive map library.
- Leaflet.heat / simpleheat --- heatmap visualization.
Please consult the respective providers' terms and attribution
requirements when deploying or redistributing the project.
License
No license file was included in the supplied project files. Add a
LICENSE file before granting reuse or redistribution rights.
