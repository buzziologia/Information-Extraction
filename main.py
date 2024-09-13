import openai
import pandas as pd

# Configure sua chave de API da OpenAI
openai.api_key = 'sk-xwcB27vDpSC6aiKkqpY78OV-3kzJll9rfQEdm7TCrGT3BlbkFJJ59npxNMxZ5vNJZ4LlbkE5zp34o04wNq2rzaPddBoA'


# voce é, sua função é, contexto, verbo
# deixar mais objetivo o que eu quero na saida
# Função para gerar os campos preenchidos com base na descrição
# dar mais limites nos exemplos, um chassi tem em media, 12 letras
def preencher_dados_veiculo(descricao):
    prompt = f"""
    Instrução: Processar descrições de veículos e obter dados precisos para posterior validação. As informações extraídas devem ser formatadas corretamente para garantir todos os detalhes nessários.
    Contexto: Dada uma descrição de veículo, identifique e extraia as seguintes informações: marca, modelo, trim, ano, combustível, placa e chassi.
    Entrada: {descricao}
    Saída: 
    { 
    "Marca": {marca if marca else 'Não informado'}, 
    "Modelo" : {modelo if modelo else 'Não informado'}, 
    "Trim": {trim if trim else 'Não informado'}, 
    "Ano": {ano if ano else 'Não informado'}, 
    Combustível": {combustivel if combustivel else 'Não informado'} ,
    "Placa": {placa if placa else 'Não informado'}, 
    "Chassi", {chassi if chassi else 'Não informado'}
    }
    Se algum dado não puder ser inferido, indique 'Não informado' para o campo correspondente.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    # Extrair a resposta gerada pelo modelo
    resposta = response['choices'][0]['text'].strip()

    # Parsear a resposta para extrair os valores
    dados = {}
    for linha in resposta.split('\n'):
        if ': ' in linha:
            chave, valor = linha.split(': ', 1)
            dados[chave.strip()] = valor.strip()

    return dados


# Carrega a tabela
df = pd.read_csv('tabela_veiculos.csv')

# Preencher os dados para cada linha que tiver campos em branco
for index, row in df.iterrows():
    if pd.isnull(row['Marca']) or pd.isnull(row['Modelo']) or pd.isnull(row['Trim']) or pd.isnull(
            row['Ano']) or pd.isnull(row['Chassi']) or pd.isnull(row['Placa']):
        dados_preenchidos = preencher_dados_veiculo(
            row['Descrição'],
            row['Marca'],
            row['Modelo'],
            row['Trim'],
            row['Ano'],
            row['Chassi'],
            row['Placa']
        )

        # Atualiza a linha do dataframe com os valores retornados
        df.at[index, 'Marca'] = dados_preenchidos.get('Marca', 'Não informado')
        df.at[index, 'Modelo'] = dados_preenchidos.get('Modelo', 'Não informado')
        df.at[index, 'Trim'] = dados_preenchidos.get('Trim', 'Não informado')
        df.at[index, 'Ano'] = dados_preenchidos.get('Ano', 'Não informado')
        df.at[index, 'Chassi'] = dados_preenchidos.get('Chassi', 'Não informado')
        df.at[index, 'Placa'] = dados_preenchidos.get('Placa', 'Não informado')

# Salva a tabela preenchida
df.to_csv('tabela_veiculos_preenchida.csv', index=False)

print("Dados preenchidos e tabela salva com sucesso.")
