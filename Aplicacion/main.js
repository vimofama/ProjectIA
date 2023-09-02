document.addEventListener("DOMContentLoaded", function () {
    const botonLimpiar = document.getElementById("limpiar");
    const form = document.getElementById("prediction-form");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        let tip_naci = document.getElementById('nacionalidad').value;
        let mes = document.getElementById('mes').value;
        let dia = document.getElementById('dia').value;
        let via_tran = document.getElementById('transporte').value;
        let pais = document.getElementById('pais').value;

        console.log("tip_naci " + tip_naci);
        console.log("mes " + mes);
        console.log("dia " + dia);
        console.log("via_tran " + via_tran);
        console.log("pais " + pais);

        let data = {
            "tip_naci": tip_naci,
            "mes_movi": mes,
            "dia_movi": dia,
            "via_tran": via_tran,
            pais: 1
        }

        console.log(data);

        sendDataToServer(data);
    });

    function sendDataToServer(data) {
        const url = "http://127.0.0.1:5000/predict"; // Actualizar con la URL correcta
        fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(result => {
                // Manejar la respuesta del servidor aquí
                const predictionResult = document.getElementById('prediction-result');
                console.log(result.prediction[0]);
                const predictionValue = result.prediction[0];
                let category = "";

                if (predictionValue === 1){
                    category = "Turismo";
                } else if (predictionValue === 2) {
                    category = "Negocios";
                } else if (predictionValue === 3) {
                    category = "Eventos";
                } else if (predictionValue === 4) {
                    category = "Estudios";
                } else if (predictionValue === 5) {
                    category = "Residencia";
                } else if (predictionValue === 6) {
                    category = "Transeúnte";
                } else if (predictionValue === 7) {
                    category = "Tripulación";
                } else {
                    category = "Otros";
                }

                predictionResult.value = JSON.stringify(category, null, 2);
            })
            .catch(error => {
                console.error("Error en la solicitud:", error);
            });
    }

    botonLimpiar.addEventListener("click", function (evnet){
        evnet.preventDefault();
        form.reset();
    });
});
