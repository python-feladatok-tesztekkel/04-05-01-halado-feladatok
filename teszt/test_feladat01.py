from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOsszeg(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.feladat01()
        elvart = 5
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg, hogy hányszor fordul elő, hogy a szám a következő szám négyzete!")
