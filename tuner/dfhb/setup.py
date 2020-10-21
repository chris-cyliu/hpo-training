# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import setuptools

setuptools.setup(
    name = 'DFHB',
    version = '1.5',
    packages = setuptools.find_packages(exclude=['*test*']),

    python_requires = '>=3.6',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: ',
        'NNI Package :: advisor :: DFHB :: dfhb.dfhb_advisor.DFHB :: dfhb.dfhb_advisor.DFHBClassArgsValidator'
    ],
    install_requires = [
        'ConfigSpace==0.4.7'
    ],
    author = 'DFHB Team',
    author_email = 'nni@microsoft.com',
    description = 'NNI control for Neural Network Intelligence project',
    license = 'MIT',
    url = 'https://github.com/Microsoft/nni'
)
