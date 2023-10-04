from fake_useragent import UserAgent
from requests.exceptions import ConnectionError
from requests_cache import CachedSession


def validate_image_url(url: str) -> bool:        
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    session = CachedSession("requests_cache", expire_after=600)
    try:
        r = session.head(url, headers={"User-agent": UserAgent().random})
        if r.headers["content-type"] in image_formats:
            return True
    except ConnectionError:
        pass

    return False