# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="servicenow-rapid7-plugin",
      version="3.1.1",
      description="ServiceNow is a tool for managing incidents and configuration management. Using the ServiceNow plugin for Rapid7 InsightConnect, users can manage all aspects of incidents including creation, search, updates, as well as monitor them for changes",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_servicenow']
      )
