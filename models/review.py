#!/usr/bin/python3
"""
Module with class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review
    """
    place_id = ""
    user_id = ""
    text = ""
