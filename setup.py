from setuptools import setup

import versioneer

with open('README.md') as f:
    readme = f.read()

setup(
    name='blindspin',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    long_description=readme,
    packages=['blindspin'],
    url='https://github.com/kennethreitz/blindspin',
    license='MIT',
    author='Kennethreitz',
    author_email='me@kennethreitz.org',
    description='Braille Spinner for Click',
    extras_require={
        'test': [
            'click',
            'pytest',
            'six',
        ]
    }
)

