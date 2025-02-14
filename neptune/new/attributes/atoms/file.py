#
# Copyright (c) 2020, Neptune Labs Sp. z o.o.
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
import os
from typing import Optional

from neptune.new.attributes.atoms.atom import Atom
from neptune.new.internal.operation import UploadFile, UploadFileContent
from neptune.new.internal.utils import base64_encode, verify_type
from neptune.new.types.atoms.file import File as FileVal

# pylint: disable=protected-access


class File(Atom):
    def assign(self, value: FileVal, wait: bool = False) -> None:
        verify_type("value", value, FileVal)

        if value.path is not None:
            operation = UploadFile(
                self._path, ext=value.extension, file_path=os.path.abspath(value.path)
            )
        elif value.content is not None:
            operation = UploadFileContent(
                self._path,
                ext=value.extension,
                file_content=base64_encode(value.content),
            )
        else:
            raise ValueError("File path and content are None")

        with self._container.lock():
            self._enqueue_operation(operation, wait)

    def upload(self, value, wait: bool = False) -> None:
        self.assign(FileVal.create_from(value), wait)

    def download(self, destination: Optional[str] = None) -> None:
        verify_type("destination", destination, (str, type(None)))
        self._backend.download_file(
            self._container_id, self._container_type, self._path, destination
        )

    def fetch_extension(self) -> str:
        # pylint: disable=protected-access
        val = self._backend.get_file_attribute(self._container_id, self._container_type, self._path)
        return val.ext
