import requests

base_url = 'http://127.0.0.1:8000/api/'

def get_licenses_plates():
  """
  get all licenses plates
  """
  response = requests.get(base_url + 'plate/')
  if response.status_code == 200:
    data = response.json()
    return data
  else:
    return 'Error:', response.status_code

def get_license_plate(license_plate):
  """
  get a license plate
  """
  response = requests.get(base_url + 'plate/' + license_plate)
  if response.status_code == 200:
    data = response.json()
    return data
  else:
    return 0

def make_match(license_plate):
  """
  make match, if the license plate is in the database
  """
  if get_license_plate(license_plate):
    return True
  return False

if __name__ == '__main__':
  input_license_plate =input('Enter a license plate: ')
  print(make_match(input_license_plate))
