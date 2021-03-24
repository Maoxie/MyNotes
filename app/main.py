#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
@author: yangzhitao
@license: 
@contact: yangzhitao@sensetime.com
@software: pycharm
@time: 2021/3/24 16:59
@desc: 
"""
import os
from pathlib import Path
import sys
from typing import Dict

from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel

from app.utils.shell_tools import shell

PRJ_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PRJ_ROOT))

app = FastAPI()
print(f"TOKEN: {os.environ['MY_NOTES_TOKEN']}")


class RequestBody(BaseModel):
    token: str


class Response(BaseModel):
    code: int = 200
    msg: str = "success"
    content: Dict = {}


@app.post("/api/rebuild/", response_model=Response)
async def rebuild(body: RequestBody, background_tasks: BackgroundTasks):
    token = os.environ["MY_NOTES_TOKEN"]
    if body.token == token:
        background_tasks.add_task(rebuild_docs_handler)
        return Response(msg="Start rebuilding")
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


def rebuild_docs_handler():
    commands = (
        "cd {PRJ_ROOT / 'docs'} && git pull -f",
        "cd {PRJ_ROOT} && python3 -m mkdocs build",
    )
    for cmd in commands:
        shell.run(cmd)
