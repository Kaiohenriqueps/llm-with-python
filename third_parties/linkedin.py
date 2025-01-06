import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Kaiohenriqueps/61ba15f83811669904ce6655ed2b7b31/raw/424b89cd0b83f49827573e606d11391574c01d26/kaio-pedroza.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f"Bearer {os.environ['PROXYCURL_API_KEY']}"}
        response = requests.get(
            api_endpoint,
            headers=header_dic,
            params={"url": linkedin_profile_url},
            timeout=10,
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
