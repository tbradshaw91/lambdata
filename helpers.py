#!/users/bin/env/python
'''
def any_nulls(X):
  '''
  Checks for Nulls
  '''
  nulls = False
  for col in X.columns:
    col_nulls = X[col].isna().sum()
    if col_nulls != 0:
      nulls = True
      print('The ' + str(col) + ' feature has ' + str(col_nulls) + ' null observations')
    else:
      continue
  if not nulls:
    print('No nulls')



