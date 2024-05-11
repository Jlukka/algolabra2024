# algolabra2024
# Documentation
[Project specification](https://github.com/Jlukka/algolabra2024/blob/main/documentation/specification.md)
[Implementation](https://github.com/Jlukka/algolabra2024/blob/main/documentation/implementation.md)
[Testing](https://github.com/Jlukka/algolabra2024/blob/main/documentation/testing.md)
[User instructions](https://github.com/Jlukka/algolabra2024/blob/main/documentation/instructions.md)


# Weekly reports

# Usage

## Installing

Clone the repository with following command

> git clone https://github.com/Jlukka/algolabra2024.git

Change directory to the root directory and run following commands to install dependencies

> poetry install

## Terminal commands

To launch the program use following command

> poetry run invoke start

To run the tests associated with the code use following command

> poetry run invoke test

To generate a coverage report of the tests use following command

> poetry run invoke coverage

To create html version of the coverage report use following command

> poetry run invoke coverage-report

To generate a pylint report on the code run following command

> poetry run invoke lint

To automatically format the code with autopep8 run the following command

> poetry run invoke format
