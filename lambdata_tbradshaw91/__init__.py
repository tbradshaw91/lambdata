#!/usr/bin/env python
"""
lambdata - a collection of Data Science helper functions
"""
import pandas as pd
import numpy as np 
from . import example_module

Y = example_module.increment(example_module.x)
TEST = pd.DataFrame(np.ones(10))

""" For Fun """
class Dog:
  """ Testing Woof """
  def __init__(self, name):
     self.name = name
     self.tricks = []

  def add_trick(self, trick):
      self.tricks.append(trick)

class DataCleaner:
  """A Class for cleaning up your data"""
   def __init__(self, df):
       self.df = df

   def remove_nulls(self):
       self.df

