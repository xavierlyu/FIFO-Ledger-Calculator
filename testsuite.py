#!/usr/bin/python

import os
import filecmp
import unittest

"""
To run test suite, type `chmod +x testsuite.py; ./testsuite.py`
or `python3 testsuite.py`
"""


class TestFIFO(unittest.TestCase):
    def test_given(self):
        os.system("python3 fifo.py transactions1.csv")
        self.assertTrue(filecmp.cmp("transactions1.out", "transactions1.ref"))
        os.system("python3 fifo.py transactions2.csv")
        self.assertTrue(filecmp.cmp("transactions2.out", "transactions2.ref"))
        os.system("python3 fifo.py transactions3.csv")
        self.assertTrue(filecmp.cmp("transactions3.out", "transactions3.ref"))

    def test_sell_all(self):
        # test against buying a small amount of shares many times and then sell all
        os.system("python3 fifo.py transactions7.csv")
        self.assertTrue(filecmp.cmp("transactions7.out", "transactions7.ref"))
        os.system("python3 fifo.py transactions8.csv")
        self.assertTrue(filecmp.cmp("transactions8.out", "transactions8.ref"))

    def test_sell_half(self):
        # buy a lot of shares, then sell half
        os.system("python3 fifo.py transactions9.csv")
        self.assertTrue(filecmp.cmp("transactions9.out", "transactions9.ref"))

    def test_buy_sell_buy_sell(self):
        # buy sell buy sell buy sell buy sell etc.
        os.system("python3 fifo.py transactions10.csv")
        self.assertTrue(filecmp.cmp("transactions10.out", "transactions10.ref"))
        os.system("python3 fifo.py transactions11.csv")
        self.assertTrue(filecmp.cmp("transactions11.out", "transactions11.ref"))
        os.system("python3 fifo.py transactions12.csv")
        self.assertTrue(filecmp.cmp("transactions12.out", "transactions12.ref"))

    def test_random(self):
        # test against some random ledgers
        os.system("python3 fifo.py transactions4.csv")
        self.assertTrue(filecmp.cmp("transactions4.out", "transactions4.ref"))
        os.system("python3 fifo.py transactions5.csv")
        self.assertTrue(filecmp.cmp("transactions5.out", "transactions5.ref"))
        os.system("python3 fifo.py transactions6.csv")
        self.assertTrue(filecmp.cmp("transactions6.out", "transactions6.ref"))

    def test_multi(self):
        # multiple buy low sell high
        os.system("python3 fifo.py transactions13.csv")
        self.assertTrue(filecmp.cmp("transactions13.out", "transactions13.ref"))
        os.system("python3 fifo.py transactions14.csv")
        self.assertTrue(filecmp.cmp("transactions14.out", "transactions14.ref"))
        # same as 13 but randomized order
        os.system("python3 fifo.py transactions15.csv")
        self.assertTrue(filecmp.cmp("transactions15.out", "transactions15.ref"))

    def test_net_lost(self):
        # test transcations lose money
        os.system("python3 fifo.py transactions16.csv")
        self.assertTrue(filecmp.cmp("transactions16.out", "transactions16.ref"))
        os.system("python3 fifo.py transactions17.csv")
        self.assertTrue(filecmp.cmp("transactions17.out", "transactions17.ref"))

    def test_combo(self):
        # test combination of stuff mentioned above
        os.system("python3 fifo.py transactions18.csv")
        self.assertTrue(filecmp.cmp("transactions18.out", "transactions18.ref"))
        os.system("python3 fifo.py transactions19.csv")
        self.assertTrue(filecmp.cmp("transactions19.out", "transactions19.ref"))
        os.system("python3 fifo.py transactions20.csv")
        self.assertTrue(filecmp.cmp("transactions20.out", "transactions20.ref"))
        os.system("python3 fifo.py transactions21.csv")
        self.assertTrue(filecmp.cmp("transactions21.out", "transactions21.ref"))
        os.system("python3 fifo.py transactions22.csv")
        self.assertTrue(filecmp.cmp("transactions22.out", "transactions22.ref"))

    def test_speed(self):
        # test against a large file
        os.system("python3 fifo.py transactions23.csv")
        self.assertTrue(filecmp.cmp("transactions23.out", "transactions23.ref"))


if __name__ == "__main__":
    unittest.main()
