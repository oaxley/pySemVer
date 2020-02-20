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
class TestFactory(unittest.TestCase):

    def setUp(self):
        self.zero = SemanticVersion(major=0, minor=1, patch=2)
        self.one  = SemanticVersion(major=1, minor=2, patch=3)

    #
    # tests for string representation __str__
    #
    def test_str_no_prerelease_no_build(self):
        self.assertEqual(str(self.zero), '0.1.2')

    def test_str_with_prerelease_no_build(self):
        self.zero.pre_release = "alpha"
        self.assertEqual(str(self.zero), '0.1.2-alpha')

    def test_str_no_prerelease_with_build(self):
        self.zero.build = "1234"
        self.assertEqual(str(self.zero), '0.1.2+1234')

    def test_str_with_prerelease_with_build(self):
        self.zero.pre_release = "alpha"
        self.zero.build = "1234"
        self.assertEqual(str(self.zero), '0.1.2-alpha+1234')

    #
    # tests for Python representation __repr__
    #
    def test_repr_no_prerelease_no_build(self):
        self.assertEqual(repr(self.zero), 'SemanticVersion(major=0, minor=1, patch=2, pre_release="", build="")')

    def test_repr_with_prerelease_no_build(self):
        self.zero.pre_release = "alpha"
        self.assertEqual(repr(self.zero), 'SemanticVersion(major=0, minor=1, patch=2, pre_release="alpha", build="")')

    def test_repr_no_prerelease_with_build(self):
        self.zero.build = "1234"
        self.assertEqual(repr(self.zero), 'SemanticVersion(major=0, minor=1, patch=2, pre_release="", build="1234")')

    def test_repr_with_prerelease_with_build(self):
        self.zero.pre_release = "alpha"
        self.zero.build = "1234"
        self.assertEqual(repr(self.zero), 'SemanticVersion(major=0, minor=1, patch=2, pre_release="alpha", build="1234")')

    #
    # tests for equality a == b
    #
    def test_eq_non_instance(self):
        self.assertFalse(self.zero == 3)

    def test_eq_no_prerelease_no_build(self):
        other = SemanticVersion(major=0, minor=1, patch=2, pre_release="", build="")
        self.assertTrue(self.zero == other)

    def test_eq_no_prerelease_with_build(self):
        self.zero.build = "1234"
        other = SemanticVersion(major=0, minor=1, patch=2, pre_release="", build="1234")
        self.assertTrue(self.zero == other)

    def test_eq_no_prerelease_with_different_build(self):
        self.zero.build = "1234"
        other = SemanticVersion(major=0, minor=1, patch=2, pre_release="", build="2345")
        self.assertTrue(self.zero == other)

    def test_eq_with_prerelease_no_build(self):
        self.zero.pre_release = "alpha"
        other = SemanticVersion(major=0, minor=1, patch=2, pre_release="alpha", build="")
        self.assertTrue(self.zero == other)

    def test_eq_with_prerelease_with_build(self):
        self.zero.pre_release = "alpha"
        self.zero.build = "1234"
        other = SemanticVersion(major=0, minor=1, patch=2, pre_release="alpha", build="1234")
        self.assertTrue(self.zero == other)

    def test_eq_with_prerelease_with_different_build(self):
        self.zero.pre_release = "alpha"
        self.zero.build = "1234"
        other = SemanticVersion(major=0, minor=1, patch=2, pre_release="alpha", build="2345")
        self.assertTrue(self.zero == other)

    def test_eq_false(self):
        self.assertFalse(self.zero == self.one)

    #
    # tests for non equality a != b
    #
    def test_neq_non_instance(self):
        self.assertTrue(self.zero != 3)

    def test_neq_no_prerelease_no_build(self):
        self.assertTrue(self.zero != self.one)

    def test_neq_no_prerelease_with_same_build(self):
        self.zero.build = "1234"
        self.one.build = "1234"
        self.assertTrue(self.zero != self.one)

    def test_neq_no_prerelease_with_different_build(self):
        self.zero.build = "1234"
        self.one.build = "2345"
        self.assertTrue(self.zero != self.one)

    def test_neq_with_same_prerelease_no_build(self):
        self.zero.pre_release = "alpha"
        self.one.pre_release = "alpha"
        self.assertTrue(self.zero != self.one)

    def test_neq_with_different_prerelease_no_build(self):
        self.zero.pre_release = "alpha"
        self.one.pre_release = "beta"
        self.assertTrue(self.zero != self.one)

    def test_neq_false(self):
        self.assertFalse(self.one != self.one)

    #
    # tests for lesser a < b
    #
    def test_lt_non_instance(self):
        with self.assertRaises(TypeError):
            self.one < 3

    def test_lt_true_no_prerelease_no_build(self):
        self.assertTrue(self.zero < self.one)

    def test_lt_false_no_prerelease_no_build(self):
        self.assertFalse(self.one < self.zero)

    def test_lt_false_same_version_no_prerelease_no_build(self):
        self.assertFalse(self.zero < self.zero)

    def test_lt_with_prerelease_precedence_no_build(self):
        other = SemanticVersion(major=0, minor=1, patch=2, pre_release="alpha", build="")
        self.assertTrue(other < self.zero)

    def test_lt_with_prerelease_no_build(self):
        self.zero.pre_release = "beta"
        other = SemanticVersion(major=0, minor=1, patch=2, pre_release="alpha", build="")
        self.assertTrue(other < self.zero)

    def test_lt_with_same_prerelease_no_build(self):
        self.zero.pre_release = "alpha"
        other = SemanticVersion(major=0, minor=1, patch=2, pre_release="alpha", build="")
        self.assertFalse(other < self.zero)

    #
    # tests for lesser or equal a <= b
    #
    def test_le_non_instance(self):
        with self.assertRaises(TypeError):
            self.one <= 3

    def test_le_true_not_equal_no_prerelease_no_build(self):
        self.assertTrue(self.zero <= self.one)

    def test_le_true_equal_no_prerelease_no_build(self):
        self.assertTrue(self.zero <= self.zero)

    def test_le_false_no_prerelease_no_build(self):
        self.assertFalse(self.one <= self.zero)

    #
    # tests for greater a > b
    #
    def test_gt_non_instance(self):
        with self.assertRaises(TypeError):
            self.one > 3

    def test_gt_false_equal_no_prerelease_no_build(self):
        self.assertFalse(self.zero > self.zero)

    def test_gt_false_not_equal_no_prerelease_no_build(self):
        self.assertFalse(self.zero > self.one)

    def test_gt_true_no_prerelease_no_build(self):
        self.assertTrue(self.one > self.zero)

    #
    # tests for greater or equal a >= b
    #
    def test_ge_non_instance(self):
        with self.assertRaises(TypeError):
            self.one >= 3

    def test_ge_true_equal_no_prerelease_no_build(self):
        self.assertTrue(self.one >= self.one)

    def test_ge_true_not_equal_no_prerelease_no_build(self):
        self.assertTrue(self.one >= self.zero)

    def test_ge_false_no_prerelease_no_build(self):
        self.assertFalse(self.zero >= self.one)


