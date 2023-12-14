__all__ = [
    "pytest_sessionfinish",
]

import pytest


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    if exitstatus == 5:
        # Suppress error if no tests found
        session.exitstatus = 0
