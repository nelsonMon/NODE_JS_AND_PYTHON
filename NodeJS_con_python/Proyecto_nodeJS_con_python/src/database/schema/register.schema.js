/** require */
const mongoose = require('mongoose');
const { Schema } = mongoose;

/** schema */

const RegisterSchema = new Schema(
    {
        Sexo: { type: String, required: true },
        Longitud: { type: Number, required: true },
        Diametro: { type: Number, required: true },
        Altura: { type: Number, required: true },
        Peso_entero: { type: Number, required: true },
        Peso_cascara: { type: Number, required: true },        
        Peso_visceras: { type: Number, required: true },
        Peso_caparazon: { type: Number, required: true },
        anillos:{ type: Number, required: true },

    }
);

/** export */
module.exports = mongoose.model('Register', RegisterSchema);

