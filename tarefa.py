from datetime import datetime

class Tarefa:

    def __init__(self, titulo, descricao, data_vencimento, status="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        # Trasnforma a string de data de fato em um objeto no formato data (datetime)
        # Formato utilizado vai ser: dia/mes/ano
        self.data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
        self.status = status

    def __repr__(self):
        return f"Tarefa(titulo='{self.titulo}'  )"

    
    
