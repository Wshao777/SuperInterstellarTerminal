# This file will contain the Pydantic models for data validation.
# For example: Order, Rider, Customer models.

from pydantic import BaseModel

class HealthCheck(BaseModel):
    status: str = "OK"
