random_csv_generator
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy|
|code_climate_maintainability| |pip| |downloads|

Tool for rendering plausible real-life csv data.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install random_csv_generator

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime
get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

Tool for rendering plausible real-life csv data.

Usage examples
-----------------------------------------------
Currently the generated CSV contains FAKE data about italian
persons and some FAKE financial informations.

.. code:: python

    from random_csv_generator image random_csv

    df = random_csv(300) # To generate a CSV with 300 rows


+-----------+---------------+-----------+-------------------------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+---------------------------+----------------+-------+----------------------+-----------------+------------------+---------------+---------------+
| region    | province      | surname   | name                    | sex   | birth_municipality   | birth_province   | birth_region   |   birth_cap | birth_province_code   | birthdate   | address                   |   house_number |   cap | municipality         | province_code   | codice_fiscale   | total_debit   | payed_debit   |
+===========+===============+===========+=========================+=======+======================+==================+================+=============+=======================+=============+===========================+================+=======+======================+=================+==================+===============+===============+
| Toscana   | Siena         | Veronese  | Giorgio                 | M     | Castelnovo Bariano   | Rovigo           | Veneto         |       45030 | RO                    | 2000-12-08  | Via Traversa Stazione     |             15 | 53034 | Colle Di Val D'elsa  | SI              | VRNGRG00T08C215S | 15.347,00 €   | 1.763,00 €    |
+-----------+---------------+-----------+-------------------------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+---------------------------+----------------+-------+----------------------+-----------------+------------------+---------------+---------------+
| Lombardia | Brescia       | Barsotti  | Laura                   | F     | Santa Luce           | Pisa             | Toscana        |       56040 | PI                    | 1981-04-16  | Via Martiri Della Libertà |            291 | 25030 | Roncadelle           | BS              | BRSLRA81D56I217W | 24.015,00 €   | 12.250,00 €   |
+-----------+---------------+-----------+-------------------------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+---------------------------+----------------+-------+----------------------+-----------------+------------------+---------------+---------------+
| Calabria  | Vibo Valentia | Landi     | Edoardo                 | M     | Certaldo             | Firenze          | Toscana        |       50052 | FI                    | 1999-07-31  | Corso Umberto I           |            250 | 89822 | Serra San Bruno      | VV              | LNDDRD99L31C540R | 73.788,00 €   | 70.486,00 €   |
+-----------+---------------+-----------+-------------------------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+---------------------------+----------------+-------+----------------------+-----------------+------------------+---------------+---------------+
| Lazio     | Frosinone     | Rossi     | Giuseppe Oreste Massimo | M     | Baricella            | Bologna          | Emilia Romagna |       40052 | BO                    | 1953-09-10  | Borgo San Nicola          |            114 |  3020 | Pastena              | FR              | RSSGPP53P10A665N | 17.640,00 €   | 15.303,00 €   |
+-----------+---------------+-----------+-------------------------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+---------------------------+----------------+-------+----------------------+-----------------+------------------+---------------+---------------+
| Umbria    | Perugia       | Piras     | Maurizio                | M     | Sadali               | Cagliari         | Sardegna       |       08030 | CA                    | 1957-06-14  | Piazza D. Alighieri       |              3 |  6061 | Castiglione Del Lago | PG              | PRSMRZ57H14H659Q | 11.106,00 €   | 10.210,00 €   |
+-----------+---------------+-----------+-------------------------+-------+----------------------+------------------+----------------+-------------+-----------------------+-------------+---------------------------+----------------+-------+----------------------+-----------------+------------------+---------------+---------------+

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/random_csv_generator.png
   :target: https://travis-ci.org/LucaCappelletti94/random_csv_generator
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_random_csv_generator&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_random_csv_generator
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_random_csv_generator&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_random_csv_generator
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_random_csv_generator&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_random_csv_generator
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/random_csv_generator/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/random_csv_generator?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/random-csv-generator.svg
    :target: https://badge.fury.io/py/random-csv-generator
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/random-csv-generator
    :target: https://pepy.tech/badge/random-csv-generator
    :alt: Pypi total project downloads

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/d158345b4c244c5f9937bf8630309f85
    :target: https://www.codacy.com/manual/LucaCappelletti94/random_csv_generator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/random_csv_generator&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/c42969b9aebeb260cdbf/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/random_csv_generator/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/c42969b9aebeb260cdbf/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/random_csv_generator/test_coverage
    :alt: Code Climate Coverate
