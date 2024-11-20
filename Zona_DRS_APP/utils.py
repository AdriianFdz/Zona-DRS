from mailjet_rest import Client ## Crear README

api_key = "393a85964b33b20c11f0df6932330dd1"
api_secret = "90dced41296f8ae4052a8d5074824bf4"

def send_email(obj):
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    imagenes = obj.imagenesReparacion.all()
    print(imagenes)
    imagenes_reparacion = "" 
    for imagen in imagenes:
        print(imagen.url)
        imagenes_reparacion += f'<img src="{imagen.url}" alt="Imagen de reparación" style="max-width:100%;"><br/>'
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "adrianeskolapios@gmail.com",
                    "Name": "ZonaDRS Taller"
                },
                "To": [
                    {
                        "Email": f"{obj.vehiculo.propietario.correo}",
                        "Name": "Cliente"
                    }
                ],
                "Subject": "Reparación finalizada",
                "TextPart": f"Hola, su reparación ha sido finalizada.",
                "HTMLPart": f"""
                    <h3>Estimado {obj.vehiculo.propietario.nombre} {obj.vehiculo.propietario.apellido1},</h3>
                    <p>La reparación de su vehículo <b>{obj.vehiculo.modelo} {obj.vehiculo.marca}</b> con matrícula <b>{obj.vehiculo.matricula}</b> ha sido reparado. Puedes recogerlo en nuestro taller.</p>
                    {imagenes_reparacion}
                    <br/>
                    <p>Gracias por confiar en nuestro taller.</p>
                """
            }
        ]
    }
    
    result = mailjet.send.create(data=data)