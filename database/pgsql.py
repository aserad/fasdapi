from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os


# -----------------------数据库配置-----------------------------------
DB_ORM_CONFIG = {
    "connections": {
        "base": {
            # 'engine': 'tortoise.backends.mysql',  # mysql
            'engine':  'tortoise.backends.asyncpg',
            "credentials": {
                'host': os.getenv('DB_HOST', '127.0.0.1'),
                'user': os.getenv('DB_USER', 'postgres'),
                'password': os.getenv('DB_PASSWORD', 'postgres'),
                'port': int(os.getenv('DB_PORT', 5432)),
                'database': os.getenv('DB_NAME', 'fasdapi'),
            }
        },
        # "db2": {
        #     'engine': 'tortoise.backends.mysql',
        #     "credentials": {
        #         'host': os.getenv('DB2_HOST', '127.0.0.1'),
        #         'user': os.getenv('DB2_USER', 'root'),
        #         'password': os.getenv('DB2_PASSWORD', '123456'),
        #         'port': int(os.getenv('DB2_PORT', 3306)),
        #         'database': os.getenv('DB2_DB', 'db2'),
        #     }
        # },
        # "db3": {
        #     'engine': 'tortoise.backends.mysql',
        #     "credentials": {
        #         'host': os.getenv('DB3_HOST', '127.0.0.1'),
        #         'user': os.getenv('DB3_USER', 'root'),
        #         'password': os.getenv('DB3_PASSWORD', '123456'),
        #         'port': int(os.getenv('DB3_PORT', 3306)),
        #         'database': os.getenv('DB3_DB', 'db3'),
        #     }
        # },

    },
    "apps": {
        "base": {"models": ["models.base", "aerich.models"], "default_connection": "base"},
        # "db2": {"models": ["models.db2"], "default_connection": "db2"},
        # "db3": {"models": ["models.db3"], "default_connection": "db3"}
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}


async def register_pgsql(app: FastAPI):
    # 注册数据库
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=False,   # 启动服务时是否自动创建表结构
        add_exception_handlers=False,
    )
