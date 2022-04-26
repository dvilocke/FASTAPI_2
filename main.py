
from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field
from pydantic import EmailStr

from fastapi import FastAPI, Body, Form, Header, Cookie, UploadFile, File
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

'''la clase LoginOut se instancia, se llena el modelo, al tener el modelo listo,
podemos convertir ese modelo a un diccionario, y fastApi lo devuelve por nosotros
en formato JSON'''
@app.post(
    path= '/login/',
    response_model = LoginOut,
    status_code= status.HTTP_200_OK
)
def login(username : str = Form(...), password : str = Form(...)):
    return LoginOut(username = username)


# cookies and Headers Parameters

@app.post(
    path = '/contact',
    status_code= status.HTTP_200_OK
)
def contact(
        first_name : str = Form(
            ...,
            max_length = 20,
            min_length = 1
        ),
        last_name: str = Form(
            ...,
            max_length=20,
            min_length=1
        ),
        email : EmailStr = Form(...),
        message : str = Form(
            ...,
            min_length = 20
        ),
        user_agent : Optional[str] = Header(default=None),
        ads : Optional[str] = Cookie(default=None)
):
    return user_agent

# files
@app.post(
    path = '/post-image/',
    status_code= status.HTTP_200_OK
)
def post_image(
        image : UploadFile = File(...)
):
    return {
        'Filename' : image.filename,
        'Format': image.content_type,
        'Size(kb)' : round(len(image.file.read()) / 1024, ndigits=2)
    }










