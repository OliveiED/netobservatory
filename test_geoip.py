from app.services.geoip_service import get_geoip


result = get_geoip("8.8.8.8")

print(result)
