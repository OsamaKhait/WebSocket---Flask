from flask import Flask
from flask_socketio import SocketIO, emit
from datetime import datetime

# Création de l’application Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # clé requise par Flask (sessions, sécurité)

# Intégration de Socket.IO pour gérer les WebSockets
# cors_allowed_origins="*" : autorise la connexion depuis n’importe quel client
socketio = SocketIO(app, cors_allowed_origins="*")

# Route HTTP simple pour tester que le serveur tourne
@app.route("/")
def index():
    return "Flask-SocketIO server is running."

# Événement WebSocket : quand un client envoie "get_time"
@socketio.on("get_time")
def handle_get_time():
    now = datetime.now()
    payload = {
        "type": "TIME",
        "iso": now.isoformat(),                    # format ISO (ex: 2025-09-24T10:17:04)
        "locale": now.strftime("%d/%m/%Y %H:%M:%S")  # format lisible FR
    }
    # On renvoie l’heure au client sous l’événement "time_response"
    emit("time_response", payload)

# Lancement du serveur Socket.IO (sur http://localhost:5000)
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)