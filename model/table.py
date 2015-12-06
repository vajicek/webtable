
class Table:

  def get_view(self):
    return self.table

  def __init__(self):
    self.table=dict(header=['a','b','c','d'], data=[[1,2,3,4],[5,6,7,8],[9,10,11,12]])
