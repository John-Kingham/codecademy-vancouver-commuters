import unittest
from skyroute_database import landmark_choices, landmark_stations, metro_stations
from skyroute import shortest_route, route_from


class TestSkyRoute(unittest.TestCase):

    def test_find_any_route(self):
        start = landmark_choices["1"]
        end = landmark_choices["2"]
        any_route = ["TEST STATION 1", "TEST STATION 3", "TEST STATION 2"]
        self.assertEqual(route_from(start, end), any_route)

    def test_find_shortest_route(self):
        start = landmark_choices["1"]
        end = landmark_choices["2"]
        short_route = ["TEST STATION 1", "TEST STATION 2"]
        self.assertEqual(shortest_route(start, end), short_route)
