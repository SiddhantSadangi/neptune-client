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
from enum import Enum

from neptune.new.internal.utils import verify_type


class ProjectMemberRoleDTO(Enum):
    VIEWER = 'viewer'
    MEMBER = 'member'
    MANAGER = 'manager'

    @staticmethod
    def from_str(role: str):
        verify_type('role', role, str)

        __DEPRECATED_ROLES__ = {
            ProjectMemberRole.MEMBER: ProjectMemberRole.CONTRIBUTOR,
            ProjectMemberRole.MANAGER: ProjectMemberRole.OWNER
        }
        if role in __DEPRECATED_ROLES__:
            warnings.warn(
                f"The role '{role}' was renamed to '{__DEPRECATED_ROLES__.get(role)}'",
                DeprecationWarning)
        role = __DEPRECATED_ROLES__.get(role, role)

        return {
            'viewer': ProjectMemberRoleDTO.VIEWER,
            'contributor': ProjectMemberRoleDTO.MEMBER,
            'owner': ProjectMemberRoleDTO.MANAGER
        }.get(role)
