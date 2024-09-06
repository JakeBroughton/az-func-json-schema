# Azure Function Local Settings Schemas

A project to extend the base [json schema](https://json.schemastore.org/local.settings.json) to include any missing keys, including those that are function runtime specific.

## Usage/Examples

Grab the raw language-specific schema file and add it at the top of your `local.settings.json`

```json
{
  "$schema": "https://raw.githubusercontent.com/JakeBroughton/az-func-json-schema/node/local.settings.json",
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "node"
  }
}
```

## Add a New Language

Clone the project

```bash
  git clone https://github.com/JakeBroughton/az-func-json-schema.git
```

Create a new folder

```bash
  mkdir go
```

Copy the `minimal-base-template.json`

```
  cp minimal-base-template.json go/local.settings.dev.json
```

Add your new folder to the merge script

```diff
-  folders = ['node', 'python']
+  folders = ['node', 'python', 'go']
```

## Contributing

Contributions are always welcome!

If you notice a property or set of values that is not covered, feel free to create an issue or raise a PR.

## Roadmap

- Add more languages
- Add further missing properties from the existing languages
