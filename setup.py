import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hivemind",
    version="0.0.1",
    author="RU-ITech",
    maintainer="Davis Raymond Muro",
    maintainer_email="davisraymondmuro@gmail.com",
    description="Django REST API for RU-ITECH Software Stack",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RuItech/HiveMind",
    packages=setuptools.find_packages(),
    install_requires=[
        'Django >= 2.0',
        'djangorestframework',
        'django-filter',
        'psycopg2'
        ],
    classifiers=[
        "Programming Language :: Python :: 3", "Framework :: Django :: 2"
    ],
)
