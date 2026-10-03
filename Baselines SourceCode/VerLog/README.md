# VerLog: local C/C++ adaptation

This directory contains the locally adapted VerLog source used for the baseline. It includes C/C++ Git-diff and method extraction with ENRE-CPP, VerLog-style call/method graph prompts, selectable dependency context, configurable OpenAI-compatible LLM providers, concurrent summarization, and final synthesis. The prompt assets are included. The original Android/Java differ source is retained for provenance; Android SDK archives and experiment outputs are excluded.

The only packaging edit to the Python implementation replaces the machine-specific ENRE-CPP default path with the bundled relative path. Model credentials are read from environment variables.

From this directory, install `requirements.txt`, provide `SILICONFLOW_API_KEY`, and run:

```sh
python src/verlog_cpp.py --git-repo /path/to/repository --ref-version BASE_TAG --tgt-version TARGET_TAG --project-name PROJECT --output-dir /path/to/output --ref-enre-json /path/to/base-enre.json --tgt-enre-json /path/to/target-enre.json --model SiliconFlow --context-mode full --no-translate-zh
```

Python, Git and Java are required. Existing ENRE JSON files can be supplied as above. 
