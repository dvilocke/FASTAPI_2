
from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field

from fastapi import FastAPI, Body, Form
from fastapi import  status


app = FastAPI()

#creation of the models
class HairColor(Enum):
    white = 'white'
    brown = 'brown'
    black = 'black'
    blonde = 'blonde'
    red = 'red'

class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Miguel'
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Ramirez'
    )
    age: int = Field(
        ...,
        gt=0,
        lt=115,
        example=22
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)


class Person(PersonBase):
    password : str = Field(..., min_length=8)

class PersonOut(PersonBase):
    pass

class LoginOut(BaseModel):
    #Field() campo del modelo
    username : str = Field(default=..., max_length = 20, example = 'miguel2021', description='esto sirve')
    message: str = Field(default='Login Succesfully')

@app.get(path='/', status_code=status.HTTP_200_OK)
def home():
    return {

    }

@app.post(path='/person/new/', response_model=PersonOut, status_code=status.HTTP_201_CREATED)
def create_person(
        person : Person = Body(...)
):
    return person

@app.post(
    path= '/login/',
    response_model = LoginOut,
    status_code= status.HTTP_200_OK
)
def login(username : str = Form(...), password : str = Form(...)):
    return LoginOut(username = username)








