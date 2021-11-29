

 
<div align="center">
  <a href="https://github.com/CNES/shareloc"><img src="docs/source/images/shareloc_picto.svg" alt="Shareloc" title="Shareloc"  width="20%"></a>

<h4>ShareLoc an API dedicated to localization functions</h4>

[![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](CONTRIBUTING.md)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0/)
[![Documentation](https://readthedocs.org/projects/shareloc/badge/?version=latest)](https://shareloc.readthedocs.io/?badge=latest)

<p>
  <a href="#overview">Overview</a> .
  <a href="#why-shareloc">Why Shareloc</a> .
  <a href="#quick-start">Quick Start</a> .
  <a href="#main-functions">Main Functions</a> .
  <a href="#documentation">Documentation</a> .
  <a href="#contribution">Contribution</a> .
</p>
</div>

## Overview

Shareloc is an open source satellite geolocation library. 
It performs image (row, col) to geographic (lat, lon, h) or projected (x, y, h) mapping using RPC model or direct location grids, and reverse (gounrd to sensor mapping). 
This mapping is done at constant elevation (ellipsoïdal Earth model) or byline of sight (LOS) instersection with DEM. 
These functionnalities are a key component when projecting an image on ground.

## Why Shareloc

Shareloc development has been motivated by the need of a full python component for CNES studies, and the need of an underlying geomrical component for <a href="https://github.com/CNES/cars">CARS</a>    


## Quick start

### installation

Shareloc can be installed in a  [virtualenv](https://docs.python.org/3/library/venv) using the following commands:

```
git clone https://gitlab.cnes.fr/cars/shareloc.git
cd shareloc
make install
source venv/bin/activate # to go in installed dev environment
```

Dependencies : **git**, **make**

### example

Shareloc is designed as an API. Please refer the [notebook directory](notebooks) for examples. 


## Main Functions

* Direct/inverse localisation on ellipsoid
* Direct localisation on 2.5D DEM
* Line of sight triangulation
* Rectification grid creation
* Rectification grid interpolation

## Documentation

See [Shareloc generation README](docs/README.md) to rebuild documentation.

## Contribution

To do a bug report or a contribution, see the [**Contribution Guide**](CONTRIBUTING.md).  
For project evolution, see [**Changelog**](CHANGELOG.md)