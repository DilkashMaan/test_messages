# import asyncio
# import websockets


# async def handler(websocket):
#     async for message in websocket:
#         print(f"Received message: {message}")
#         # Echo the received message back to the client
#         await websocket.send(f"Echo: {message}")
#     await websocket.send("Hello, World!")


# async def main():
#     async with websockets.serve(handler, "localhost", 8765):
#         print("WebSocket server started")
#         await asyncio.Future() 



# asyncio.run(main())


# from fastapi import FastAPI, WebSocket
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# @app.get("/")
# async def get():
#     return HTMLResponse("WebSocket server is running.")

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         try:
#             data = await websocket.receive_text()
#             print("Received:", data)
#             await websocket.send_text(f"Echo: {data}")
#         except Exception as e:
#             print("WebSocket connection closed:", e)
#             break


from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()

connected_clients = set()

@app.get("/")
async def get():
    return HTMLResponse("WebSocket server is running.")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            print("Received:", data)
            for client in connected_clients:
                await client.send_text({data})
    except WebSocketDisconnect:
        print("Client disconnected")
        connected_clients.remove(websocket)
    except Exception as e:
        print("WebSocket connection closed with error:", e)
        connected_clients.remove(websocket)

