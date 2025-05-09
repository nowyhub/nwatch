import requests
from typing import Dict


def get_detailed_ip_info(ip_address: str) -> Dict:
    ipapi_data = requests.get(f"https://ipapi.co/{ip_address}/json").json()
    ipapi_com_data = requests.get(
        f"http://ip-api.com/json/{ip_address}").json()

    return {
        "ip": ipapi_data.get("ip"),
        "city": ipapi_data.get("city"),
        "region": ipapi_data.get("region"),
        "country": ipapi_data.get("country_name"),
        "latitude": ipapi_com_data.get("lat"),
        "longitude": ipapi_com_data.get("lon"),
        "timezone": ipapi_com_data.get("timezone"),
        "postal": ipapi_com_data.get("zip"),
        "isp": ipapi_data.get("org"),
        "asn": ipapi_data.get("asn"),
        "country_code": ipapi_data.get("country_code"),
        "currency": ipapi_data.get("currency"),
        "languages": ipapi_data.get("languages"),
        "calling_code": ipapi_data.get("country_calling_code")
    }
