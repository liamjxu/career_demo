import streamlit as st
import requests
import json
from streamlit_extras.stylable_container import stylable_container


st.write("# Finding Causal Graphs with LLMs")


st.write("Given each obtained question and expert response, we prompt an LLM to 1) identify the critical factors (causal variables) in fulfilling the question, along with the rationales behind them; 2) identify potential edges between those causal variables and estimate the causal strength of the edges, and 3) iteratively merge causal graphs across user queries.")
st.write("The process is visualized in the following flowchart:")

st.write("")

st.image('images/flowchart.png')

tabs = st.tabs(['Prompt 1', 'Prompt 2'])

prompt1 = requests.get('https://github.com/liamjxu/career_demo/blob/main/templates/get_variables_and_graph.jinja2').text
prompt1 = json.loads(prompt1)['payload']['blob']['rawLines']

prompt2 = requests.get('https://github.com/liamjxu/career_demo/blob/main/templates/merge_graphs.jinja2').text
prompt2 = json.loads(prompt2)['payload']['blob']['rawLines']

with tabs[0]:
    with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,
    ):
        st.code('\n'.join(prompt1), language='jinja2')
with tabs[1]:
    with stylable_container(
        "codeblock",
        """
        code {
            white-space: pre-wrap !important;
        }
        """,
    ):
        st.code('\n'.join(prompt2), language='jinja2')









# with open('typical_tasks_example_questions_graphs_merged.json', 'r') as f:
#     data = json.load(f)

# all_queries = data[0]['simulated_queries']
# all_graphs = data[0]['res_graphs']
# merged_graph = data[0]['merged_graphs']

# tabs = st.tabs(['Query 0', 'Query 1', 'Query 2', 'Query 3', 'Query 4', 'Merged'])

# for idx, (query, res) in enumerate(zip(all_queries, all_graphs)):
#     # Create multiple tabs
#     with tabs[idx]:
#       with st.container():
#           # Create a graphlib graph object
#           graph = graphviz.Digraph()

#           for edge in res[1]:
#               graph.edge(edge[0], edge[1], label=str(edge[2]))
#           st.write("## Query")
#           st.write(query)
#           st.write("## Causal Graph Created from Query")
#           st.write("The edge label numbers are GPT's scores (out of 10) for causal relationships represented by the edges.")
#           st.graphviz_chart(graph)
#           st.write("## Causal Graph Node Explanation")
#           st.write(res[0])
#           st.write("## Causal Graph Reasoning")
#           st.write(res[2])

# with tabs[-1]:
#     with st.container():
#         # Create a graphlib graph object
#         graph = graphviz.Digraph()

#         for edge in merged_graph[1]:
#             graph.edge(edge[0], edge[1], label=str(edge[2]))
#         st.write("## The Merged Causal Graph Created from All Queries")
#         st.write("This is a merged graph created from all the queries. The main goal is to check reusability of the individually generated causal graphs.")
#         st.write("The edge label numbers are GPT's scores (out of 10) for causal relationships represented by the edges.")
#         st.write("## Causal Graph Created from Queries")
#         st.graphviz_chart(graph)
#         st.write("## Causal Graph Node Explanation")
#         st.write(merged_graph[0])
#         st.write("## Causal Graph Reasoning")
#         st.write(merged_graph[2])