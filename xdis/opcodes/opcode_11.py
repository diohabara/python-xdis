# (C) Copyright 2019-2023 by Rocky Bernstein
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
CPython 1.1 bytecode opcodes

This is used in bytecode disassembly. This is similar to the
opcodes in Python's dis.py library.
"""

import xdis.opcodes.opcode_12 as opcode_12

# This is used from outside this module
from xdis.cross_dis import findlabels
from xdis.opcodes.base import (  # Although these aren't used here, they are exported
    extended_format_CALL_FUNCTION,
    extended_format_MAKE_FUNCTION_10_27,
    extended_format_RAISE_VARARGS_older,
    extended_format_RETURN_VALUE,
    finalize_opcodes,
    format_extended_arg,
    format_MAKE_FUNCTION_10_27,
    format_RAISE_VARARGS_older,
    init_opdata,
    update_pj2,
)

version_tuple = (1, 1)  # 1.2 is the same
python_implementation = "CPython"

loc = l = locals()
init_opdata(l, opcode_12, version_tuple)

update_pj2(globals(), l)

opcode_arg_fmt = {
    "EXTENDED_ARG": format_extended_arg,
    "MAKE_FUNCTION": format_MAKE_FUNCTION_10_27,
    "RAISE_VARARGS": format_RAISE_VARARGS_older,
}

finalize_opcodes(l)

opcode_extended_fmt = {
    "CALL_FUNCTION": extended_format_CALL_FUNCTION,
    "MAKE_FUNCTION": extended_format_MAKE_FUNCTION_10_27,
    "RAISE_VARARGS": extended_format_RAISE_VARARGS_older,
    "RETURN_VALUE": extended_format_RETURN_VALUE,
}

# These are used outside of this module
findlinestarts = opcode_12.findlinestarts
