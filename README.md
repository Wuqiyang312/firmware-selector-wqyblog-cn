# OpenWrt Firmware Selector

A simple OpenWrt firmware selector using autocompletion. Uses plain
HTML/CSS/JavaScript. Checkout the [Demo](https://firmware-selector.openwrt.org).

![image](misc/screenshot.png)

## Quick Run

* Download the sources and change the working directory
* Start webserver (e.g. `python3 -m http.server`)
* Go to [http://localhost:8000/www/](http://localhost:8000/www/) in your web browser

Configure with [config.js](www/config.js).

## Attended SysUpgrade (ASU)

[ASU](https://github.com/openwrt/asu) is a build server that builds OpenWrt images with a given list of packages on request. The firmware-selector can be used as an interface to send these requests and to download the images when finished.

### UCI-Defaults

The Firmware Selector allows to define a script to be placed in the `/etc/uci-defaults/` folder of the OpenWrt image. These scripts are executed once on the first reboot and then deleted. See the [OpenWrt documentation](https://openwrt.org/docs/guide-developer/uci-defaults) on this topic.

## Translations

Visit [weblate.org](https://hosted.weblate.org/projects/openwrt/firmware-wizard/) to contribute new translations or to improve them.

## Similar Projects

- [Gluon Firmware Selector](https://github.com/freifunk-darmstadt/gluon-firmware-selector): For [Gluon](https://github.com/freifunk-gluon/) images, now with pictures.
- [Freifunk Hennef Firmware Downloader](https://github.com/Freifunk-Hennef/ffhef-fw-dl): Similar to the project above, but PHP based.
- [LibreMesh Chef](https://github.com/libremesh/chef/): Allows to select configurations.
- [GSoC Firmware Selector](https://github.com/sudhanshu16/openwrt-firmware-selector/): Result of the GSoC
- [FFB Firmware Selector](https://github.com/freifunk-bielefeld/firmware-selector): Build for Freifunk Bielefeld
