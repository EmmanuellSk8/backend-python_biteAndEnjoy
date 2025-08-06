from sib_api_v3_sdk import Configuration, ApiClient
from sib_api_v3_sdk.api import TransactionalEmailsApi
from sib_api_v3_sdk.models import SendSmtpEmail
from config import BREVO_API_KEY
from jinja2 import Environment, FileSystemLoader
import os


env = Environment(loader=FileSystemLoader("templates"))

def render_template(template_name: str, context: dict) -> str:
    template = env.get_template(template_name)
    return template.render(**context)

def send_email(to_email: str, subject: str, template_name: str, context: dict):
    configuration = Configuration()
    configuration.api_key['api-key'] = BREVO_API_KEY

    api_client = ApiClient(configuration)
    api_instance = TransactionalEmailsApi(api_client)

    html_content = render_template(template_name, context)

    email = SendSmtpEmail(
        to=[{"email": to_email}],
        sender={"email": "biteandenjoy2@gmail.com", "name": "Bite and Enjoy"},
        subject=subject,
        html_content=html_content,
    )

    try:
        response = api_instance.send_transac_email(email)
        print(f"Correo enviado: {response}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
