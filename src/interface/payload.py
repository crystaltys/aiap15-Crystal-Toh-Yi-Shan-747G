import datetime
from pydantic import BaseModel


class Payload(BaseModel):
    onboard_wifi_service : int
    embark_disembark_time_convenient : int
    ease_of_online_booking: int
    gate_location: int
    onboard_dining_service: int
    online_check_in: int
    cabin_comfort: int
    onboard_entertainment: int
    cabin_service: int
    baggage_handling: int
    port_check_in_service: int
    onboard_service : int
    cleanliness : int
    cruise_distance : int
    source_traffic_company_website : int
    source_traffic_search_engine : int
    source_traffic_social_media : int
    is_holiday : int
