# GUI Source Directory Structure

This page captures notes on the directory structure of the GUI client-side code.

## Structure Overview

The following illustrates the directory structure:

```
webapp  
 +-- app  
 | +-- fw  
 | | +-- layer  
 | | +-- mast  
 | | +-- nav  
 | | +-- remote  
 | | +-- svg  
 | | +-- util  
 | | +-- widget  
 | |   
 | +-- view  
 |     +-- device  
 |     +-- sample  
 |     +-- topo  
 |  
 +-- data  
 |   +-- img  
 |   +-- map  
 |  
 +-- tests  
 |   +-- app  
 |   |   +-- fw  
 |   |   |   +...  
 |   |   +-- view  
 |   |   |   +...  
 |   |   +...  
 |   +-- e2e  
 |  
 +-- tp  
 |  
 +-- WEB-INF
```

```
 
```

## app directory

The app directory contains subdirectories

* **fw** for framework related code
  + That is, features/functions shared by all "views"
* **view** for view related code
  + That is, a subdirectory for each "view" implemented
  + The name of the subdirectory is the "id" of the view

## app / fw directory

The **fw** subdirectory contains the following subdirectories, providing a number of categories of functionality:

* **util**
  + General functions
  + Key Handler
  + Theme Service
  + Alert Service
* **svg**  
  + Glyph Service
  + Icon Service
  + GeoDataService
  + Map Service
  + Zoom Service
  + SVG Utilities Service
* **layer**
  + Flash Service (transient messages)
  + Panel Service (floating panels)
  + Quick Help Service (key bindings, mouse gestures)
  + Veil Service (loss of server connection)
* **widget**
  + Button Service (normal, toggle, radiobuttonset)
  + Toolbar Service
  + Table Service
  + Tooltip Service
* **remote**
  + Login Service
  + Web Socket Service
  + REST Service
* **mast**
  + Masthead functions
* **nav**
  + Navigation Service

## app / view directory

The **view** subdirectory contains a subdirectory for each implemented view.

For example, **topo** contains the code implementing the *Topology View*.

## data directory

The **data** directory contains subdirectories for static data files

* **img** - images (*.png* etc.)
* **map** - GeoJSON map data
* ...

## tests directory

The **tests** directory contains karma / jasmine unit tests and end-to-end (scenario) tests for javascript modules.

## tp directory

The **tp** directory contains third-party code, such as *AngularJS, D3, jquery, topojson*, etc.

## WEB-INF directory

The **WEB-INF** directory contains the *web.xml* file for configuring the web bundle.
