from zeep import Client, Settings
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

def check(word):
    url = data['url']
    settings = Settings(strict=False)
    client = Client(wsdl=url, settings=settings)
    #print(client.service.checkText('tabl')[0]['s'])
    return client.service.checkText(word)[0]['s']