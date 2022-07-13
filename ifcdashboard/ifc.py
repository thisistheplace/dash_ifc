from typing import DefaultDict
import ifcopenshell
from collections import defaultdict
import pandas as pd
import time

from .constants import IFC_TYPES

class IfcProducts:
    def __init__(self, data: list):
        self._data = data
        self._df = None
    
    @property
    def data(self):
        return self._data

    @property
    def df(self) -> pd.DataFrame:
        if self._df is None:
            output = defaultdict(list)
            for prod in self._data:
                [output[k].append(v) for k, v in prod.get_info().items()]
            self._df = pd.DataFrame.from_dict(output)
        return self._df


class IfcFile:
    def __init__(self, ifc_str):
        now = time.time()
        self._file = ifcopenshell.file.from_string(ifc_str)
        print(f"Loading time: {time.time() - now}")
        self._products = self.load_products()

    def load_products(self):
        products = {}
        for prod_type in IFC_TYPES:
            products[prod_type] = IfcProducts(self._file.by_type(prod_type))
        return products

    @property
    def product_count(self) -> pd.DataFrame:
        """ Dataframe of product counts in IFC data """
        products = {}
        for prod_type in IFC_TYPES:
            products[prod_type] = [len(self._products[prod_type].data)]
        return pd.DataFrame.from_dict(products)
    
    def get_product(self, prod_type: str) -> pd.DataFrame:
        """ Dataframe of product info """
        if prod_type in self._products:
            return self._products[prod_type].df
        else:
            raise KeyError(f"Product type {prod_type} does not exist")
