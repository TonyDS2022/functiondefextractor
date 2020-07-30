"""Koninklijke Philips N.V., 2019 - 2020. All rights reserved."""

import os


class TestResource:
    """This test class stores data required to test the functionality
    skipping from the presentation layer to IO layer"""
    tst_resource_folder = os.path.join(os.path.dirname(__file__), os.pardir, "test_resource")
    par_dir = os.path.join(os.path.dirname(__file__), os.pardir)
