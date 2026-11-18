# Organizador de Documentos Excel

> Automação de tarefas e organização de planilhas do Excel.

---

## Sobre o Projeto:
Este projeto está sendo feito em Python com interface gráfica usando CustomTkinter. O objetivo principal é automatizar a rotina administrativa, com seleção de pastas, filtragem de arquivo excel, validação de caminhos de diretório com segurança e organização de forma automatizada.

---

## Tecnologias Utilizadas:
* **Python**
* **CustomTkinter**
* **Tkinter** (filedialog e messagebox)
* **OS / Shutil**

---

## Funcionalidades Atuais:
* **Interface Gráfica (GUI):** Janela intuitiva e com dimensões fixas desenvolvida com CustomTkinter.
* **Validação de Pastas:** Verificação (`os.path.isdir`) para garantir que os diretórios selecionados realmente existem.
* **Segurança e filtro nos campos:** Inputs de bloqueio de texto (`state="disabled"`) e Varredura automática de extensão Excel
* **Feedback Visual:** Alertas via pop-up (`messagebox`) informando o sucesso da operação ou avisando caso nenhum arquivo seja encontrado.

---

## Como usar:
1. Abra a aplicação.
2. Selecione a pasta de origem onde estão as planilhas.
3. Selecione a pasta de destino para onde os arquivos organizados devem ir.
4. Clique no botão Processar Planilhas.

---

## Próximos Passos (Roadmap):
O projeto está em evolução. As próximas melhorias planejadas são:
- **Tratamento de Dados com Pandas:** Integrar a biblioteca Pandas para ler e realizar tratamento nas planilhas (como remoção de linhas duplicadas e tratamento de colunas) antes de salvá-las.
- **Modularização do Código:** Separar a camada de interface gráfica (`interface.py`) da camada de lógica.
- **Barra de Progresso:** Adicionar uma barra de progresso visual (`CTkProgressBar`) para acompanhar o andamento de grandes lotes de planilhas.

