import streamlit as st
from dotenv import load_dotenv

# Load env FIRST
load_dotenv()

from src.agents.planner import planner_agent
from src.agents.executor import executor_agent

st.set_page_config(page_title="Agentic Healthcare AI", page_icon="🏥")

st.title("🏥 Agentic Healthcare AI Assistant")

st.markdown("Ask about insurance claims, rejections, or healthcare queries.")

query = st.text_input("💬 Enter your query:")

if query:
    with st.spinner("Thinking..."):
        plan = planner_agent(query)
        result = executor_agent(plan)

    st.subheader("🧠 Plan (Agent Decision)")
    st.json(plan)

    st.subheader("⚡ Result")
    st.write(result)