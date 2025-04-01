document.addEventListener("DOMContentLoaded", function () { //Esperamos a que el DOM se cargue completamente
    const robayo = document.getElementById("title"); //Obtenemos el elemento robayo
    if (robayo) {
        robayo.addEventListener("click", function () {
            robayo.style.transition = "transform 0.5s ease-in-out"; // Añadimos una transición al elemento robayo
            robayo.style.transform = "rotate(360deg)"; // Rotamos el elemento robayo 360 grados
            setTimeout(() => {
                this.removeAttributeNode.style.transform = "rotate(0deg)"; // Volvemos a la posición original
            }
                , 500); // Esperamos 0.5 segundos para volver a la posición original
        });
    }

});