#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      const Rectangle = {};
      return 'Rectangle' + Rectangle;
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
