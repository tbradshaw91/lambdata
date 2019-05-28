""" Testing if this actually works
"""

class Dog:
  def __init__(self, name):
      self.name = name
      self.tricks = []

  def add_trick(self, trick):
      self.tricks.append(trick)

class DataCleaner:
  """ A class for cleaning up your data!"""

  def __init__(self, df):
      self.df = df

  def remove_nulls(self):
      self.df

