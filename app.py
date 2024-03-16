import streamlit as st
import graphviz
import json
from st_pages import Page, show_pages, add_page_title


# temp_data = [
#             {
#                 "Professional Networking": "Building relationships with individuals in your desired field to gain insights, advice, and potential job opportunities.",
#                 "Skill Development": "Acquiring new skills or improving existing ones that are relevant to the target role.",
#                 "Industry Knowledge": "Understanding the trends, challenges, and opportunities within the target industry.",
#                 "Project Experience": "Gaining practical experience through projects that demonstrate relevant skills and knowledge.",
#                 "Resume and LinkedIn Optimization": "Enhancing your resume and LinkedIn profile to highlight relevant skills, experiences, and achievements.",
#                 "Interview Preparation": "Practicing and improving interview skills, specifically focusing on the target role and company.",
#                 "Job Application": "Applying for roles that match your skills and career aspirations.",
#                 "Education Level": "The highest level of education attained, which can influence eligibility for certain positions.",
#                 "Work Experience": "The amount and relevance of work experience in the marketing field.",
#                 "Networking": "Building professional relationships that can lead to job opportunities and career advice.",
#                 "Leadership Skills": "Ability to lead and manage teams effectively.",
#                 "Strategic Thinking": "Capability to develop long-term plans and visions for a company's marketing efforts.",
#                 "Communication Skills": "Effectiveness in conveying ideas, both verbally and in writing.",
#                 "Certifications": "Additional qualifications specific to marketing or management that can enhance a resume.",
#                 "Company Size": "The size of the company where one works, which can impact the types of experiences and opportunities available.",
#                 "CMO Position": "The end goal of becoming a Chief Marketing Officer at a Fortune 500 company.",
#                 "Education": "Formal academic qualifications obtained.",
#                 "Technical Skills": "Specific technical knowledge or proficiencies related to a job.",
#                 "Industry Experience": "Practical experience working in a specific industry.",
#                 "Professional Certifications": "Credentials that demonstrate a specific skill or knowledge area, often recognized industry-wide.",
#                 "Project Management Skills": "Ability to plan, execute, and oversee projects to completion.",
#                 "Leadership Experience": "Experience in leading teams or projects, demonstrating ability to manage and inspire others.",
#                 "Senior Engineering Position": "A high-level role involving oversight of projects and potentially leading a team of engineers.",
#                 "Understanding of Blockchain": "Comprehensive knowledge of blockchain technology and its applications.",
#                 "Understanding of Cryptocurrency": "In-depth knowledge of cryptocurrency markets, trading, and regulatory environment.",
#                 "Target Companies": "Identifying and targeting companies that align with career goals and values.",
#                 "Project Management Experience": "Years of experience and expertise in managing projects, including planning, execution, and team management.",
#                 "Adaptability": "Ability to adjust to new environments, technologies, and challenges.",
#                 "Company Fit": "Alignment with a company's culture, values, and needs.",
#                 "Project Fit": "Alignment with the requirements and challenges of a specific project."
#             },
#             [
#                 [
#                     "Skill Development",
#                     "Project Experience",
#                     8
#                 ],
#                 [
#                     "Skill Development",
#                     "Resume and LinkedIn Optimization",
#                     7
#                 ],
#                 [
#                     "Professional Networking",
#                     "Job Application",
#                     6
#                 ],
#                 [
#                     "Industry Knowledge",
#                     "Interview Preparation",
#                     7
#                 ],
#                 [
#                     "Project Experience",
#                     "Interview Preparation",
#                     8
#                 ],
#                 [
#                     "Resume and LinkedIn Optimization",
#                     "Job Application",
#                     9
#                 ],
#                 [
#                     "Interview Preparation",
#                     "Job Application",
#                     8
#                 ],
#                 [
#                     "Job Application",
#                     "Target Position",
#                     7
#                 ],
#                 [
#                     "Education Level",
#                     "Work Experience",
#                     7
#                 ],
#                 [
#                     "Work Experience",
#                     "Networking",
#                     8
#                 ],
#                 [
#                     "Work Experience",
#                     "Industry Knowledge",
#                     9
#                 ],
#                 [
#                     "Work Experience",
#                     "Leadership Skills",
#                     8
#                 ],
#                 [
#                     "Networking",
#                     "Target Position",
#                     6
#                 ],
#                 [
#                     "Industry Knowledge",
#                     "Strategic Thinking",
#                     9
#                 ],
#                 [
#                     "Leadership Skills",
#                     "Target Position",
#                     8
#                 ],
#                 [
#                     "Strategic Thinking",
#                     "Target Position",
#                     7
#                 ],
#                 [
#                     "Communication Skills",
#                     "Leadership Skills",
#                     7
#                 ],
#                 [
#                     "Certifications",
#                     "Industry Knowledge",
#                     6
#                 ],
#                 [
#                     "Company Size",
#                     "Target Position",
#                     5
#                 ],
#                 [
#                     "Education",
#                     "Technical Skills",
#                     8
#                 ],
#                 [
#                     "Education",
#                     "Industry Experience",
#                     7
#                 ],
#                 [
#                     "Technical Skills",
#                     "Professional Certifications",
#                     7
#                 ],
#                 [
#                     "Industry Experience",
#                     "Networking",
#                     6
#                 ],
#                 [
#                     "Networking",
#                     "Target Position",
#                     5
#                 ],
#                 [
#                     "Professional Certifications",
#                     "Project Management Skills",
#                     6
#                 ],
#                 [
#                     "Project Management Skills",
#                     "Leadership Experience",
#                     8
#                 ],
#                 [
#                     "Leadership Experience",
#                     "Target Position",
#                     9
#                 ],
#                 [
#                     "Technical Skills",
#                     "Target Position",
#                     4
#                 ],
#                 [
#                     "Education",
#                     "Understanding of Blockchain",
#                     8
#                 ],
#                 [
#                     "Education",
#                     "Understanding of Cryptocurrency",
#                     7
#                 ],
#                 [
#                     "Skill Development",
#                     "Understanding of Blockchain",
#                     9
#                 ],
#                 [
#                     "Skill Development",
#                     "Understanding of Cryptocurrency",
#                     8
#                 ],
#                 [
#                     "Networking",
#                     "Project Experience",
#                     7
#                 ],
#                 [
#                     "Understanding of Blockchain",
#                     "Project Experience",
#                     8
#                 ],
#                 [
#                     "Understanding of Cryptocurrency",
#                     "Project Experience",
#                     7
#                 ],
#                 [
#                     "Project Experience",
#                     "Target Companies",
#                     9
#                 ],
#                 [
#                     "Industry Knowledge",
#                     "Technical Skills",
#                     8
#                 ],
#                 [
#                     "Technical Skills",
#                     "Certifications",
#                     7
#                 ],
#                 [
#                     "Project Management Experience",
#                     "Technical Skills",
#                     6
#                 ],
#                 [
#                     "Networking",
#                     "Company Fit",
#                     7
#                 ],
#                 [
#                     "Networking",
#                     "Project Fit",
#                     6
#                 ],
#                 [
#                     "Certifications",
#                     "Company Fit",
#                     5
#                 ],
#                 [
#                     "Adaptability",
#                     "Company Fit",
#                     8
#                 ],
#                 [
#                     "Adaptability",
#                     "Project Fit",
#                     7
#                 ],
#                 [
#                     "Company Fit",
#                     "Project Fit",
#                     9
#                 ]
#             ],
#             "\n\nThe merged causal graph integrates key variables and relationships from multiple career paths, ensuring a comprehensive overview of factors influencing career development across different industries. This graph is designed to be versatile, catering to individuals aiming for roles in data science, marketing (specifically a CMO position), engineering (with a focus on senior engineering positions), and fields involving blockchain and cryptocurrency. It also addresses the transition to technology project management roles.\n\n1. **Skill Development** and **Education** are foundational across all graphs, emphasizing the importance of continuous learning and formal qualifications in career advancement.\n2. **Networking** is a recurring variable, highlighting its universal value in uncovering opportunities and gaining insights across industries.\n3. **Project Experience** is crucial for demonstrating practical skills and knowledge, with its importance underscored in fields like data science, engineering, and blockchain.\n4. **Industry Knowledge** and **Technical Skills** are closely linked, reflecting the need to stay updated with industry trends and technical advancements.\n5. **Leadership Skills** and **Strategic Thinking** are key for higher-level positions, such as CMO or senior engineering roles, indicating the importance of management and vision.\n6. **Adaptability**, **Company Fit**, and **Project Fit** are introduced to emphasize the importance of aligning personal values and skills with organizational and project requirements, especially in transitioning to new roles or industries.\n\nThis graph serves as a versatile tool for individuals navigating their career paths, offering insights into the interconnectedness of various factors and their impact on achieving career goals."
#         ]

# with st.container():
#     st.write(f"Temp Tab")
#     # Create a graphlib graph object
#     graph = graphviz.Digraph()

#     for edge in temp_data[1]:
#         graph.edge(edge[0], edge[1], label=str(edge[2]))
#     # st.write(query)
#     st.graphviz_chart(graph)

show_pages(
    [
        Page("app.py", "Curating a Career Plan"),
        Page("page2.py", "Suggesting Potential Occupations and Wage Projections"),
        Page("page3.py", "Making Optimal Choices Among Alternatives"),
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