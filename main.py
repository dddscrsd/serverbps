import asyncio
import os
import websockets

async def handler(websocket):
    print("Client connected")
    try:
        # Сразу шлем «приветствие» — Unity WebGL часто ждёт подтверждения
        await websocket.send('{"type":"hello","status":"ok"}')

        async for message in websocket:
            print("Game sent:", message)
            # Эхо‑ответ: возвращаем то же самое, чтобы соединение жило
            await websocket.send(message)
    except Exception as e:
        print("Disconnected:", e)

async def main():
    # Railway сам даёт порт через переменную окружения
    port = int(os.getenv("PORT", 8080))
    # Создаём сервер (это объект, не корутина)
    server = websockets.serve(handler, "0.0.0.0", port)
    print(f"WebSocket server running on port {port}")
    # Запускаем сервер как корутину
    await server

if __name__ == "__main__":
    asyncio.run(main())

