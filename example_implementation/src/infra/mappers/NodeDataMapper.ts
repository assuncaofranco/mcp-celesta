/**
 * NodeDataMapper - Mapeador de nós de ação
 * Registra e gerencia os nós disponíveis no sistema
 */

import { ActionNode } from '../../domain/nodes/ExternalLoggerNode';
import { ExternalLoggerNode } from '../../domain/nodes/ExternalLoggerNode';

// Exemplo de outros nós (assumindo que existem)
// import { OtherActionNode } from '../../domain/nodes/OtherActionNode';

export class NodeDataMapper {
  private static nodes: Map<string, ActionNode> = new Map();

  /**
   * Registra todos os nós disponíveis
   */
  static initialize(): void {
    // Registro do novo nó ExternalLoggerNode
    const externalLoggerNode = new ExternalLoggerNode();
    this.nodes.set(externalLoggerNode.getName(), externalLoggerNode);

    // Exemplo de registro de outros nós
    // const otherNode = new OtherActionNode();
    // this.nodes.set(otherNode.getName(), otherNode);
  }

  /**
   * Obtém um nó pelo nome
   * @param name - Nome do nó
   * @returns O nó correspondente ou undefined se não encontrado
   */
  static getNode(name: string): ActionNode | undefined {
    return this.nodes.get(name);
  }

  /**
   * Lista todos os nós registrados
   * @returns Array com os nomes dos nós
   */
  static listNodes(): string[] {
    return Array.from(this.nodes.keys());
  }

  /**
   * Verifica se um nó está registrado
   * @param name - Nome do nó
   * @returns true se o nó está registrado, false caso contrário
   */
  static hasNode(name: string): boolean {
    return this.nodes.has(name);
  }
}

// Inicializa os nós ao carregar o módulo
NodeDataMapper.initialize();



