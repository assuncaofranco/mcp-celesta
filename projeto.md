Celesta Architect: Master Blueprint (v3.0)
🎯 Visão Geral
O Celesta é um ecossistema de engenharia de software híbrido. Ele utiliza um LLM Local (7B) como um "Project Scout" (Gerente de Projeto) para realizar a descoberta e filtragem de contexto, e um LLM Global (Claude 3.5 Sonnet) como o "Expert" para execução técnica. O foco central é a eficiência cirúrgica: contexto mínimo para qualidade máxima.

🏗️ 1. Arquitetura de Sistema
A. Camada de Interface (Dual Mode)
CLI Terminal (celesta_run.py): Interface otimizada para tarefas rápidas e automação via linha de comando.

MCP Server (server.py): Servidor de protocolo para integração nativa com IDEs e Claude Desktop.

B. Camada de Orquestração (core/orchestrator.py)
Coordena o fluxo de inteligência:

Scout Phase: Local LLM analisa a intenção e seleciona ferramentas.

Assembly Phase: ContextBuilder coleta, limpa e formata os dados.

Expert Phase: Envio do dossiê final para o Claude/Gemini.

🛠️ 2. Toolkit de Ferramentas Especializadas
A. Ferramentas PHP/Symfony
find_entity_by_table(table_name): Localiza entidades Doctrine via mapeamento de DB.

extract_validation_rules(file): Extrai apenas Constraints e Assertions de classes PHP.

find_route_by_name(route_name): Mapeia rotas em Controllers (Attributes) ou arquivos YAML.

check_bundles_config(): Analisa o config/bundles.php para entender extensões ativas.

B. Ferramentas Golang
find_http_handlers(): Varre o projeto em busca de implementações de Handlers/Gin/Echo.

extract_interface_implementations(interface): Identifica quais structs satisfazem uma interface.

check_go_mod_dependencies(): Analisa o go.mod para entender o stack de bibliotecas.

find_middleware_chain(): Mapeia a ordem de execução de middlewares em rotas.

⚙️ 3. Sistema de Configuração e Paths
O sistema utiliza caminhos absolutos baseados em variáveis de ambiente para garantir portabilidade total.

Global (~/.celesta/config.yaml)
YAML

paths:
projects_root: "~/Dev/projects" # Raiz global de projetos
cache_dir: "~/.celesta/cache"
llm:
local_endpoint: "http://localhost:11434"
model: "llama3:7b"
Por Projeto (.celesta/project.yaml)
YAML

project:
name: "wallet-api"
type: "symfony" # [symfony | golang]
hints:
api_prefix: "/api/v1"
orm: "doctrine"
blueprints:
new_endpoint:
detect_by: ["api", "route", "controller"]
required_files: ["src/Controller/", "src/Entity/"]
always_include: ["composer.json", "config/services.yaml"]
never_include: ["var/", "vendor/", "node_modules/"]
🧹 4. Módulo de Otimização de Contexto (ContextBuilder)
Responsável por transformar código bruto em informação legível para IA, economizando até 80% de tokens.

Estratégias de Minificação:
PHP: Remove comentários de licença, espaços em branco e agrupa propriedades de entidades. Mantém Attributes do PHP 8+.

Golang: Preserva documentação godoc de funções exportadas, remove corpos de funções não relacionadas (Skeleton View) e ignora go.sum.

Segurança: O SecretScanner automático remove chaves .env, tokens JWT e senhas antes de qualquer envio para a nuvem.

📚 5. Ciclo de Aprendizado (Feedback Loop)
O Celesta não apenas executa, ele evolui com o seu código.

Cache Estruturado: Cada missão bem-sucedida gera um log em .celesta/cache/ contendo (Query -> Arquivos_Relevantes).

Sintetização de Dados: O sistema utiliza o Gemini para "limpar" esses logs e criar pares de treinamento de alta qualidade.

Fine-Tuning Local: Os dados sintetizados são usados em um pipeline no Google Colab (QLoRA) para treinar o modelo 7B local, tornando o "Scout" cada vez mais preciso nos seus padrões específicos.