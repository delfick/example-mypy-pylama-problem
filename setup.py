from confusion import VERSION

from setuptools import setup, find_packages

# fmt: off

setup(
      name = 'confusion'
    , version = VERSION
    , packages = find_packages(include="confusion.*", exclude=["tests*"])
    , package_data={'confusion': ['py.typed']}
    )

# fmt: on
