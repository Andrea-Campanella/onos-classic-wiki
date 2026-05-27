# Pipeconf

## Interpreter

Translate table ID, criterion, instructions into protocol-independent ones

### Treatment interpreter

Interpret sets of instructions to specific PI action

### Table counter support

Interpret table ID to PI counter ID

## Pipeliner

Compiles Flow Objectives to flows and groups

### Pipeliner translation result

Data structure includes translation result, which comes from sub-pipeliners below.

### Filtering pipeliner

Translate filtering objective to flows for tables inside filtering control block.

### Forwarding pipeliner

Translate forwarding objective to flows for tables inside forwarding control block.

### Next pipeliner

Translate next objective to flows and groups for tables inside next control block.
