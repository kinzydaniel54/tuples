def format_itineraries(itineraries):
    result = ""
    for i, itinerary in enumerate(itineraries, 1):
        traveler_name, origin, destination = itinerary
        result += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return result.strip()  # Remove trailing newline

# Example usage:
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_output = format_itineraries(itineraries)
print(formatted_output)
