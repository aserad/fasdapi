from fastapi import APIRouter
# from api.endpoints.test import test_oauth2
# from api.endpoints import user, role, access, websocket
# from api.extends import sms, wechat, cos

api_router = APIRouter(prefix="/api/v1")
# api_router.post("/test/oath2", tags=["测试oauth2授权"])(test_oauth2)
# api_router.include_router(user.router, prefix='/admin', tags=["用户管理"])
# api_router.include_router(role.router, prefix='/admin', tags=["角色管理"])
# api_router.include_router(access.router, prefix='/admin', tags=["权限管理"])
# api_router.include_router(websocket.router, prefix='/ws', tags=["WebSocket"])
# api_router.include_router(wechat.router, prefix='/wechat', tags=["微信授权"])
# api_router.include_router(sms.router, prefix='/sms', tags=["短信接口"])
# api_router.include_router(cos.router, prefix='/cos', tags=["对象存储接口"])

