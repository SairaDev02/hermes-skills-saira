# Change Impact Map

Use this map before accepting a change. The source role records affected IDs and routes the change through the shared handoff.

| Change source | Usually affects | Required follow-up |
|---|---|---|
| Requirement | Architecture, interfaces, tasks, QA, release | Change record and regenerated downstream links |
| Quality target | Architecture, tasks, tests, monitoring | Recheck feasibility and operational gates |
| Architecture/module boundary | Interfaces, tasks, fixtures, review scope | Revalidate decomposability and ownership |
| Interface contract | Tasks, implementation, integration tests, fixtures | Version contract and regenerate dispatch bundles |
| Data model or migration | Requirements, tasks, fixtures, deployment, rollback | Compatibility and rollback assessment |
| Task scope or output contract | Implementation, QA, review | Reissue affected dispatch bundle |
| Test case or fixture | Coverage, implementation feedback, review gate | Preserve test IDs and update evidence status |
| Security or dependency rule | Architecture, tasks, CI, runtime configuration | Update constitution/ADR and security evidence |
| Review finding | Task specification, implementation, QA, architecture | Use feedback record; re-review changed revision |
| Release or environment rule | CI, deployment, monitoring, rollback | Update operational readiness handoff |
