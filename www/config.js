/* exported config */

var config = {
  // Show help text for images
  show_help: true,

  // Path to were overview.json can be found
  versions: {"22.03.6": "data/22.03.6", "22.03.5": "data/22.03.5", "19.07.8": "data/19.07.8", "21.02.6": "data/21.02.6", "21.02.0": "data/21.02.0", "23.05.0": "data/23.05.0", "22.03.3": "data/22.03.3", "21.02.5": "data/21.02.5", "22.03.4": "data/22.03.4", "21.02.2": "data/21.02.2", "19.07.7": "data/19.07.7", "19.07.5": "data/19.07.5", "22.03.2": "data/22.03.2", "22.03.1": "data/22.03.1", "21.02.1": "data/21.02.1", "21.02.4": "data/21.02.4", "19.07.4": "data/19.07.4", "23.05.1": "data/23.05.1", "19.07.10": "data/19.07.10", "22.03.0": "data/22.03.0", "19.07.9": "data/19.07.9", "19.07.6": "data/19.07.6", "21.02.7": "data/21.02.7", "23.05.2": "data/23.05.2", "21.02.3": "data/21.02.3", "23.05.3": "data/23.05.3"},

  // Pre-selected version (optional)
  default_version: "23.05.3",

  // Image download URL
  image_url: "https://mirror.nju.edu.cn/openwrt/",

  // Info link URL (optional)
  info_url: "https://openwrt.org/start?do=search&id=toh&q={title} @toh",

  // Attended Sysupgrade Server support (optional)
  asu_url: "http://10.100.111.41:81",
  asu_extra_packages: [ "luci" ],
  // asu_extra_packages: [ "luci" ],
};
