import setuptools

long_desc = open("README.md").read()
liscense = open("LICENSE").read()
required = ["python-dateutil"]

setuptools.setup(
    name="python-PyFrame",
    version="1.0.1",
    author="LilTOJustice",
    author_email="muianick4@gmail.com",
    license=liscense,
    description="A simple python API wrapper for api.warframestat.us",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/LilTOJustice/PyFrame",
    install_requires=required,
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)