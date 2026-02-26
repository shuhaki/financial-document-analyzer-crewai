## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai.tools import tool
from crewai_tools import SerperDevTool
from pypdf import PdfReader

## Creating search tool
search_tool = SerperDevTool()

## Creating custom pdf reader tool
@tool("read_financial_document")
def read_data_tool(path: str = 'data/sample.pdf') -> str:
    """Tool to read data from a pdf file from a path

    Args:
        path (str, optional): Path of the pdf file. Defaults to 'data/sample.pdf'.

    Returns:
        str: Full Financial Document file
    """
    
    reader = PdfReader(path)
    
    full_report = ""
    for page in reader.pages:
        # Clean and format the financial document data
        content = page.extract_text()
        
        # Remove extra whitespaces and format properly
        if content:
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
                
            full_report += content + "\n"
            
    return full_report

class FinancialDocumentTool:
    read_data_tool = read_data_tool

## Creating Investment Analysis Tool
@tool("analyze_investment")
def analyze_investment_tool(financial_document_data: str) -> str:
    """Tool to analyze investment opportunities from financial document data"""
    # Process and analyze the financial document data
    processed_data = financial_document_data
    
    # Clean up the data format
    i = 0
    while i < len(processed_data):
        if processed_data[i:i+2] == "  ":  # Remove double spaces
            processed_data = processed_data[:i] + processed_data[i+1:]
        else:
            i += 1
            
    # TODO: Implement investment analysis logic here
    return "Investment analysis functionality to be implemented"

class InvestmentTool:
    analyze_investment_tool = analyze_investment_tool

## Creating Risk Assessment Tool
@tool("create_risk_assessment")
def create_risk_assessment_tool(financial_document_data: str) -> str:
    """Tool to create risk assessment from financial document data"""
    # TODO: Implement risk assessment logic here
    return "Risk assessment functionality to be implemented"

class RiskTool:
    create_risk_assessment_tool = create_risk_assessment_tool

