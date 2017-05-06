from app import create_app, socketio

app = create_app()

print("Python server running on http://0.0.0.0:5000")
socketio.run(app, host='0.0.0.0', port=5000)
