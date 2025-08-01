📈 Pipeline de Dados de Ações
English | Português

Uma ferramenta profissional de extração e análise de dados financeiros construída com Python e Streamlit. Extraia, transforme e baixe dados limpos de ações do Yahoo Finance com uma interface web elegante.

## 🚀 [Demo ao Vivo](https://your-app-url.streamlit.app/)

Mostrar Imagem

## ✨ Funcionalidades

- **Interface Web**: Dashboard Streamlit limpo e profissional
- **Ferramenta CLI**: Interface de linha de comando para desenvolvedores e automação
- **Pipeline de Dados**: Processo ETL com tratamento adequado de erros
- **Múltiplos Períodos**: De 1 mês até dados históricos máximos
- **Exportação CSV**: Baixe datasets limpos e prontos para análise
- **Estilo Personalizado**: Tema escuro com design profissional
- **Validação de Entrada**: Trata símbolos inválidos e casos extremos

## 🛠️ Stack Tecnológica

- **Python 3.8+**
- **Streamlit** - Interface web
- **yfinance** - API do Yahoo Finance
- **Pandas** - Manipulação de dados
- **CSS Personalizado** - Estilo profissional

## 📦 Instalação

### Opção 1: Use o App Web

Visite o [demo ao vivo](https://your-app-url.streamlit.app/) - nenhuma instalação necessária!

### Opção 2: Execute Localmente

bash

`*# Clone o repositório*
git clone https://github.com/yourusername/stock-data-pipeline.git
cd stock-data-pipeline

*# Instale as dependências*
pip install -r requirements.txt

*# Execute o app web*
streamlit run src/streamlit_app.py

*# Ou use o CLI*
python src/cli_app.py`

## 🎯 Como Usar

### Interface Web

1. Digite um símbolo de ação (ex: AAPL, GOOGL, TSLA)
2. Selecione o período desejado
3. Clique em "Get Stock Data"
4. Visualize a prévia dos dados e baixe o CSV completo

### Linha de Comando

bash

`python src/cli_app.py
*# Siga as instruções para inserir símbolo e período*`

### Integração via API

python

`from src.data_pipeline import extract_data, transform_data

*# Extrair dados brutos*
raw_data = extract_data("AAPL", "1y")

*# Limpar e transformar*
clean_data = transform_data(raw_data)`

## 📁 Estrutura do Projeto

`stock-data-pipeline/
├── src/
│   ├── streamlit_app.py     # Interface web
│   ├── cli_app.py          # Ferramenta de linha de comando
│   ├── data_pipeline.py    # Lógica ETL principal
│   └── styles.css          # Estilo personalizado
├── data/                   # Diretório de saída (ignorado pelo git)
├── requirements.txt        # Dependências
├── README.md              # Versão em inglês
├── README_pt.md           # Este arquivo
└── .gitignore            # Regras do Git`

## 🔧 Desenvolvimento

### Desenvolvimento Local

bash

`*# Instalar em modo de desenvolvimento*
pip install -e .

*# Executar testes (se implementado)*
pytest tests/

*# Executar o app Streamlit com recarga automática*
streamlit run src/streamlit_app.py`

### Arquitetura do Pipeline de Dados

1. **Extrair**: Buscar dados da API do Yahoo Finance
2. **Transformar**: Limpar nomes de colunas, tratar dados ausentes, conversão de tipos
3. **Carregar**: Salvar em arquivos CSV com timestamp

## 📊 Dados Suportados

- **Preços de Ações**: Abertura, Máxima, Mínima, Fechamento, Fechamento Ajustado
- **Dados de Volume**: Informações de volume de negociação
- **Períodos**: 1d, 5d, 1mo, 3mo, 1y, 5y, Ytd, Max
- **Mercados**: Todas as bolsas suportadas pelo Yahoo Finance

## 🤝 Contribuindo

1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/funcionalidade-incrivel`)
3. Commit suas mudanças (`git commit -m 'Adiciona funcionalidade incrível'`)
4. Push para a branch (`git push origin feature/funcionalidade-incrivel`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](https://www.notion.so/datadaim/LICENSE) para detalhes.

## 🙏 Agradecimentos

- Yahoo Finance por fornecer dados financeiros gratuitos
- Equipe Streamlit pelo framework web incrível
- A comunidade Python de ciência de dados

## 📧 Contato

**Seu Nome** - pdaim.analytics@gmail.com

Link do Projeto: https://github.com/PedroDaim/YFinance_Data_Pipeline
