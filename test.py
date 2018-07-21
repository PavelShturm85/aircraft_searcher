import unittest
from aircraft_list import AircraftSearcher


class TestAircraftList(unittest.TestCase):

    def setUp(self):
        self.A = AircraftSearcher(
            200, (50.0, 4.0), (50.0, 4.0), (50.0, 4.0), (50.0, 4.0))
        self.B = AircraftSearcher(200.1, (50, 4), (50, 4), (50, 4), (50, 4))
        self.C = AircraftSearcher(0, (0, 0), (0, 0), (0, 0), (0, 0))
        self.D = AircraftSearcher(2000, (90, -180), (-90, 180), (90, -180), (-90, 180))
        self.E = AircraftSearcher(-20000, (280, -190), (-280, 190), (380, -190), (-280, 190))
        self.object_list = [self.A, self.B, self.C, self.D, self.E ]

    def test_init(self):

        self.assertEqual((self.A._km, self.A._min_latitude, self.A._max_latitude, self.A._latitude_on_min_longitude, self.A._min_longitude, self.A._latitude_on_max_longitude,
                          self.A._max_longitude), (int(200), float(50.0), float(50.0), float(50.0), float(4.0), float(50.0), float(4.0)))
        self.assertEqual((self.B._km, self.B._min_latitude, self.B._max_latitude, self.B._latitude_on_min_longitude, self.B._min_longitude, self.B._latitude_on_max_longitude,
                          self.B._max_longitude), (float(200.1), float(50), float(50), float(50), float(4), float(50), float(4)))
        self.assertEqual((self.C._km, self.C._min_latitude, self.C._max_latitude, self.C._latitude_on_min_longitude, self.C._min_longitude, self.C._latitude_on_max_longitude,
                          self.C._max_longitude), (int(0), float(0), float(0), float(0), float(0), float(0), float(0)))

    def test_corrected_coordinates(self):

        for obj in self.object_list:
            coordinate = obj._get_corrected_coordinates
            self.assertGreaterEqual(coordinate[2], -180)
            self.assertGreaterEqual(coordinate[0], -90)
            self.assertLessEqual(coordinate[3], 180)
            self.assertLessEqual(coordinate[1], 90)


if __name__ == '__main__':
    unittest.main()
