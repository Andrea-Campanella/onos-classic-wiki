# UI Service - RandomService

# RandomService

RandomService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [Util module](https://wiki.onosproject.org/display/ONOS/UI+View+-+Framework+Libraries) with the name `random.js`. It provides useful functions that use random numbers. To use these functions, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

| Name | Summary |
| --- | --- |
| `spread` | Given a value, will return a random integer between -value / 2 and value / 2. |
| `randomDim` | For a given dimension, return a number from 0 to the dimension, within constraints. |

# Function Descriptions

## spread

Given a value, will return a random integer between -value / 2 and value / 2.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| rs.spread(`s`); | `s` - any number | given some value, **`s`**, returns an integer between -`s`/2 and `s`/2   Example: `s` = 100; result in the range [-50..50) |

## randomDim

For a given dimension, return a number from 0 to the dimension, within constraints.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| rs.randomDim(`d`); | `d` - any number | for a given dimension, **`d`**, returns a random value somewhere between 0 and `d` where the value is within (**`d`** / (2 \* sqrt(2))) of **`d`**/2. |
