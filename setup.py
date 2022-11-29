import os

from setuptools import find_packages
from setuptools import setup


def local_file(path: str) -> str:
    return os.path.relpath(
        os.path.join(
            os.path.dirname(__file__),
            path,
        ),
    )


with open(local_file('README.md')) as f:
    long_description = f.read()


with open(local_file('gibberish_detector_tr/__version__.py')) as f:
    VERSION = ''    # make linters happy
    exec(f.read())


setup(
    name='gibberish_detector_tr',
    packages=find_packages(exclude=(['test*', 'tmp*'])),
    version=VERSION,
    description='Detects gibberish strings with Turkish character.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='Aaron Loo <admin@aaronloo.com>',
    url='https://github.com/zeynepgulhanuslu/gibberish-detector-turkish',
    entry_points={
        'console_scripts': [
            'gibberish-detector-tr = gibberish_detector_tr.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: General',
        'Topic :: Utilities',
    ],
)
