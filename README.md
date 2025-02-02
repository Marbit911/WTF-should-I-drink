# WTF should I drink?

Welcome to **WTF should I drink?**. Ever found yourself standing dumbstruck in front of your prized wine collection, scratching your head, wondering which bottle should grace tonight's dinner? Fear not! This interactive command-line companion will rescue you from indecision by intelligently analyzing your wine data from a CellarTracker CSV file. It offer vegetarian food pairings and checks the drinking window for each wine. 

## Contents

- [WTF should I drink?](#wtf-should-i-drink)
  - [Contents](#contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)

## Features

- **Wine Data Collection**: Automatically gathers wine data from a CSV file.
- **Vegetarian Pairings**: Provides three vegetarian food pairing suggestions for each wine.
- **Drinking Window Check**: Assesses whether each wine is within its optimal drinking window.
- **Confiurable ChatGPT integration**: The prompts for OpenAI GPT model can be changed to the personal liking. 

## Installation

Clone the repository to your local machine:

```bash
git clone git@github.com:Marbit911/WTF-should-I-drink.git
```

Ensure you have Python 3.6+ installed. Install the required packages using pip:

```bash
pip install openai
```

## Usage
Make sure to replace the placeholder values in the script with your CSV file path and OpenAI API key.

```bash
file_path = 'ENTER PATH TO CELLAR TRACKER CSV-FILE HERE'
# Add your OpenAI API key here
openai.api_key = 'YOUR OPEN API KEY'

# Path to the CSV file
file_path = 'YOUR FILE PATH'
```