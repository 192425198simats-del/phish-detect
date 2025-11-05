"""Pydantic schema definitions for PhishGuard API endpoints."""

from pydantic import BaseModel


class URLRequest(BaseModel):
    """Input payload carrying a URL to classify."""

    url: str


class URLResponse(BaseModel):
    """Model prediction output structure for URL classification."""

    url: str
    prediction_label: int
    score: float
    message: str
