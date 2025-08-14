import requests
# import: pip install requests

usernames = [
    ["potayto", 15],
    ["sejicgndslj1", 296]
]
url = "https://solved.ac/api/v3/search/user"

print(f"{'handle':<15} | {'rating':<7} | {'points':<6} | gap")
print("-" * 50)

previous_points = None

previous_points = None

for username, prev_points in usernames:
    params = {"query": username}
    res = requests.get(url, params=params)
    data = res.json()

    if data["count"] > 0:
        user = data["items"][0]
        points = user["rating"] - prev_points  # your "points" calculation
        if previous_points is None:
            gap = "-"
        else:
            gap = points - previous_points
        print(f"{user['handle']:<15} | {user['rating']:<7} | {points:<6} | {gap}")
        previous_points = points
    else:
        points = 0 - prev_points
        if previous_points is None:
            gap = "-"
        else:
            gap = points - previous_points
        print(f"{username:<15} | {'N/A':<7} | {points:<6} | {gap}")
        previous_points = points
