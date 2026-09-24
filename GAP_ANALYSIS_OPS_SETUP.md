# Prime Bridge Media — Operations Setup Gap Analysis
**Date:** Sept 24, 2026 | **Phase:** Pre-Operations  
**Target:** ₹3-5L MRR (Oct '26), ₹1Cr (Dec '27)  
**Markets:** Chandigarh, Mohali, Panchkula, Zirakpur | **Niches:** 7 (Doctors, Restaurants, Salons, Gyms, Lawyers, Real Estate, Jewellers)

---

## CRITICAL BLOCKERS (Do first)

### 1. **Sales Pipeline is Manual / No CRM**
| Gap | Impact | Priority |
|---|---|---|
| Lead tracking is Google Sheets only | No real-time visibility into pipeline. Can't scale past 30 leads. | 🔴 CRITICAL |
| No scoring/qualification automation | Every lead gets same follow-up time regardless of readiness | 🔴 CRITICAL |
| No conversion tracking | Can't measure ACOS or funnel efficiency | 🔴 CRITICAL |

**Status:** `5-week-playbook.md` defines manual daily calls, but no infrastructure to scale  
**Action needed:**
- [ ] Migrate Lead Tracker to proper CRM (Airtable or HubSpot free tier)
- [ ] Add automated lead scoring (GBP review count, website age, social presence)
- [ ] Build Telegram bot for daily stats: "5 conversations, 1 meeting booked, pace to ₹5L is 45 days"

---

### 2. **n8n Automation is Imported but Not Active**
| Component | Status | Missing |
|---|---|---|
| n8n instance running | ✅ `n8n.kunaldahiya.me` up | — |
| Workflow imported | ✅ `PBM - SEO Blog Draft Factory.json` exists | Credentials not wired |
| Credentials configured | ❌ BLOCKED | OpenRouter API key, Pexels API key, n8n owner account |
| Schedule enabled | ❌ BLOCKED | Waiting on credential step |
| Dry-run completed | ❌ BLOCKED | Phase 3 test never ran |

**Status:** Content pipeline ready to draft but stopped at Phase 0.3  
**Action needed:**
- [ ] Complete n8n owner-account setup (Phase 0.1)
- [ ] Obtain + configure credentials: OpenRouter, Pexels (Phase 1)
- [ ] Wire credentials to 6 workflow nodes (Phase 2)
- [ ] Run manual dry-run with one validated topic (Phase 3)
- [ ] Activate daily schedule (Phase 4)

**Cost to un-block:** ~$10/mo (Pexels + OpenRouter)

---

### 3. **Lead Gen at Scale Has No Automation**
| Tool | Status | Gap |
|---|---|---|
| Apify MCP | ✅ Installed | No actors wired to any workflow |
| LinkedIn/Apollo scraping | ✅ Available (GFXToolz) | Manual local-Chrome only; not integrated into n8n |
| Email finder/verifier | ✅ Available (Apify) | No scoring or dedup pipeline |
| Phone/Maps extraction | ✅ Available | No scheduled imports |

**Status:** `prime-bridge-lead-gen` skill exists but workflows are proof-of-concept only  
**Action needed:**
- [ ] Build n8n workflow: Apify scraper → Email finder → Verification → Obsidian write
- [ ] Schedule weekly: Monday 08:00 IST (pull new targets from niche x city matrix)
- [ ] Create scoring gate: ICP ≥7 → add to **PBM Lead Tracker** sheet automatically
- [ ] Set up Telegram alert: "123 new leads pulled, 45 qualified for outreach"

---

### 4. **Email Outreach Has No Execution System**
| Component | Status | Gap |
|---|---|---|
| Sequence template | ✅ Drafted | Never scheduled or tested |
| SendGrid / Resend | ✅ Resend (local SMTP relay working on VPS) | No n8n integration for bulk send |
| Reply tracking | ❌ | No webhook to Obsidian or Lead Tracker |
| Unsubscribe handling | ⚠️ | Manual only |

**Status:** `prime-bridge-outreach` skill describes manual cold outreach; no bot  
**Action needed:**
- [ ] Build n8n Email Campaign node: pull from Lead Tracker → variable substitution → send via Resend
- [ ] Test one-off send to 5 vetted leads (verify Resend reputation + delivery)
- [ ] Add reply webhook: Resend → n8n → update Lead Tracker status
- [ ] Set up approval gate: user reviews template before bulk send

---

## INFRASTRUCTURE GAPS (Setup, not capability)

### 5. **Obsidian Vault Structure is Incomplete**
| Path | Status | Issue |
|---|---|---|
| `PBM/Site/` | ⚠️ Partial | No Drafts → QA → Live workflow |
| `PBM/SEO/` | ⚠️ Partial | No Keyword Plans, no structured Reports |
| `PBM/Funnels/` | ❌ Missing | No email sequence templates |
| `PBM/Blog/` | ⚠️ Partial | Drafts exist, no Queue or Published archive |
| `PBM/Images/` | ❌ Missing | No brand asset library |
| `PBM/Ops/` | ❌ Missing | No uptime, backup, or alert logs |
| `PBM/State/` | ❌ Missing | No system-state.json or pending-approvals.md |

**Action needed:**
- [ ] Create full vault structure per pbm-orchestrator spec
- [ ] Migrate existing docs into new folders
- [ ] Wire folders to bot outputs (n8n → Obsidian)

---

### 6. **VPS Is Running but Not Fully Instrumented**
| Service | Status | Gap |
|---|---|---|
| WordPress (primebridgemedia.com) | ✅ Live, cached | No monitoring. Manual audits only. |
| n8n (n8n.kunaldahiya.me) | ✅ Running | No backups scheduled. No error logging beyond Telegram. |
| Hermes gateway (systemd) | ✅ Running | Cron jobs won't fire until verified. No status dashboard. |
| DNS, SSL, backups | ⚠️ | No automated renewal or backup checks. |

**Action needed:**
- [ ] Set up uptime monitoring: UptimeRobot or Hermes cron job
- [ ] Configure automated backups: WordPress daily, n8n config weekly
- [ ] Create ops dashboard: site health, last backup, SSL expiry
- [ ] Test Hermes cron: `hermes cron status` → verify "Gateway running"

---

### 7. **GSC, Rank Tracking, Analytics Not Wired**
| Tool | Status | Gap |
|---|---|---|
| Google Search Console | ✅ Live | No API integration. Data manual-only. |
| Semrush / GFXToolz | ⚠️ Local Chrome only | No scheduled rank tracking. No Obsidian writes. |
| Apify SERP scraper | ✅ Available | Never scheduled or wired to reporting. |
| Rank Math schema | ✅ Live | Never validated at scale. |

**Status:** `pbm-seo` skill describes ideal workflow; infrastructure is 30% complete  
**Action needed:**
- [ ] Wire GSC API: create OAuth2 credentials, test one query
- [ ] Build n8n weekly SEO report: GSC pull + SERP check + anomaly detection → Obsidian
- [ ] Create Telegram alert: "3 rank drops >5, 2 new keywords, 1 technical flag"
- [ ] Schedule: every Sunday 08:00 IST

---

## PROCESS GAPS (Workflows, not tech)

### 8. **No Content Pillar / Topic Map Strategy**
| Gap | Impact |
|---|---|
| No keyword universe defined for 7 niches × 4 cities | Can't prioritize which pages to build first. Blog randomness. |
| No content brief template | Writers have no specs. Long revision cycles. |
| No internal link strategy | Pillar pages exist in isolation; no contextual links. |
| No schema/FAQ standardization | Inconsistent structured data; rank variance. |

**Status:** Programmatic SEO pipeline exists but no content direction  
**Action needed:**
- [ ] Create one complete topic map for Doctors × Chandigarh (50-100 keywords, 5-8 pillars)
- [ ] Document content brief format (keyword, intent, word count, internal links, schema)
- [ ] Define pillar-to-cluster internal link strategy
- [ ] Use this as template for remaining 27 niche×city universes

---

### 9. **Sales Messaging / Pitch Deck Not Standardized**
| Asset | Status | Gap |
|---|---|---|
| 1-page PDF audit | ✅ Template exists | No Elementor page to generate dynamically |
| Website case study | ❌ Missing | Can't show portfolio to prospects |
| Video walk-through | ❌ Missing | No screen-record of demo audit |
| Niche-specific pitch | ⚠️ Partial | Generic only; no "Doctors in Chandigarh" angle |

**Status:** Manual proposals generated ad-hoc; no scalable asset pipeline  
**Action needed:**
- [ ] Build Elementor page: "Audit Results" → pull via shortcode from n8n webhook
- [ ] Record 3-min video: "Here's what I saw + recommended fix" (template)
- [ ] Create 1-pager per niche: market size, average client budget, PBM fit
- [ ] Deploy proposal generator: Gap observed + budget → PDF one-click

---

### 10. **Team / Handoff Processes Not Documented**
| Function | Status | Handoff |
|---|---|---|
| Lead enrichment | Bot-ready | Who runs it? When? Approval gate? |
| Content drafting | Bot-ready | Manual review bottleneck. No SLA. |
| Site edits | Manual | No staging. No approval workflow. |
| Reporting | Manual | Weekly digest exists; no auto-send. |
| Client onboarding | Manual | Phone-based only. No form or automations. |

**Status:** Single-person (you) doing everything; no delegation or subs  
**Action needed:**
- [ ] Document each bot's input/output (even if you're running it)
- [ ] Define approval gates and SLAs (e.g., "content review ≤24h")
- [ ] Create runbooks for each recurring task
- [ ] Plan for: who runs SEO audit, who does client follow-ups, who handles refunds?

---

## MEASUREMENT GAPS (Data, dashboards)

### 11. **No KPI Dashboard / Reporting Automation**
| KPI | Tracking | Frequency |
|---|---|---|
| MRR / ARR | Google Sheet (manual) | Monthly, ad-hoc |
| Lead volume | Google Sheet (manual) | Weekly, manual count |
| Conversion rate | Not tracked | — |
| Average deal size | Not tracked | — |
| Client LTV | Not tracked | — |
| Content output | Git history (manual) | Monthly review |
| Rank movements | Manual SERP checks | Weekly, sample only |

**Status:** No automated reporting; can't see trends or forecast  
**Action needed:**
- [ ] Create KPI dashboard: Google Sheet or Airtable (pull from CRM, GSC, n8n)
- [ ] Set up weekly auto-report: Telegram push + Obsidian write
- [ ] Define targets: "₹5L/wk MRR, 10 qualified leads/wk, 30% close rate, ₹15K ASP"
- [ ] Monthly forecast: "At this pace, ₹1Cr by [DATE]?"

---

### 12. **No Client Data / Outcome Tracking**
| Gap | Impact |
|---|---|
| No project outcomes recorded | Can't build portfolio. Can't measure ROI. |
| No before/after metrics | Can't quote "80 leads in 14 days" with proof. |
| No testimonial system | Can't ask for/collect social proof. |
| No NPS or satisfaction tracking | Can't identify churn risk. |

**Status:** First client in Week 2; no systems in place yet  
**Action needed:**
- [ ] Create Client Delivery Sheet: name, service, start date, target metric, actual result, testimonial
- [ ] Build 3-column Obsidian case study template (gap, solution, proof)
- [ ] Wire into: Lead Tracker status, Telegram win alert, proposal generator

---

## CAPABILITY GAPS (Skills, tooling)

### 13. **Lawyer / Medical Compliance Not Built**
| Niche | Issue | Risk |
|---|---|---|
| Doctors | YMYL (ICMR ART Act 2021); content claims risky | High; need legal review gate |
| Lawyers | Bar association restrictions; local licensing varies | Medium; need compliance checklist |

**Status:** Mentioned in skills but no actual workflows  
**Action needed:**
- [ ] Create doctor content gate: flag medical claims → human review before publish
- [ ] Create lawyer content checklist: licensing, bar rules, jurisdiction
- [ ] Coordinate with legal counsel for each niche

---

### 14. **Local Market Intelligence Tools Missing**
| Use case | Status |
|---|---|
| Real estate comps | No integration. Manual lookups only. |
| Medical clinic / doctor listings | No integration. Manual search. |
| Competitor ad tracking | No integration. |

**Status:** `prime-bridge-medical-ops` and `prime-bridge-real-estate-ops` skills exist but not built  
**Action needed:**
- [ ] Wire Apify MCP for real-estate comps (zillow-style scraper)
- [ ] Build doctor directory integration (healthgrades, practo equivalents)
- [ ] Add Meta/Google Ad Library checks to competitor analysis

---

## QUICK-WIN OPPORTUNITIES (Do in parallel)

### ✓ Quick wins (1-2 days)
- [ ] Enable Hermes cron: `hermes cron status` + verify gateway
- [ ] Set up basic uptime monitoring (UptimeRobot free tier)
- [ ] Create Obsidian folder structure (copy pbm-orchestrator spec)
- [ ] Add weekly Telegram digest: "X leads, Y conversations, Z meetings"

### ✓ Medium wins (3-5 days)
- [ ] Complete n8n credential setup + do Phase 3 dry-run
- [ ] Build CRM: import Lead Tracker into Airtable + add scoring
- [ ] Create one complete keyword map (Doctors, Chandigarh) + content briefs
- [ ] Record pitch video + deploy proposal generator

### ✓ Bigger wins (1-2 weeks)
- [ ] Build lead-gen workflow: Apify → email finder → scoring → CRM
- [ ] Build weekly SEO report: GSC + SERP scraper + Obsidian write
- [ ] Create email campaign workflow: template → send via Resend → tracking
- [ ] Deploy KPI dashboard: MRR, leads, conversion, forecast

---

## PRIORITY ROADMAP (By business impact)

### WEEK 1 (Sept 24–30): Remove blockers
- [ ] Fix n8n (credentials + dry-run) → unblock content factory
- [ ] Wire CRM scoring → stop wasting time on unqualified leads
- [ ] Get cron running → unblock automation reliability

### WEEK 2 (Oct 1–7): Automate sales pipeline
- [ ] Build lead-gen bot (Apify → CRM)
- [ ] Build email campaign (template → send → tracking)
- [ ] Create proposal generator (PDF one-click)

### WEEK 3 (Oct 8–14): Automate reporting
- [ ] Wire GSC + SERP tracking → weekly digest
- [ ] Build KPI dashboard (MRR, leads, conversion)
- [ ] Create client delivery tracker (portfolio building)

### WEEK 4+ (Oct 15+): Expand niches + scale
- [ ] Complete keyword maps for 7 niches × 4 cities
- [ ] Scale lead-gen to all markets
- [ ] Standardize content + sales processes

---

## COST BREAKDOWN (Monthly recurring)

| Service | Current | Needed | Monthly cost |
|---|---|---|---|
| n8n (self-hosted) | ✅ | — | $0 |
| WordPress + LiteSpeed | ✅ | — | $0 (included in VPS) |
| VPS (DO droplet) | ✅ | — | $12 |
| OpenRouter (LLM API) | — | ✅ | ~$20 (1-2 drafts/day) |
| Pexels (images) | — | ⚠️ | $0 free tier (50/mo) or $10 premium (750/mo) |
| Apify (scraping) | ✅ | — | $0 (included in MCP) |
| Airtable (CRM) | — | ✅ | $10-20 (free tier may work) |
| GSC API | ✅ | — | $0 |
| Resend (email) | ✅ | — | $0 (included in relay) |
| UptimeRobot (monitoring) | — | ✅ | $0 free tier |
| **Total** | ~$12 | ~$32-52 | **$44-64/mo** |

---

## SIGN-OFF CHECKLIST

Preconditions to "ops ready":

- [ ] n8n: daily content draft running ≥3 days without error
- [ ] Lead-gen: 50+ new leads/week flowing to CRM automatically
- [ ] Email: 1 campaign tested end-to-end (send + reply webhook)
- [ ] Reporting: 2 consecutive weeks of auto-generated weekly digest
- [ ] CRM: 20+ prospects tracked; ≥1 qualified at 7+ ICP score
- [ ] Hermes cron: `status` shows "Gateway running" + ≥1 job fired
- [ ] Obsidian: vault structure complete + bot outputs flowing
- [ ] VPS: backups scheduled + uptime monitoring running
- [ ] Team: runbooks written for top 5 recurring tasks
- [ ] Sales: at least 1 proposal generated via one-click tool

---

**Next step:** Pick week 1 blockers. Start with n8n credentials. ETA to "ops ready": 2-3 weeks.

