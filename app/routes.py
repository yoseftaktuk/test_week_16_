from fastapi import FastAPI, HTTPException, APIRouter
import models
import utils



app = FastAPI()
router = APIRouter()

@router.