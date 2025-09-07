# Contributing

Thank you for your interest in contributing to k8s-datamodel!

## Development Setup

### Prerequisites

- Python 3.10+
- Poetry for dependency management
- Access to a Kubernetes cluster for testing

### Installation

```bash
# Clone the repository
git clone https://github.com/brun-s/k8s-datamodel.git
cd k8s-datamodel

# Install dependencies using uv
uv sync

# Install pre-commit hooks
pre-commit install
```

## Development Workflow

### Code Style

This project follows the conventions:
- Use conventional commits for commit messages
- Pre-commit hooks for code formatting and linting
- Unit tests for all new features

### Testing

```bash
# Run unit tests
pytest

# Run with coverage
pytest --cov=src/k8s_inventory_cli
```

### Commit Messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new database export feature
fix: resolve issue with CRD parsing
docs: update API documentation
test: add unit tests for operators module
```

### Pull Request Process

1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes following the coding standards
4. Add/update tests for your changes
5. Update documentation as needed
6. Submit a pull request with a clear description

### Documentation

- Use MkDocs with Material theme
- Update relevant documentation for any changes
- Include examples and use cases
- Test documentation builds locally:

```bash
mkdocs serve
```

## Project Structure

```
src/
  k8s_inventory_cli/           # Main package
    commands/                  # CLI command modules
    core/                      # Core functionality
    exporters/                 # Export format handlers
    inventory/                 # Inventory collection logic
docs/                          # Documentation
  examples/                    # Comprehensive examples
  usage/                       # Usage guides
  api/                         # API reference
tests/                         # Unit tests
```

## Release Process

1. Update version in `pyproject.toml`
2. Update CHANGELOG.md
3. Create a git tag using conventional commit format
4. GitHub Actions handles the rest:
   - Generates changelog
   - Updates mkdocs.yml and docs/index.md
   - Publishes to PyPI
   - Deploys documentation

## Questions or Issues?

- Open an issue for bug reports or feature requests
- Start a discussion for questions or ideas
- Check existing issues before creating new ones

We appreciate all contributions, big and small! 🎉
