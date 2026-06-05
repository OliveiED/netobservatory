import geoip2.database

# =========================
# MAXMIND DATABASES
# =========================

CITY_DB = "/root/geoip/GeoLite2-City.mmdb"
ASN_DB = "/root/geoip/GeoLite2-ASN.mmdb"

# =========================
# LOAD READERS
# =========================

city_reader = geoip2.database.Reader(CITY_DB)
asn_reader = geoip2.database.Reader(ASN_DB)

# =========================
# GEOIP LOOKUP
# =========================

def get_geoip_data(ip):

    result = {
        "country": None,
        "city": None,
        "asn": None,
        "as_org": None
    }

    try:

        city_response = city_reader.city(ip)

        result["country"] = city_response.country.name
        result["city"] = city_response.city.name

    except Exception:
        pass

    try:

        asn_response = asn_reader.asn(ip)

        result["asn"] = asn_response.autonomous_system_number
        result["as_org"] = (
            asn_response.autonomous_system_organization
        )

    except Exception:
        pass

    return result
