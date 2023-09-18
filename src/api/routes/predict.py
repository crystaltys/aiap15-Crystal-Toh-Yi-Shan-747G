import httpx
from fastapi import APIRouter, HTTPException
from starlette.requests import Request
from src.interface.payload import Payload
from src.interface.response import Results
from src.services.predictor import Predict


router = APIRouter()

@router.post("/data", response_model=Results) # listens for POST request at cluster_data
async def post_predict(request: Request, block_data: Payload = None) -> Results:
    try:
        engine: Predict = request.app.state.engine
        ticket_result: Results = engine.process(block_data)
        return ticket_result
        
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=f"HTTP Error: {str(e)}")