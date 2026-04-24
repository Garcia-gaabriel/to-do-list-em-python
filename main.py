from tarefa import Tarefa
from persistencia import carregar_tarefas, salvar_tarefas

tarefa1 = Tarefa("Estudar Python", "Vendo video aulas no youtube", "24/04/2026")

salvar_tarefas([tarefa1])

tarefas = carregar_tarefas()
print(tarefas[0].detalhes())