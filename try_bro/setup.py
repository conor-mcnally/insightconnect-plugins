# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='try_bro-rapid7-plugin',
      version='1.0.2',
      description='Upload PCAP files to an instance of Bro Network Security Monitor for analysis and access to Bro logs',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_try_bro']
      )
