from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOsszeg(TestCase):
    def test_feladat02(self):
        aktualis = feladatok.feladat02()
        elvart = 4
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg, azon számpárok számát amelyek összege pontossan 100!")
