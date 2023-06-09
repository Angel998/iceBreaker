import sys
from dotenv import load_dotenv
from config import APP_PATH

# Resolvers para cada caso de uso
import resolvers.basic as resolverBasic
import resolvers.webscrap as resolverWebscrap
import resolvers.agentLinkedin as resolverAgentLinkedin

# Cargar variables de entorno
def loadEnv():
    load_dotenv(APP_PATH + "/.env")

# Obtiene los parametros para ejecucion de resolvers
def getPassedParams():
    response = {
        'resolver': 'basic',
        'param': None
    }
    arguments = sys.argv
    if len(arguments) > 1:
        response['resolver'] = arguments[1].lower()
    if len(arguments) > 2:
        response['param'] = arguments[2]

    return response

def executeResolver(params = {}):
    match params['resolver']:
        case 'basic':
            resolverBasic.mainFuncitoon()
        case 'webscrap':
            resolverWebscrap.mainFunction()
        case 'agent_linkedin':
            resolverAgentLinkedin.mainFunction(params['param'])
        case _:
            print("No hay resolver para: " + params['resolver'])

if __name__ == "__main__":
    loadEnv()
    params = getPassedParams()
    executeResolver(params)
