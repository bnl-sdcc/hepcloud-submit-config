#
# Basic setup file for pip install
#

import os
import sys
from setuptools import setup, find_packages

#example_files = ['examples/%s' %file for file in os.listdir('examples') if os.path.isfile('examples/%s' %file) ]

setup(
    name="hepcloud-submit-config",
    version='0.90',
    description='Python Libraries for BNL HEPCloud usage.',
    long_description='''Python Libraries for BNL HEPCloud usage.''',
    license='BSD',
    author='John Hover',
    author_email='jhover@bnl.gov',
    url='https://github.com/bnl-sdcc/hepcloud-submit-config',
    #python_requires='>=2.7',
    packages=[ 'hepcloud',
               ],
    install_requires=[],
    
    data_files=[ ('/etc/condor/config.d/', ['etc/97_projectname.config']),
                 ('/etc/condor/', ['etc/mkprojectnamemapfile.conf']),
                 ('/etc/cron.d/', ['etc/mkprojectnamemapfile.cron']),              
        ],
    )


