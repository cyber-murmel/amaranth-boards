from os.path import dirname
from pkgutil import iter_modules
from importlib import import_module
from jinja2 import Template, Environment, FileSystemLoader
from pathlib import Path
import black

module_names = [
    name for _, name, _ in iter_modules(["./amaranth_boards"])
]
modules = {name: import_module(f"amaranth_boards.{name}") for name in module_names}
platforms = {
    name: [item for item in module.__all__ if item.endswith("Platform")]
    for name, module in modules.items()
    if hasattr(module, "__all__")
}

_template = Template(
    """
# This file has been auto-generated with 'gen_util_platform.py'

{% for module_name, platform_names in platforms.items() %}
from ..{{ module_name }} import {{ platform_names|join(', ') }}
{%- endfor %}

__all__ = [ "get_platform_names", "get_platform_by_name", ]

_ALL_PLATFORM_NAMES = [
    {%- for module_name, platform_names in platforms.items() %}
    {%- for platform_name in platform_names %}
    "{{ platform_name[:-1 * ("Platform"|length)] }}",
    {%- endfor %}
    {%- endfor %}
]

def get_platform_names():
    return _ALL_PLATFORM_NAMES

def get_platform_by_name(name):
    {%- for module_name, platform_names in platforms.items() %}
    {%- for platform_name in platform_names %}
    if "{{ platform_name[:-1 * ("Platform"|length)] }}" == name:
        return {{ platform_name }}
    {%- endfor %}
    {%- endfor %}
"""
)

path = "amaranth_boards/utils/platform.py"

with open(path, "w") as output_file:
    output_file.write(_template.render(platforms=platforms))

black.format_file_in_place(
    Path(path), fast=False, mode=black.FileMode(), write_back=black.WriteBack.YES
)
