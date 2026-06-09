import streamlit as st
from prompt import severity_prompt,final_prompt
from parser import sev_parser,parser
from model import llm
from langfuse.langchain import CallbackHandler

st.title("Complaint Analyzer",text_alignment = "center")



severity_chain=severity_prompt | llm | sev_parser


chain=final_prompt | llm | parser


complaint = st.text_area("Enter Complaint")

if st.button("Analyze"):

    severity = severity_chain.invoke({
        "complaint": complaint
    })

    response = chain.invoke({
    "complaint": complaint,
    "severity": severity
    },
    config={"callbacks" : [CallbackHandler()]})

    st.json(response)