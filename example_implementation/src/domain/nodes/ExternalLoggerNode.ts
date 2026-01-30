/**
 * ExternalLoggerNode - Nó de ação que loga mensagens recebidas
 * Implementa a interface ActionNode seguindo o padrão do projeto
 */

export interface ActionNode {
  execute(message: string): Promise<void>;
  getName(): string;
}

export class ExternalLoggerNode implements ActionNode {
  private readonly name: string = 'ExternalLoggerNode';

  /**
   * Executa a ação de logar a mensagem recebida
   * @param message - Mensagem a ser logada
   */
  async execute(message: string): Promise<void> {
    console.log(`[ExternalLoggerNode] ${new Date().toISOString()} - ${message}`);
  }

  /**
   * Retorna o nome do nó
   */
  getName(): string {
    return this.name;
  }
}



