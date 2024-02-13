#!/usr/bin/node

exports.esrever = function (list) {
  const reversedArray = [];
  let len = list.length - 1;
  for (let i = 0; i < list.length; i++, len--) {
    reversedArray[i] = list[len];
  }

  return reversedArray;
};
