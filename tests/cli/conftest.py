import pytest
from brickflow.cli.projects import MultiProjectManager


@pytest.fixture(autouse=True)
def reset_multi_project_manager_singleton():
    """Reset the MultiProjectManager singleton before each test."""
    # Clear the singleton instance if it exists
    if hasattr(MultiProjectManager, "instance"):
        delattr(MultiProjectManager, "instance")
    yield
    # Optionally clean up after test
    if hasattr(MultiProjectManager, "instance"):
        delattr(MultiProjectManager, "instance")
