# from email_client import send_email
 
# if __name__ == "__main__":
#      reservation_data = {
#         "action": "actualizada",
#         "name": "Emmanuel Guerra",
#         "date": "2025-08-02, 7:30 PM",
#     }

#      send_email(
#       to_email="emmanuel50354@gmail.com",
#       subject="Correo de prueba",
#       template_name="email-action.template.html",
#       context=reservation_data
#     )

# main.py

from email_client import send_email

if __name__ == "__main__":
    # Para probar el código de confirmación
    send_email(
        to_email="emmanuel50354@gmail.com",
        subject="Código de confirmación",
        template_name="email-code.template.html",
        context={
            "name": "Emmanuel",
            "date": "31/07/2025",
            "clave": "123456"
        }
    )

    # Para probar actualización o eliminación
    send_email(
        to_email="emmanuel50354@gmail.com",
        subject="Reserva actualizada",
        template_name="email-email-action.template.html",
        context={
            "name": "Emmanuel",
            "date": "31/07/2025",
            "action": "actualizada"
        }
    )
