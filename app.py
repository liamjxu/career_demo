import streamlit as st
import graphviz
import json
from st_pages import Page, show_pages, add_page_title


show_pages(
    [
        Page("app.py", "Curating a Career Plan", icon="1️⃣"),
        Page("page2.py", "Suggesting Potential Occupations and Wage Projections", icon="2️⃣"),
        Page("page3.py", "Making Optimal Choices Among Alternatives", icon="3️⃣"),
    ]
)

with open('typical_tasks_example_questions_graphs_merged.json', 'r') as f:
    data = json.load(f)

all_queries = data[0]['simulated_queries']
all_graphs = data[0]['res_graphs']
merged_graph = data[0]['merged_graphs']

tabs = st.tabs(['Query 0', 'Query 1', 'Query 2', 'Query 3', 'Query 4', 'Merged'])

for idx, (query, res) in enumerate(zip(all_queries, all_graphs)):
    # Create multiple tabs
    with tabs[idx]:
      with st.container():
          # Create a graphlib graph object
          graph = graphviz.Digraph()

          for edge in res[1]:
              graph.edge(edge[0], edge[1], label=str(edge[2]))
          st.write("## Query")
          st.write(query)
          st.write("## Causal Graph Created from Query")
          st.write("The edge label numbers are GPT's scores (out of 10) for causal relationships represented by the edges.")
          st.graphviz_chart(graph)
          st.write("## Causal Graph Node Explanation")
          st.write(res[0])
          st.write("## Causal Graph Reasoning")
          st.write(res[2])

with tabs[-1]:
    with st.container():
        # Create a graphlib graph object
        graph = graphviz.Digraph()

        for edge in merged_graph[1]:
            graph.edge(edge[0], edge[1], label=str(edge[2]))
        st.write("## Causal Graph Created from Queries")
        st.graphviz_chart(graph)
        st.write("## Causal Graph Node Explanation")
        st.write(merged_graph[0])
        st.write("## Causal Graph Reasoning")
        st.write(merged_graph[2])