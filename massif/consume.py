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


def is_banned(license_plate):
    """
    check if the license plate is banned
    """
    if make_match(license_plate):
        data = get_license_plate(license_plate)
        if data['status'] == 'BANNED':
            return True
        return False
    return 'License plate not found'


def post_captured_plates(files, data):
    # Send a POST request to the API endpoint with the file data and form data
    upload_url = base_url + 'plate_captured/'
    response = requests.post(upload_url, files=files, data=data)

    # Check the response status code
    if response.status_code == 201:
        # Image upload successful
        print('Image uploaded successfully!')
        print('Image URL:', response.json()['image_license'])
    else:
        # Image upload failed
        print('Image upload failed:', response.text)


if __name__ == '__main__':
    input_license_plate = input('Enter a license plate: ')
    print(is_banned(input_license_plate))
