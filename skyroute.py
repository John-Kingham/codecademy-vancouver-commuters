from skyroute_database import landmark_choices, landmark_stations
from skyroute_database import metro_stations, closed_stations


def shortest_route(start, end):
    """
    Returns the shortest Vancouver metro route between two landmarks.

    Parameters
    ----------
    start : str
        The name of the starting landmark
    end : str
        The name of the destination landmark

    Returns
    -------
    None
        If no route exists.
    list : (of strings)
        Station names along the shortest route.
    """
    stations_open = open_stations()

    # check to see if any route exists. If not, exit.

    any_route = None
    for start_station in landmark_stations[start]:
        for end_station in landmark_stations[end]:
            any_route = dfs(stations_open, start_station, end_station)
            if any_route:
                break
        if any_route:
            break
    if not any_route:
        return

    # find and return the shortest route

    routes = []
    for start_station in landmark_stations[start]:
        for end_station in landmark_stations[end]:
            route = bfs(metro_stations, start_station, end_station)
            if route:
                routes.append(route)
    if routes:
        return min(routes, key=len)


def open_stations():
    """
    Returns a graph of stations with all edges to closed stations removed.
    """
    temp_graph = metro_stations
    for station in temp_graph:
        if station in closed_stations:
            temp_graph[station] = set()
        else:
            temp_graph[station] -= closed_stations
    return temp_graph


def dfs(graph, current_vertex, target_vertex, visited=None):
    """
    A depth-first search.
    """
    if visited is None:
        visited = []
    visited.append(current_vertex)
    if current_vertex == target_vertex:
        return visited
    for neighbour in graph[current_vertex]:
        if neighbour not in visited:
            path_to_target = dfs(graph, neighbour, target_vertex, visited)
            if path_to_target:
                return path_to_target


def bfs(graph, start_vertex, target_value):
    """
    A breadth-first search.
    """
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()
    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)
        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                if neighbour == target_value:
                    return path + [neighbour]
                else:
                    bfs_queue.append([neighbour, path + [neighbour]])
