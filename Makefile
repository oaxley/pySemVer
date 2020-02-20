# -*- coding: utf-8 -*-
#
# Simple Semantic Versioning Library - Makefile
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

.PHONY: clean test build

# clean the sources tree
clean:
	@rm -rf .mypy_cache .tox
	@rm -rf build dist *.egg-info
	@rm -f .coverage

# execute the test cases
test:
	@poetry run coverage run -m unittest
	@poetry run coverage report

# build the python package
build:
	@rm -rf build dist *.egg-info
	@poetry build
