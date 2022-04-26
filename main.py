#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel, Field
from pydantic import EmailStr

#FastAPI
from fastapi import HTTPException
from fastapi import FastAPI, Body, Form, Header, Cookie, UploadFile, File, Path
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

@app.post(path='/person/new/', response_model=PersonOut, status_code=status.HTTP_201_CREATED, tags = ['Persons'], summary = 'Create Person in the app')
def create_person(person : Person = Body(...)):
    """
    create Person

    This path operation crate a person in the app and save the information in the database

    Parameters:
    - Request body parameter:
        - **person : Person** -> A Person model with first name, last name, age, hair color and marital status

    returns a person model with first name, last name, age, hair color and marital status
    """
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

# HTTTPException
persons = [
    1,2,3,4,5
]
@app.get(
    path = '/person/detail/{person_id}',
    tags = ['Persons']
)
def show_person(
        person_id : int =  Path(
            ...,
            gt=0,
            example=123
        )
):
    if person_id not in persons:
        #recuerda que ponemos raise porque vamos a generar una exception
        #devemos devolver siempre un status code
        #los detalles tambien
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'This person Doesn exist!'
        )
    else:
        return {
            person_id : "Is Exists!"
        }










