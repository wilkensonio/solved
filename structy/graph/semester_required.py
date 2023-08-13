
"""
semesters required
Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long the prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.
"""


def semesters_required(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)

    # final courses all node that have no neighbor
    distance = {}
    for course in graph:
        if not graph[course]:
            distance[course] = 1  # set to 1 meaning only one semester is needed

    for course in graph:
        traverse_distance(graph, course, distance)

    return max(distance.values())


def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]

    max_distance = 0
    for neigh in graph[node]:
        neigh_dist = traverse_distance(graph, neigh, distance)
        max_distance = max(max_distance, neigh_dist)
    distance[node] = max_distance + 1
    return distance[node]


def build_graph(num_courses, prereq: list[tuple[[int, int]]]):
    graph = {}

    for id in range(num_courses):
        graph[id] = []

    for pre_req in prereq:
        a, b = pre_req
        graph[a].append(b)

    return graph


num_courses = 6
prereqs = [
    (1, 2),
    (2, 4),
    (3, 5),
    (0, 5),
]
print(semesters_required(num_courses, prereqs))
