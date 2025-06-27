from fastapi import APIRouter, Depends, HTTPException

from ..dependencies.auth_dependencies import user_by_token
from ..models.user_models import User
from ..models.workspase_models import WorkSpace, Ingredient
from ..schema.workspace_schema import WorkSpacePostSchema, WorkSpaceGetSchema
from ..schema.responses import MessageResponse, ErrorResponse
from ..services.base import create_model, get_model_by_id, delete_model
from ..services.workspace_services import get_workspaces_by_phone

workspace_router = APIRouter()


@workspace_router.post(
    "/",
    responses={
        200: {'model': MessageResponse},
        400: {'model': ErrorResponse},
        401: {'model': ErrorResponse},
    },
    response_model=MessageResponse
)
async def post_workspace(workspace: WorkSpacePostSchema, user: User = Depends(user_by_token)):
    new_workspace = WorkSpace(**workspace.model_dump())
    new_workspace.user_phone = user.phone
    await create_model(new_workspace)
    return {"message": f"WorkSpace {new_workspace.name} created!"}


@workspace_router.get(
    "/",
    responses={
        200: {'model': list[WorkSpaceGetSchema]},
        400: {'model': ErrorResponse},
        401: {'model': ErrorResponse},
    },
    response_model=list[WorkSpaceGetSchema]
)
async def get_workspace(user: User = Depends(user_by_token)):
    return await get_workspaces_by_phone(user.phone)


@workspace_router.delete(
    "/<workspace_id>",
    responses={
        200: {'model': MessageResponse},
        400: {'model': ErrorResponse},
        401: {'model': ErrorResponse},
    },
    response_model=MessageResponse
)
async def delete_work(workspace_id: int, user: User = Depends(user_by_token)):
    workspace = await get_model_by_id(WorkSpace, workspace_id)
    if not workspace:
        raise HTTPException(status_code=400, detail="Not exists")
    if user.phone != workspace.user_phone:
        raise HTTPException(status_code=400, detail="Not your workspace")
    await delete_model(workspace)
    return {"message" : "deleted"}





