# Controlled Cybersecurity Lab Architecture

## Purpose
Provide an isolated, authorized environment for evaluating DBSARE without exposing third-party systems.

## Topology
Attacker Simulator -> Target Network -> Telemetry -> DBSARE Defender.

## Components
Attacker simulator, intentionally vulnerable or instrumented targets, network telemetry, logs/PCAP, DBSARE evidence pipeline, and evaluation harness.

## Safety boundaries
The lab must be isolated, owned or explicitly authorized, resettable, and observable. Experiments must not target public or third-party infrastructure.

## Evaluation
Measure detection, evidence quality, correlation, reasoning traceability, investigation completion, false positives/negatives, latency, resource use, and policy compliance.
