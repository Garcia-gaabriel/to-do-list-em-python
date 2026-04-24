from tarefa import Tarefa
from persistencia import carregar_tarefas, salvar_tarefas

tarefa1 = Tarefa("Estudar Python", "Vendo video aulas no youtube", "24/04/2026")
print(tarefa1)
print(tarefa1.detalhes())