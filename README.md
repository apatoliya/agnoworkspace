## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd 1-Basic-Agents
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run streamlit_app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Start asking questions about Thai cuisine in the chat interface!

## Sample Questions

You can ask questions like:
- How do I make Pad Thai?
- What is the history of Thai curry?
- What are common Thai ingredients?
- How do I make Tom Yum soup?

## Project Structure

- `streamlit_app.py`: The main Streamlit application file
- `agent_memory.py`: Contains the AI agent configuration and knowledge base setup
- `requirements.txt`: Lists all required Python packages
- `.env`: Environment variables file (not included in repository)

## Technologies Used

- Streamlit: For the web interface
- OpenAI GPT-3.5-turbo: For natural language understanding and responses
- Agno: For agent management and knowledge base integration
- LanceDB: For vector database storage
- DuckDuckGo: For web search capabilities

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 