# Claim-Verify

Claim-Verify is a pre-execution risk engine for humans and AI agents.

It evaluates claims, tasks, or proposed actions before execution by estimating:

- structural validity
- evidentiary support
- decision risk
- expected cost of error
- token / compute waste risk

It then assigns an execution permission:

- allow
- allow_with_warning
- block

## Purpose

Claim-Verify reduces decision error and prevents execution on unsupported or invalid claims.

It does not determine absolute truth.  
It determines whether acting is justified.

## Usage

Run with JSON input:

python verify.py --input claims.json

Run with raw text:

python verify.py --text_input "your input here"

Run JSON output:

python verify.py --input claims.json --json

## Output

Each result includes:

- structural_validity
- truth_status
- evidence_strength
- decision_risk
- expected_error_cost
- token_waste_risk
- execution_permission
- enforcement_reason
