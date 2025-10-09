import { useState } from "react";
import Botao from "../Botao/Botao";

const Tarefas = () => {
  const [tasks, setTasks] = useState<string[]>([]);
  const [newTask, setNewTask] = useState("");

  const AddTask = () => {
    if (newTask.trim() !== "") {
      setTasks([...tasks, newTask]);
      setNewTask("");
    }
  };

  const RemoverTarefa = (index: number) => {
    setTasks(tasks.filter((_, i) => i !== index));
  };

  return (
    <>
      <h2>Lista de Tarefas</h2>
      <input type='text' placeholder='Digite uma tarefa' value={newTask} onChange={(e) => setNewTask(e.target.value)} />
      <Botao cor='green' texto='Adicionar tarefa' onClick={AddTask} />
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>
            {task}
            <Botao cor='red' texto='Excluir tarefa' onClick={() => RemoverTarefa(index)} />
          </li>
        ))}
      </ul>
    </>
  );
};

export default Tarefas;
