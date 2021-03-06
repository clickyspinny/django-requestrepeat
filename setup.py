import os
from setuptools import setup, find_packages

#with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
#    README = readme.read()

# allow setup.py to be run from any path
#os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-requestrepeat',
    version='0.3',
    packages = find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A django app that repeats one http POST into several.',
    long_description=README,
    url='https://github.com/clickyspinny/django-requestrepeat/tree/master/requestrepeat',
    author='Oceana Technologies',
    author_email='ben@oceanatech.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)