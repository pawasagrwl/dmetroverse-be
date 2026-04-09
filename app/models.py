"""
Shared enums and types used across routers.
"""
from enum import Enum


class Lang(str, Enum):
    en = "en"
    hi = "hi"


class RouteType(str, Enum):
    least_distance = "least-distance"
    minimum_interchange = "minimum-interchange"
