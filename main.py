import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain

# Load environment variables
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

# Initialize LLM
llm = ChatGroq(
    model='llama3-70b-8192',
    temperature=0.3
)

# Neo4j connection details
uri = os.getenv('NEO4J_URI')
username = os.getenv('NEO4J_USERNAME')
password = os.getenv('NEO4J_PASSWORD')

# Initialize Neo4jGraph
graph = Neo4jGraph(url=uri, username=username, password=password)

schema = """
Entities (Nodes):
- Person (Criminal, Accused, Suspect, Witness, Police Officer)
  - person_id (Unique Identifier)
  - name
  - alias (if any)
  - DOB
  - address
  - national_id
  - criminal_record_status (Yes/No)

- Crime (Reported Incident)
  - crime_id (Unique Identifier)
  - crime_type (Robbery, Fraud, Homicide, etc.)
  - date
  - location
  - severity
  - description

- Modus Operandi (Method of Crime)
  - mo_id (Unique Identifier)
  - technique (Example: ATM Skimming, Cyber Fraud, Armed Robbery)
  - common_patterns
  - related_evidence

- Case (Legal Investigation & Trial)
  - case_id
  - case_status (Under Investigation, Closed, Trial, etc.)
  - court_hearing_dates
  - assigned_officer_id

- Evidence
  - evidence_id
  - type (DNA, CCTV Footage, Fingerprint, etc.)
  - collected_from_location
  - linked_crime_id

Relationships (Edges):
- (:Person)-[:COMMITTED]->(:Crime)
- (:Crime)-[:FOLLOWS]->(:Modus_Operandi)
- (:Person)-[:ASSOCIATED_WITH]->(:Person)
- (:Crime)-[:HAS_EVIDENCE]->(:Evidence)
- (:Person)-[:INVESTIGATED_IN]->(:Case)
- (:Case)-[:ASSIGNED_TO]->(:Person {role: 'Police Officer'})
"""

# Initialize GraphCypherQAChain
chain = GraphCypherQAChain.from_llm(
    llm=llm, 
    graph=graph, 
    verbose=True, 
    allow_dangerous_requests=True, 
    schema=schema
)

# Streamlit UI
st.title("Crime Investigation AI - Neo4j + LangChain")
st.write("Enter your query to fetch data from the crime knowledge graph.")

query = st.text_input("Query", "List all criminals involved in robbery cases.")

if st.button("Run Query"):
    with st.spinner("Processing..."):
        response = chain.invoke({"query": query})
        st.subheader("Response:")
        st.write(response["result"])