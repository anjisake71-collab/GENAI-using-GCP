import os
import certifi

# Must be set BEFORE grpc/vertexai imports
os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = certifi.where()
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

# rest of your existing imports below...

from fastapi import FastAPI # FASTAPI to create backend APIs
from fastapi.middleware.cors import CORSMiddleware # SIMILAR GLIB # CORS = Cross orginina resource sharing, which allows our React frontend to communicate with our FastAPI backend without running into cross-origin issues. We will configure it to allow requests from any origin for simplicity, but in a production application, you should restrict this to your frontend's domain.
from app.routes.chat import router as chat_router # import the chat router we defined in routes/chat.py, which contains the API endpoint for handling chat requests. We will include this router in our FastAPI app to make the /chat endpoint available.

app = FastAPI()

# ADD THIS CORS CONFIG 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React
    allow_credentials=True,
    allow_methods=["*"], # GET, POST, PUT, DELET
    allow_headers=["*"],
)

app.include_router(chat_router)
# FRONTE React App -> Local host: 3000
# bACKEND -> lOCAL HOST: 8000