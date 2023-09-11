from fastapi import FastAPI, Request
from api.model import Kind, Measurement, Tax, TaxType, Rule
from api.entries import PostEntriesInputDTO, EntriesService, PostEntriesOutputDTO

app = FastAPI()

# mock database.
dummy_db = {
    "rules": {
        1: Rule(1, "Default", 0.05)
    },
    "kinds": {
        1: Kind(1, "Food"),
        2: Kind(2, "Medical"),
        3: Kind(
            3, "Book"),
        4: Kind(4, "Cosmetic"),
        5: Kind(5, "Others")
    },
    "measurements": {
        1: Measurement(1, "box"),
        2: Measurement(2, "bar"),
        3: Measurement(3, "bottle"),
        4: Measurement(4, "packet")
    },
    "taxes": {
        1: Tax(1, "Value Added Tax", 1, 10, [1, 2, 3]),
        2: Tax(2, "Import", 2, 5)
    },
    "tax_type": {
        1: TaxType(1, "Sales Tax"),
        2: TaxType(2, "Duty Tax"),
    },
    "entries": {},
    "products": {},
}


@app.get("/api/entries")
async def get_entries_input_props():
    return EntriesService(dummy_db).get_input_props()


@app.post("/api/entries")
async def post_entries(payload: Request):
    data = payload.json()
    entries_service = EntriesService(dummy_db)

    res = entries_service.calculate(PostEntriesInputDTO(** await data), rule_id=1)

    payload = PostEntriesOutputDTO(**res)
    return payload
