"""
This module contains any common code that can be shared by multiple modules
"""

def enum(**enums):
    return type('Enum', (), enums)

