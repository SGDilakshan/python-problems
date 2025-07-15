# You are given a list of timestamps in the format "HH:MM". Write a Python function that finds the minimum difference in minutes between any two timestamps in the list. Assume the list is circular — e.g., "23:59" and "00:01" are 2 minutes apart.

def time_to_minutes(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def find_min_time_difference(times):
    minutes = sorted(time_to_minutes(t) for t in times)
    minutes.append(minutes[0] + 1440)  # Wrap around for circular comparison
    min_diff = min(b - a for a, b in zip(minutes, minutes[1:]))
    return min_diff

# Example usage
times = ["23:59", "00:01", "12:30", "04:15"]
result = find_min_time_difference(times)
print("Minimum time difference:", result, "minutes")
