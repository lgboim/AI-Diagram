# AI-Diagram

Welcome to AI-Diagram, an innovative project leveraging the power of artificial intelligence to generate detailed Graphviz diagrams from textual descriptions. This tool aims to simplify the process of visualizing complex architectures, workflows, or any system you can describe in text. Whether you're documenting software architecture, designing a network, or planning a system's layout, AI-Diagram can translate your words into a clear, concise diagram.

## Features

- **Text to Diagram**: Simply describe the architecture or system in text, and AI-Diagram generates a visual representation using Graphviz.
- **Integration with Groq API**: Utilizes the advanced capabilities of the Groq API for natural language understanding, ensuring high-quality diagram generation.
- **Customizable Output**: Offers flexibility in the generated diagram's format and style, catering to various documentation needs.
- **Easy to Use**: Designed with a user-friendly interface, making it accessible for both technical and non-technical users.
- **Open Source**: AI-Diagram is open source, inviting contributions and improvements from the community.

## Getting Started

Follow these steps to get AI-Diagram up and running on your local machine:

### Prerequisites

- Python 3.6+
- Groq API key (Obtain one from [Groq's official website](https://console.groq.com/docs/quickstart))
- Graphviz installed and configured in your system's PATH

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/AI-Diagram.git
   ```
2. Navigate to the cloned directory:
   ```
   cd AI-Diagram
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Set your Groq API key as an environment variable:
   ```
   export GROQ_API_KEY=<your-api-key-here>
   ```
2. Start the Streamlit application:
   ```
   streamlit run app.py
   ```
3. Enter your architectural description in the provided text area and hit "Generate Diagram".

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Groq API for enabling the natural language understanding capabilities.
- The Streamlit team for creating an amazing tool for quickly building data applications.
- The Graphviz team for their powerful graph visualization software.
