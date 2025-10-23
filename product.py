#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Product:
    def __init__(self, _name: str, _stock: int, _price: float, _is_unit: bool):
        self.name: str = _name
        self.stock: int = _stock
        self.price: float = _price
        self.is_unit: bool = _is_unit
