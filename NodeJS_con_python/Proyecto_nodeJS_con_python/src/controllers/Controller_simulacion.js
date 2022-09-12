const { render } = require('ejs');
const express = require('express');

const RegisterSchema = require('../database/schema/register.schema'); // HISTORICOS DE FALLOS

const controller = {};
// toda esta parte ejecuta las ecuaciones necesarias para la generación de variables y numeros aleatorios. 
// Por último, se envia los datos al cliente para su posterior visualización, la cual tambien utiliza javascript.
controller.Simulacion2 = (req, res) => {

    var variablesaplicativo = {
        // variables de salida de costos 
        Suma_total_C2: 0,
        Suma_total_C1: 0,
        // variables de Recursos material
        Costo_penalizacion_hora: 0,
        Costo_mantener_hora: 0,
        Alpha: 0,
        Pedido_repuestos_optimos: 0,
        probabilidad_Qs_j: 0,
        Costo_total_TC: 0,
        // variables de Recursos himano
        Longitud_prom_cola: 0,
        promedio_numero_sistema: 0,
        promedio_espera_cola: 0,
        promedio_espera_sistema: 0,
        Ro: 0,
        P_delay: 0,
    }

    function generar_numeros_aleatorias(selector_generador_numeros, n) {

        switch (selector_generador_numeros) {
            case 'ALGORITMO SIMULA':
                /* Simula*/
                ////console.log('simula')
                xi = 123456789 - Math.floor((Math.random() * (100 - 20) + 20))
                a = Math.pow(5, 13)
                c = 0
                m = Math.pow(2, 35)
                let X_SIMULA = new Array();
                for (let i = 0; i < n; i++) {
                    xi = (a * xi + c) % m
                    X_SIMULA[i] = xi / (m - 1)
                    ////console.log(i)
                    ////console.log(X_SIMULA[i])
                }

                data = X_SIMULA
                break;
            case 'ALGORITMO APL':
                /*APL*/
                ////console.log('apl')
                xi = 123456789 - Math.floor((Math.random() * (100 - 20) + 20))
                a = Math.pow(7, 5);
                c = 0;
                m = Math.pow(2, 31) - 1
                let X_LL = new Array();
                for (let i = 0; i < n; i++) {
                    xi = (a * xi + c) % m;
                    X_LL[i] = xi / (m - 1);
                }

                data = X_LL
                break;
            case 'ALGORITMO FOLTRAN':
                /*FOLTRAN*/
                ////console.log('FOLTRAN')
                xi = 123456789 - Math.floor((Math.random() * (100 - 20) + 20))
                a = 630360016
                c = 0
                m = Math.pow(2, 31) - 1
                let X_FOLTRAN = new Array();
                for (let i = 0; i < n; i++) {
                    xi = (a * xi + c) % m
                    X_FOLTRAN[i] = xi / (m - 1)
                }
                data = X_FOLTRAN
                break;
            case 'ALGORITMO DE VB':
                /*VBL*/
                ////console.log('VBL')
                let X_VB = new Array();
                xi = 123456789 - Math.floor((Math.random() * (100 - 20) + 20))
                a = 1140671485
                c = 12820163
                m = Math.pow(2, 24)
                for (let i = 0; i < n; i++) {
                    xi = (a * xi + c) % m
                    X_VB[i] = xi / (m - 1)
                }
                data = X_VB
                break;
            default:
            ////console.log('Lo lamentamos, opcion no valida, por favor seleccione uno de los algoritmos generadores');

        }
        ////console.log(data)
        return data;
    }

    function generar_variables_aleatorias() {

        let n = req.body.cantidad_NUSO;
        n = Number(n)

        if (req.body.class_algorit_V_ale == 'Distribución') {
            expr3 = req.body.class_algorit_generador_2
        } else {
            expr3 = req.body.class_algorit_V_ale
        }

        /* datos que vienen de fiabilidad*/
        let media_fiabialidad = 10;
        let des_esta_fiabilida = 2;
        let grados_libertad = 13;
        let tasa = 0.5
        let Escala = 2;
        let forma = 5;
        /* datos que vienen de fiabilidad*/
        let Z1 = new Array();
        let Z2 = new Array();

        let data_normal = new Array();
        let data_log_normal = new Array();
        let data_chi_cuadrado = new Array();
        let data_chi_cuadrado_2 = new Array();
        let data_t = new Array();
        let data_f = new Array();
        /*vectores para weibull*/
        let V = new Array();
        let Z = new Array();
        let Y = new Array();
        let W = new Array();


        let data_exponencial = new Array();
        let data_weibull = new Array();
        let data_gamma = new Array();
        let data = new Array();
        let j = 1;

        switch (expr3) {

            case "Distribución Normal":

                data1 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                data2 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                for (let i = 0; i < data2.length; i++) {
                    Z1[i] = Math.sqrt(-2 * Math.log(data1[i])) * Math.cos(2 * Math.PI * data2[i]);
                    Z2[i] = Math.sqrt(-2 * Math.log(data2[i])) * Math.cos(2 * Math.PI * data1[i]);
                    ////console.log(i);
                    ////console.log(Z1[i]);
                    ////console.log(Z2[i]);
                    data_normal[i] = media_fiabialidad + des_esta_fiabilida * Z2[i];
                    ////console.log(data_normal[i]);
                }
                data = data_normal;
                ////console.log(data);
                break;

            case "Distribución Log Normal":

                media_fiabialidad = 3;
                des_esta_fiabilida = 0.5;
                data1 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                data2 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                //////console.log(data2)
                for (let i = 0; i < data2.length; i++) {
                    Z1[i] = Math.sqrt(-2 * Math.log(data1[i])) * Math.cos(2 * Math.PI * data2[i]);
                    ////console.log(Z1[i])
                    Z2[i] = Math.sqrt(-2 * Math.log(data2[i])) * Math.cos(2 * Math.PI * data1[i]);
                    data_log_normal[i] = Math.exp(media_fiabialidad + des_esta_fiabilida * Z2[i]);
                }
                data = data_log_normal;
                break;

            case "Distribución chi cuadrado":
                for (let i = 0; i < n; i++) {
                    data_chi_cuadrado[i] = 0
                }
                while (j <= grados_libertad) {
                    data1 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                    data2 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);;
                    for (let i = 0; i < n; i++) {
                        Z1[i] = Math.pow(Math.sqrt(-2 * Math.log(data1[i])) * Math.cos(2 * Math.PI * data2[i]), 2);
                        data_chi_cuadrado[i] = data_chi_cuadrado[i] + Z1[i]
                    }
                    j = j + 1;
                }
                data = data_chi_cuadrado;
                break;

            case "Distribución t":
                for (let i = 0; i < n; i++) {
                    data_chi_cuadrado[i] = 0
                    ////console.log(data_chi_cuadrado[i])
                }
                while (j <= grados_libertad) {
                    data1 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                    data2 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                    for (let i = 0; i < n; i++) {
                        Z1[i] = Math.pow(Math.sqrt(-2 * Math.log(data1[i])) * Math.cos(2 * Math.PI * data2[i]), 2);
                        data_chi_cuadrado[i] = data_chi_cuadrado[i] + Z1[i]
                    }
                    j = j + 1;
                }
                data1 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                data2 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                for (let i = 0; i < data2.length; i++) {
                    Z1[i] = Math.sqrt(-2 * Math.log(data1[i])) * Math.cos(2 * Math.PI * data2[i]);
                    Z2[i] = Math.sqrt(-2 * Math.log(data2[i])) * Math.cos(2 * Math.PI * data1[i]);

                    data_normal[i] = media_fiabialidad + des_esta_fiabilida * Z2[i];
                    data_t[i] = data_normal[i] / data_chi_cuadrado[i];
                }
                data = data_t;
                break;

            case "Distribución f":

                for (let i = 0; i < n; i++) {
                    data_chi_cuadrado[i] = 0
                    ////console.log(data_chi_cuadrado[i])
                }

                while (j <= grados_libertad) {
                    data1 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                    data2 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                    for (let i = 0; i < n; i++) {
                        Z1[i] = Math.pow(Math.sqrt(-2 * Math.log(data1[i])) * Math.cos(2 * Math.PI * data2[i]), 2);
                        data_chi_cuadrado[i] = data_chi_cuadrado[i] + Z1[i]
                    }
                    j = j + 1;
                }

                j = 1;
                for (let i = 0; i < n; i++) {
                    data_chi_cuadrado_2[i] = 0
                }
                while (j <= grados_libertad + 3) {
                    data1 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                    data2 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                    for (let i = 0; i < n; i++) {
                        Z1[i] = Math.pow(Math.sqrt(-2 * Math.log(data1[i])) * Math.cos(2 * Math.PI * data2[i]), 2);
                        data_chi_cuadrado_2[i] = data_chi_cuadrado_2[i] + Z1[i]
                    }
                    j = j + 1;
                }

                for (let i = 0; i < data2.length; i++) {
                    data_f[i] = data_chi_cuadrado[i] / data_chi_cuadrado_2[i];
                }
                data = data_f
                break;
            case "Distribución Exponencial":
                data1 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                data2 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                for (let i = 0; i < data2.length; i++) {
                    Z1[i] = Math.sqrt(-2 * Math.log10(data1[i])) * Math.cos(2 * Math.PI * data2[i]);
                    Z2[i] = Math.sqrt(-2 * Math.log10(data2[i])) * Math.cos(2 * Math.PI * data1[i]);
                    data_exponencial[i] = (-1 / tasa) * Math.log10(Z2[i]);
                }
                data = data_exponencial;
                break;
            case "Distribución Weibull":
                /*weibull*/
                data1 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                data2 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                /*////console.log(data2)*/
                /*////console.log(Math.max.apply(Math,data2))*/
                /*////console.log(Math.min.apply(Math,data2))*/
                for (let i = 0; i < data2.length; i++) {
                    temp = 1 / forma
                    data_weibull[i] = Math.pow((-1 * Math.log(1 - data2[i])), temp) * Escala
                }
                data = data_weibull
                break;
            case "Distribución Gamma":
                /* D. Gamma  */
                Escala = 0.3;
                forma = 5;
                //////console.log('entro en logaritmica')
                const a = 1 / (Math.sqrt(2 * forma - 1))
                const b = forma - Math.log(4)
                const q = forma + 1 / forma
                const teta = 4.5
                const d = 1 + Math.log(teta)
                let i = 0
                while (i < n) {
                    data1 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                    data2 = generar_numeros_aleatorias(req.body.AlgoritmoGN, n);
                    V[i] = a * Math.log(data1[i] / (1 - data1[i]))
                    Y[i] = forma * Math.exp(V[i])
                    Z[i] = Math.pow(data1[i], 2) * data2[i]
                    W[i] = b + q * V[i] - Y[i]
                    /*////console.log(W[i]+d-teta*Z[i])*/
                    /*////console.log('EL VALOR DE V ES '+ V[i] + 'EL VALOR DE Y ES ' + Y[i] + 'EL VALOR DE Z ES ' + Z[i] + 'CON UNA R1' + data1[i] + 'Y CON R2 DE' + data2[i])*/
                    if (W[i] + d - teta * Z[i] >= 0) {
                        data_gamma[i] = Escala * Y[i];
                        i = i + 1;
                    }
                    else {
                        if (W[i] >= Math.log(Z[i])) {
                            data_gamma[i] = Escala * Y[i];
                            i = i + 1;

                        }
                    }
                }
                data = data_gamma;
                break;
            default: ////console.log('Por favor seleccione un metódo de generación de variables aleatorias');
        }
        return data;
    }
    data2 = generar_variables_aleatorias();
    res.json(data2);
}

module.exports = controller;