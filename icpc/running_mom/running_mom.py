import sys


def parse_input(flights):

    n_trips = (int)(flights[0][0])
    check_safe = flights[n_trips+1:]
    check_safe = [i for arr in check_safe for i in arr]

    flight_graph = {}
    for dep, des in flights[1:n_trips + 1]:
        if dep not in flight_graph:
            flight_graph[dep] = [des]
        else:
            flight_graph[dep].append(des)

    return flight_graph, check_safe


def running_mom(from_parse):
    graph, check = parse_input(from_parse)
    visited = set()  # remember
    visitting = set()  # cycle detected

    def dfs(city):
        if city in visited:
            return
        visited.add(city)
        for des in graph.get(city, []):
            dfs(des)
            if des in visited:
                visitting.add(des)
        visited.remove(city)

    res = []
    for flight in check:
        dfs(flight)
        if flight in visitting:
            res.append(flight + ' safe')
        else:
            res.append(flight + ' trapped')

    return '\n'.join(res)


flights = []

for flight in sys.stdin:
    flights.append(flight.split())

sys.stdout.write(running_mom(flights) + '\n')
