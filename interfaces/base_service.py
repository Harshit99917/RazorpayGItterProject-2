"""
BaseServiceInterface.py
-----------------------
Purpose: Abstract base for all services.

Design Pattern:
- Interface (Abstract Base Class)

SOLID Principles:
- ISP: Forces minimal method structure.
"""

from abc import ABC, abstractmethod

class BaseServiceInterface(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
