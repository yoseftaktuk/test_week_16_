from fastapi import FastAPI, HTTPException, APIRouter
# import models
# import utils
from dal import Mongo_qury



app = FastAPI()
router = APIRouter()

@router.get('/employees/engineering/high-salary')
def get_employees_engineering_high_salary():
    try:
        return Mongo_qury.get_engineering_high_salary_employees()
    except HTTPException as e:
        return str(e)
    
@router.get('/employees/by-age-and-role')
def get_employees_by_age_and_role():
    try:
        return Mongo_qury.get_employees_by_age_and_role()
    except HTTPException as e:
        return str(e)

@router.get('/employees/top-seniority') 
def get_employees_top_seniority():
    try:
        return Mongo_qury.get_top_seniority_employees_excluding_hr()
    except HTTPException as e:
        return str(e)

@router.get('/employees/age-or-seniority')
def get_employees_age_or_seniority():
    try: 
        return Mongo_qury.get_employees_by_age_or_seniority()
    except HTTPException as e:
        return str(e)
    
@router.get('/employees/managers/excluding-departments')    
def get_employees_managers_excluding_departments():
    try:
        return Mongo_qury.get_managers_excluding_departments()
    except HTTPException as e:
        return str(e)
    
@router.get('/employees/by-lastname-and-age')   
def get_employees_by_lastname_and_age():
    try: 
        return Mongo_qury.get_employees_by_lastname_and_age()
    except HTTPException as e:
        return str(e)