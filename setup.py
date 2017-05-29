from setuptools import setup, find_packages
import os

setup(
    name = "pxmake",
    version = "2.1.5.dev0",
    packages = find_packages(),
    install_requires = ["lupa>=1.4"],
    author = "TitanSnow",
    author_email = "tttnns1024@gmail.com",
    url = "https://github.com/TitanSnow/pxmake",
    description = "xmake implement on python focuses on reuse python's library and API compatibility",
    license = "Apache 2.0",
    python_requires = ">=3.3",
    entry_points = {
        "console_scripts": [
            "pxmake = xmmachine:main"
        ]
    },
    data_files = [(root, [os.path.join(root, f) for f in files]) for root, dirs, files in os.walk("xmake")],
    zip_safe = False
)
