#%%

import requests
import json

#%%
json_data = {"parameter": {"state_name": "Bayela", "lga": 108, "sector": "RURAL", "credit_mean": 70, "income_mean": 600}}
URL = 'http://127.0.0.1:8000/predict'

def request_prediction(URL: str, data: dict) -> int:
    """
    This function accepts

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
    #return response
    prediction = json.loads(response)['emission']
    return round(prediction)


#%%
deployed_url = 'https://emission--api.herokuapp.com/predict'

#%%
request_prediction(URL=deployed_url, data=json_data)
    
  
#%%
requests.get(url='https://emission--api.herokuapp.com/')    
    
    
    
# %%
# req = requests.post(url=URL,
#               json=json_data
#               )

# response = req.content
# prediction = json.loads(response)['emission']
# round(prediction, 2)



# echo '{"parameter": {"state_name": "Bayela", "lga": 108, "sector": "RURAL", "credit_mean": 70, "income_mean": 600}}' | http POST http://127.0.0.1:8000/predict

# {"parameter": {"state_name": "Bayela", "lga": 108, "sector": "RURAL", "credit_mean": 70, "income_mean": 600}}


# %%
