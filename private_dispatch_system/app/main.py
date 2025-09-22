from typing import List, Dict, Any
from fastapi import FastAPI
from . import models, services

app = FastAPI(title="Private Dispatch System")

# --- System Endpoints ---

@app.get("/", response_model=models.HealthCheck, tags=["System"])
def read_root():
    """Returns the welcome message and system status."""
    return services.get_system_status()

@app.get("/health", response_model=models.HealthCheck, tags=["System"])
def health_check():
    """
    Health check endpoint.
    Returns the system status.
    """
    return services.get_system_status()

# --- Data Endpoints ---

@app.get("/api/v1/orders", response_model=List[Dict[str, Any]], tags=["Data"])
def get_orders():
    """
    Retrieves all order records from the connected Google Sheet.
    """
    return services.get_all_orders_from_sheet()
