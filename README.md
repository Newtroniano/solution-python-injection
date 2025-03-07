# Solution Python Injection

## Introdução
Este projeto consiste em uma API RESTful desenvolvida em Python utilizando Flask RESTful e o padrão de injeção de dependências. A solução tem como objetivo principal migrar dados armazenados em arquivos Excel para um banco de dados e gerenciá-los por meio de uma API estruturada e flexível.

A documentação pode ser acessada em: [solution-python-injection](https://docs.google.com/document/d/1RhJq_rF3GSZz9ygavwMX_POhPJmyCCFOIO6QoGNNwqk/edit?usp=sharing)

## Tecnologias Utilizadas
- **Python 3**
- **Flask RESTful** para desenvolvimento da API
- **Pandas** para manipulação de dados
- **SQL Server** (ou outros bancos de dados compatíveis)
- **Streamlit** para interface de interação
- **Docker** (implementação futura para conteinerização)
- **Azure** (compatível para deploy em nuvem)

## Funcionalidades
1. **Migração de Dados**
   - Upload de arquivos Excel contendo informações de clientes e produtos.
   - Processamento dos dados e inserção no banco de dados.

2. **Gerenciamento via API**
   - Endpoints para visualizar, adicionar, modificar e excluir registros.
   - Utilização de padrão de injeção de dependências para maior flexibilidade.

3. **Interface Simples com Streamlit**
   - Permite upload de arquivos e interação com os dados do banco.

4. **Facilidade de Manutenção e Escalabilidade**
   - Arquitetura flexível permitindo mudanças de banco de dados sem alteração do código principal.
   - Pronto para integração com serviços em nuvem.

5. **Futuro suporte a Docker**
   - Planejamento para implementação de Docker para facilitar a implantação e escalabilidade da aplicação.

## Instalação e Execução
### Requisitos
- Python 3 instalado
- Dependências listadas no arquivo `requirements.txt`
- Banco de dados configurado (SQL Server por padrão, mas pode ser ajustado)

### Passos
1. Clone o repositório:
   ```sh
   git clone https://github.com/Newtroniano/solution-python-injection.git
   cd solution-python-injection
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure a conexão com o banco de dados no arquivo apropriado.
4. Execute a API:
   ```sh
   python app.py
   ```
5. Para utilizar a interface Streamlit:
   ```sh
   streamlit run app_frontend.py
   ```


## Contribuição
1. Fork o repositório.
2. Crie uma branch para suas modificações:
   ```sh
   git checkout -b minha-nova-feature
   ```
3. Realize suas alterações e faça commit:
   ```sh
   git commit -m "Adiciona nova funcionalidade"
   ```
4. Envie suas alterações para o repositório remoto:
   ```sh
   git push origin minha-nova-feature
   ```
5. Abra um Pull Request no GitHub.

