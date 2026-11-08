
# Antaratna – AI-Driven Archaeological Discovery

## Overview

Antaratna is an AI-driven archaeological discovery platform that uses satellite imagery, terrain analysis, and anomaly detection to identify potential buried archaeological sites without excavation.

The project focuses on Hampi, Karnataka, and aims to help archaeologists identify areas that may require further investigation using non-invasive technologies.

## Problem Statement

Traditional archaeological exploration is time-consuming, expensive, and often requires extensive field surveys and excavation.

Antaratna addresses this challenge by combining geospatial data and AI-assisted analysis to identify potential archaeological anomalies and prioritize areas for investigation.

## Key Features

### 1. Discover
- Interactive satellite map of the Hampi region.
- Visualization of potential archaeological anomaly zones.
- Heatmap displaying areas with higher anomaly scores.
- Zone-wise potential scores and coordinates.
- Filtering of candidate zones and zones near known monuments.
- Vegetation, soil, and terrain anomaly visualization.

### 2. Reconstruct (Planned)
- AI-assisted reconstruction of potential archaeological structures.
- Visualization using historical references and available imagery.
- Confidence-based reconstruction outputs.

### 3. Fragments (Planned)
- Computer vision-based artifact fragment analysis.
- Identification of potentially matching fragments.
- AI-assisted matching suggestions for expert review.

## Demonstration – Hampi

The current prototype demonstrates archaeological anomaly visualization around Hampi, Karnataka.

| Metric | Value |
|---|---:|
| Detection zones displayed | 168 |
| Candidate zones | 155 |
| Zones near known sites | 13 |
| Known monuments flagged in demo | 6/6 |

**Area of Interest:** Hampi, Karnataka, India

**Coordinates:** 15.335° N, 76.462° E

These figures represent prototype demonstration outputs and should not be interpreted as independently verified archaeological discoveries.

## Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Mapping and Visualization
- Leaflet.js
- Leaflet.heat
- Esri World Imagery

### Geospatial Data Sources
- Sentinel-2 L2A
- Copernicus DEM GLO-30

### Design
- Fraunces
- IBM Plex Sans
- IBM Plex Mono

## System Workflow

1. Select the geographical Area of Interest.
2. Obtain satellite imagery and elevation data.
3. Analyze vegetation, soil, and terrain patterns.
4. Identify potential anomalies.
5. Generate anomaly scores and candidate zones.
6. Visualize the results through an interactive map.
7. Prioritize potential locations for expert investigation.

## Repository Structure

```text
Antaratna/
│
├── index.html
├── discover.html
├── reconstruct.html
├── fragments.html
└── README.md
```

## Getting Started

### Prerequisites

- Modern web browser
- Python (optional, for local server)
- Internet connection for map tiles

### Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Navigate into the project:

```bash
cd Antaratna
```

### Run Locally

Run a local Python server:

```bash
python -m http.server 8000
```

Open the following URL:

```text
http://localhost:8000
```

Alternatively, open `index.html` directly in your browser.

## Understanding Anomaly Zones

The application displays potential anomaly zones based on the prototype's scoring and visualization system.

- **Candidate Zones:** Potential anomalies that may require further investigation.
- **Zones Near Known Sites:** Anomalies located near documented archaeological monuments.
- **Potential Score:** A ranking signal used to prioritize zones for review.

These scores do not independently confirm the existence of buried structures.

## Future Enhancements

- Integration of automated satellite imagery preprocessing.
- Advanced vegetation and soil anomaly detection.
- LiDAR-based terrain analysis.
- Multimodal geospatial data fusion.
- Improved anomaly classification models.
- Archaeologist feedback and field-validation workflows.
- AI-assisted 3D reconstruction.
- Artifact fragment matching using computer vision.

## Limitations

- The current repository contains a frontend demonstration with embedded zone data.
- The complete satellite preprocessing and model-training pipeline is not included.
- Reconstruction and fragment matching are planned modules.
- Anomaly predictions require expert interpretation and field validation.

## Responsible Use

Antaratna is designed as a decision-support tool for non-invasive archaeological research.

It does not replace archaeological expertise, confirm discoveries, or authorize excavation. All potential findings require appropriate validation and permissions.

## Data Sources and Credits

- Sentinel-2 L2A
- Copernicus DEM GLO-30
- Esri World Imagery
- Leaflet.js
- Leaflet.heat

Please follow the respective data providers' attribution and usage requirements.

## License

No license has currently been specified. A license should be added before permitting reuse or redistribution.
