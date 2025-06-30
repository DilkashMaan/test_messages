import asyncio
import websockets


async def handler(websocket):
    async for message in websocket:
        print(f"Received message: {message}")
        # Echo the received message back to the client
        await websocket.send(f"Echo: {message}")
    await websocket.send("Hello, World!")


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server started")
        await asyncio.Future() 



asyncio.run(main())


 





