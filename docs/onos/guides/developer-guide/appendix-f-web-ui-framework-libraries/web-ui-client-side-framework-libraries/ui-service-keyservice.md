# UI Service - KeyService

# 

# KeyService

KeyService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [Util module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `keys.js`. It provides an API to bind key presses to functions. To use these functions, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `bindQhs` | Binds the [QuickHelpService](ui-service-quickhelpservice.md) to the KeyService. |
| `installOn` | Installs the key listener on a [d3 selection](https://github.com/mbostock/d3/wiki/Selections) of an element and sets up global key bindings. |
| `keyBindings` | Get or set keybindings for a view. |
| `unbindKeys` | Unbind keybindings for a view. |
| `gestureNotes` | Get or set notes about other view gestures besides keybindings. |
| `enableKeys` | Enable or disable keybindings. |

# Function Descriptions

## bindQhs

Binds the [QuickHelpService](ui-service-quickhelpservice.md) to the *KeyService*. This is called for you when *onos.js* runs, so you won't have to call this yourself.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ``` ks.bindQhs(qhs); ``` | `qhs` - the injected *QuickHelpService* from the setup *onos.js* created | none |

## installOn

Installs the key listener on a [d3 selection](https://github.com/mbostock/d3/wiki/Selections) of an element and sets up global keybindings. This is called for you when *onos.js* runs, so you won't have to call this yourself.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ``` ks.installOn(elem); ``` | `elem` - d3 selection of the 'body' element from *onos.js* | none |

## keyBindings

Get or set keybindings for a view. 

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ``` ks.keyBindings(x); ``` | This function is getter / setter.  **x** -   * `undefined` * object with keybindings (see below) * function reference (see below) | if **x** is `undefined`, returns an object containing 4 properties  **globalKeys**: *array of strings representing the globally bound keys*  **maskedKeys**: *array of strings representing keys the view can't use*  **viewKeys**: *array of strings representing the view bound keys*  **viewFunction**: *boolean of whether the view has a general key handler*  if **x** is defined, no return value |

There are two options for setting up keybindings – giving an object with key mappings or a function reference for a general key handler.

### Key Mappings

The format for setting key mappings is to use the logical name of the key as the object property name, and a two-element array as the object property value.

```
 var keys = {
	// the first array member is a function reference to be executed on keydown
	// the second array member is a string used for quick help / tooltips
	A: [aFunction, 'Description for aFunction'],
	B: [bFunction, 'Description for bFunction'],
 
	leftArrow: [leftFunction, 'Description for leftFunction'],
	space: [spaceFunction, 'Description for spaceFunction'],
 
	// the _helpFormat property tells the QuickHelpService how to display the help information
	// it's an array of arrays
	_helpFormat: [
		// list all of your bindings. '-' will create a separator
		// each array is a new section
		['A', '-', 'B'],
		['leftArrow', 'alt']
	]
};
ks.keyBindings(keys);       // bind the keys
```

The descriptions are displayed in the [QuickHelp](ui-service-quickhelpservice.md) panel to give a helpful hint to the user as to what the button does. They may also be used as tooltip text.

The object property must be the logical name of the key that you want the function to be executed on. See the section below for a complete list.

### Function Reference

Additionally, you can provide a function to be executed for all keys for which there is no explicit binding. For example:

```
var keys = { ... };    // as above
 
function keyFallback(token, key, code, event) {
    $log.debug('Fallback keystroke:', token, key, code, event);
}
 
// map explicit key bindings
ks.keyBindings(keys);
 
// register a fallback function for any unmapped keys
ks.keyBindings(keyFallback);
```

Note that the fallback function receives 4 parameters:

* ***token*** - always the string *"keyev"*
* ***key*** - the logical name for the key
* ***code*** - the key code
* ***event*** - the *KeyboardEvent* (same as *d3.event*)

## unbindKeys

Unbind keybindings for a view. You typically want to call this when your view is destroyed.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ``` ks.unbindKeys(); ``` | none | none |

## gestureNotes

Get or set notes on the [QuickHelp Panel](ui-service-quickhelpservice.md) about other view gestures besides keybindings.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ``` ks.gestureNotes(g); ``` | `g` - `undefined` or array of notes (see below) | if **`g`** is `undefined`, will return the current gesture notes  if g is defined, will not return anything |

```
// array of arrays for formatting the notes on the QuickHelp Panel
ks.gestureNotes([
	// each array is one line
	// first member is the name of the gesture
	// second member is the description
	['click', 'select an item'],
	['shift-click', 'selects multiple items'],
	['esc', 'deselect item(s)']
]);
```

## enableKeys

Enable or disable keybindings. Enabled allows the bound key functions to execute; disabled doesn't execute the functions.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| ``` ks.enableKeys(b); ``` | `b` - true to enable keybindings, false otherwise | none |

# Global Keybindings

There a few reserved keys that are shared among all views.

| Key | Logical Name | Function |
| --- | --- | --- |
| \ or / | ``` slash, backSlash ``` | Show / hide quickhelp |
| esc | ``` esc ``` | Dismiss quickhelp, hide navigation, cancel selections \* |
| T | ``` T ``` | Toggle theme |

\* You can still bind a function to the 'esc' key. Your function will be called after the quickhelp and navigation (the global functions) have been hidden. Your function should return true if it consumes the event, and false otherwise. In this way, successive <esc> key presses will cancel a chain of features.

# List of Logical Keystroke Names

The remaining logical names recognized by the *KeyService* are as follows:

| Logical Name | Notes |
| --- | --- |
| ``` A, B, C, ... Z ``` | alpha keys |
| ``` 0, 1, 2, ... 9 ``` | numeric keys |
| ``` F1, F2, F3, ... F12 ``` | function keys |
| ``` semicolon, comma, equals, dash, dot ``` |  |
| ``` quote, backQuote, openBracket, closeBracket ``` |  |
| ``` delete, tab, enter, ctrl, space ``` |  |
| ``` leftArrow, upArrow, rightArrow, downArrow ``` |  |
| ``` cmdLeft, cmdRight, alt, shift ``` | Typically reserved to allow mouse-gesture augmentation |
