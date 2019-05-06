# mautrix-facebook - A Matrix-Facebook Messenger puppeting bridge
# Copyright (C) 2019 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from mautrix.util.color_log import ColorFormatter as BaseColorFormatter, PREFIX, MXID_COLOR, RESET

FBCHAT_COLOR = PREFIX + "35;1m"  # magenta


class ColorFormatter(BaseColorFormatter):
    def _color_name(self, module: str) -> str:
        fbchat = ["fbchat.util", "fbchat.request", "fbchat.client"]
        for prefix in fbchat:
            if module.startswith(prefix):
                return (FBCHAT_COLOR + prefix + RESET
                        + "." + MXID_COLOR + module[len(prefix) + 1:] + RESET)
        return super()._color_name(module)
