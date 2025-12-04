import json
from datetime import datetime, timedelta

start_date = datetime(year=2025, month=12, day=1, hour=6, minute=0)

with open('./leaderboard.json') as f:
    data = json.load(f)

members = [ m for m in data['members'].values() if m['local_score'] > 0 ]
members.sort(key=lambda m: m['local_score'], reverse=True)

timestamps = {}
for m in members:
    m['star_stats'] = {}
    for day, day_stat in m['completion_day_level'].items():
        for star, star_stat in day_stat.items():
            key = f'{int(day):02}_{star}'
            m['star_stats'][key] = { 'time': datetime.fromtimestamp(star_stat['get_star_ts']) }
            if key not in timestamps:
                timestamps[key] = []
            timestamps[key].append(m['star_stats'][key])

for v in timestamps.values():
    v.sort(key=lambda m: m['time'])
    for i in range(len(v)):
        v[i]['rank'] = i+1
        v[i]['prev'] = v[i-1]['time'] if i else None

sorted_stars = sorted(timestamps.keys(), reverse=True)

for i, m in enumerate(members):
    print(f"{i+1}: {m['name']} ({m['local_score']})")
    for s in sorted_stars:
        if s in m['star_stats']:
            stat = m['star_stats'][s]
            print(
                f"  {s}: {stat['rank']} -> {stat['time']}",
                f"(+{stat['time'] - stat['prev']})"
                if stat['prev'] else
                f"({stat['time'] - (start_date + timedelta(days=int(s[:2])-1))})")
