# -*- coding: utf-8 -*-
#
# Unit tests for the Simple SemVer library
#
# Copyright 2020 Sebastien LEGRAND
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#----- Imports
import unittest

from pysemver import SemanticVersion


#----- Classes
class TestParsing(unittest.TestCase):

    def test_parse_not_instance(self):
        with self.assertRaises(ValueError):
            SemanticVersion.parse(123)

    def test_parse_correct_build(self):
        result = SemanticVersion(major=1, minor=2, patch=3, pre_release="", build="1234")
        a = SemanticVersion.parse("1.2.3+1234")
        self.assertEqual(result, a)

    def test_parse_multiple_build(self):
        result = SemanticVersion(major=1, minor=2, patch=3, pre_release="", build="1234")
        a = SemanticVersion.parse("1.2.3+1234+2345")
        self.assertEqual(result, a)

    def test_parse_no_build(self):
        result = SemanticVersion(major=1, minor=2, patch=3, pre_release="", build="")
        a = SemanticVersion.parse("1.2.3")
        self.assertEqual(result, a)

    def test_parse_correct_prerelease(self):
        result = SemanticVersion(major=1, minor=2, patch=3, pre_release="alpha", build="")
        a = SemanticVersion.parse("1.2.3-alpha")
        self.assertEqual(result, a)

    def test_parse_multiple_prerelease(self):
        result = SemanticVersion(major=1, minor=2, patch=3, pre_release="alpha", build="")
        a = SemanticVersion.parse("1.2.3-alpha-beta")
        self.assertEqual(result, a)

    def test_parse_no_prerelease(self):
        result = SemanticVersion(major=1, minor=2, patch=3, pre_release="", build="")
        a = SemanticVersion.parse("1.2.3")
        self.assertEqual(result, a)

    def test_parse_empty_version(self):
        result = SemanticVersion(major=0, minor=0, patch=0, pre_release="alpha", build="")
        a = SemanticVersion.parse("-alpha")
        self.assertEqual(result, a)

    def test_parse_no_patch(self):
        result = SemanticVersion(major=1, minor=2, patch=0, pre_release="", build="")
        a = SemanticVersion.parse("1.2")
        self.assertEqual(result, a)

    def test_parse_no_minor(self):
        result = SemanticVersion(major=1, minor=0, patch=0, pre_release="", build="")
        a = SemanticVersion.parse("1")
        self.assertEqual(result, a)

    def test_parse_wrong_patch(self):
        result = SemanticVersion(major=1, minor=2, patch=0, pre_release="", build="")
        a = SemanticVersion.parse("1.2.3a")
        self.assertEqual(result, a)

    def test_parse_wrong_minor(self):
        result = SemanticVersion(major=1, minor=0, patch=3, pre_release="", build="")
        a = SemanticVersion.parse("1.2a.3")
        self.assertEqual(result, a)

    def test_parse_wrong_major(self):
        result = SemanticVersion(major=0, minor=2, patch=3, pre_release="", build="")
        a = SemanticVersion.parse("1a.2.3")
        self.assertEqual(result, a)

    def test_parse_complete_version(self):
        result = SemanticVersion(major=1, minor=2, patch=3, pre_release="alpha", build="2345")
        a = SemanticVersion.parse("1.2.3-alpha+2345")
        self.assertEqual(result, a)
