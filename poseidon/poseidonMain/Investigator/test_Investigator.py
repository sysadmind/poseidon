#!/usr/bin/env python
#
#   Copyright (c) 2016 In-Q-Tel, Inc, All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
Test module for Investigator.py

Created on 28 June 2016
@author: dgrossman, tlanham
"""
from Investigator import Investigator
import pytest


def test_Investigator():
    Investigator()


def test_register_algo():
    investigator = Investigator()
    investigator.register_algorithm('cube_fn', lambda x: x**3)


def test_process_new_machine():
    investigator = Investigator()
    ip = '0.0.0.0'
    investigator.process_new_machine(ip)
