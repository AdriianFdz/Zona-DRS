function filtrarPorNumeroReparacion() {
    document.getElementById('searchInput').addEventListener('keyup', function() {
            let filter = this.value.trim(); // Tomar el valor ingresado y eliminar espacios en blanco
            let list = document.getElementById('reparacionesList');
            let items = list.getElementsByTagName('li');
        
            for (let i = 0; i < items.length; i++) {
                // Obtener el texto del enlace dentro del <li>
                let link = items[i].getElementsByTagName('a')[0];
                let textContent = link.textContent.trim(); // Obtener el texto completo
        
                // Extraer solo el número de reparación
                let idText = textContent.split(':')[1].split('|')[0].trim(); // Extraer el número de la reparación
        
                // Mostrar u ocultar dependiendo de si el número de reparación empieza con el valor del filtro
                if (idText.startsWith(filter)) {
                    items[i].style.display = ''; // Mostrar el elemento
                } else {
                    items[i].style.display = 'none'; // Ocultar el elemento
                }
            }
        });
}

function filtrarPorMatricula() {
    document.getElementById('searchInput').addEventListener('keyup', function () {
        let filter = this.value.toLowerCase().trim(); // Convertir el valor a minúsculas y eliminar espacios en blanco
        let list = document.getElementById('reparacionesList');
        let items = list.getElementsByTagName('li'); // Obtener todos los elementos <li>
        
        for (let i = 0; i < items.length; i++) { // Recorrer cada <li>
            let link = items[i].getElementsByTagName('a')[0]; // Seleccionar el primer enlace dentro del <li>
            let textContent = link.textContent.toLowerCase(); // Obtener el texto del enlace en minúsculas
            
            // Dividir el texto para extraer el campo de matrícula
            let matriculaText = textContent.split('|')[1].trim(); // Matrícula es el segundo campo, separado por '|'
            
            // Mostrar u ocultar el <li> según si coincide el filtro
            if (matriculaText.includes(filter)) {
                items[i].style.display = ''; // Mostrar si coincide
            } else {
                items[i].style.display = 'none'; // Ocultar si no coincide
            }
        }
    });
}