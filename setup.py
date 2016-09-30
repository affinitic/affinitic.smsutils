# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.2'

long_description = (open('README.rst').read())

setup(name='affinitic.smsutils',
      version=version,
      description="send sms",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Buildout",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Topic :: Software Development :: Code Generators",
      ],
      keywords='sms affinitic',
      author='Affinitic',
      author_email='info@affinitic.be',
      url='https://github.com/affinitic/affinitic.smsutils',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['affinitic'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      extras_require=dict(),
      entry_points="""
      [console_scripts]
      send_sms = affinitic.smsutils.send_sms:main
      receive_sms = affinitic.smsutils.receive_sms:main
      """,

      )
