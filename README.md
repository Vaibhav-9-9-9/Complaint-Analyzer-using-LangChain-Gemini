<body>

<div class="container">

<h1>🚨 Complaint Analyzer using LangChain & Gemini</h1>

<h2>📌 Overview</h2>

<p>
Complaint Analyzer using LangChain & Gemini is an AI-powered application that
automatically analyzes customer complaints and converts unstructured text into
structured business insights.
</p>

<p>
The application leverages <strong>Google Gemini 2.5 Flash</strong> through
<strong>LangChain</strong> to classify customer complaints, estimate severity,
identify the root issue, and recommend an appropriate action.
The final response is generated in a clean and validated JSON format,
making it easy to integrate with CRM platforms, helpdesk systems,
and customer support workflows.
</p>

<hr>

<h2>🎯 Project Objective</h2>

<p>
Automate customer complaint analysis by generating the following structured outputs:
</p>

<ul>
    <li>Complaint Category</li>
    <li>Severity Level</li>
    <li>Root Issue</li>
    <li>Recommended Action</li>
</ul>

<hr>

<h2>✨ Features</h2>

<h3>📂 Complaint Category Classification</h3>

<ul>
    <li>Billing Issue</li>
    <li>Delivery Delay</li>
    <li>Product Defect</li>
    <li>Technical Issue</li>
    <li>Customer Service Issue</li>
</ul>

<h3>⚠️ Severity Prediction</h3>

<p>
Predicts complaint severity as
<strong>High</strong>,
<strong>Medium</strong>,
or
<strong>Low</strong>.
</p>

<h3>🔍 Root Issue Identification</h3>

<p>
Extracts the primary issue behind the complaint while remaining grounded
strictly in the customer's input text.
</p>

<h3>💡 Recommended Action</h3>

<p>
Generates concise and context-aware resolution recommendations based on
complaint category, severity level, and identified root issue.
</p>

<h3>📄 Structured JSON Output</h3>

<pre>
{
    "complaint_category":"Delivery Issue",
    "severity":"High",
    "root_issue":"Delayed shipment",
    "recommended_action":"Escalate to logistics team and provide delivery update."
}
</pre>

<hr>

<h2>🏗️ Tech Stack</h2>

<table>

<tr>
    <th>Technology</th>
    <th>Purpose</th>
</tr>

<tr>
    <td>Python</td>
    <td>Programming Language</td>
</tr>

<tr>
    <td>LangChain</td>
    <td>LLM Orchestration Framework</td>
</tr>

<tr>
    <td>Google Gemini 2.5 Flash</td>
    <td>Large Language Model</td>
</tr>

<tr>
    <td>Streamlit</td>
    <td>User Interface</td>
</tr>

<tr>
    <td>Pydantic</td>
    <td>Structured Output Validation</td>
</tr>

<tr>
    <td>JsonOutputParser</td>
    <td>JSON Parsing</td>
</tr>

<tr>
    <td>Langfuse</td>
    <td>Observability & Tracing</td>
</tr>

<tr>
    <td>python-dotenv</td>
    <td>Environment Variable Management</td>
</tr>

</table>

<hr>

<h2>📂 Project Structure</h2>

<pre>
Complaint-Analyzer-using-LangChain-Gemini/

│── main.py
│── model.py
│── parser.py
│── prompt.py
│── requirements.txt
│── .env
│── README.md
</pre>

<hr>

<h2>⚙️ Installation</h2>

<pre>
git clone &lt;repository-url&gt;

cd Complaint-Analyzer-using-LangChain-Gemini

python -m venv base

# Windows
base\Scripts\activate

# Linux/macOS
source base/bin/activate

pip install -r requirements.txt
</pre>

<hr>

<h2>🔑 Environment Variables</h2>

<pre>
gemini_key=YOUR_GEMINI_API_KEY

LANGFUSE_SECRET_KEY=YOUR_SECRET_KEY

LANGFUSE_PUBLIC_KEY=YOUR_PUBLIC_KEY
</pre>

<hr>

<h2>▶️ Run the Application</h2>

<pre>
streamlit run main.py
</pre>

<hr>

<h2>📝 Example Input</h2>

<pre>
I ordered a laptop two weeks ago,
but it has not been delivered.

Customer support keeps giving generic
responses without any update.
</pre>

<hr>

<h2>📤 Example Output</h2>

<pre>
{
    "complaint_category":"Delivery Issue",
    "severity":"High",
    "root_issue":"Delayed shipment",
    "recommended_action":"Escalate the complaint to the logistics team and provide an updated delivery timeline."
}
</pre>

<hr>

<h2>🔄 Workflow</h2>

<div class="workflow">

Customer Complaint
        

        ▼

Severity Prediction

        
        ▼

Structured Complaint Analysis

        
        ▼

Category Identification

        
        ▼

Root Issue Detection

        
        ▼

Recommended Action Generation

        
        ▼

Validated JSON Output

</div>

<hr>

<h2>💼 Use Cases</h2>

<ul>

<li>Customer Support Automation</li>

<li>Complaint Prioritization</li>

<li>CRM Integration</li>

<li>Helpdesk Ticket Classification</li>

<li>Customer Experience Analytics</li>

<li>Service Quality Monitoring</li>

</ul>

<hr>

<h2>🚀 Future Enhancements</h2>

<ul>

<li>Multi-language Support</li>

<li>Automated Complaint Routing</li>

<li>Analytics Dashboard</li>

<li>Batch Complaint Processing</li>

<li>REST API Deployment</li>

<li>Ticketing System Integration</li>

</ul>

<hr>

## 🌐 Live Demo

🔗 **Live Application:** https://complaint-analyzer-using-langchain-gemini-kcnjdnfheqqfgghcmrp3.streamlit.app/

Experience the Complaint Analyzer by entering a customer complaint and receiving a structured analysis including:
- Complaint Category
- Severity Level
- Root Issue
- Recommended Action

<h2>🤝 Contribution</h2>

<p>
Contributions are welcome and appreciated. Whether it's fixing bugs,
improving documentation, adding new features, or optimizing existing
functionality, your contributions can help enhance this project.
</p>

<h3>How to Contribute</h3>

<ol>
    <li>Fork the repository.</li>
    <li>Create a new feature or bug-fix branch.</li>
    <li>Implement your changes and test them thoroughly.</li>
    <li>Commit your changes with a clear and descriptive message.</li>
    <li>Push your branch to your forked repository.</li>
    <li>Submit a Pull Request for review.</li>
</ol>

<p>
Please ensure that your code follows best practices, maintains readability,
and includes appropriate documentation where necessary.
</p>

<p>
Thank you for helping improve this project and supporting the open-source community.
</p>
