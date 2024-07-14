from api.api import api_router
from views.api import views_router
from fastapi import APIRouter


router = APIRouter()
# 视图路由
router.include_router(views_router)
# API路由
router.include_router(api_router)


# @router.get("/")
# def index():
#     return {"message": "Hello World"}

