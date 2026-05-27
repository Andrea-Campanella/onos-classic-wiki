# XOS CORD Views

# Subscriber View:

<http://10.254.1.22:8000/admin/dashboard/cord/>

Currently shows a list of subscribers (note: this list may be empty, if no subscribers have been created by ONOS). Click a subscriber id to view the settings for that subscriber.

The only editable fields are three checkboxes, for Firewall, URL Filter, and CDN respectively, and two text areas for configuring the Firewall rules and URL Filter.

The Firewall Rule and URL Filter text areas default to some plausible-looking text, This text isn't used for anything at the moment, so don't worry about the syntax. The intent is to put something in there that the vCPE image will understand.

# Operator View:

<http://10.254.1.22:8000/serviceGrid/>

This is a list of Icons for vOLT, vCPE, and vBNG. These icons currently bring up very generic service description pages.
