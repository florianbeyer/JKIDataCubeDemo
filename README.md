# WC(P)S demo of JKI Datacubes

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14215012.svg)](https://doi.org/10.5281/zenodo.14215012) [![Version](https://img.shields.io/badge/version-1.6.1-blue)](https://github.com/florianbeyer/JKIDataCubeDemo/releases/tag/V1.6.1) [![Findable Accessible Interoperable Reusable](https://img.shields.io/badge/research%20code%20mangement-FAIR-green)](https://doi.org/10.1038/sdata.2016.18)


## Introduction

This repository demonstrates, how to query the Data Cubes provided by the [JKI](https://www.julius-kuehn.de/en/) using Python and OGC web services WCS and WCPS.  
The JKI datacube uses rasdaman enterprise in the background. The software is a database software specially designed for multidimensional large-scale raster data time series, which provides OGC web services (WMS, WCS and WCPS) as an interface.

All Datacubes have a spatial coverage of the area of Germany and come with spatial resolutions between 10 m and 1 km.

### definitions
**Data Cubes** are a new paradigm for storing and analyzing geo raster (e.g. Earth observation) data. Datacubes, which are multi-dimensional arrays (often spatiotemporal), offer significant advantages over traditional data storage methods by simplifying access to and analysis of large datasets.  

**WCS** [OGC Web Coverage Service](https://www.ogc.org/de/publications/standard/wcs/) is a standard defined by the Open Geospatial Consortium (OGC) for serving geospatial data as coverages, which are digital representations of spatially continuous phenomena (e.g., satellite imagery, climate models, or terrain data). WCS provides interoperable access to such data, allowing users to query, extract, and retrieve data in formats suitable for analysis and visualization.  

**WCPS**   [OGC Web Coverage Processing Service](https://www.ogc.org/publications/standard/wcps/) is an extension of the OGC Web Coverage Service (WCS) standard that enables advanced querying and processing of geospatial coverages through a declarative query language. It allows users to perform complex operations—such as filtering, subsetting, arithmetic, or spatial-temporal analysis—directly on large coverage datasets, without needing to download them first.  

## Features

The Juypter notebook demonstrates the following:

- How to access and and request multi-dimensional raster time series as data cubes
- How to get information of available Datcubes and their metadata
- Datacube 1 PHASE data: entry dates of phenological stages
- Datecube 2 EO data: earth observation data from Sentinel-2 are requested and a vegeation index called SAVi is calculated
- Datacube 3 Weather: daily precipitation sums (in mm) are requested
- A joint plot of all received data is printed
- verything is shown using a winter wheat field in Germany 2020.


## Repository Structure

```plaintext
├── data/                          # example geo vector files
│   ├── bavaria.geojson            # example field in Bavaria (Germany)
│   ├── lower_saxony.geojson       # example field in Lower Saxony (Germany)
│   └── winterwheat2020.geojson    # winter wheat field from 2020 in Lower Saxony (Germany)
├── functions/                     # required functions used in juypter notebook
│   ├── func_datacube_DWD.py       # main function to query precipitation data cube
│   ├── func_datacube_PHASE.py     # main function to query PHASE data cube
│   ├── func_datacube_S2_WCPS.py   # main function to query Sentinel-2 data cube
│   └── func_misc.py               # additional functions used in the notebook
├── CITATION.cff                   # plain text files with human- and machine-readable citation information for software
├── codemeta.json                  # minimal metadata schema for science software and code
├── credentials.py                 # credential files to get acces to restricted data cubes
├── DemoPhaseWCS.ipynb             # jupyter notebook and main file for demonstration
├── requirements.txt               # required python packages
├── DATA_LICENSE.txt               # license file for data files
├── LICENSE                        # license file for code
├── README.md                      # project description
```

### credentials.py

If you have access to restricted data cubes (such as the Sentinel-2 datacube, showed in the Jupyter Notebook), it is recommended add your credentials in the `credentials.py` **on your local machine**.

### codemeta.json, CITATION.cff & licensing

The Repository is also used to show best practices on "How to publish scientific code?" in order to fulfil the [FAIR principles of Wilkinson et al. 2016](https://doi.org/10.1038/sdata.2016.18)
The FAIR principles emphasize making data Findable, Accessible, Interoperable, and Reusable, ensuring its long-term value for research and collaboration.

Therefore the repository is also published on zenodo as described [HERE]()

* [codemeta.json](https://codemeta.github.io/) --> metadata schema for science software and code
* [CITATION.cff](https://citation-file-format.github.io/)  --> citation information for software


## Python3 settings

* script was developed with python 3.12.1
* geopandas, rasterio (geodata packages)
* xmltodict, tqdm
* ipyleaflet (for interactive map vizualisation in Juypter Notebook)
* all packages: see `├── requirements.txt` for our python environment

Conda Info (selected):
```
          conda version : 24.1.2
    conda-build version : 24.1.1
         python version : 3.11.5.final.0
                 solver : libmamba (default)
       virtual packages : __archspec=1=haswell
                          __conda=24.1.2=0
                          __glibc=2.35=0
                          __linux=5.15.0=0
                          __unix=0=0
           channel URLs : https://repo.anaconda.com/pkgs/main/linux-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/linux-64
                          https://repo.anaconda.com/pkgs/r/noarch
               platform : linux-64
             user-agent : conda/24.1.2 requests/2.31.0 CPython/3.11.5 Linux/5.15.0-89-generic ubuntu/22.04.3 glibc/2.35 solver/libmamba conda-libmamba-solver/24.1.0 libmambapy/1.5.6 aau/0.4.2
                UID:GID : 1002:1003
             netrc file : None
           offline mode : False
```


## Project supported and granted

<a href="https://fairagro.net/en/">
  <img src="https://fairagro.net/wp-content/uploads/2023/12/Fairagro_Logo_mittelachsig_Verlauf.png" alt="FAIRagro project" width="300">
</a>  

[www.fairagro.net](https://fairagro.net/en/)


![Funded by DFG](https://fairagro.net/en/wp-content/uploads/sites/3/2024/03/dfg_logo_schriftzug_blau_foerderung_en.1-300x111.jpg) ![Part of NFDI](https://fairagro.net/en/wp-content/uploads/sites/3/2023/10/nfdi_4c_Wortmarke_Zusatz_quer-Cooperation-01-300x147.png)


## Licensing

This repository contains both code and data. They are licensed separately:

- **Code** are every files ending with *.py and *.ipynb: Licensed under the MIT License. See [LICENSE](LICENSE) for details.
- **Data** are all other files: Licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). See [DATA_LICENSE.txt](DATA_LICENSE.txt) for details.