import requests
from typing import Dict
import time


def get_detailed_ip_info(ip_address: str) -> Dict:
    result = {
        "ip": ip_address,
        "city": "Unknown",
        "region": "Unknown",
        "country": "Unknown",
        "latitude": "Unknown",
        "longitude": "Unknown",
        "timezone": "Unknown",
        "postal": "Unknown",
        "isp": "Unknown",
        "asn": "Unknown",
        "country_code": "Unknown",
        "currency": "Unknown",
        "languages": "Unknown",
        "calling_code": "Unknown"
    }

    # Try ipapi.co first
    try:
        response = requests.get(f"https://ipapi.co/{ip_address}/json",
                                timeout=5)
        if response.status_code == 200:
            ipapi_data = response.json()
            if "error" not in ipapi_data:
                result.update({
                    "city":
                    ipapi_data.get("city", "Unknown"),
                    "region":
                    ipapi_data.get("region", "Unknown"),
                    "country":
                    ipapi_data.get("country_name", "Unknown"),
                    "isp":
                    ipapi_data.get("org", "Unknown"),
                    "asn":
                    ipapi_data.get("asn", "Unknown"),
                    "country_code":
                    ipapi_data.get("country_code", "Unknown"),
                    "currency":
                    ipapi_data.get("currency", "Unknown"),
                    "languages":
                    ipapi_data.get("languages", "Unknown"),
                    "calling_code":
                    ipapi_data.get("country_calling_code", "Unknown")
                })
    except Exception as e:
        print(f"ipapi.co error: {str(e)}")

    # Add small delay to prevent rate limiting
    time.sleep(1)

    # Try ip-api.com as backup
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}",
                                timeout=5)
        if response.status_code == 200:
            ipapi_com_data = response.json()
            if ipapi_com_data.get("status") == "success":
                result.update({
                    "latitude":
                    ipapi_com_data.get("lat", result["latitude"]),
                    "longitude":
                    ipapi_com_data.get("lon", result["longitude"]),
                    "timezone":
                    ipapi_com_data.get("timezone", result["timezone"]),
                    "isp":
                    ipapi_com_data.get("isp", result["isp"])
                })
    except Exception as e:
        print(f"ip-api.com error: {str(e)}")

    return result
