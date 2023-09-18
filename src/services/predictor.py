import json
import yaml
import joblib
import numpy as np
from fastapi import HTTPException
from src.interface.payload import Payload
from src.interface.response import Results
from datetime import datetime
from datetime import date


class Predict:

    def __init__(self, cfg_filepath):
        self._cfg = None

        with open(cfg_filepath, "r") as ymlfile:
            self._cfg = yaml.safe_load(ymlfile)

            self.scaler_mod = self._cfg['enc-path']['joblib_path']
            self.rfc = self._cfg['rfc-path']['joblib_path']

    def process(self, payload: Payload):
       if payload is None:
            raise HTTPException(status_code=422, detail="Request payload is empty")
       
       ticket_mapping = {
           0 : 'Deluxe',
           1 : 'Luxury',
           2 : 'Standard'
       }

       ord = [
            payload.onboard_wifi_service,
            payload.embark_disembark_time_convenient,
            payload.ease_of_online_booking,
            payload.gate_location,
            payload.onboard_dining_service,
            payload.online_check_in,
            payload.cabin_comfort,
            payload.onboard_entertainment,
            payload.cabin_service,
            payload.baggage_handling,
            payload.port_check_in_service,
            payload.onboard_service,
            payload.cleanliness,
            payload.cruise_distance
            ]
       usr_input = np.append(self.run_standard_scaling(ord) ,np.array([payload.source_traffic_company_website, payload.source_traffic_search_engine,
                                                     payload.source_traffic_social_media, payload.is_holiday]))
       callback = ticket_mapping[self.run_rfc(usr_input)]
       return Results(ticket_res=callback)
        
    def run_standard_scaling(self, numerics: list):
        loaded_scaler = joblib.load(self.scaler_mod)
        scaled_new_data = loaded_scaler.transform(np.array([numerics]))[0]  # Replace 'new_data' with your new data
        return scaled_new_data
    
    def run_rfc(self, input):
        loaded_kmeans = joblib.load(self.rfc)
        res = loaded_kmeans.predict(np.array([input]))[0]
        return res
    
    def run(self, scaled_data):
        pca_res = self.run_pca(scaled_data)
        res = self.run_kmeans(pca_res)
        return res

    
    