from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOsszeg(TestCase):
    def test_feladat05(self):
        aktualis = feladatok.feladat05()
        elvart = 4
        self.assertEqual(elvart, aktualis, "Nem jól határozta meg, a leghosszabb szigorúan növekvő számsorozatot hosszát!")
