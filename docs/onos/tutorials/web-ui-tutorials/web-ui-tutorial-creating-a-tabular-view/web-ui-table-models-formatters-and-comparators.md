# Web UI - Table Models, Formatters and Comparators

# 

# Overview

Table views in the ONOS Web UI are supported by java code running on the server. See the [Creating a Tabular View](../web-ui-tutorial-creating-a-tabular-view.md) tutorial for details on implementing a table view.

When the [Table Builder Service](../../../guides/developer-guide/appendix-f-web-ui-framework-libraries/web-ui-client-side-framework-libraries/ui-service-tablebuilderservice.md) is used to create the client-side code for a table view, "data request" events will be sent to the server automatically:

* when the table view is first loaded
* every 2 seconds, if auto-refresh is enabled
* every time a column header is clicked (for a new sort order)

The typical structure of a table request handler on the server side can be [seen in the tutorial](../web-ui-tutorial-creating-a-tabular-view.md).

This page will focus on how to customize the default behavior.

# Default Behavior

By default, a [TableModel](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/TableModel.java) instance is created for you, which uses a default [Formatter](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/CellFormatter.java) and default [Comparator](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/CellComparator.java) for each table column.

When a request is made for table data, a list of items is retrieved from the business layer; each item corresponding to a single row in the table. The columns of the table represent attributes of the item. Populating the table model involves iterating over the list of items to add new [TableModel.Row](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/TableModel.java#L238-L287) instances for each one. The [cell(String columnId, Object value)](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/TableModel.java#L248-L252) method is used to associate an object with a particular column for that row. Typical code might look like this:

```
    @Override
    protected void populateTable(TableModel tm, ObjectNode payload) {
        FooService fs = get(FooService.class);
        for (Foo foo : fs.getFoos()) {
            populateRow(tm.addRow(), foo);
        }
    }
 
    private void populateRow(TableModel.Row row, Foo foo) {
        row.cell(ID, foo.id())
                .cell(BAR, foo.bar())
                .cell(BAZ, foo.baz())
                .cell(DESC, foo.description());
    }
```

Once the table model has been constructed and populated, the table rows are sorted (based on selected column and sort direction), and then the model is converted into a JSON representation to be shipped back to the client for displaying in the table view.

## DefaultCellComparator

The default cell comparator compares objects in a column by looking to see if the objects implement the ***Comparable<T>*** interface:

* if they do, delegate to the *compareTo()* method
* if they do not, convert the objects with *toString()* and then compare

This has the advantage of using the natural sort order for objects where the comparable behavior has already been implemented.

## DefaultCellFormatter

The default cell formatter simply invokes the ***toString()*** method on each object, to generate the string representation to be displayed in the table cell.

# Customizing the Behavior

But what if a particular object does not implement ***Comparable<T>***, and sorting by string representation would produce an undesirable ordering? And what if the *toString()* of an object is not appropriate for display? Fortunately, you can override the default behavior and provide your own comparators and formatters.

The ***createTableModel()*** method in your [TableRequestHandler](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/TableRequestHandler.java#L70-L72) should be overridden to look something like this:

```
    @Override
    protected TableModel createTableModel() {
        TableModel tm = super.createTableModel();
        tm.setComparator(BAR, new BarComparator());  // see Comparators section below
        tm.setFormatter(BAZ, new BazFormatter());    // see Formatters section below
        return tm;
    }
```

The *setComparator()* and *setFormatter()* methods are invoked to explicitly set the cell comparator and cell formatter instances to use for objects in the specific columns. All other columns will fall back to the default comparator and formatter.

## Custom Cell Comparator

A custom comparator would be defined something like this, (typically as a private inner class in your table request handler):

```
private static class BarComparator extends AbstractCellComparator {
    @Override
    protected int nonNullCompare(Object o1, Object o2) {
        Bar b1 = (Bar) o1;
        Bar b2 = (Bar) o2;
 
        // get some property from o1
        // compare to the same property from o2
        // return ...
        //   * a negative value, if o1 < o2
        //   * zero, if o1 == o2
        //   * a positive value, if o1 > o2

        return ... ;
    }
}
```

Note that the [AbstractCellComparator](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/cell/AbstractCellComparator.java) takes care of null values and guarantees that ***o1*** and ***o2*** will both be non-null if this method is called.

Note that null values are permitted in the table model cells, and are treated as "smaller" than non-null values.

## Custom Cell Formatter

A custom formatter might be defined something like this, (typically as a private inner class in your table request handler):

```
private static class BazFormatter extends AbstractCellFormatter {
    @Override
    protected String nonNullFormat(Object value) {
        Baz b = (Baz) value;
        return b.toDisplayString();
    }
}
```

Once again, the ***value*** parameter is guaranteed to be non-null, if the [AbstractCellFormatter](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/cell/AbstractCellFormatter.java) invokes this method.

## Out of the Box Formatters

A number of formatters are already defined and available for your use. See the [org.onosproject.ui.table.cell](https://github.com/opennetworkinglab/onos/tree/master/core/api/src/main/java/org/onosproject/ui/table/cell) package:

| Formatter | Value Class | Format Description | Example |
| --- | --- | --- | --- |
| [AppIdFormatter](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/cell/AppIdFormatter.java) | [ApplicationId](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/core/ApplicationId.java) | *"(app-id) : (app-name)"* | "47 : onos-app-uiref" |
| [ConnectPointFormatter](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/cell/ConnectPointFormatter.java) | [ConnectPoint](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/net/ConnectPoint.java) | *"(element ID)/(port)"* | "00:00:00:00:00:00:00:01/5" |
| [EnumFormatter](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/cell/EnumFormatter.java) | Enum<?> | Replaces \_ with space and capitalizes the result | SomeEnum.DO\_SOMETHING → "Do Something" |
| [HexFormatter](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/cell/HexFormatter.java) | Integer | Prefix with "0x" and converted to hex | 20 → "0x14" |
| [HostLocationFormatter](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/cell/HostLocationFormatter.java) | [HostLocation](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/net/HostLocation.java) | *"(device-id)/(port)"* | "00:00:00:00:00:00:00:0e/13" |
| [NumberFormatter](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/cell/NumberFormatter.java)\* | Number | Uses a *java.text.DecimalFormat* with pattern *"#,##0.00000"* | 1234.56 → "1,234.56000" |
| [TimeFormatter](https://github.com/opennetworkinglab/onos/blob/master/core/api/src/main/java/org/onosproject/ui/table/cell/TimeFormatter.java)\*\* | [DateTime](http://www.joda.org/joda-time/apidocs/org/joda/time/DateTime.html) | Uses a [DateTimeFormatter](http://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormatter.html) | new DateTime(2015, 5, 4, 15, 30) → "3:30:00 PM UTC" |

\*Using the *NumberFormatter* no-args constructor; a java.text.NumberFormat instance can also be provided.

\*\*Note that *Locale* and *TimeZone* can also be set on the formatter.
