from flask import Flask
import requests
import jsonpickle

app = Flask(__name__)

@app.route('/getLatest')
def getLatest():
    # Your Firebase Realtime Database URL
    firebase_url = 'https://rpi-greenhouse-bf808-default-rtdb.firebaseio.com/'

    # Your Firebase Realtime Database secret key
    firebase_secret = 'AIzaSyABpXh1DI7Ai4JlO3DSLYdmKEkekH3jkIM'

    # Construct the URL for the Firebase data and sort by timestamp in descending order
    firebase_url += '.json?orderBy="$key"&limitToLast=1'

    # Send a GET request to fetch the latest data from Firebase
    response = requests.get(firebase_url, params={'auth': firebase_secret})

    if response.status_code == 200:
        data = response.json()
        latest_entry = data[list(data.keys())[0]]  # Get the latest entry
        return latest_entry
        # print(f'Latest Data from Firebase: {latest_entry}')
    else:
        print(f"Failed to read data. Status code: {response.status_code}")
        return response.text

@app.route('/getAll')
def getAll():
    # Your Firebase Realtime Database URL
    firebase_url = 'https://rpi-greenhouse-bf808-default-rtdb.firebaseio.com/'

    # Your Firebase Realtime Database secret key
    firebase_secret = 'AIzaSyABpXh1DI7Ai4JlO3DSLYdmKEkekH3jkIM'

    # Construct the URL for the Firebase data
    firebase_url += '.json'

    # Send a GET request to fetch all data from Firebase
    response = requests.get(firebase_url, params={'auth': firebase_secret})

    if response.status_code == 200:
        data = response.json()
        return jsonpickle.encode(data)
        # print('All Data from Firebase:')
        # for d in data:
        #     print(f'Data: {d}')
    else:
        print(f"Failed to read data. Status code: {response.status_code}")
        return response.text

if __name__ == '__main__':
    app.run(debug=True)
