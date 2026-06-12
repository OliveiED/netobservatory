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
# CACHE
# =========================

geo_cache = {}

MAX_CACHE_SIZE = 100000

# =========================
# GEOIP LOOKUP
# =========================

def get_geoip_data(ip):

    # Retorna do cache
    if ip in geo_cache:
        return geo_cache[ip]

    result = {
        "country": None,
        "city": None,
        "asn": None,
        "as_org": None
    }

    # ---------------------
    # CITY
    # ---------------------

    try:

        city_response = city_reader.city(ip)

        result["country"] = (
            city_response.country.name
        )

        result["city"] = (
            city_response.city.name
        )

    except Exception:
        pass

    # ---------------------
    # ASN
    # ---------------------

    try:

        asn_response = asn_reader.asn(ip)

        result["asn"] = (
            asn_response.autonomous_system_number
        )

        result["as_org"] = (
            asn_response.autonomous_system_organization
        )

    except Exception:
        pass

    # ---------------------
    # CACHE SAVE
    # ---------------------

    if len(geo_cache) >= MAX_CACHE_SIZE:

        # Limpa cache quando atingir limite
        geo_cache.clear()

    geo_cache[ip] = result

    return result
