#%%

import requests
import json
from constant import API_URL

#%%
json_data = {"parameter": {"state_name": "Bayela", "lga": 108, "sector": "RURAL", "credit_mean": 70, "income_mean": 600}}
URL = 'http://127.0.0.1:8000/predict'

def request_prediction(URL: str, data: dict) -> int:
    """
    This function accepts API url link and data, makes a request to 
    machine learning API and returns the prediction result in 2 decimal places

    Parameters
    ----------
    URL : str
        The API link.
    data : dict
        input data to be used for prediction.

    Returns
    -------
    int
        prediction.

    """
    req = requests.post(url=URL, json=data)
    response = req.content
    prediction = json.loads(response)['emission']
    return round(prediction)

#%%
request_prediction(URL=URL, data=json_data)
    
    
# %%
API_URL
# %%
