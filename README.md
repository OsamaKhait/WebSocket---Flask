# Mini-Projet WebSocket avec Flask

Projet réalisé par **Osama** et **Quentin**.

## Description
Ce projet est une démonstration simple de l’utilisation de **WebSocket** avec **Flask** et **Socket.IO**.  
L’application permet au client de demander l’heure courante au serveur, qui lui répond en JSON.

## Fonctionnement
1. L’utilisateur clique sur le bouton **"Obtenir l'heure"** dans la page web.
2. Le **client (JavaScript)** envoie un événement Socket.IO nommé **`get_time`** au serveur Flask.
3. Le **serveur Flask** répond avec un objet JSON contenant l’heure courante.

### Exemple de payload JSON
```json
{
  "type": "TIME",
  "iso": "2025-09-24T10:17:04.152158",
  "locale": "24/09/2025 10:17:04"
}
```

## 🖥️ Exemple de page

<img width="1470" height="956" alt="Capture d’écran 2025-09-24 à 10 18 02" src="https://github.com/user-attachments/assets/fbf6a258-8bd7-419b-b878-6153011b37c2" />


### Schéma de communication
- **Client → Serveur** : `get_time`  
- **Serveur → Client** : `time_response` + payload JSON (heure courante)
- Le client demande l’heure au serveur avec "get_time", et le serveur lui répond avec "time_response" contenant l’heure courante en JSON.


## 📦 Technologies utilisées
- [Flask](https://flask.palletsprojects.com/)  
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/)  
- JavaScript (Socket.IO côté client)  

---
