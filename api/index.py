from fastapi import FastAPI, Request
from .db import dummy_db
from .entries import PostEntriesInputDTO, EntriesService, PostEntriesOutputDTO

app = FastAPI()


'''
inside every domain endpoint, there must be only one service class. 
This class's job is to take care of the business logic for that domain.
'''


@app.get("/api/entries")
async def get_entries_input_props():
    return EntriesService(dummy_db).get_input_props()


@app.post("/api/entries")
async def post_entries(payload: Request):
    _data = payload.json()
    entries_service = EntriesService(dummy_db)
    data = await _data

    res = entries_service.calculate(PostEntriesInputDTO(**data), rule_id=1)

    payload = PostEntriesOutputDTO(**res)
    return payload
