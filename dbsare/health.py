"""Runtime health checks for the Linux foundation."""

import platform
import sys

def report() -> dict:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "architecture": platform.machine(),
    }
