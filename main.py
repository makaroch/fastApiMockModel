from fastapi import FastAPI

from src.api import router

app = FastAPI()

app.include_router(router)

def run_fast_api():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

def run_calculation():
    from src.services import calculate_locations
    calculate_locations()

if __name__ == "__main__":
    import threading

    t1 = threading.Thread(target=run_fast_api)
    t2 = threading.Thread(target=run_calculation)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")
