from typing import *
import collections

class Solution:
    def Strongest_Extension(self, class_name: str, extensions: List[str]) -> str:
        def calculate_strength(extension: str) -> float:
            uppercase_count = sum(1 for char in extension if char.isupper())
            lowercase_count = sum(1 for char in extension if char.islower())
            return uppercase_count - lowercase_count

        max_strength = float('-inf')
        strongest_extension = None

        for extension in extensions:
            strength = calculate_strength(extension)
            if strength > max_strength:
                max_strength = strength
                strongest_extension = extension

        return f"{class_name}.{strongest_extension}"