
# AmethystPy

Automate Google Forms reponses with ChatGPT's aid


## Configuration Variables

To run this project, you will need to add the following variables to your config.ini file

```ini
[OPTIONS]
MAX_ATTEMPT : 10
RETRY_INTERVAL : 5
API_KEY : sk-4xxx,sk-8xxx,sk-pxxx
CHATGPT_MODELS : gpt-3.5-turbo-0125,gpt-3.5-turbo,gpt-3.5-turbo-1106
FORCE_MODEL : gpt-3.5-turbo

[ENDPOINTS]
FORMS_URL: https://docs.google.com/forms/d/e/<unique id>
```


## Usage/Examples

```python
from amethyst import AmethystPy

run = AmethystPy()

```

