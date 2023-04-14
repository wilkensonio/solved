import sys


def parse_input(flights: list):  # -> dict, list

    n_trips = (int)(flights[0][0])
    check_safe = [i for arr in flights[n_trips+1:] for i in arr]

    flight_graph = {}

    for dep, des in flights[1:n_trips + 1]:
        if dep not in flight_graph:
            flight_graph[dep] = [des]
        else:
            flight_graph[dep].append(des)

    return flight_graph, check_safe


def find_safe_cities(from_parse: list):
    graph, check = parse_input(from_parse)
    visited = set()  # remember
    visit = set()
    safe = set()  # cycle detected

    def dfs(city: str):
        if city in visited:
            safe.add(city)
            return
        if city not in visited and city in visit:
            return

        visited.add(city)
        visit.add(city)

        for dest in graph.get(city, []):
            dfs(dest)

        visited.remove(city)

    res = []
    for flight in check:
        visit.clear()
        dfs(flight)
        if flight in safe:
            res.append(flight + ' safe')
        else:
            res.append(flight + ' trapped')

    print('\n'.join(res))


flights = []


for flight in sys.stdin:

    flights.append(flight.split())

find_safe_cities(flights)
