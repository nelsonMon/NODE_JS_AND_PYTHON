const { render } = require('ejs');
const express = require('express');

const RegisterSchema = require('../database/schema/register.schema'); // datos del dataframe

const controller = {};

//acá se lee la base de datos no relacional y se envia la información al cliente. Allí se renderizará y se visualizará en una tabla
controller.actualizar = async (req, res) => {
    console.log('entro en este controller')
    var temp = await RegisterSchema.find()
    console.log(temp)
    const tabs=0
    //const temp=0
    res.render('index.ejs', {tabs,temp});
};

module.exports = controller;