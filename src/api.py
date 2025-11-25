from fastapi.routing import APIRouter

from src.schemas.ner import RequestCreateNerTask, NerTaskResponse

from src.services import add_task_to_queue
from src.storage import mock_storage

router = APIRouter(
    prefix="/api",
    tags=["api"],
)


@router.post("/locations")
def get_locations(data: RequestCreateNerTask) -> NerTaskResponse:
    task_id = add_task_to_queue(data)
    return NerTaskResponse(response="ok", task_id=task_id)

@router.get("print")
def print_storage():
    print(mock_storage.data)