# CovidAnalysis
![CI](https://github.com/maldins46/CovidAnalysis/workflows/CI/badge.svg)
![CD](https://github.com/maldins46/CovidAnalysis/workflows/CD/badge.svg)
![Auto update data](https://github.com/maldins46/CovidAnalysis/workflows/Auto%20update%20data/badge.svg)
![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=alert_status)
![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=sqale_rating)
![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=sqale_index)
![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=ncloc)

A Python module used to extract relevant information from Italian Open Data, toghether with a neat Angular client used to show the results. The repository uses [Open Data from the Italian Protezione Civile](https://github.com/pcm-dpc/COVID-19), and the [open data about Italian Vacination Plan](https://github.com/italia/covid19-opendata-vaccini). Also, [geojson-taly](https://github.com/openpolis/geojson-italy) is used in order to generate the geographical charts.

## How to use the Python module

The `/chart-generation` folder contains the Python code for the generation of charts and summary tables. A Python interpreter in order to try it (code is tested with Python 3.8). Then, install the dependencies shown into the file `requirements.txt`, executing in the project root the following lines:

```bash
python -m pip install virtualenv
python -m virtualenv --python=python venv
./venv/bin/pip install -r requirements.txt --upgrade
```

These commands will install all the required dependencies in a virtual environment inside the project root. You can use your preferred Python interpreter (for example, on my MacBook i use `python3` instead of Python, as `python` points to the default interpreter, 2.7).

To run chart generation or test, make sure to enable the environement first by terminal, with:

```bash
 source venv/bin/activate
```

Use the following command to generate all the assets, like charts in PNG and summary tables in JSON. Assets will be saved in the project subfolder `/charts`.

```bash
python ./chart-generation/generate_covid_charts.py
python ./chart-generation/generate_vaccine_charts.py
```

You can also run python tests using:

```bash
python -m pytest ./chart-generation/test_chart_generation.py
``` 

## How to use the Angular client

The `/client` folder contains an Angular client used to show the results of the Python elaborations. These elaborations are triggered twice a day with GitHub Actions, and the assets are automatically saved into the GitHub Pages web space. This space (under the branch `gh-pages`) contains also the deployed and minified Angular client delivered at each push on `main` branch. To try the Angular client locally, `Node` and `angular-cli` are needed. Run the following command to execute a local Angular server instance:

```bash
ng serve
```

## The repo website

Consult [the repository website](https://maldins46.github.io/CovidAnalysis) for a neat live COVID-19 dashboard, comprising the latest version of the charts.
