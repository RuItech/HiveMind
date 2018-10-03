# Hivemind

[![Build Status](https://travis-ci.com/RuItech/HiveMind.svg?branch=master)](https://travis-ci.com/RuItech/HiveMind)

Hivemind is a Django Restful API created with the purpose of simplifying Club Membership Management.

## Installation

1. Launch Dedicated Virtual Environment for Hivemind (Virtual Environment should run on Python3.6).

    ```code
    virtualenv -p /path/to/python/3 hivemind
    source hivemind/bin/activate
    ```

2. Install [pipenv](https://pipenv.readthedocs.io/en/latest/)

    ```code
    pip install pipenv
    ```

3. Install Package Requirements.

    - DEVELOPERS / CONTRIBUTORS: Install Dev Packages

        ```code
        pipenv install --dev
        ```

    - NORMAL USERS: Install Packages

        ```code
        pipenv install
        ```

4. OPTIONAL: Run Tests

    ```code
    python manage.py test
    ```

## Contibutions

We welcome all contributions to the Repository. If you'd like to contribute to the Repository, read the [Contribution Guide](https://github.com/RuItech/HiveMind/blob/master/CONTRIBUTING.md) for steps on how to go about making your first Contribution.
