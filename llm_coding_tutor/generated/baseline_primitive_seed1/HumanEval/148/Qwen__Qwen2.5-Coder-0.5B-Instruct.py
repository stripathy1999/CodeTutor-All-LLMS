from typing import List

def bf(planet1: str, planet2: str) -> List[str]:
    # List of planets sorted by their proximity to the Sun
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # Find indices of the given planets
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    
    # If either planet is not found, return an empty tuple
    if idx1 == -1 or idx2 == -1:
        return []
    
    # Ensure idx1 is less than idx2 for correct slicing
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    
    # Slice the list to get the planets between the two given planets
    return planets[idx1 + 1:idx2]