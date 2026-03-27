"""Version 1: minimal claim verification report structure."""

def verify_claim(claim, sources, facts, gaps, verdict):
    print("=" * 60)
    print("CLAIM")
    print("-" * 60)
    print(claim)
    print()

    print("SOURCES")
    print("-" * 60)
    for source in sources:
        print(f"- {source}")
    print()

    print("FACTS")
    print("-" * 60)
    for fact in facts:
        print(f"- {fact}")
    print()

    print("GAPS / CONTRADICTIONS")
    print("-" * 60)
    for gap in gaps:
        print(f"- {gap}")
    print()

    print("VERDICT")
    print("-" * 60)
    print(verdict)
    print("=" * 60)


if __name__ == "__main__":
    claims = [
        {
            "claim": "Cerebras delivers significantly lower latency than Nvidia for large model inference",
            "sources": [
                "Cerebras benchmark or product page describing inference performance",
                "Nvidia documentation or third party benchmark describing GPU inference architecture",
            ],
            "facts": [
                "Cerebras reports lower latency or higher tokens per second for some large model inference workloads",
                "Nvidia large model inference uses multi GPU systems with interconnect overhead",
            ],
            "gaps": [
                "Benchmark conditions may differ across vendors and may not be directly comparable",
                "Vendor reported performance may not generalize across all models and workloads",
            ],
            "verdict": "PARTIALLY VERIFIED",
        },
        {
            "claim": "Coinbase and USDC will become the primary settlement layer for AI agents",
            "sources": [
                "Coinbase documentation on Base, USDC, and agent infrastructure",
                "Articles or reports discussing USDC usage and agent based payments",
            ],
            "facts": [
                "USDC is widely used for on chain settlement and stable value transfer",
                "Coinbase provides infrastructure including Base and wallets that can support agent transactions",
            ],
            "gaps": [
                "No guarantee Coinbase will dominate over all competitors in agent settlement",
                "Regulation and competing protocols could change the outcome",
            ],
            "verdict": "UNVERIFIED",
        },
        {
            "claim": "x402 will dominate HTTP-native agent micropayments",
            "sources": [
                "Documentation or examples describing x402 or HTTP based agent payments",
                "Articles or posts discussing agent to agent payments over HTTP or API calls",
            ],
            "facts": [
                "x402 is designed to allow payments directly through HTTP requests",
                "Agent systems can call APIs and execute transactions programmatically without human intervention",
            ],
            "gaps": [
                "x402 is still early and not widely adopted across the internet",
                "Other payment protocols or blockchains could compete with HTTP based payment systems",
            ],
            "verdict": "UNVERIFIED",
        },
        {
            "claim": "Waymo is already safer than human drivers in deployed urban environments",
            "sources": [
                "Waymo safety reports or official data on autonomous driving performance",
                "Third party studies comparing autonomous vehichle safety to human drivers",
            ],
            "facts": [
                "Waymo reports lower accident rates per mile compared to human drivers in some deployments",
                "Autonomous vehichles operate without fatigue or human error factors",
            ],
            "gaps": [
                "Waymo data may be limited to specific cities and conditions",
                "Safety comparisons may vary depending on metrics and reporting methods",
            ],
            "verdict": "partially verified",
        }
    ]

    for c in claims:
        verify_claim(
            c["claim"],
            c["sources"],
            c["facts"],
            c["gaps"],
            c["verdict"],
        )
        print()
