import os
from setuptools import setup, find_packages
import subscribe


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-subscribe",
    version=subscribe.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, subsription, generic',
    author='Martin Brochhaus',
    author_email='mbrochh@gmail.com',
    url="https://github.com/bitmazk/django-subscribe",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django',
    ],
)
