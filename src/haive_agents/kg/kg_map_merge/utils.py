import networkx as nx
import matplotlib.pyplot as plt
from langchain_neo4j.graphs.graph_document import GraphDocument
import numpy as np
from typing import List, Union, Optional
from langchain_core.documents import Document
from haive_core.models.llm.base import LLMConfig, AzureLLMConfig
from haive_agents.document_agents.kg.kg_map_merge.agent import StructuredKGAgent
from haive_agents.document_agents.kg.kg_map_merge.config import ParallelKGAgentConfig

def visualize_graph(graph_document: GraphDocument, output_file: str = "knowledge_graph.png"):
    """Visualize the graph document using NetworkX and matplotlib."""
    if not graph_document:
        print("No graph to visualize")
        return
        
    # Create a NetworkX graph
    G = nx.DiGraph()
    
    # Add nodes
    for node in graph_document.nodes:
        # Get node properties as label
        props = node.properties or {}
        label = f"{node.id}\n({node.type})"
        if props:
            label += "\n" + "\n".join(f"{k}: {v}" for k, v in props.items())
            
        G.add_node(node.id, label=label, type=node.type)
    
    # Add edges
    for rel in graph_document.relationships:
        G.add_edge(
            rel.source.id, 
            rel.target.id, 
            label=rel.type,
            type=rel.type
        )
    
    # Draw the graph
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    
    # Draw nodes by type with different colors
    node_types = set(nx.get_node_attributes(G, 'type').values())
    colors = plt.cm.Set3(np.linspace(0, 1, len(node_types)))
    color_map = dict(zip(node_types, colors))
    
    for node_type, color in color_map.items():
        nodelist = [n for n, attr in G.nodes(data=True) if attr.get('type') == node_type]
        nx.draw_networkx_nodes(
            G, pos, 
            nodelist=nodelist,
            node_color=[color],
            node_size=2000, 
            alpha=0.8,
            label=node_type
        )
    
    # Draw edges by type with different colors and line styles
    edge_types = set(nx.get_edge_attributes(G, 'type').values())
    edge_colors = plt.cm.tab10(np.linspace(0, 1, len(edge_types)))
    edge_color_map = dict(zip(edge_types, edge_colors))
    
    for edge_type, color in edge_color_map.items():
        edgelist = [(u, v) for u, v, attr in G.edges(data=True) if attr.get('type') == edge_type]
        nx.draw_networkx_edges(
            G, pos,
            edgelist=edgelist,
            width=1.5,
            alpha=0.7,
            edge_color=[color],
            connectionstyle='arc3,rad=0.1',
            arrowsize=15,
            label=edge_type
        )
    
    # Add node labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    
    # Add edge labels
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=edge_labels,
        font_color='black',
        font_size=8,
        font_family='sans-serif'
    )
    
    # Add legend
    plt.legend(loc="upper right", scatterpoints=1, title="Node Types")
    
    # Save the visualization
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_file, format='png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Graph visualization saved to {output_file}")
from langchain_community.graphs.graph_document import GraphDocument, Node, Relationship
a=GraphDocument(nodes=[Node(id='Pierre Curie', type='Person', properties={}), Node(id='magnetism', type='Field', properties={}), Node(id='crystallography', type='Field', properties={}), Node(id='radioactivity', type='Field', properties={}), Node(id='France', type='Country', properties={})], relationships=[Relationship(source=Node(id='Pierre Curie', type='Person', properties={}), target=Node(id='France', type='Country', properties={}), type='HAS_NATIONALITY', properties={}), Relationship(source=Node(id='Pierre Curie', type='Person', properties={}), target=Node(id='crystallography', type='Field', properties={}), type='MADE_CONTRIBUTIONS_TO', properties={}), Relationship(source=Node(id='Pierre Curie', type='Person', properties={}), target=Node(id='magnetism', type='Field', properties={}), type='MADE_CONTRIBUTIONS_TO', properties={}), Relationship(source=Node(id='Pierre Curie', type='Person', properties={}), target=Node(id='radioactivity', type='Field', properties={}), type='MADE_CONTRIBUTIONS_TO', properties={})], source=Document(metadata={}, page_content='Pierre Curie was a French physicist who made pioneering contributions to crystallography, magnetism, and radioactivity.'))
visualize_graph(a)

from typing import Dict, Any, Tuple
# Helper function to create and run the agent
async def create_knowledge_graph(
    documents: List[Union[str, Document]],
    llm_config: Optional[LLMConfig] = None,
    allowed_nodes: Optional[List[str]] = None,
    allowed_relationships: Optional[Union[List[str], List[Tuple[str, str, str]]]] = None,
    node_properties: Union[bool, List[str]] = False,
    relationship_properties: Union[bool, List[str]] = False,
    additional_transformer_args: Optional[Dict[str, Any]] = None,
    custom_system_prompt: Optional[str] = None
) -> GraphDocument:
    """
    Create a knowledge graph from multiple documents using parallel processing.
    
    Args:
        documents: List of documents or text strings
        llm_config: LLM configuration to use
        allowed_nodes: List of allowed node types (optional)
        allowed_relationships: List of allowed relationship types (optional)
        node_properties: Whether to extract node properties and which ones
        relationship_properties: Whether to extract relationship properties and which ones
        additional_transformer_args: Additional arguments for the GraphTransformer
        custom_system_prompt: Custom system prompt for graph extraction
        
    Returns:
        The merged knowledge graph
    """
    # Set defaults
    llm_config = llm_config or AzureLLMConfig()
    allowed_nodes = allowed_nodes or []
    allowed_relationships = allowed_relationships or []
    additional_transformer_args = additional_transformer_args or {}
    
    # Create agent config
    config = ParallelKGAgentConfig(
        llm_config=llm_config,
        allowed_nodes=allowed_nodes,
        allowed_relationships=allowed_relationships,
        node_properties=node_properties,
        relationship_properties=relationship_properties,
        graph_transformer_args=additional_transformer_args,
        custom_system_prompt=custom_system_prompt
    )
    
    # Create and initialize the agent
    agent = StructuredKGAgent(config)
    
    # Run the agent
    result = await agent.arun({"contents": documents})
    
    # Return the merged graph
    return result.get("merged_graph")
