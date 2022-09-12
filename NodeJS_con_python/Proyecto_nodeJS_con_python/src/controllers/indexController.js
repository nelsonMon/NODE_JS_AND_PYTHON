const { render } = require('ejs');
const express = require('express');

const controller = {};

controller.start = (req, res) => {
    const tabs=0
    const temp=0
    res.render('index.ejs', {tabs,temp});
};

module.exports = controller;