from uuid import UUID

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status
from fastapi.responses import HTMLResponse

from app.container import CONTAINER
from app.services.schemas.game import GameCreateSchema, GameSchema
from app.services.types.game_status import GameStatusType


router = APIRouter(prefix="/games", tags=["GAMES"])


@router.post("", summary="Create game", status_code=status.HTTP_201_CREATED)
async def create_game(game: GameCreateSchema) -> None:
    """Create game."""
    service = CONTAINER.game_service()
    await service.create(game=game)


@router.get("", summary="Get games")
async def get_games(
    status: GameStatusType | None = None,
    presenter_uuid: UUID | None = None,
    package_uuid: UUID | None = None,
) -> list[GameSchema]:
    """Get games."""
    service = CONTAINER.game_service()
    await service.get_all(status=status, presenter_uuid=presenter_uuid, package_uuid=package_uuid)

    return []


@router.get("/{uuid}", summary="Get game by UUID")
async def get_game_by_uuid(uuid: UUID) -> GameSchema:
    """Get game by UUID."""
    service = CONTAINER.game_service()
    return await service.get(uuid=uuid)


connections: dict[UUID, list[WebSocket]] = {}


@router.websocket("/{uuid}")
async def start_game(websocket: WebSocket, uuid: UUID) -> GameSchema:
    """Start game."""
    try:
        await websocket.accept()

        if not connections.get(uuid):
            connections[uuid] = []

        connections[uuid].append(websocket)

        print(connections)
        while True:
            data = await websocket.receive_text()

            for websock in connections[uuid]:
                await websock.send_text(f"Game: {uuid}. Message sent was: {data}")
    except WebSocketDisconnect:
        print(f"Removed websocket: {websocket}")
        connections[uuid].remove(websocket)


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>

            <br/><br/>
            <input onclick="sendAnswer1(event)" type="button" id="player1"
                value="Player1" autocomplete="off"/>
            <input onclick="sendAnswer2(event)" type="button" id="player2"
                value="Player2" autocomplete="off"/>

        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket(
                "ws://localhost:8080/api/v1/games/a270b5c1-b35b-430d-9c97-86dbd64aa994"
            );
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };

            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }

            function sendAnswer1(event) {
                var input = document.getElementById("player1")
                ws.send(input.id)
                event.preventDefault()
            }
            function sendAnswer2(event) {
                var input = document.getElementById("player2")
                ws.send(input.id)
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@router.get("/chat/chat")
async def chat() -> HTMLResponse:
    return HTMLResponse(html)
