"""FastAPI application scaffolding for PhishGuard."""

from fastapi import FastAPI

from .schemas import URLRequest, URLResponse


app = FastAPI(title="PhishGuard API", version="0.1.0")


@app.get("/health", response_model=dict)
def health_check() -> dict:
	"""Health probe endpoint to verify service availability."""
	# TODO: Enhance with dependency checks (model load status, external services).
	return {"status": "ok"}


@app.post("/predict", response_model=URLResponse)
def predict_url(payload: URLRequest) -> URLResponse:
	"""Return a placeholder phishing prediction for the provided URL."""
	# TODO: Replace with actual feature extraction and model inference pipeline.
	return URLResponse(
		url=payload.url,
		prediction_label="unknown",
		score=0.0,
		message="Placeholder response; implement model-backed prediction.",
	)
