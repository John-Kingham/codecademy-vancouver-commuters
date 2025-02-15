from skyroute_database import landmark_choices, landmark_stations, metro_stations


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
    if route_from(start, end):
        routes = []
        for start_station in landmark_stations[start]:
            for end_station in landmark_stations[end]:
                route = bfs(metro_stations, start_station, end_station)
                if route:
                    routes.append(route)
        if routes:
            print(f"routes[] = {routes}")
            return min(routes, key=len)


def route_from(start, end):
    """
    Returns any route if there is one.

    Parameters
    ----------
    start : str
        The name of the start landmark
    end : str
        The name of the end landmark

    Returns
    -------
    None
        If no route exists.
    list : (of strings)
        The station names along the route.
    """
    for start_station in landmark_stations[start]:
        for end_station in landmark_stations[end]:
            route = dfs(metro_stations, start_station, end_station)
            if route:
                return route


def dfs(graph, current_vertex, target_vertex, visited=None):
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


a_route = route_from(landmark_choices["1"], landmark_choices["2"])
short_route = shortest_route(landmark_choices["1"], landmark_choices["2"])
print(a_route)
print(short_route)

