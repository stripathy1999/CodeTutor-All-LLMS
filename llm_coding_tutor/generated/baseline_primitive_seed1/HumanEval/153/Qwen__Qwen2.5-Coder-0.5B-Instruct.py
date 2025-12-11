from typing import *
from collections import *

class Solution:
    def Strongest_Extension(self, class_name: str, extensions: List[str]) -> str:
        max_strength = float('-inf')
        strongest_extension = None
        
        for extension in extensions:
            strength = sum(1 for char in extension if char.isupper()) - sum(1 for char in extension if char.islower())
            if strength > max_strength:
                max_strength = strength
                strongest_extension = extension
        
        return f"{class_name}.{strongest_extension}"


```