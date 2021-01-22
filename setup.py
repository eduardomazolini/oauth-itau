# coding: utf-8

"""
    oAuth

    oAuth para produção  # noqa: E501

    OpenAPI spec version: 1.40.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "oauth-itau"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    
REQUIRES.append("aiohttp")

setup(
    name=NAME,
    version=VERSION,
    description="oAuth",
    author_email="",
    url="",
    keywords=["Swagger", "oAuth"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    oAuth para produção  # noqa: E501
    """
)
