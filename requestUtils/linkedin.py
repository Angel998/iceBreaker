import os 
import requests
from langchain.serpapi import SerpAPIWrapper

# Retorna la Data de un perfil Linkedin de prueba
def scrape_linkedin_profile_test():
    response = requests.get(
        "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    )
    return getCleanJsonFromLinkedinScrape(response.json())

# Retorna la data de un perfil Linkedin mediante apy nubela
def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )
    return getCleanJsonFromLinkedinScrape(response.json())

# Limpia el contenido de una respuesta JSON de api Linkedin
def getCleanJsonFromLinkedinScrape(jsonData):
    data = {
        k: v
        for k, v in jsonData.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data

# Busca la URL del perfil de Linkedin de una persona segun su nombre con Google
def get_linkedin_profile_url(text: str) -> str:
    """Searches for Linkedin Profile Page"""
    search = SerpAPIWrapper()
    result = search.run(f"{text}")
    return result
