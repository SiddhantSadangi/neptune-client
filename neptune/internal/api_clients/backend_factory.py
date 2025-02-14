#
# Copyright (c) 2021, Neptune Labs Sp. z o.o.
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

from neptune.backend import BackendApiClient
from neptune.exceptions import InvalidNeptuneBackend
from neptune.internal.api_clients import (
    HostedNeptuneBackendApiClient,
    OfflineBackendApiClient,
)


def backend_factory(*, backend_name, api_token=None, proxies=None) -> BackendApiClient:
    if backend_name == "offline":
        return OfflineBackendApiClient()

    elif backend_name is None:
        return HostedNeptuneBackendApiClient(api_token, proxies)

    else:
        raise InvalidNeptuneBackend(backend_name)
