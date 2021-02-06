# CovidAnalysis
![CI](https://github.com/maldins46/CovidAnalysis/workflows/CI/badge.svg)
![CD](https://github.com/maldins46/CovidAnalysis/workflows/CD/badge.svg)
![Auto update data](https://github.com/maldins46/CovidAnalysis/workflows/Auto%20update%20data/badge.svg)
![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=alert_status)
![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=sqale_rating)
![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=sqale_index)
![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=maldins46_CovidAnalysis&metric=ncloc)

Python module used to extract relevant information from Italian Government Covid Open Data. The repository uses [Open Data from the Italian Government](https://github.com/pcm-dpc/COVID-19) as a Git Submodule. As such, a plain clone does not initialize submodules. You have to clone the project this way:

```
git clone --recurse-submodules https://github.com/maldins46/CovidAnalysis.git 
```
Besides performing the clone, also recursively initialize submodules. Also, the submodule have to be updated manually periodically, by using

```
git submodule update --remote --recursive
```

Charts are automatically updated each day. Consult [the repository website](https://maldins46.github.io/CovidAnalysis) for a neat live COVID-19 dashboard, comprising the latest version of the charts. You can also download all the available charts in PNG format [from here](https://github.com/maldins46/CovidAnalysis/releases/latest).
