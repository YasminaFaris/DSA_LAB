import json
def findStations(stations):
    global cities
    cities_to_cover = set(cities)
    
    selected_stations = []
    
    while cities_to_cover:
        best_station = None
        best_coverage = 0
        
        for station_name, station_cities in stations.items():
            coverage = len(set(station_cities) & cities_to_cover)
            if coverage > best_coverage:
                best_station = station_name
                best_coverage = coverage
        
        if best_coverage == 0:
            break
        
        selected_stations.append(best_station)
        cities_to_cover -= set(stations[best_station])
        
    selected_stations.sort()
    return selected_stations

def main():
    cities = json.loads(input())
    n = int(input())
    stations_dict = {}

    for _ in range(n):
        station_info = json.loads(input())
        stations_dict[station_info["Name"]] = station_info["Cities"]
    
    result = findStations(stations_dict)
    print(result)
main()