import setuptools

with open("README.md") as file:
    long_description = file.read()

setuptools.setup(
    name="latex-render",
    version="0.0.1",
    author="Alve Svarén",
    author_email="alve@hotmail.se",
    description="A simple library and cli to render latex code to images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alvesvaren/mccli",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
