import platform
import sys

from setuptools import setup, Extension
import setuptools_scm  # noqa  Ensure it’s installed

# Check for 64-bit
if sys.maxsize > 2**32 and (
    platform.machine() == "x86_64" or platform.machine() == "AMD64"
):
    DEFINE_MACROS = [("USE_SSE2", None)]
else:
    DEFINE_MACROS = []

setup(
    ext_modules=[
        Extension(
            "dnaio._core", sources=["src/dnaio/_core.pyx"], define_macros=DEFINE_MACROS
        ),
    ],
)
