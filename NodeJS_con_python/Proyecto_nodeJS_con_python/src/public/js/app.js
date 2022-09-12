// NOTA PERSONAL - LOS .LOG EJECUTADOS EN LA RESPUESTA DEL JSON SOLO SE VISUALIZAN EN EL TERMINAL DEL NAVEGADOR

const sc = window.screen;
const conio = document.querySelector('.conio');
// conio.style.height = (sc.height * 0.6) + 'px';

//  window.addEventListener('resize', (event) => {
//      conio.style.height = (sc.height * 0.6) + 'px';
//      //alert(sc.height);
//  }, true);


function Carga_datos() {
  const Cantidad_data = document.querySelector('#numero_data_mostrar').value;
  // alert(Cantidad_data)
  // alert(typeof(Cantidad_data))
  alert('Se va a cargar los datos a la base de datos usados en el aplicativo')
  const other_parameters = {
    method: "POST",
    body: JSON.stringify({}),
    headers: { "Content-type": "application/json" }
  }

  const url = 'http://127.0.0.1:8000/carga/'+Cantidad_data
  fetch(url)
    .then(response => response.json())
    .then(json => {
      console.log('fiteo de datos')
    })
  // const AlgoritmoGN = document.querySelector('#AlgoritmoGN').value;
  // const cantidad_NUSO = document.querySelector('#cantidad_NUSO').value;
  // const class_algorit_V_ale = document.querySelector('#class_algorit_V_ale').value;
  // const class_algorit_generador_2 = document.querySelector('#class_algorit_generador_2').value;
  // alert(AlgoritmoGN);
  // //alert(cantidad_NUSO);
  // //alert(class_algorit_V_ale);
  // //alert(class_algorit_generador_2);
  // fetch('http://localhost:4100/Calculo_Modulo_simulacion', { method: 'POST', body: JSON.stringify({ AlgoritmoGN, cantidad_NUSO, class_algorit_V_ale, class_algorit_generador_2 }), headers: { "Content-type": "application/json" } })
  //   .then(response => response.json())
  //   .then(json => {
  //     console.log(json);
  //     data = json;
  //     generate_graphics(data)
  //   })

}
// acá se llama otra función usando node js, la cual se encuentra en el archivo Controller_simulación, 
//posteriormente llama la función generate_graphics para realizar el grafico
function graficar_variables() {
  const AlgoritmoGN = document.querySelector('#AlgoritmoGN').value;
  const cantidad_NUSO = document.querySelector('#cantidad_NUSO').value;
  const class_algorit_V_ale = document.querySelector('#class_algorit_V_ale').value;
  const class_algorit_generador_2 = document.querySelector('#class_algorit_generador_2').value;
  alert(AlgoritmoGN);
  //alert(cantidad_NUSO);
  //alert(class_algorit_V_ale);
  //alert(class_algorit_generador_2);
  fetch('http://localhost:4100/Calculo_Modulo_simulacion', { method: 'POST', body: JSON.stringify({ AlgoritmoGN, cantidad_NUSO, class_algorit_V_ale, class_algorit_generador_2 }), headers: { "Content-type": "application/json" } })
    .then(response => response.json())
    .then(json => {
      console.log(json);
      data = json;
      generate_graphics(data)
    })

}

function generate_graphics(data) {

  let selector_graficos = document.querySelector('#metodo_grafico')
  console.log(selector_graficos.selectedIndex)
  expr = selector_graficos.selectedIndex

  switch (expr) {

    case 1:
      var trace = {
        x: data,
        type: 'histogram',
      };
      var data_Graphics = [trace];

      var layout = {
        title:'Histograma de variables aleatorias obtenidos por números aleatorios',
        autosize: false,
        width: 600,
        height: 600,
        margin: {
          l: 50,
          r: 50,
          b: 100,
          t: 100,
          pad: 4
        },
        paper_bgcolor: '#7f7f7f',
        plot_bgcolor: '#c7c7c7'
      };
      Plotly.newPlot('Plotly_VA', data_Graphics, layout, { scrollZoom: true });

      break;
    case 2:
      /* CAJAS Y BIGOTES*/
      var trace1 = {
        y: data,
        type: 'box',
        name: 'Datos en cajas de bigotes'
      }
      var data_Graphics = [trace1];
      var layout = {
        title:'Diagrama de cajas y bigotes',
        autosize: false,
        width: 600,
        height: 600,
        margin: {
          l: 50,
          r: 50,
          b: 100,
          t: 100,
          pad: 4
        },
        paper_bgcolor: '#7f7f7f',
        plot_bgcolor: '#c7c7c7'
      };
      Plotly.newPlot('Plotly_VA', data_Graphics, layout, { scrollZoom: true });
      break;
    case 3:
      /* DISPERSION*/
      data_x = range(1, data.length)
      //alert('hola')
      var trace1 = {
        x: data_x,
        y: data,
        mode: 'markers',
        type: 'scatter'
      };
      var data_Graphics = [trace1];
      var layout = {
        title:'Dispersión',
        autosize: false,
        width: 600,
        height: 600,
        margin: {
          l: 50,
          r: 50,
          b: 100,
          t: 100,
          pad: 4
        },
        paper_bgcolor: '#7f7f7f',
        plot_bgcolor: '#c7c7c7'
      };
      Plotly.newPlot('Plotly_VA', data_Graphics, layout, { scrollZoom: true });
      break;
    default:
    //alert('Lo lamentamos, opcion no valida por favor seleccione un tipo de gráfico');  
  }
}