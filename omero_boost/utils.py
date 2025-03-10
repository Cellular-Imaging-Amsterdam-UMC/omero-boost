import json
import os
from django.conf import settings
from omero_adi.utils.ingest_tracker import (
    log_ingestion_step, 
    STAGE_NEW_ORDER, 
)


def get_react_build_file(logical_name):
    """
    Returns the hashed filename for a React build file.
    """
    current_dir = os.path.dirname(__file__)
    manifest_path = os.path.join(
        current_dir, "static/omero_boost/assets/asset-manifest.json"
    )
    manifest_path = os.path.normpath(manifest_path)

    try:
        with open(manifest_path, "r") as manifest_file:
            manifest = json.load(manifest_file)
        path = manifest.get(
            logical_name, logical_name
        )  # Fallback to logical_name if not found
        # Remove first slash
        return path[1:]
    except FileNotFoundError:
        return logical_name


def create_upload_order(order_dict):
    # Log the new order using the original attributes.
    log_ingestion_step(order_dict, STAGE_NEW_ORDER)
