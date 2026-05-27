# UI Service - Table Directives

# Table Directives

Table Directives are an extension of the [Widget module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `table.js`. It provides [Angular directives](https://docs.angularjs.org/guide/directive) for [Tabular View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-tabular-view.md) features. To use these directives, see the documentation on [Angular directives](https://docs.angularjs.org/guide/directive).

## Directives

| Name | Other Attributes | Summary |
| --- | --- | --- |
| `onos-table-resize` | col-width | Resizes the table to fit the available window space and sets table columns to custom widths. |
| `onos-sortable-header` | colId, sortable | Sorts the table contents by the header and direction indicated on click. |
| `onos-flash-changes` | id-prop, ng-repeat-complete, row-id | Flashes the table rows whose information is new or updated. |

> Note that all of these directives can be used with each other. All of the Tabular Views use all three directives in tandem.

# Directive Usage

## onos-table-resize

Resizes the table to fit the available window space and sets table columns to custom widths.

### Example Usage

This is the minimum HTML to get this directive to work.

```
<div class="summary-list" onos-table-resize>
	<div class="table-header">
		<table>
			<tr>
				<td col-width="50px">ID</td>
				<td class="table-icon">Foo</td>
				<td>Bar</td>
				<td col-width="350px">Baz</td>
			</tr>
		</table>
	</div>
	<div class="table-body">
		<table>
			<tr ng-repeat="item in tableData track by $index">
				<td>{{item.id}}</td>
				<td>{{item.foo}}</td>
				<td>{{item.bar}}</td>
				<td>{{item.baz}}</td>
			</tr>
		</table>
	</div>
</div>
```

Also, you must include these styles in your CSS.

```
div.summary-list {
    border-spacing: 0;
}
 
div.summary-list table {
    border-collapse: collapse;
    table-layout: fixed;
    empty-cells: show;
    margin: 0;
}

div.summary-list div.table-body {
    overflow-y: scroll;
}
```

| Requirements | Other Attributes | Summary |
| --- | --- | --- |
| * `onos-table-resize` has to be on a <div> that has two child <div>s * the two child <div>s are classed "`table-header`" and "`table-body`" * the child <div>s each have <table> and <tr> elements inside of them * *ALL elements within the <tr> must be **<td>** elements NOT <th>* | `col-width` - (optional) the value for this attribute should be a number in pixels of how wide you would like this column to be. Make sure you include the "px".  `class="table-icon"` - (optional) if this column will be holding an icon, you can class the column as `table-icon`, which will adjust the width of the column to the default size for icons  *\*\* If these attributes are not included, then the columns will be the default calculated size. \*\** | This directive looks for the "table-header" and "table-body" classes, selects all the <td> elements, and sizes them so that table fits within the window. |

## onos-sortable-header

Sorts the table contents by the header and direction indicated on click.

### Example Usage

```
<div class="summary-list">
	<div onos-sortable-header>
		<table>
			<tr>
				<td colId="id" sortable>ID</td>
				<td colId="foo" sortable>Foo</td>
				<td colId="bar" sortable>Bar</td>
				<td>Baz</td>
			</tr>
		</table>
	</div>
	<div>
		<table>
			<tr ng-repeat="item in tableData track by $index">
				<td>{{item.id}}</td>
				<td>{{item.foo}}</td>
				<td>{{item.bar}}</td>
				<td>{{item.baz}}</td>
			</tr>
		</table>
	</div>
</div>
```

| Requirements | Other Attributes | Summary |
| --- | --- | --- |
| * onos-sortable-header has to be on an element that has children that represent the table header row (<td> elements)   + in the above example, the directive is on the <div>, but it would also work on the <table> or <tr> elements * the <td> elements you want to be sortable must have the `sortable` and the `colId` attributes (see right -->) * *ALL column headers must be **<td>** elements NOT <th>* | `sortable` - (required) put this attribute (with no value) on the td element whose column you want to be sortable.  `colId` - (required) this attribute's value must be the tag of the column's contents which you want to sort by. As shown above, to sort by ID, the attribute must be `colId="id"`  *\*\* If you don't include these attributes, then the column won't be sortable. \*\** | This directive selects all of the <td> elements below the `onos-sortable-header` attribute and checks if they have the `sortable` attribute. If it does, then it installs a sort click event on the <td> element. |

## onos-flash-changes

Flashes the table rows whose information is new or updated.

### Example Usage

```
<div class="summary-list">
	<div>
		<table>
			<tr>
				<td>ID</td>
				<td>Foo</td>
				<td>Bar</td>
				<td>Baz</td>
			</tr>
		</table>
	</div>
	<div>
		<table onos-flash-changes id-prop="id">
			<tr ng-repeat="item in tableData track by $index"
				ng-repeat-complete row-id="{{item.id}}">
				<td>{{item.id}}</td>
				<td>{{item.foo}}</td>
				<td>{{item.bar}}</td>
				<td>{{item.baz}}</td>
			</tr>
		</table>
	</div>
</div>
```

You will also need CSS to style the table flash.

```
div.summary-list tr {
    transition: background-color 500ms;
}
.light div.summary-list tr.data-change {
    background-color: #FDFFDC;
}
.dark div.summary-list tr.data-change {
    background-color: #5A5600;
}
```

| Requirements | Other Attributes | Summary |
| --- | --- | --- |
| * `onos-flash-changes` must be on the <div> or <table> elements that represent the table body * `id-props` must be on the same element as `onos-flash-changes` (see right) * include the directive `ng-repeat-complete` in the same element that `ng-repeat` is in * include `row-id` attribute with the interpolated unique identifier (see right) | `id-props` - the value for this attribute must be the property key for the unique identifier. Most often, the unique identifier will be "id", but not always.  `row-id` - put the [interpolated value](https://docs.angularjs.org/api/ng/service/$interpolate) of the unique identifier for this item as the value for this attribute, such as {{item.id}} (which will evaluate to the actual value at runtime)  `ng-repeat-complete` - tells `onos-flash-changes` to start looking for the elements that have changed in the dataset | Finds changes in the tableData set and finds the element that corresponds to those changes. The class "`data-change`" will appear for a 1.5 seconds and then be removed. |
