📋 Checklist de Implementação: Celesta Architect

🏗️ Fase 1: Infraestrutura e Configuração (O alicerce)
Esta fase estabelece como o sistema se localiza e entende o ambiente.

[ ] 1.1. ConfigLoader & Environment: Criar core/config_loader.py.

Ler CELESTA_PROJECTS_ROOT.

Carregar e validar ~/.celesta/config.yaml e .celesta/project.yaml.

[ ] 1.2. Path Resolver: Implementar lógica no FileManager para traduzir caminhos relativos do YAML em caminhos absolutos do sistema.

🛠️ Fase 2: Context & Code Tools (O canivete suíço)
Aqui criamos as ferramentas que o Scout usará para "enxergar" o código.

[ ] 2.1. Basic Minifier: Implementar em core/context_builder.py a remoção de ruído (espaços, comentários simples).

[ ] 2.2. Symfony-Specific Tools: Implementar find_route_by_name e extract_validation_rules.

[ ] 2.3. Go-Specific Tools: Implementar extract_interface_implementations e check_go_mod_dependencies.

[ ] 2.4. Secret Scanner: Adicionar filtro de segurança para remover chaves sensíveis antes da montagem do dossiê.

🤖 Fase 3: Local LLM & Scout Logic (O cérebro)
Integração com o modelo 7B para tomada de decisão.

[ ] 3.1. Ollama/Local Client: Criar core/local_llm_client.py para comunicação via API (HTTP) com o modelo local.

[ ] 3.2. Scout Prompting: Desenvolver o "System Prompt" que ensina o modelo 7B a usar as ferramentas listadas no YAML.

[ ] 3.3. Blueprint Engine: Lógica para o Scout reconhecer padrões (ex: se detectar "API", ativar blueprint de endpoint).

📦 Fase 4: Assembly & Expert Delivery (A entrega)
Preparação do Dossiê para o Claude.

[ ] 4.1. Markdown Dossier Builder: Criar core/prompt_builder.py para converter o contexto coletado em um arquivo Markdown estruturado (com breadcrumbs).

[ ] 4.2. Claude CLI Bridge: Ajustar o cli/celesta_run.py para disparar o comando final para o executável do Claude.

💾 Fase 5: Cache & Aprendizado (A memória)
Transformar execuções em conhecimento futuro.

[ ] 5.1. Hash Cache: Implementar o sistema de cache em .celesta/cache/ baseado no hash da query.

[ ] 5.2. Dataset Generator: Criar training/dataset_generator.py para exportar os logs de sucesso para o formato de treinamento (JSONL).