from langchain_core.output_parsers import JsonOutputParser,PydanticOutputParser,StrOutputParser
from pydantic import BaseModel,Field


sev_parser=StrOutputParser()


class Output_Format(BaseModel):
  complaint_category : str = Field('Mention the compalint category precisely based on the complaint')
  severity : str = Field('Mention the severity precisely based on the complaint')
  root_issue : str = Field('Mention the root_issue precisely based on the complaint')
  recommended_action : str = Field('Analyzing the issue give precise recommended action based on the category,severity and root_issue')


parser=JsonOutputParser(pydantic_object=Output_Format)

fi=parser.get_format_instructions()
