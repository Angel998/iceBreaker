from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from requestUtils.linkedin import scrape_linkedin_profile
from appAgents.linkedin import agent_get_linkedin_profile_url

def mainFunction(personName = "Eden Marco"):
    linkedin_profile_url = agent_get_linkedin_profile_url(personName)
    summary_template = """
        given the Linkedin information {information} about a person from i want you to create:
        1. a short summary
        2. tow interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)
    print(chain.run(information=linkedin_data))