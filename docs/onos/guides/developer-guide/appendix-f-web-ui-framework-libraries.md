# Appendix F: Web UI Framework Libraries

In the development of the ONOS Web GUI, a number of useful libraries and helper classes were created with the idea that these should be used both in the core codebase as well as re-used by ONOS applications looking to [add their own content](../../tutorials/web-ui-tutorials.md) to the GUI.

On the client-side we have a number of [framework libraries](appendix-f-web-ui-framework-libraries/web-ui-client-side-framework-libraries.md), implemented as AngularJS factories, providing:

* APIs to create "panels" and display "quick-help"
* APIs to navigate to other "views"
* APIs to access the REST and WebSocket services
* various SVG-related functions, such as registering custom "glyphs", using icons
* APIs to create widgets (tables, toolbars, buttons, tooltips, etc.)
* various miscellaneous functions (key binding, user preference persistence, general utility functions, etc.)

On the server-side, a [number of Java classes](appendix-f-web-ui-framework-libraries/web-ui-server-side-helper-classes.md) are provided to simplify the task of ONOS application business logic shipping data back to the GUI:

* Message handlers / Request handlers (processing events from the GUI)
* Table models, cell comparators and formatters (constructing table view data)
* Link maps, topology highlights, node selection models, property panel models (manipulating data for the Topology View)
