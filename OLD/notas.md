"""#### Connecting with MongoDB for VS Code

Quando perguntei como faríamos para aceder ou submeter ficheiros na BD em código, a professora respondeu que podíamos fazer isso manualmente e que não seria exigido por agora. No entanto, fui pesquisar, e aqui está:

Tive problemas ao testar, após aplicar a *connection string* (passo 3). Posso estar a fazer algo de errado no setup/criação da BD no Mongo ou pode ser apenas da conexão UMinho que não permite.

1. **Instalar MongoDB for VS Code**:  
    - No VS Code, abre "Extensions" na navegação à esquerda e procura por "MongoDB for VS Code". Seleciona a extensão e clica em instalar.

2. **No VS Code, abrir o Command Palette**:
    - Clica em "View" e abre "Command Palette".
    - Pesquisa por "MongoDB: Connect" no Command Palette e clica em "Connect with Connection String".

3. **Conectar ao seu deployment MongoDB**:
    - Cola a *connection string* no Command Palette:
    
    `mongodb+srv://**bigdata:bioinfo24**@bigdata.l3at7tn.mongodb.net/`

A senha para *bigdata* está incluída na *connection string* para a sua configuração inicial. Esta senha não estará disponível novamente após sair deste fluxo de conexão.

Clique em “Create New Playground” no MongoDB for VS Code para começar."""


#troubleshoot?
import pymongo
from urllib.parse import quote_plus

username = quote_plus('<username>')
password = quote_plus('<password>')
cluster = '<clusterName>'
authSource = '<authSource>'
authMechanism = '<authMechanism>'

uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism

client = pymongo.MongoClient(uri)

result = client["<dbName"]["<collName>"].find()

# print results
for i in result:
    print(i)
