# ml_upgrade

Python-based service used for dependency remediation and security validation testing.

## Features

- Dockerized Python application
- Cryptography integration
- Config-driven execution
- Security validation workflows
- Test coverage

## Vulnerable Dependency

| Package | Version |
|----------|----------|
| cryptography | 46.0.5 |

## Build

```bash
docker build -t ml_upgrade .
```

## Run

```bash
docker run -p 8080:8080 ml_upgrade
```

## API

```bash
GET /health
```

## Security Notes

This repository intentionally contains vulnerable dependencies for:
- CVE remediation demonstrations
- SBOM validation
- Security scanning workflows
- Automated dependency upgrade testing
