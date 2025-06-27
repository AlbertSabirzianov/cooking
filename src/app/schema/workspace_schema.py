from pydantic import BaseModel


class WorkSpacePostSchema(BaseModel):
    name: str
    color: str


class WorkSpaceGetSchema(WorkSpacePostSchema):
    id: int
