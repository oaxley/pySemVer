# -*- coding: utf-8 -*-
#
# Simple Semantic Versioning Library
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

# ----- Imports
from __future__ import annotations
from typing import List

import sys

# ----- Classes
class SemanticVersion:
    """Simple class to handle version management according to Semantic Versioning 2.0"""

    def __init__(
        self,
        *,
        major: int,
        minor: int,
        patch: int,
        pre_release: str = "",
        build: str = "",
    ) -> None:
        """Constructor"""
        self.major = major
        self.minor = minor
        self.patch = patch
        self.pre_release = pre_release
        self.build = build

    #
    # Representation operators
    #
    def __str__(self) -> str:
        """String representation"""
        string = f"{self.major}.{self.minor}.{self.patch}"
        if self.pre_release != "":
            string += f"-{self.pre_release}"
        if self.build != "":
            string += f"+{self.build}"
        return string

    def __repr__(self) -> str:
        """Python representation"""
        string = f"major={self.major}, minor={self.minor}, patch={self.patch}"
        string += ", pre_release="
        if self.pre_release != "":
            string += f'"{self.pre_release}"'
        else:
            string += '""'

        string += ", build="
        if self.build != "":
            string += f'"{self.build}"'
        else:
            string += '""'

        return f"SemanticVersion({string})"

    #
    # Comparison operators
    # build is not taken into account during comparison as per Semantic Versioning rules.
    #
    def __eq__(self, other) -> bool:
        """Rich comparison operator '=='"""
        if not isinstance(other, SemanticVersion):
            return NotImplemented

        return (self.major, self.minor, self.patch, self.pre_release) == (
            other.major,
            other.minor,
            other.patch,
            other.pre_release,
        )

    def __ne__(self, other) -> bool:
        """Rich comparison operator '!='"""
        result = self.__eq__(other)
        if result == NotImplemented:
            return result
        return not result

    def __lt__(self, other) -> bool:
        """Rich comparison operator '<'"""
        if not isinstance(other, SemanticVersion):
            return NotImplemented

        left = f"{self.major}.{self.minor}.{self.patch}"
        right = f"{other.major}.{other.minor}.{other.patch}"

        if left < right:
            return True
        elif left > right:
            return False

        # both version are equals
        # we need to check for the pre_release tag

        # no pre_release, no need to go further
        # if other.pre_release is empty, both version are equals so self < other is false
        # if other.pre_release is not empty, self > other (precedence rule) so self < other is false
        if self.pre_release == "":
            return False

        # 1.0.0 (other) has precedence other 1.0.0-alpha (self)
        if other.pre_release == "" and self.pre_release != "":
            return True

        # both pre-release are not empty, need to compare according to AlphaNum values
        if self.pre_release < other.pre_release:
            return True

        return False

    def __le__(self, other) -> bool:
        """Rich comparison operator '<='"""
        if not isinstance(other, SemanticVersion):
            return NotImplemented

        if (self.__eq__(other) == True) or (self.__lt__(other) == True):
            return True

        return False

    def __gt__(self, other) -> bool:
        """Rich comparison operator '>'"""
        if not isinstance(other, SemanticVersion):
            return NotImplemented

        if (self.__eq__(other) == True) or (self.__lt__(other) == True):
            return False

        return True

    def __ge__(self, other) -> bool:
        """Rich comparison operator '>='"""
        if not isinstance(other, SemanticVersion):
            return NotImplemented

        if (self.__eq__(other) == True) or (self.__gt__(other) == True):
            return True

        return False

    @classmethod
    def parse(cls, version: str) -> SemanticVersion:
        """Parse a string version and create a SemanticVersion object"""
        if not isinstance(version, str):
            raise ValueError("Version should be a valid Python string.")

        values: List[str] = []

        # extract the build value
        if "+" in version:
            values = version.split("+")
            version = values[0]
            build = values[1]
        else:
            build = ""

        # extract the pre-release value
        if "-" in version:
            values = version.split("-")
            version = values[0]
            pre_release = values[1]
        else:
            pre_release = ""

        # extract version information
        if version != "":
            values = version.split(".")

        numbers: List[int] = []
        for i in range(3):
            try:
                numbers.append(int(values[i]))
            except (ValueError, IndexError):
                numbers.append(0)

        # create a new object
        return cls(
            major=numbers[0],
            minor=numbers[1],
            patch=numbers[2],
            pre_release=pre_release,
            build=build,
        )
