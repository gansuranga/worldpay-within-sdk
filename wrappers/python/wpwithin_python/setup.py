from setuptools import setup, find_packages

setup(
    name="wpwithin_python",
    version="0.3",
    packages=['wpwithin_python'],
    install_requires=[
        'thriftpy'
    ],
    include_package_data=True
)
