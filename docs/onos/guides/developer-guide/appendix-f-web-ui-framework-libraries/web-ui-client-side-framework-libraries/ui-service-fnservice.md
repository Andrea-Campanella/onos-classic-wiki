# UI Service - FnService

# FnService - Function Service

FnService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [Util module](../web-ui-client-side-framework-libraries.md) with the name `fn.js`. It provides general purpose functions that are useful throughout the client-side application. To use these functions, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

> Note: some of these functions are repeats of jQuery functions. Since we are not using jQuery, we wrote our own implementations.

| Name | Summary |
| --- | --- |
| `isF` | Checks if argument is a function. |
| `isA` | Checks if argument is an array. |
| `isS` | Checks if argument is a string. |
| `isO` | Checks if argument is an object. |
| `contains` | Checks if an array contains a value. |
| `areFunctions` | Checks if given strings are names of functions on an API and whether the API has functions that are not listed. |
| `areFunctionsNonStrict` | Checks if given strings are names of functions on an API. (Doesn't care about unlisted functions.) |
| `windowSize` | Returns inner dimensions of the window minus given values. |
| `isMobile` | Returns true if the device viewing the GUI is a mobile device. |
| `isChrome` | Returns true if the browser being used is Chrome. |
| `isSafari` | Returns true if the browser being used is Safari. |
| `isFirefox` | Returns true if the browser being used is Firefox. |
| `debugOn` | Returns true if the debug flag is turned on in query params. |
| `debug` | Conditionally writes a debug message to the console. |
| `find` | Searches through an array of objects looking for the object with a specific property name and property value and returns its index. |
| `inArray` | Finds an item's index in the array. |
| `removeFromArray` | Removes the first occurrence of the specified item from the array. |
| `isEmptyObject` | Returns true if the object is empty (has no non-default properties). |
| `cap` | Returns the given string with only the first letter capitalized. |
| `noPx` | Return the argument without the 'px' suffix. |
| `noPxStyle` | Return the element's style property without the 'px' suffix. |
| `endsWith` | Checks if the given string ends with a given suffix. |
| `parseBitRate` | Returns a Number version of the given string bit rate. |

# Function Descriptions

> Note: Green Text means that the return value is truthy. Red Text means that the return value is falsy.

## isF

Short for "is Function". Checks if argument is a function.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.isF(f);` | `f` - the variable to check if it is a function | **`f`** if `typeof` is 'function'  `null` if **`f`** is not a function |

## isA

Short for "is Array". Checks if argument is an array.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.isA(a);` | `a` - the variable to check if it is an array | `a` if [isArray (ECMA5)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray) returns true  `null` if `a` is not an array |

## isS

Short for "is String". Checks if argument is a string.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.isS(s);` | `s` - the variable to check if it is a string | **`s`** if `typeof` is 'string'  `null` if `s` is not a string |

## isO

Short for "is Object". Checks if argument is an object.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.isO(o);` | `o` - the variable to check if it is an object | `o` if `typeof` is 'object' and the constructor is Object  `null` if **`o`** is not an object |

## contains

Checks if an array contains an item.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.contains(a, x);` | `a` - the array to search  `x` - the item to look for | the index of `x` if it is in **`a`** (the index may be 0 – not truthy!)  false if `a` isn't an array  -1 if **`x`** isn't in the array |

## areFunctions

Checks if given strings are names of functions on an API and whether the API has functions that are not listed. This is used for unit testing.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.areFunctions(api, fnNames);` | `api`: the factory API object to check  `fnNames`: an array of strings of function names that should be on the API | true if   * `fnNames` given are names of functions on `api` * `api` only contains the functions in `fnNames`   false if   * `fnNames` isn't an array * if there are names in `fnNames` that `api` doesn't have * `api` has functions not accounted for in `fnNames` |

## areFunctionsNonStrict

Checks if given strings are names of functions on an API. This function is similar to areFunctions, but doesn't care about unlisted functions.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.areFunctionsNonStrict(api, fnNames);` | `api`: the factory API object to check  `fnNames`: an array of strings of function names that should be on the API | true if   * `fnNames` given are names of functions on `api`   false if   * `fnNames` isn't an array * if there are names in `fnNames` that `api` doesn't have |

## windowSize

Returns inner dimensions of the browser window minus given values.

| Example Usage | Arguments | Default Params | Return Value |
| --- | --- | --- | --- |
| `fs.windowSize(offH, offW);` | `offH` - number value to be subtracted from the browser window height  `offW` - number value to be subtracted from the browser window width | `offH`: 0 (if offH is falsy)  `offV`: 0 (if offW is falsy) | an object with members:   * height: window inner height minus `offH` (if given) * width: window inner width minus `offW` (if given) |

## isMobile

Returns true if the device viewing the GUI is a mobile device.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.isMobile();` | none | true if the device viewing the GUI is a mobile device  false otherwise |

## isChrome

Returns true if the browser being used is Chrome.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.isChrome();` | none | true if the user is viewing the GUI in Google Chrome  false otherwise |

## isSafari

Returns true if the browser being used is Safari.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.isSafari();` | none | true if the user is viewing the GUI in Safari  false otherwise |

## isFirefox

Returns true if the browser being used is Firefox.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.isFirefox();` | none | true if the user is viewing the GUI in Mozilla Firefox  false otherwise |

## debugOn

Returns true if the debug flag is turned on in query params.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.debugOn(tag);` | **`tag`**: string of which debug flag you are looking for | true if debug flag is turned on for `tag`  `undefined` otherwise |

## debug

Conditionally logs a debug message to the console. This function checks to see if the given tag is in the set of active debug flags, via a call to *debugOn()*. If the flag is active, the remaining arguments are passed to *$log.debug()* to write a debug message to the console. If the flag is not active, nothing is logged.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.debug(tag, arg1, arg2, ...);` | **tag**: debug flag to test for  *arg1, arg2, ...* : arguments passed to $log.debug() | none |

## find

Searches through an array of objects looking for the object with a specific property name (tag) and property value (key) and returns its index.

| Example Usage | Arguments | Default Params | Return Values |
| --- | --- | --- | --- |
| `fs.find(key, array, tag);` | **`key`**: property value you are searching for  **`array`**: array of objects to search through  **`tag`**: property name you are searching for | **`tag`**: 'id' | the index of the object in the array, if found (the index may be 0 – not truthy!)  -1 if it wasn't found |

> Note: this function searches for a specific name-value pair in an object, as in:
>
> 'tag': 'key'
>
> 'tag' defaults to 'id' for searching through objects because 'id' is usually unique.

## inArray

Finds an item's index in the array.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.inArray(item, array);` | `item`: the item to search for in the array  `array`: the array to search | the index of the item in the array, if found (the index may be 0 – not truthy!)  -1 if it wasn't found |

## removeFromArray

Removes the first occurrence of the specified item from the array.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.removeFromArray(item, array);` | `item`: the item to remove from the array  `array`: the array to remove from | true if the removal was made  false otherwise |

## isEmptyObject

Returns true if the object is empty (has no non-default properties / looks like this: `{}`).

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.isEmptyObject(obj);` | `obj`: the object to check to see if it is empty | true if it is empty  false otherwise |

## cap

Returns the given string with only the first letter capitalized.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| `fs.cap(s);` | `s`: the string to properly capitalize | `s` properly capitalized |

> Example: fs.cap('sOme STRing'); --> 'Some string'

## noPx

Return the argument without the 'px' suffix.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.noPx(num);` | `num`: string number with a 'px' you want to be turned into a number value | the number from the pixel string |

> Example: fs.noPx('50px'); --> 50

## noPxStyle

Return the element's style property without the 'px' suffix.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.noPxStyle(elem, prop);` | `elem`: the d3 selection of an element  `prop`: the style property you want the number of | the number value of the style property |

> Example: fs.noPxStyle(d3.select('h2'), 'height'); --> 100

## endsWith

Checks if the given string ends with a given suffix.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.endsWith(str, suffix);` | `str`: the string you want to check  `suffix`: the suffix you want to look for | true if the **`str`** ends with **`suffix`**  false otherwise |

## parseBitRate

Returns a Number version of the given string bit rate.

| Example Usage | Arguments | Return Values |
| --- | --- | --- |
| `fs.parseBitRate(str);` | `str`: the string that you want the bit rate from | the number value of the bit rate |

> Example: fs.parseBitRate('4Mbps'); --> 4
