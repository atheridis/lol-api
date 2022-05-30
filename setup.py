from setuptools import find_packages, setup

setup(
    name="lol_api",
    version="0.1.1",
    url="https://github.com/Atheridis/lol-api.git",
    author="Georgios Atheridis",
    authoer_email="atheridis@tutamail.com",
    description="A simple League of Legends API wrapper",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.9",
)
