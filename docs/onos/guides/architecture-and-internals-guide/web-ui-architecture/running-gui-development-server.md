# Running GUI Development Server

> Note: This page refers to the legacy GUI, not GUI2. See [Appendix I - GUI2 Development](../../developer-guide/appendix-i-gui2-development.md) instead

To help with UI development we provide a dedicated environment that introduce an auto reload feature and allow you to change your javascript files without recompiling the application.

## Prerequisites:

1. NodeJS & NPM
2. \*nix environment

   NodeJS version

   UI Development server uses a special `harmony\_destructuring` flag that works well with node versions > 5.x

   For node version >= 6, you may want to use `–harmony\_destructuring\_bind` instead.

   Disabling JS minification

   From ONOS 1.10 onwards, JS & CSS files will be **minified** for better performance. However this minification would prevent the file changes getting picked up by development server.

   So make sure you comment out **40**th line in `tools/gui/gulp-tasks/bundles/bundle-js/index.js` before attempting to use this.

## Installing NodeJS 5.x from tar.gz option:

Though there are several versions of NodeJS and several ways to install NodeJS, installing from pre-built tar.gz package is the most efficient way.

* Download Node 5.x version using wget
* Install NodeJS binary in /usr/local as follows
* **NodeJS 5.x installation**

  ```
  cd /usr/local
  tar --strip-components 1 -xzf <path-to-downloaded>/node-v5<ver>-linux-x64.tar.gz
  ```
* Verify installation
* **Verifying Installation**

  ```
  :~/onos/web/gui/src/main/webapp$ node -v
  v5.12.0
  ```

## Installing & Starting Development Server:

1. Enter ***`web/gui/src/main/webapp/`*** folder
2. Run ***`npm install`*** to install required dependency
3. Run ***`npm start`*** to open start the development environment

In the console you should see something like:

**Development Server Console**

```
In the console you should see something like:
```
Dev server is up and listening on http://localhost: 8182
[BS] Proxying: http://localhost:8181
[BS] Access URLs:
 ----------------------------------
       Local: http://localhost:3000
    External: http://10.1.8.46:3000
 ----------------------------------
          UI: http://localhost:3002
 UI External: http://10.1.8.46:3002
 ----------------------------------
[BS] Watching files...
```
```

To open ONOS visit the local URL (eg: `<http://localhost:3000>`) plus `/onos/ui`  
(eg: `<http://localhost:3000/onos/ui>`)

## Loading files from external applications

The UI development environment provide the ability to serve UI files from an external forlder that can be specified with:

***`ONOS\_EXTERNAL\_APP\_DIRS="appName:path-to-the-first-folder" npm start`***

***Eg:***  
***`ONOS\_EXTERNAL\_APP\_DIRS="sampleCustom:../../meow/sample/meowster-sample/" npm start`***

Note that **ONOS\_EXTERNAL\_APP\_DIRS** is an environment variable,so it can be set with

**ONOS\_EXTERNAL\_APP\_DIRS**

```
export ONOS_EXTERNAL_APP_DIRS="sampleCustom:../../meow/sample/meowster-sample/"
```
