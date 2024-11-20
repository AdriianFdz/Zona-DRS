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
                <!DOCTYPE html>
                <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>ZonaDRS - Reparación Completada</title>
                </head>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 20px;">
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                        <img src="https://i.imgur.com/rwYPUcD.png" alt="Logo ZonaDRS" style="max-height: 100px;">
                        <h1 style="color: #000000; margin: 0;">ZonaDRS</h1>
                    </div>
                    <p>Estimado/a <strong>{obj.vehiculo.propietario.nombre} {obj.vehiculo.propietario.apellido1}</strong>,</p>
                    <p>
                        Nos complace informarle que la reparación de su vehículo 
                        <strong>{obj.vehiculo.marca} {obj.vehiculo.modelo}</strong> con matrícula 
                        <strong>{obj.vehiculo.matricula}</strong> ha sido completada.
                    </p>
                    <p>Puede pasar a recoger su vehículo en nuestro taller.</p>
                    <p>Le adjuntamos imágenes de las piezas reparadas:</p>
                    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                        {imagenes_reparacion}
                    </div>
                    <br/>
                    <p>Muchas gracias por confiar en nuestro taller.</p>
                    <p><strong>ZonaDRS</strong></p>
                </body>
                </html>
                """
            }
        ]
    }
    
    result = mailjet.send.create(data=data)