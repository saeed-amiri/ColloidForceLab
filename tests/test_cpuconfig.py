"""
Test for the cpuconfig module in common
"""
# pylint: disable=import-error

import os
import unittest

import multiprocessing

from src.common import logger
from src.common.cpuconfig import ConfigCpuNr


class TestConfigCpuNr(unittest.TestCase):
    """
    Test the relaibility of the ConfigCpuNr class
    """

    def setUp(self) -> None:
        """Set up test environment"""
        self.log_name = "test_ConfigCpuNr"
        self.log: str = logger.setup_logger(log_name=f'{self.log_name}.log')
        self.cpu_config = ConfigCpuNr(log=self.log)

    def tearDown(self) -> None:
        """Clean up test environment"""
        for file in os.listdir('.'):
            if file.startswith(self.log_name):
                os.remove(file)

    def test_get_hostname(self) -> None:
        """Test the get_hostname method"""
        hostname = self.cpu_config.get_hostname()
        self.assertIsInstance(hostname, str)
        self.assertTrue(hostname)

    def test_get_core_nr(self) -> None:
        """Test the get_core_nr method"""
        core_nr = self.cpu_config.get_core_nr()
        # check if the core number is an integer
        self.assertIsInstance(core_nr, int)

        aval_core_nr: int = multiprocessing.cpu_count()
        self.assertEqual(core_nr, aval_core_nr)


if __name__ == '__main__':
    unittest.main()
