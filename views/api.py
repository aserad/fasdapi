from fastapi import APIRouter
from views.viewpoints import home

views_router = APIRouter()

views_router.include_router(home.router)

