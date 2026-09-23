"""
Run this on YOUR OWN machine (not in this chat) -- Microsoft Planetary
Computer is public, no account/captcha needed, but this sandbox's network
can't reach it directly.

Setup (one time):
    pip install pystac-client planetary-computer rasterio rioxarray odc-stac numpy

Then just run:
    python download_hampi_data.py

It will:
  1. Search Sentinel-2 L2A for a recent low-cloud scene over Hampi
  2. Clip Red (B04), NIR (B08), SWIR (B11) to a ~5km box around Hampi
  3. Pull the matching Copernicus DEM GLO-30 tile for the same box
  4. Save red.tif, nir.tif, swir.tif, dem.tif -- upload these 4 files back
     to the chat and they drop straight into pipeline.py, no changes needed.
"""
import pystac_client
import planetary_computer
import rioxarray
import numpy as np
from odc.stac import stac_load

# --- Area of interest: ~5km box around Hampi, Karnataka ---
LAT, LON = 15.335, 76.462   # Hampi center (adjust if you want a different zone)
DELTA = 0.023               # ~2.5km each direction -> ~5km box
BBOX = [LON - DELTA, LAT - DELTA, LON + DELTA, LAT + DELTA]  # [minlon,minlat,maxlon,maxlat]

catalog = pystac_client.Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1",
    modifier=planetary_computer.sign_inplace,
)

print("Searching Sentinel-2 L2A over Hampi...")
search = catalog.search(
    collections=["sentinel-2-l2a"],
    bbox=BBOX,
    datetime="2025-01-01/2026-09-01",
    query={"eo:cloud_cover": {"lt": 10}},
    sortby=[{"field": "properties.eo:cloud_cover", "direction": "asc"}],
    max_items=5,
)
items = list(search.items())
if not items:
    raise SystemExit("No low-cloud Sentinel-2 scenes found -- widen the date range or cloud threshold.")

item = items[0]
print(f"Using scene: {item.id} (cloud cover {item.properties.get('eo:cloud_cover')}%, date {item.datetime})")

ds = stac_load(
    [item],
    bands=["B04", "B08", "B11"],
    bbox=BBOX,
    resolution=0.00009,  # ~10m in degrees (EPSG:4326 resolution must be in
                         # CRS units, not meters -- this was the bug)
    crs="EPSG:4326",
)

red = ds["B04"].isel(time=0).astype("float32") / 10000.0   # scale to reflectance 0-1
nir = ds["B08"].isel(time=0).astype("float32") / 10000.0
swir = ds["B11"].isel(time=0).astype("float32") / 10000.0

red.rio.write_crs("EPSG:4326", inplace=True)
nir.rio.write_crs("EPSG:4326", inplace=True)
swir.rio.write_crs("EPSG:4326", inplace=True)

print(f"Band shape: {red.shape} (should be roughly 500x500, not 1x1 -- if it's tiny, the resolution/CRS units are off again)")

red.rio.to_raster("red.tif")
nir.rio.to_raster("nir.tif")
swir.rio.to_raster("swir.tif")
print("Saved red.tif, nir.tif, swir.tif")

# --- DEM: Copernicus DEM GLO-30 (also public on Planetary Computer) ---
print("Searching Copernicus DEM GLO-30...")
dem_search = catalog.search(collections=["cop-dem-glo-30"], bbox=BBOX)
dem_items = list(dem_search.items())
if not dem_items:
    raise SystemExit("No DEM tile found for this bbox.")

dem_ds = stac_load(dem_items, bands=["data"], bbox=BBOX, resolution=0.00027, crs="EPSG:4326")
dem = dem_ds["data"].isel(time=0).astype("float32")
dem.rio.write_crs("EPSG:4326", inplace=True)
dem.rio.to_raster("dem.tif")
print("Saved dem.tif")

print("\nDone. Upload red.tif, nir.tif, swir.tif, dem.tif back to the chat.")
