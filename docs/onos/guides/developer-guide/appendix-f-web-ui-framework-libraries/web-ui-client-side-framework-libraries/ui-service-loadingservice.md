# UI Service - LoadingService

# LoadingService

LoadingService is an *Angular Factory* in the [Layer module](../web-ui-client-side-framework-libraries.md), implemented by `loading.js`. It provides an API to start and stop a *"Loading..."* animation in the center of the window.

![](../../../../../assets/onos-loading.png)

| Name | Summary |
| --- | --- |
| [start](#UIServiceLoadingService-start) | Starts the animation |
| [stop](#UIServiceLoadingService-stop) | Stops the animation |
| [waiting](#UIServiceLoadingService-waiting) | Returns true if `start()` has been called but `stop()` has not |

# Function Descriptions

## start

Starts the "Loading..." animation after a 500ms delay.

(This function is idempotent)

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| `ls.start();` | none | none |

## stop

Cancels the delayed start task and stops the "Loading..." animation.

(This function is idempotent)

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| `ls.stop();` | none | none |

## waiting

Returns true if `start()` has been called and `stop()` has not.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| `if (ls.waiting()) ...` | none | *true*, if waiting to be stopped; *false* otherwise |
