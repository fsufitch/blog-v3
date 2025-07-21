# Filip's Blog V3

...

## Building &mdash; Native

You need:

- Python 3.11+
- `uv`
  - Preferably via pipx: `pipx install uv`
- `make`

Steps:

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Use the `Makefile`:

   ```bash
   uv run make html
   ```

Results are in [`build/html`](build/html).

## Building &mdash; Container

You need:

- `podman` or `docker` CLI
- `make`

To run the build:

```bash
make docker-html
```

This creates results in `build/html/docker-html.tar`. To also extract for viewing, use instead:

```bash
make docker-html && tar -xf docker-html.tar -C build
```

This also places the results in [`build/html`](build/html).
