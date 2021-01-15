from fastapi import FastAPI
import config as cfg

app = FastAPI(debug=cfg.DEBUG, title="Project Name")