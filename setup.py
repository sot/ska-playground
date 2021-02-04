from setuptools import setup

try:
    from testr.setup_helper import cmdclass
except ImportError:
    cmdclass = {}

setup(name='play',
      author='Chandra operations',
      description='Playground for Ska',
      use_scm_version=True,
      setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
      zip_safe=False,
      packages=['play'],
      tests_require=['pytest'],
      cmdclass=cmdclass,
      )
