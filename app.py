import streamlit as st

from llm import ManufacturingCopilot


st.set_page_config(
    page_title="GenAI Manufacturing Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 GenAI Manufacturing Copilot")

st.write(
    "Ask manufacturing-related questions and generate structured assembly instructions."
)

question = st.text_area(
    "Question",
    placeholder="Generate assembly instructions for the cockpit..."
)

if st.button("Generate"):
    copilot = ManufacturingCopilot()
    with st.spinner("Generating assembly instructions..."):
        result = copilot.ask(question)

    st.success("Generation completed.")

    st.header("Assembly")
    st.write(result.assembly)

    with st.expander("🔧 Required Tools", expanded=True):
        for tool in result.required_tools:
            st.write(f"  - {tool}")

    with st.expander("⚙️ Operations", expanded=True):
        for i, operation in enumerate(result.operations, start=1):
            st.write(f"{i}. {operation}")

    with st.expander("⚠️ Warnings", expanded=True):
        for warning in result.warnings:
            st.warning(warning)