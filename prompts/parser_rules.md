### Parser Rules

- All parsing logic must yield only fields specified in the documentation.
- No field may be guessed or filled if not available. When in doubt, leave as null.
- If a PDF or patch note cannot provide a value, record "verified": false.