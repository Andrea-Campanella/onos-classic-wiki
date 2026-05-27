# UI Service - FlashService

# FlashService

FlashService is an [Angular Factory](https://docs.angularjs.org/guide/services) in the [Layer module](../web-ui-client-side-framework-libraries.md) with the name `flash.js`. It provides an API to "flash" messages on the screen. To use these functions, see the documentation on [injecting Angular services](https://docs.angularjs.org/guide/di).

An example of a flash message is on the [Topology View](../../../administrator-guide/interacting-with-onos/the-onos-web-gui/gui-topology-view.md):

![](../../../../../assets/image2015-7-17-11216.png)

Flash messages only appear for a short amount of time and then disappear.

| Name | Summary |
| --- | --- |
| `initFlash` | Initialize the FlashService. |
| `flash` | Flash the given message on the screen. |
| `enable` | Enable or disable flash messages from showing. |

# Function Descriptions

## initFlash

Initialize the FlashService with options. The FlashService is already initialized in `onos.js`, so you probably won't have to call this function.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| flash.initFlash(`opts`); | `opts` - an object with options for flash messages. If `undefined`, default settings (see below) will be used. | sets up the flash service to be used, no return value |

The FlashService has various default settings for messages. Below is the defaultSettings object, that will be [angular.extended](https://docs.angularjs.org/api/ng/function/angular.extend) if you provide an opts object.

```
defaultSettings = {
        fade: 200, // fade time (ms)
        showFor: 1200 // show message time (ms)
    };
```

## flash

Flash the given message on the screen. Message will appear immediately, stay on screen for settings.showFor time, then fade away for settings.fade time.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| flash.flash(`msg`); | `msg` - string with the message to flash on screen | none |

## enable

Enable or disable flash messages. Enable will show flash messages, disable will disable flash messages.

| Example Usage | Arguments | Return Value |
| --- | --- | --- |
| flash.enable(**`b`**); | `b` - truthy or falsy value of whether to enable flash messages  truthy will enable  falsy will disable | flash messages are enabled or disabled  no return value |
