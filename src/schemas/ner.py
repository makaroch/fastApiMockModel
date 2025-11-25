from pydantic import BaseModel, UUID4


class RequestCreateNerTask(BaseModel):
    text: str
    sleep: int


class NerTask(RequestCreateNerTask):
    task_id: UUID4


class NerTaskResponse(BaseModel):
    response: str
    task_id: UUID4
