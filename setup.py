# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='toutatis-updated',
    version="1.32",
    packages=find_packages(),
    author="DogeDev010",
    install_requires=["argparse","requests","phonenumbers","pycountry"],
    description="It is a tool written to retrieve private information such as Phone Number, Mail Address, ID on Instagram accounts via API.",
    long_description="It is a tool written to retrieve private information such as Phone Number, Mail Address, ID on Instagram accounts via API.",
    include_package_data=True,
    url='https://github.com/DogeDev010/toutatis-updated',
    entry_points = {'console_scripts': ['toutatis = toutatis.core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
