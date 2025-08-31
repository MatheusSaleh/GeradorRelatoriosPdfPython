from fastapi import FastAPI
from fastapi.responses import FileResponse
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

app = FastAPI()

# Configura o Jinja2 (templates)
env = Environment(loader=FileSystemLoader("templates"))

@app.get("/relatorio")
def gerar_relatorio():
    # Dados de exemplo (podem vir do banco)
    produtos = [
        {"nome": "Camiseta", "quantidade": 10, "preco": 200},
        {"nome": "Tênis", "quantidade": 5, "preco": 500},
        {"nome": "Boné", "quantidade": 3, "preco": 90},
    ]

    # Renderiza o template
    template = env.get_template("relatorio.html")
    html_code = template.render(produtos=produtos)

    # Gera o PDF
    output_path = "relatorio.pdf"
    HTML(string=html_code).write_pdf(output_path)

    # Retorna o PDF como download
    return FileResponse(output_path, media_type="application/pdf", filename="relatorio.pdf")
