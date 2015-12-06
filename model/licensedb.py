import sys

from LicenseDatabase import LicenseDatabase

class LicenseTable:

  def get_list(self):
    table=dict(typeRenderer=dict(action='actionRenderer'),
               cellType=['str','action'],
               header=['#','action'], data=[])
    lic_keys = self.db.GetLicenses()
    for key in lic_keys:
      table['data'] += [[key,[dict(action='edit', param=key, label='Edit')]]]
    return table

  def get_item(self, row_id):
    lic = self.db.GetLicense(str(row_id))
    return lic

  def set_item(self, row_id, value):
    self.db.PutLicense(value[0])

  def remove_item(self, row_id):
    pass

  def __init__(self, filename):
    self.db = LicenseDatabase(filename)
