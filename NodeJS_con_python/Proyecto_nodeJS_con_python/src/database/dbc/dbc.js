/** require */
const mongoose = require('mongoose');

/** start */
mongoose.connect(
    'mongodb://127.0.0.1:27017/data_nodejs_python', {
    useNewUrlParser: true,
    useUnifiedTopology: true
},
)
    .then(db => console.log('mongoose has been connected'))
    .catch(err => console.log('NO SE CONECTO NADA'));

/** export */
module.exports = mongoose;