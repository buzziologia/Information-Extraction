# Interação com LLM-s
## Desenvolvido com a finalidade de executar alguns comandos no prompt dos seguintes LLM's:
* Copilot
* Chat GPT
* Gemini

## Extração de informações de documentos
Elementos do prompt:
* Instrução: Processar descrições de veículos e obter dados precisos para posterior validação . As informações extraídas devem ser formatadas corretamente para garantir todos os detalhes nessários.
* Contexto: Dado uma descrição de veículo, identifique e extraia as seguintes informações: marca, modelo, trim, ano, combustível, placa e chassi.
* Entrada: Descrição do véiculo: [tabela de descrições de veículos]
* Saída: Formato Json
{
"Marca": marca,
 "Modelo" : modelo, 
"Trim": trim, 
"Ano": ano, 
Combustível": combustível,  
"Placa": placa, 
"Chassi", chassi
}
  
dados armazenados em diferentes datasets para posterior validação e incremento da precisão
