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
        return f"Tarefa(titulo='{self.titulo}', descricao='{self.descricao}', " \
               f"data_vencimento='{self.data_vencimento.strftime('%d/%m/%Y')}', status='{self.status}')"
    
    # Marca tarefa como concluída
    def marcar_concluida(self):
        self.status = "Concluída"

    # Registra tarefa como atrasada se a data atual é maior do que a de vencimento
    # e se o status dela é Pendete... 
    def esta_atrasada(self):
        return datetime.now() > self.data_vencimento and self.status == "Pendente"
    
    # Criando funções para editar titulo, etc...
    def editar_titulo(self, titulo):
        self.titulo = titulo

    def editar_descricao(self, descricao):
        self.descricao = descricao

    def editar_data_vencimento(self, data_vencimento):
        self.data = datetime.strptime("%d/%m/%Y")
    
    # Definindo o retorno para o usuario
    def detalhes(self):
        status = "Atrasada" if self.esta_atrasada() else self.status
        return (f"Título: {self.titulo}\n"
                f"Descrição: {self.descricao}\n"
                f"Data de vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\n"
                f"Status: {self.status}")
    


    
    
