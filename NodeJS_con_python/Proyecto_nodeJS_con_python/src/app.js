// toda esta sección se usa para configurar los parámetros del servidor como puerto de conexión 
// rutas y entre otros. 
//include
const express = require('express');
const path = require('path');

//import
const routes = require('./routes/routes');
const { urlencoded } = require('express');
const dbc = require('./database/dbc/dbc');


//construct
const app = express();

//settings
app.set('port', process.env.PORT || 4100);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');
//static files
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'library')));

//middlewares
app.use(express.json());
app.use(express.urlencoded({
    extended: false
}));

//routes
app.use('/', routes);

app.get('*', (req, res) => {
    res.send('error');
});

//main
app.listen(app.get('port'), () => {
    console.log('server on port 4100');
});
