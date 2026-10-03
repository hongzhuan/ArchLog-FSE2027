# Codex-Arch

Codex-Arch uses the same general-purpose Codex with additional task instructions and raw SemArc architecture context for both versions:

- `ArchSem.json`: component responsibilities.
- `ClusterComponent.json`: relationships between components and clusters.
- `NamedClusters.json`: cluster names and file assignments.
- A task prompt asks Codex to inspect source changes and commit/PR evidence, identify changes affecting module functions, interfaces or collaboration, distinguish important changes from routine maintenance, and combine commits describing the same change.
- An output template organizes important changes under the supplied architecture modules and routine changes under changelog categories; entries retain concrete commit/PR links.

The additions are inputs and prompt/template constraints. Codex chooses retrieval, judgment, aggregation and assignment itself. 
