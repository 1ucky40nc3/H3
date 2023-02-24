from setuptools import (
    setup,
    find_packages
)


setup(
    name="h3",
    version="0.0.1",
    author="Tri Dao*, Daniel Y. Fu*, Khaled K. Saab, Armin W. Thomas, Atri Rudra, Christopher Ré",
    description="Hungry Hungry Hippos (H3)",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="Apache License Version 2.0, January 2004",
    url="https://github.com/HazyResearch/H3",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
)
