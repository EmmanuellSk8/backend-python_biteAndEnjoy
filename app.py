# app.py
from flask import Flask, request, jsonify
from email_client import send_email
from flask_cors import CORS
from config import BACKEND_URL

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [BACKEND_URL, "http://localhost:3000"]}})

@app.route("/send-email", methods=["POST"])

def handle_send_email():
    data = request.json

    required_fields = ["action", "to_email", "name", "date", "clave"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}),400


    email_type = data["type"]

    if email_type == "code":
        if "clave" not in data:
            return jsonify({"error": "Missing field: clave for code email"}), 400
        
        send_email(
            to_email=data["to_email"],
            subject="Código de confirmación",
            template_name="email-code.template.html",
            context={
                "name": data["name"],
                "date": data["date"],
                "clave": data["clave"]
            }
        )

    elif email_type == "action":
        if "action" not in data:
            return jsonify({"error": "Missing field: action for action email"}),400
        
        send_email(
            to_email=data["to_email"],
            subject=f"Reserva {data['action']}",
            template_name="email-action.template.html",
            context={
                "name": data["name"],
                "date": data["date"],
                "action": data["action"]
            }
        )
    else:
        return jsonify({"error": "Invalid email type. Must be 'action'"}),400
    
    return jsonify({"message": "Correo enviado correctamente"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
