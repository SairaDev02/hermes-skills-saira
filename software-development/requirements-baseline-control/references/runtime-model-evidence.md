# Runtime and Model Evidence Recipe

Use this reference when a baseline depends on an upstream runtime, native library, model bundle, tokenizer, voice asset, or other distributed artifact.

## Evidence pass

1. Identify the exact local dependency version from the manifest and lockfile.
2. Query upstream repository metadata and record the default branch, current revision, license, release tags, and claimed target platforms.
3. Fetch the upstream tree recursively and filter it for the relevant model/runtime names, API examples, platform examples, release scripts, `LICENSE`, `NOTICE`, and model documentation.
4. Fetch raw examples and docs rather than relying on rendered or truncated pages. Capture the input/output contract, optional controls, callbacks, platform assumptions, and failure behavior.
5. Query release metadata and record the exact asset name, archive size, URL, digest if present, and release tag. If the API omits a digest, say so and generate a local checksum only for an artifact actually downloaded and verified.
6. Inspect the local integration manifest, smoke example, model directory, README, and license files. Record model files, reference assets, total unpacked size, sample rate, startup result, runtime factor, thread count, and benchmark settings as separate evidence fields.

## Requirements extraction

Translate evidence into implementation-neutral requirements for:

- offline/network behavior;
- input assets and reference data;
- output format, sample rate, and playback contract;
- user controls and visible states;
- invalid/missing asset behavior;
- performance measurement protocol;
- packaging size and release-manifest contents;
- license, attribution, prohibited-use, and notice obligations.

Keep a library/runtime version, crate name, model filename, or API type in a constraint only when the project explicitly commits to it. Otherwise record it as evidence or a dependency candidate.

## License reconciliation

Maintain separate rows for:

| Component | Typical source | Required review |
|---|---|---|
| Runtime/library code | Upstream repository `LICENSE` and package metadata | License, notices, patent/trademark terms |
| Model weights/export | Model README, model card, artifact archive, linked license | Commercial rights, attribution, prohibited uses, redistribution |
| Tokenizer/data/reference audio | Artifact directory and source repository | Separate copyright/license and user-consent implications |
| Generated/sample assets | Bundle README and asset provenance | Distribution and modification rights |

If sources disagree, preserve the exact wording and mark the release decision **Open**. Do not replace a local warning with a more permissive upstream summary without legal disposition.

## Minimum evidence record

```text
upstream_repo:
upstream_revision:
local_dependency_version:
model_bundle:
release_tag:
archive_size:
archive_url:
archive_digest:
local_files:
platform_claims:
input_contract:
output_contract:
benchmark_settings:
reported_result:
independent_result:
code_license:
model_license:
asset_licenses:
prohibited_use_terms:
release_decision:
```

`reported_result` and `independent_result` must remain separate. A smoke test demonstrates technical behavior; it does not establish stakeholder validation or legal clearance.
