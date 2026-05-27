# Web UI Tutorials - Add Maps Tutorial

# Overview

Maps are used as a background to place the devices in a topology in geographical locations.

Applications can create and inject maps into the topology view.

This tutorial will show you:

* How and where to get map data
* How to extract specfic data from the data set
* Optimise the extracted data for improved performance
* Adding the map to an ONOS Application

# Creating a new map

First of all we need to download a data set. A good resource to get map data from is [Natural Earth Data](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/). For this tutorial we will be using 'Download without boundary lakes'.  
Once the zip file has been downloaded extract it and open up terminal.

**cd to directory**

```
cd ~/Desktop/ne_10m_admin_0_countries_lakes
```

## Extract Map Data

Next we need to get only the countries that we require for the map we're making. For this example we will create a map of South America.  
To do this return to terminal and type:

```
ogr2ogr -f GeoJSON -where "CONTINENT=\"South America\"" south_america.json ne_10m_admin_0_countries_lakes.shp
```

If successful this will create a new file called south\_america.json. This still needs to be a converted to a topojson file before we can add it to the ONOS Application.

## Convert to a topojson file

To convert the newly created json file we need to run another command in terminal

```
topojson -o south_america.topojson --properties name=NAME -- south_america.json
```

If the map you're creating has a complex coastline it may need to be simplified to improve the performance in ONOS.  
To do this we just need to run the above command with an added parameter.

```
topojson -o south_america.topojson --simplify-proportion 0.2 --properties name=NAME -- south_america.json
```

--simplify-proportion is a little bit trial and error in finding the perfect number.

Lastly we need to change the name of the

# Adding the topojson to an application

Add the file to the webapp/data/maps folder.

Now we can add the map to the application. Add the UiTopoMapFactory to the component Class and UiExtenstion.Builder() for the Class.

```
protected final UiTopoMapFactory topoMapFactory =
        () -> ImmutableList.of(
                new UiTopoMap("south_america", "South America", "*south_america", 0.9)
        );

protected UiExtension extension = 
	new UiExtension.Builder(CL, coreViews)
        .messageHandlerFactory(messageHandlerFactory)
        .topoOverlayFactory(topoOverlayFactory)
        .topoMapFactory(topoMapFactory)
        .resourcePath(CORE)
        .build();
```

**UiTopoMap(String id, String description, String path, Double scale);**

Id: is the string found within the topojson file.

```
{
	"type": "Topology",
	"objects": {
		"south_america": {} //This is the Id
	}
} 
```

Description: The name to appear in the maps drop down menu  
Path: The path to the topojson resource ('\*' is a place holder for ~/data/maps)   
Scale: Sets the map scale
