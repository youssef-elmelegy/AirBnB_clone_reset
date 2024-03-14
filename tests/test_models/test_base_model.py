#!/usr/bin/python3
from models.base_model import BaseModel as BM
import unittest
class test_base_model(unittest):
    def test_init(self):
        base1 = BM()
        self.assertEqual(BM, type(base1))
        self.asser


