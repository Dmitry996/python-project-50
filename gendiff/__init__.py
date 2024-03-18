from .generate_diff import generate_diff
from .cli import parser
from .parser import open_file
from .diff_generator import diff_generator

__all__ = (
    'generate_diff',
    'parser',
    'open_file',
    'diff_generator',
)
