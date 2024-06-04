# OpenWrt Firmware Selector

A simple OpenWrt firmware selector using autocompletion. Uses plain
HTML/CSS/JavaScript. Checkout the [Demo](https://firmware-selector.openwrt.org).

![image](misc/screenshot.png)

## 快速运行

* 下载本项目并更改工作目录
* run `python3 -m http.server`
* 访问 [http://localhost:8000/www/](http://localhost:8000/www/)

配置文件 [config.js](www/config.js).

## 构建服务 (ASU)

[ASU](https://github.com/Wuqiyang312/asu-wqyblog-cn) 是一个构建服务器，它根据请求构建具有给定包列表的OpenWrt映像。固件选择器可以用作发送这些请求和完成后下载图像的接口。

## 类似项目

- [Gluon Firmware Selector](https://github.com/freifunk-darmstadt/gluon-firmware-selector): For [Gluon](https://github.com/freifunk-gluon/) images, now with pictures.
- [Freifunk Hennef Firmware Downloader](https://github.com/Freifunk-Hennef/ffhef-fw-dl): Similar to the project above, but PHP based.
- [LibreMesh Chef](https://github.com/libremesh/chef/): Allows to select configurations.
- [GSoC Firmware Selector](https://github.com/sudhanshu16/openwrt-firmware-selector/): Result of the GSoC
- [FFB Firmware Selector](https://github.com/freifunk-bielefeld/firmware-selector): Build for Freifunk Bielefeld
