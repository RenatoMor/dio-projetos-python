
# Install FastAPI, Uvicorn, and Pyngrok----------------------------------------------
!pip install fastapi nest-asyncio pyngrok uvicorn
# Sample Output----------------------------------------------------------------------
'''Collecting fastapi
  Downloading fastapi-0.100.1-py3-none-any.whl (65 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.8/65.8 kB 1.6 MB/s eta 0:00:00
Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.10/dist-packages (1.5.6)
Collecting pyngrok
  Downloading pyngrok-6.0.0.tar.gz (681 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 681.2/681.2 kB 13.3 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Collecting uvicorn
  Downloading uvicorn-0.23.2-py3-none-any.whl (59 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 59.5/59.5 kB 6.2 MB/s eta 0:00:00
Requirement already satisfied: pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,<3.0.0,>=1.7.4 in /usr/local/lib/python3.10/dist-packages (from fastapi) (1.10.12)
Collecting starlette<0.28.0,>=0.27.0 (from fastapi)
  Downloading starlette-0.27.0-py3-none-any.whl (66 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.0/67.0 kB 6.7 MB/s eta 0:00:00
Requirement already satisfied: typing-extensions>=4.5.0 in /usr/local/lib/python3.10/dist-packages (from fastapi) (4.7.1)
Requirement already satisfied: PyYAML in /usr/local/lib/python3.10/dist-packages (from pyngrok) (6.0.1)
Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.10/dist-packages (from uvicorn) (8.1.6)
Collecting h11>=0.8 (from uvicorn)
  Downloading h11-0.14.0-py3-none-any.whl (58 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.3/58.3 kB 6.1 MB/s eta 0:00:00
Requirement already satisfied: anyio<5,>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from starlette<0.28.0,>=0.27.0->fastapi) (3.7.1)
Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.4.0->starlette<0.28.0,>=0.27.0->fastapi) (3.4)
Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.4.0->starlette<0.28.0,>=0.27.0->fastapi) (1.3.0)
Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.4.0->starlette<0.28.0,>=0.27.0->fastapi) (1.1.2)
Building wheels for collected packages: pyngrok
  Building wheel for pyngrok (setup.py) ... done
  Created wheel for pyngrok: filename=pyngrok-6.0.0-py3-none-any.whl size=19866 sha256=8b5e05c31feb018225990990d28a77d98ef9dd552fd66875981ab75e07fed29e
  Stored in directory: /root/.cache/pip/wheels/5c/42/78/0c3d438d7f5730451a25f7ac6cbf4391759d22a67576ed7c2c
Successfully built pyngrok
Installing collected packages: pyngrok, h11, uvicorn, starlette, fastapi
Successfully installed fastapi-0.100.1 h11-0.14.0 pyngrok-6.0.0 starlette-0.27.0 uvicorn-0.23.2'''


# Install Flask and Flask-ngrok-------------------------------------------------------
!pip install flask_ngrok
# Sample Output-----------------------------------------------------------------------
'''Collecting flask_ngrok
  Downloading flask_ngrok-0.0.25-py3-none-any.whl (3.1 kB)
Requirement already satisfied: Flask>=0.8 in /usr/local/lib/python3.10/dist-packages (from flask_ngrok) (2.2.5)
Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from flask_ngrok) (2.27.1)
Requirement already satisfied: Werkzeug>=2.2.2 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask_ngrok) (2.3.6)
Requirement already satisfied: Jinja2>=3.0 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask_ngrok) (3.1.2)
Requirement already satisfied: itsdangerous>=2.0 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask_ngrok) (2.1.2)
Requirement already satisfied: click>=8.0 in /usr/local/lib/python3.10/dist-packages (from Flask>=0.8->flask_ngrok) (8.1.6)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->flask_ngrok) (1.26.16)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->flask_ngrok) (2023.7.22)
Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests->flask_ngrok) (2.0.12)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->flask_ngrok) (3.4)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from Jinja2>=3.0->Flask>=0.8->flask_ngrok) (2.1.3)
Installing collected packages: flask_ngrok
Successfully installed flask_ngrok-0.0.25'''

# Install FastAPI--------------------------------------------------------------------
!pip install fastapi
# Sample Output----------------------------------------------------------------------
'''Requirement already satisfied: fastapi in /usr/local/lib/python3.10/dist-packages (0.100.1)
Requirement already satisfied: pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,<3.0.0,>=1.7.4 in /usr/local/lib/python3.10/dist-packages (from fastapi) (1.10.12)
Requirement already satisfied: starlette<0.28.0,>=0.27.0 in /usr/local/lib/python3.10/dist-packages (from fastapi) (0.27.0)
Requirement already satisfied: typing-extensions>=4.5.0 in /usr/local/lib/python3.10/dist-packages (from fastapi) (4.7.1)
Requirement already satisfied: anyio<5,>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from starlette<0.28.0,>=0.27.0->fastapi) (3.7.1)
Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.4.0->starlette<0.28.0,>=0.27.0->fastapi) (3.4)
Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.4.0->starlette<0.28.0,>=0.27.0->fastapi) (1.3.0)
Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3.4.0->starlette<0.28.0,>=0.27.0->fastapi) (1.1.2)'''

# Importing Libraries---------------------------------------------------------------
import pandas as pd
import json
from fastapi import FastAPI
import nest_asyncio
from pyngrok import ngrok
import uvicorn

# Creating FastAPI instance---------------------------------------------------------
base_dados_fapi = pd.read_excel('/content/content/base_dados_flaskApi.xlsx')
print(base_dados_fapi)
# Sample Output---------------------------------------------------------------------
'''ANALISTA SEXO  FILHOS  IDADE  SALÁRIO NÍVEL UNIDADE
0        Paulo    M       4     48     2678    N2      SP
1        Pedro    M       3     26     2540    N2      SP
2         Alex    M       4     44     2353    N1      SP
3          Ana    F       4     47     2622    N2      SP
4      Vanessa    F       0     27     2087    N1      SP
5       Suzana    F       4     42     2364    N1      SP
6       Renata    F       3     34     2234    N1      SP
7      Mathias    M       0     46     2378    N1      SP
8        Vitor    M       4     26     2453    N1      SP
9       Manoel    M       2     26     2536    N2      SP
10     Leandro    M       2     34     2590    N2      SP'''

# Creating json file---------------------------------------------------------------
base_dados_fapi_json = base_dados_fapi.to_json(orient='records')
print(base_dados_fapi_json)
# Sample Output---------------------------------------------------------------------
'''[{"ANALISTA":"Paulo","SEXO":"M","FILHOS":4,"IDADE":48,"SAL\u00c1RIO":2678,"N\u00cdVEL":"N2","UNIDADE":"SP"},{"ANALISTA":"Pedro","SEXO":"M","FILHOS":3,"IDADE":26,"SAL\u00c1RIO":2540,"N\u00cdVEL":"N2","UNIDADE":"SP"},{"ANALISTA":"Alex","SEXO":"M","FILHOS":4,"IDADE":44,"SAL\u00c1RIO":2353,"N\u00cdVEL":"N1","UNIDADE":"SP"},{"ANALISTA":"Ana","SEXO":"F","FILHOS":4,"IDADE":47,"SAL\u00c1RIO":2622,"N\u00cdVEL":"N2","UNIDADE":"SP"},{"ANALISTA":"Vanessa","SEXO":"F","FILHOS":0,"IDADE":27,"SAL\u00c1RIO":2087,"N\u00cdVEL":"N1","UNIDADE":"SP"},{"ANALISTA":"Suzana","SEXO":"F","FILHOS":4,"IDADE":42,"SAL\u00c1RIO":2364,"N\u00cdVEL":"N1","UNIDADE":"SP"},{"ANALISTA":"Renata","SEXO":"F","FILHOS":3,"IDADE":34,"SAL\u00c1RIO":2234,"N\u00cdVEL":"N1","UNIDADE":"SP"},{"ANALISTA":"Mathias","SEXO":"M","FILHOS":0,"IDADE":46,"SAL\u00c1RIO":2378,"N\u00cdVEL":"N1","UNIDADE":"SP"},{"ANALISTA":"Vitor","SEXO":"M","FILHOS":4,"IDADE":26,"SAL\u00c1RIO":2453,"N\u00cdVEL":"N1","UNIDADE":"SP"},{"ANALISTA":"Manoel","SEXO":"M","FILHOS":2,"IDADE":26,"SAL\u00c1RIO":2536,"N\u00cdVEL":"N2","UNIDADE":"SP"},{"ANALISTA":"Leandro","SEXO":"M","FILHOS":2,"IDADE":34,"SAL\u00c1RIO":2590,"N\u00cdVEL":"N2","UNIDADE":"SP"}]'''

# Creating connection with ngrok----------------------------------------------------
app = FastAPI()
@app.get('/index')
async def home():
  return base_dados_fapi_json

ngrok_tunnel = ngrok.connect(8000)
print(f"Public Url:{ngrok_tunnel.public_url}/index")
nest_asyncio.apply()
uvicorn.run(app,port=8000)

# Sample Output---------------------------------------------------------------------
'''WARNING:pyngrok.process.ngrok:t=2023-07-31T20:02:25+0000 lvl=warn msg="ngrok config file found at legacy location, move to XDG location" xdg_path=/root/.config/ngrok/ngrok.yml legacy_path=/root/.ngrok2/ngrok.yml
Public Url:https://4b79-34-74-12-13.ngrok.io/index
INFO:     Started server process [1179]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     2804:14c:b6:b9eb:f907:d29d:4fb6:5927:0 - "GET /index HTTP/1.1" 200 OK
INFO:     2804:14c:b6:b9eb:f907:d29d:4fb6:5927:0 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     201.64.116.199:0 - "GET /index HTTP/1.1" 200 OK'''