from setuptools import setup, find_packages
import os

version = '0.9'

setup(name='uwosh.double_blind_review',
      version=version,
      description="Double Blind Review Workflows",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='review, double-blind, double-blind review, proposals, dropbox',
      author='Jonathan Gutow',
      author_email='gutow@uwosh.edu',
      url='https://github.com/gutow/uwosh.double_blind_review',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uwosh'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok, relations]',
          'plone.namedfile [blobs]',
          # -*- Extra requirements: -*-
          'z3c.jbot',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
#      setup_requires=["PasteScript"],
#      paster_plugins = ["ZopeSkel"],

      )
