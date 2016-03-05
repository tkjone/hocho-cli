"""Tests for our main hocho CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from hocho import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['hocho', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['hocho', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['hocho', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)
