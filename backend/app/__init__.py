"""Top‑level package for the backend application.

This package exposes a factory function to create the FastAPI app and organises
submodules such as API routes, models, services, agents and rules.
"""

from .main import create_app  # noqa: F401