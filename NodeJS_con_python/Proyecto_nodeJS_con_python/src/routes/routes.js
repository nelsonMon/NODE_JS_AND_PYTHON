const express = require('express');
const router = express.Router();

const indexController = require('../controllers/indexController');
const Actualizar_pag=require('../controllers/actualizardata');
const Controller_simulacion=require('../controllers/Controller_simulacion');

router.get('/', indexController.start);
router.post('/actualizartabla', Actualizar_pag.actualizar);
router.post('/Calculo_Modulo_simulacion', Controller_simulacion.Simulacion2);

module.exports = router;