"""
System monitoring utility for the WealthAutomation system.

This module provides functions to monitor CPU and memory usage.
"""

import os
import psutil
from .logger import log_info

class SystemMonitor:
    def __init__(self):
        log_info("SystemMonitor initialized")

    def get_usage(self):
        return {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "memory": {
                "total": psutil.virtual_memory().total,
                "used": psutil.virtual_memory().used,
                "percent": psutil.virtual_memory().percent
            },
            "disk": {
                "total": psutil.disk_usage('/').total,
                "used": psutil.disk_usage('/').used,
                "percent": psutil.disk_usage('/').percent
            }
        }

# Singleton pattern for reuse
system_monitor = SystemMonitor()
