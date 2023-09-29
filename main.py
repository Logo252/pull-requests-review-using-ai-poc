from fastapi import FastAPI
from typing import List

app = FastAPI()

# Global variable used for storing data (bad practice)
data = []


# Inefficient data manipulation
@app.post("/add_item")
def add_item(item: str):
    global data
    data.append(item)
    return {"message": "Item added successfully"}


# Insecure API endpoint with missing authentication
@app.get("/get_items")
def get_items():
    return data


@app.get("/get_item/{item_id}")
def get_item(item_id: int):
    return data[item_id]


@app.put("/update_item/{item_id}")
def update_item(item_id: int, new_item: str):
    if 0 <= item_id < len(data):
        data[item_id] = new_item
        return {"message": f"Item at index {item_id} updated successfully"}
    else:
        return {"message": "Item not found"}

# Lack of input validation
@app.post("/divide")
def divide_numbers(dividend: float, divisor: float):
    return {"result": dividend / divisor}


# Inconsistent naming and lack of documentation
@app.get("/fetch-data")
def fetchData():
    """
    Fetches data from the server.
    """
    return {"message": "Data fetched successfully"}


# Use of hard-coded values
@app.get("/config")
def get_config():
    config = {
        "api_key": "my-secret-key",
        "db_host": "localhost",
        "db_port": 5432,
    }
    return config


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
