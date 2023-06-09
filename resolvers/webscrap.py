from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from requestUtils.linkedin import scrape_linkedin_profile_test

# Obtiene la data de un perfil Linkedin de prueba y ejecuta Langchain
def mainFunction():
    profileData = scrape_linkedin_profile_test()
    summary_template = """
        given the information {information} about a person from i want you to create:
        1. a short summary
        2. tow interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    print(chain.run(information=profileData))