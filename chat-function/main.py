from fastapi import FastAPI, WebSocket
#from redis import Redis
import os
from functions_framework import create_app

# Initialize FastAPI app
app = FastAPI()

# Initialize Redis client
#redis_host = os.getenv('REDISHOST', 'localhost')  # Default to localhost if REDISHOST is not set
#redis_client = Redis(host=redis_host, port=6379)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, room: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
     #   redis_client.publish(room, data)
        await websocket.send_text(f"Message text 1 was: {data}")
        await websocket.send_text(f"Message text 2 was: {data}")
        await websocket.send_text(f"Message text 3 was: {data}")

@app.get("/")
async def root():
    return {"message": "WebSocket server is running"}

# Create the WSGI app that the functions_framework will use
def wsgi_app(environ, start_response):
    # Create a FastAPI app instance
    return create_app(app)(environ, start_response)

# Export the WSGI app as a callable
application = wsgi_app
