import asyncio
import websockets

connected_users = set()

async def handler(websocket):
    # Add user
    connected_users.add(websocket)
    try:
        async for message in websocket:
            # Broadcast to all users
            await asyncio.wait([user.send(message) for user in connected_users])
    except:
        pass
    finally:
        connected_users.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server started at ws://localhost:8765")
        await asyncio.Future()  # run forever

asyncio.run(main())
