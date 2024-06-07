"""Test logger functions"""

# pylint: disable=import-error

# tests/test_logger.py

import os
import unittest
import logging
from src.common.colors_text import TextColor as bcolors
from src.common.logger import setup_logger, check_log_file, write_header


class TestLogger(unittest.TestCase):
    """Test logger functions"""

    def setUp(self) -> None:
        """Set up test environment"""
        self.log_name = "test_log"
        # Ensure no test log files exist before tests
        for file in os.listdir('.'):
            if file.startswith(self.log_name):
                os.remove(file)

    def tearDown(self) -> None:
        """Clean up test environment"""
        for file in os.listdir('.'):
            if file.startswith(self.log_name):
                os.remove(file)

    def test_check_log_file(self) -> None:
        """Test check_log_file function"""
        # pylint: disable=consider-using-with
        log_file = check_log_file(self.log_name)
        self.assertEqual(log_file, f"{self.log_name}.1")

        # Create a log file to test increment
        open(f"{self.log_name}.1", 'a', encoding='utf-8').close()
        log_file = check_log_file(self.log_name)
        self.assertEqual(log_file, f"{self.log_name}.2")

    def test_write_header(self) -> None:
        """Test write_header function"""
        log_file = check_log_file(self.log_name)
        write_header(log_file)

        with open(log_file, 'r', encoding='utf-8') as f_log:
            header = f_log.readlines()

        self.assertEqual(len(header), 3)  # Date, directory, blank line

    def test_setup_logger(self) -> None:
        """Test setup_logger function"""
        logger = setup_logger(self.log_name)
        self.assertIsInstance(logger, logging.Logger)

        # Check if log file is created and written to
        log_file = check_log_file(self.log_name)
        print(f"{bcolors.OKGREEN}Expected log file path: "
              f"{log_file}{bcolors.ENDC}")


if __name__ == '__main__':
    unittest.main()
