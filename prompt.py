from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from parser import fi

severity_prompt=ChatPromptTemplate.from_template(
    """
    - Severe complaint with financial or service loss → should return high severity
    - Mild complaint such as minor inconvenience → should return medium or low severity
    - Complaint with unclear issue → root issue should remain broad but grounded in text

    just give the labels like High,Medium or Low instead of reasoning

    {complaint}

    """

)



final_prompt=ChatPromptTemplate.from_messages(
    
        [SystemMessagePromptTemplate.from_template(template='''AI system that reads complaint text, classifies the complaint category, estimates severity, 
                                                          and recommends an appropriate action.must rely strictly on the 
                                                          complaint content and should not exaggerate or infer unsupported facts.Give output as 
                                                          clear and crisp and short information'''),
        
        HumanMessagePromptTemplate.from_template(
            template=''' Clearly analyze the given customer complaint and return the output completely based
                              on the complaint.

                                                            
                                                "complaint_category": "string",
                                                "severity": {severity},
                                                "root_issue": "string",
                                                "recommended_action": "string"
                                              

                                                {complaint}
                                                {format_instructions}



            
            
            ''',partial_variables={'format_instructions' : fi,})
  


  
])