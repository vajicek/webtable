
class Table:

  def get_index(self, row_id):
    return [indx for indx, row in enumerate(self.table['data']) if row[0] == row_id]

  def get_view(self):
    return self.table

  def get_item(self, row_id):
    indices = self.get_index(row_id)
    if indices:
      return self.table['data'][indices[0]]
    return None

  def set_item(self, row_id, value):
    indices = self.get_index(row_id)
    if indices:
      self.table['data'][indices[0]] = value
    else:
      self.table['data'] += [value]

  def remove_item(self, row_id):
    indices = self.get_index(row_id)
    if indices:
      del self.table['data'][indices[0]]

  def __init__(self):
    self.table=dict(
                    typeRenderer=dict(action='actionRenderer'),
                    cellType=['str','str','str','action'],
                    header=['#','name','id','action'],
                    data=[[1,2,3,[dict(action='remove', param='1', label='Remove'), dict(action='edit', param='1', label='Edit')]],
                          [5,6,7,[dict(action='remove', param='5', label='Remove'), dict(action='edit', param='5', label='Edit')]],
                          [9,10,11,[dict(action='remove', param='9', label='Remove'), dict(action='edit', param='9', label='Edit')]]])
