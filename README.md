# A2A Retailmedia — the agentic retail-media hub for grocery

Connecting grocery retail to 350k makers for media buys. Not a broker, not AdWords, not a commission — the B2B agentic hub for grocery media with x402.

> Connecting grocery retail to 350k makers for media buys. Not a broker, not AdWords, not a commission — the B2B agentic hub for grocery media with x402. A2A Retailmedia is operated by GreenCore Solutions Corp.: an Agent-to-Agent (A2A) hub with a Model Context Protocol (MCP) door for grocery retail media. The retailer is the seller of media and the maker's agent is the buyer. Every grocery banner in 20 markets has a signed card with a status — unclaimed, claimed or registered — that carries only what the banner itself publishes about its media program. GreenCore Solutions Corp. owns no inventory, runs no auction, makes no creative and quotes no price. Reads are open. Call resolve_jurisdiction, then resolve_actor, then gate_transaction before the handshake tools. submit_demand needs the maker, a budget a person has approved, a Global Trade Item Number (GTIN) and a list of banners, or it returns a gap. Artificial intelligence makes mistakes. A2A Retailmedia is an agentic information source, not a recommendation. No ads, ever. No rank for sale. Trade only.

A2A Retailmedia is built and run by GreenCore Solutions Corp. (github.com/greencore-solutions). This is the public connect kit, MIT.

## The door

streamable-HTTP, stateless, server name `a2a-retailmedia`, door version 1.0.2, 19 tools (read from the wire)

- Endpoint: `https://mcp.a2a-retailmedia.ai/mcp` — any client that speaks streamable-HTTP: `{ "url": "https://mcp.a2a-retailmedia.ai/mcp", "transport": "streamable-http" }`
- Agent Card: `https://a2a-retailmedia.ai/.well-known/agent-card.json` (EdDSA, kid `a2arm-2026-10`; keyring `/.well-known/jwks.json`)
- Docs: https://a2a-retailmedia.ai/docs · Text for agents: https://a2a-retailmedia.ai/llms.txt
- Official MCP Registry: `io.github.greencore-solutions/a2a-retailmedia` (server.json in this repo)

## The cards

Every grocery banner on the record has a signed card: `https://a2a-retailmedia.ai/agents/{market}/{banner}.json`, with a page at the same address without `.json`. The signed index is `https://a2a-retailmedia.ai/agents/index.json`.

- **unclaimed** — the banner is listed; a maker's agent is referred to the banner's public media program page, or to a person where none is listed.
- **claimed** — the retailer has signed in with Microsoft and verified its domain; demand is routed to its media team.
- **registered** — the retailer's own media agent is bound to the card.

A card carries the media program, the operator, what it sells and the public program page — each only as the banner's own page states it. Never a price, inventory or a rate card. Retailers claim a card from its page.

## The twenty markets

Europe: France, Germany, Italy, Spain, Poland, UK, Netherlands, Belgium, Switzerland. Americas: United States, Canada, Mexico, Brazil. Asia-Pacific: Japan, South Korea, India, Vietnam, Thailand, Singapore, Australia.

## The tools

- **Gate** — `resolve_jurisdiction`, `resolve_actor`, `gate_transaction`
- **Find** — `find_makers`, `resolve_gtin`, `check_eligibility`, `list_banners`
- **Cards** — `get_banner_card`, `list_banner_cards`
- **Packages** — `list_packages`, `quote_package`, `find_buyer`
- **Handshake** — `submit_demand`, `receive_demand`, `a2a_handoff`
- **After** — `pull_measurement`, `renew_package`, `log_audit`
- **Makers** — `enrol_maker`

Reads are open. Three calls come before the handshake tools: `resolve_jurisdiction` → `resolve_actor` → `gate_transaction`. `submit_demand` takes the packet — the maker, a budget a person has approved, one or more Global Trade Item Numbers (GTIN), a market and a list of banners — or returns a gap naming what is missing.

## Two worked prompts

Maker side — "Which grocery banners in the UK list a retail media program, and what does each say it sells?"

Retailer side — "Show me the card for my banner in France and tell me how to claim it."

## Examples

Stock clients, no adapter: `examples/aws_strands.py` · `examples/azure_semantic_kernel.py` · `examples/google_genai.py` · `examples/generic_mcp_client.py`.

## Settle on it

The handshake settles at the door: https://a2a-retailmedia.ai/api (x402, two accept entries; a refused handoff is not settled and not charged). GreenCore Solutions Corp. quotes no price for media.

## Search words

retail media · grocery · retail media network · advertiser · maker · brand · banner · media program · agent card · claim · handshake · GTIN · x402 · AI agent · agent-to-agent · 20 markets · A2A Retailmedia · agentic hub

## Contact

https://gsc-em.com/#contact — a person at GreenCore Solutions Corp. reads it.

Built and run by GreenCore Solutions Corp.. Artificial intelligence makes mistakes. A2A Retailmedia is an agentic information source, not a recommendation. No ads, ever. No rank for sale. Trade only.
