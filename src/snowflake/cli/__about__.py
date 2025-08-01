# Copyright (c) 2024 Snowflake Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from enum import Enum, unique

VERSION = "3.11.0.dev0"


@unique
class CLIInstallationSource(Enum):
    BINARY = "binary"
    PYPI = "pypi"


# This variable is changed in binary release script
INSTALLATION_SOURCE = CLIInstallationSource.PYPI
