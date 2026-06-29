# LLM Service (starter)

A typed FastAPI microservice that extracts **schema-validated** structured data from free text using Claude. The "hello world" of production LLM engineering — and a direct fit for [Module 6](../../phases/06-llms.md).

## Run

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...        # or use a .env file
uvicorn app:app --reload
# open http://127.0.0.1:8000/docs
```

```bash
curl -X POST http://127.0.0.1:8000/extract \
  -H 'content-type: application/json' \
  -d '{"text":"Hi, I am Dana from Acme, dana@acme.io"}'
```

## Run the eval

```bash
python eval.py     # scores behavior over a dataset — your real "tests"
```

## Run in Docker

```bash
docker build -t llm-service .
docker run -p 8000:8000 -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY llm-service
```

## What this demonstrates (talk about these in interviews)
- **Structured output** via tool-calling (schema-guaranteed JSON, not "parse and pray").
- **Warm client** loaded once at startup, not per request.
- **Evals over assertions** — you can't unit-test exact LLM strings.
- Clean error handling (upstream 502 vs internal 500), typed I/O, Dockerized.

## Make it yours (the upgrade path → portfolio piece)
1. Swap the use case for something real (resume parser, support-ticket triage, invoice extractor).
2. Grow `eval.py` to 15+ cases; track the score over time.
3. Add request logging + token/cost metrics ([Module 9](../../phases/09-mlops-production.md)).
4. Add a tiny Streamlit/Gradio UI or a frontend.
5. Deploy it (Render/Fly/Modal/HF Spaces) and put the live URL in the README.
