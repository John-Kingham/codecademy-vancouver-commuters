import unittest
from skyroute_database import landmark_choices, landmark_stations, metro_stations
from skyroute import shortest_route


class TestSkyRoute(unittest.TestCase):

    def test_find_shortest_route(self):
        start = landmark_choices["1"]
        end = landmark_choices["2"]
        short_route = ["TEST STATION 1", "TEST STATION 2"]
        self.assertEqual(shortest_route(start, end), short_route)

    def test_start_station_closed(self):
        start = landmark_choices["5"]
        end = landmark_choices["6"]
        self.assertIsNone(shortest_route(start, end))

    def test_mid_station_closed(self):
        start = landmark_choices["4"]
        end = landmark_choices["6"]
        self.assertIsNone(shortest_route(start, end))

    def test_end_station_closed(self):
        start = landmark_choices["4"]
        end = landmark_choices["5"]
        self.assertIsNone(shortest_route(start, end))
