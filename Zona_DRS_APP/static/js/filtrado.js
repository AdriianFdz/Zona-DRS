function filtrarPorNumeroReparacion() {
    document.getElementById('searchInput').addEventListener('keyup', function () {
        let filter = this.value.trim(); // Tomar el valor ingresado y eliminar espacios en blanco
        let items = document.querySelectorAll('.extra-box ul.reparaciones > a'); // Seleccionar los <a> directamente

        items.forEach(item => {
            let textContent = item.textContent.trim(); // Obtener el texto completo del <a>

            // Extraer solo el número de reparación
            let idText = textContent.split(':')[1]?.split('|')[0].trim(); // Extraer el número de la reparación

            // Mostrar u ocultar dependiendo de si el número de reparación empieza con el valor del filtro
            if (idText && idText.startsWith(filter)) {
                item.style.display = ''; // Mostrar el enlace y su contenido
            } else {
                item.style.display = 'none'; // Ocultar el enlace y su contenido
            }
        });
    });
}

function filtrarPorMatricula() {
    document.getElementById('searchInput').addEventListener('keyup', function () {
        let filter = this.value.toLowerCase().trim(); // Convertir el valor a minúsculas y eliminar espacios en blanco
        let links = document.querySelectorAll('.extra-box ul.reparaciones > a'); // Seleccionar los <a> directamente dentro del <ul>

        links.forEach(link => {
            let textContent = link.textContent.toLowerCase().trim(); // Obtener el texto completo del enlace en minúsculas
            
            // Dividir el texto para extraer el campo de matrícula
            let parts = textContent.split('|'); // Dividir el texto por '|'
            let matriculaText = parts.length > 1 ? parts[1].trim() : ''; // Validar si el campo existe antes de acceder
            
            // Mostrar u ocultar el enlace según si coincide el filtro
            if (matriculaText.startsWith(filter)) {
                link.style.display = ''; // Mostrar si coincide
            } else {
                link.style.display = 'none'; // Ocultar si no coincide
            }
        });
    });
}


document.addEventListener('DOMContentLoaded', () => {
    const page = document.body.dataset.page;

    switch (page) {
        case 'detalle-vehiculo':
        case 'detalle-mecanico':
            filtrarPorNumeroReparacion();
            break;
        case 'detalle-propietario':
            filtrarPorMatricula();
            break;
        // Agrega más casos según sea necesario
        default:
            console.log('No se ha definido una función para esta página.');
    }
});
