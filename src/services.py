from uuid import uuid4
from queue import Queue

from src.schemas.ner import NerTask, RequestCreateNerTask
from src.storage import mock_storage
from src.utils import get_locations

some_queue = Queue()


def add_task_to_queue(task: RequestCreateNerTask) -> uuid4:
    task_id = uuid4()
    some_queue.put(
        NerTask(
            text=task.text,
            sleep=task.sleep,
            task_id=task_id
        )
    )
    return task_id


def get_result(task_id: uuid4) -> list[str] | None:
    return mock_storage.get(task_id)


def calculate_locations():
    while True:
        task = some_queue.get()
        print(task)
        # if task is None:
        #     continue
        locations = get_locations(task.text, task.sleep)
        mock_storage.set(task.task_id, locations)
        some_queue.task_done()
