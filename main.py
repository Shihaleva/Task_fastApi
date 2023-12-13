from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Сидоренко Софья Максимовна"}

@app.get('/tools')
async def f_indexT():
    return "Навыков нет"

@app.get('/users')
async def f_indexU():
    return "+79679636488"