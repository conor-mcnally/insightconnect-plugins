# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="ibm_qradar-rapid7-plugin",
      version="1.0.0",
      description="IBM QRadar reduces billions of events and flows into a manageable number of actionable offenses that are prioritized by their impact on your business operations. This plugin allows you to use IBM QRadar to orchestrate and automate Ariel search queries and automate offense management",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/icon_ibm_qradar']
      )