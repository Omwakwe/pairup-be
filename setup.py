from setuptools import find_packages, setup
setup(
    name="pair", packages=find_packages(exclude=['tests'],),# Include all the python modules except `tests`.
    version='0.0.1',
    description='My custom package tested with tox',
    long_description='A long description of my custom package tested with tox',
    author='remmi',
    author_email='remmi@remmi.com',
    install_requires=[
        'Django>=3.0.8',
        'djangorestframework>=3.6.0',
        # Additional requirements, or parse the requirements file and add it here
    ],
    classifiers=[
        'Programming Language :: Python',
    ],
    entry_points={
        'pytest11': [
            'tox_tested_package = tox_tested_package.fixtures'
        ]
    },
)