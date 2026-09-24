# PBM Week 1 Operations Checklist (Sept 24–30)

**Goal:** Remove 4 critical blockers. Ship 5 foundational pieces.  
**Time estimate:** 5–6 hours total  
**Success criteria:** n8n running + CRM scoring + cron verified + backups live + vault structure

---

## ✓ TASK 1: n8n Credentials & Dry-Run (90 min)

### What this unblocks
- Daily blog drafts (10–20/month)
- Rank Math schema auto-updates
- Content queue automation

### Steps

**1.1 — Owner account setup (10 min)**
```
□ Open https://n8n.kunaldahiya.me in Chrome
□ Basic Auth: admin / NX4RX0FpKNdKOUbExTFb
□ Set new strong password (store in vault/1Password)
□ Confirm login successful
```

**1.2 — Get + save credentials (15 min)**
```
□ OpenRouter: https://openrouter.ai/keys → copy API key
□ Pexels: https://www.pexels.com/api → sign up free, get API key
□ WordPress: already have (primebridgemarketing@gmail.com app password)
```

**1.3 — Wire credentials in n8n (40 min)**
```
□ Open https://n8n.kunaldahiya.me/credentials
□ Create 3 credentials:
  □ "PBM WordPress App Password" (HTTP Basic Auth)
  □ "PBM OpenRouter API" (HTTP Header: Authorization)
  □ "PBM Pexels API" (HTTP Header: Authorization)
□ Save each

□ Open workflow: https://n8n.kunaldahiya.me/workflow/PbmBlogDraftFactory01
□ Attach credentials to 6 nodes:
  □ "Create WordPress Draft" → WordPress cred
  □ "Set Rank Math SEO Data" → WordPress cred
  □ "Generate Structured Blog via LLM" → OpenRouter cred
  □ "Upload Hero to WordPress Media" → WordPress cred
  □ "Set Media Alt + Caption" → WordPress cred
  □ Remove "Generate 16:9 Hero Image" node (replace with Pexels next)
□ Save workflow
```

**1.4 — Test once (25 min)**
```
□ Open Content Queue sheet: https://docs.google.com/spreadsheets/d/1Q3hQFnC49ZqM048JQquT8-D5e2tfV-sNJJxRXli8ds0
□ Pick row 2 (Doctors × Chandigarh)
□ Fill all columns (if missing any, fill with "metrics_exception: Tricity local baseline")
□ Set column O (validation_status) = "validated"
□ Set column P (pipeline_status) = "ready_for_draft"

□ In n8n, click Execute Workflow (top right)
□ Watch for completion (should take 2–3 min)
□ Check result:
  ✓ No Telegram alert = SUCCESS
  ✓ Telegram alert with error = read it, note the field, skip for now
  ✓ WordPress draft created = check primebridgemedia.com/wp-admin/edit.php?post_type=post (should see 1 new draft)
```

**If it fails:** Don't spend >10 min debugging. Note the error, move to next task, circle back Thursday.

---

## ✓ TASK 2: Lead Tracker → Airtable (120 min)

### What this unblocks
- Lead scoring (auto-filter unqualified)
- Forecasting (know which week you hit ₹5L)
- Sales visibility (no more manual counting)

### Steps

**2.1 — Export current tracker (5 min)**
```
□ Open: https://docs.google.com/spreadsheets/d/[YOUR_SHEET_ID]/edit
   (If you don't have it, it's in pbm-crm/README.md or ask in chat)
□ File → Download → CSV
□ Save as ~/Downloads/pbm-leads-backup.csv
```

**2.2 — Create Airtable base (15 min)**
```
□ https://airtable.com → sign up free
□ Create new base: "PBM Lead Tracker"
□ Import CSV: "pbm-leads-backup.csv"
□ Import location: "Replace current sheet"
□ Confirm all 17 columns imported
```

**2.3 — Add scoring formula (45 min)**
```
□ Add new column: "icp_score" (Number)
□ In that column, add formula for each row:

ICP SCORING RULES:
  GBP exists + has ≥20 reviews + photos posted → +3
  GBP exists + <20 reviews → +1
  No GBP → 0

  Website exists + live + https → +2
  Website exists + HTTP only → +1
  No website → 0

  Instagram active (posted ≤14 days) → +2
  Instagram exists but dead (>14 days) → +1
  No Instagram → 0

  Google My Business → +1
  No GMB → 0

  TOTAL POSSIBLE: 10
  THRESHOLD: ≥7 = qualified

□ Create Airtable formula field:
  IF(
    AND(gbp_status > 0, review_count >= 20, has_photos),
    3,
    IF(gbp_status > 0, 1, 0)
  ) + 
  IF(website_exists AND https, 2, IF(website_exists, 1, 0)) +
  IF(AND(instagram_active, posts_last_14_days), 2, IF(instagram_active, 1, 0)) +
  IF(gmb_claimed, 1, 0)

□ For now: manually fill in the formula inputs from your sheet
□ Once formula working: create Airtable view "Qualified (ICP ≥7)"
```

**2.4 — Test the scoring (15 min)**
```
□ Add 3 test rows:
  - Gym with GBP, 30 reviews, active IG → should score 7–8 (qualified)
  - Restaurant with no website, no GBP → should score 0–1 (skip)
  - Salon with website + 15 GBP reviews, dead IG → should score 4–5 (maybe)
□ Confirm formula is calculating
□ Filter to "Qualified" view → should show only gym row
□ If working: leave as-is. If broken: note error, move on.
```

**2.5 — Set up sync back to Google Sheet (optional, skip if tight on time)**
```
□ Airtable → Integrations → Zapier
□ Create Zap: Airtable row added → Google Sheet row added
□ This keeps your CRM + team sheet in sync
□ If too complex: skip, come back to this next week
```

**Fallback:** If Airtable is too much, just add ICP scoring column to Google Sheet and auto-filter for ≥7. Same effect, 10 min setup.

---

## ✓ TASK 3: Verify Hermes Cron (30 min)

### What this unblocks
- All scheduled jobs (weekly SEO report, lead-gen pulls, email sends, etc.)
- Automation reliability (jobs fire when you sleep)

### Steps

**3.1 — Check cron status (5 min)**
```
□ Terminal (Windows CMD or PowerShell):
  hermes cron status

□ Expected output:
  ✓ Gateway is running — cron jobs will fire automatically
  Next job: [timestamp]

□ If you see "Gateway is NOT running":
  Go to 3.2
```

**3.2 — If gateway is down, restart it (10 min)**
```
□ Terminal:
  hermes gateway install
  hermes gateway start

□ If prompted for UAC (Windows):
  - First prompt: Allow
  - May ask for password: type it
  - If it fails: it will fall back to Startup folder (still works)

□ Verify restart:
  hermes cron status
  (should now show "Gateway is running")
```

**3.3 — Confirm a job will fire (15 min)**
```
□ Create a test cron job:
  hermes cron create \
    --trigger "0 * * * *" \
    --prompt "Print test: $(date)" \
    --name test-hourly

□ Wait ~1 min (until next hour mark)

□ Check Hermes activity log:
  Session > Activity > Recent runs
  (should see "test-hourly" executed)

□ If it executed: SUCCESS. Delete the test job:
  hermes cron delete --name test-hourly

□ If it didn't execute: gateway may still be having issues.
  Note it, move on, circle back Thursday.
```

---

## ✓ TASK 4: VPS Backups + Monitoring (45 min)

### What this unblocks
- Data safety (don't lose clients' data to hardware failure)
- Incident visibility (know immediately if site goes down)

### Steps

**4.1 — Schedule WordPress daily backup (15 min)**
```
□ SSH into VPS (terminal):
  ssh -i C:/Users/kunal/.ssh/hermes_vps_key root@198.211.108.80

□ Create backup script:
  cat > /root/backup-wp.sh << 'EOF'
  #!/bin/bash
  DATE=$(date +%Y%m%d-%H%M%S)
  mysqldump -u kunaldahiya -p[password] wordpress > /backups/wp-$DATE.sql
  tar -czf /backups/wp-$DATE.tar.gz /var/www/primebridgemedia.com/
  find /backups -name "wp-*.sql" -mtime +30 -delete
  find /backups -name "wp-*.tar.gz" -mtime +30 -delete
  EOF

□ Make executable:
  chmod +x /root/backup-wp.sh

□ Add to crontab:
  crontab -e
  # Add this line:
  0 2 * * * /root/backup-wp.sh

□ Verify:
  crontab -l
  (should show the backup job)
```

**4.2 — Set up monitoring (20 min)**
```
□ Go to https://uptimerobot.com → sign up free
□ Add monitor:
  URL: https://primebridgemedia.com
  Type: HTTPS
  Interval: 5 min
  Alert email: your@email.com

□ Repeat for n8n:
  URL: https://n8n.kunaldahiya.me
  Type: HTTPS

□ Create one Telegram integration:
  Settings → Integrations → Telegram Bot
  Paste your bot ID (8022669577) and chat ID (678550053)

□ Test it:
  Take site offline (temporarily) and verify Telegram alert fires
  Bring it back online, verify recovery alert
```

**4.3 — Document where backups go (10 min)**
```
□ Create file: C:/Users/kunal/pbm-launch-dashboard/OPS_BACKUP_RECOVERY.md

Content:
  # VPS Backup & Recovery

  ## Daily backup location
  `/backups/wp-YYYYMMDD-HHMMSS.sql` (WordPress DB)
  `/backups/wp-YYYYMMDD-HHMMSS.tar.gz` (full WP files)
  Retention: 30 days

  ## Restore procedure
  1. SSH into VPS
  2. Stop WordPress: `sudo systemctl stop nginx`
  3. Restore DB: `mysql wordpress < /backups/wp-YYYYMMDD-HHMMSS.sql`
  4. Restore files: `tar -xzf /backups/wp-YYYYMMDD-HHMMSS.tar.gz`
  5. Restart: `sudo systemctl start nginx`

  ## Uptime monitoring
  https://uptimerobot.com → PBM sites
  Alerts: Telegram chat 678550053

□ Save it to git
```

---

## ✓ TASK 5: Obsidian Vault Structure (60 min)

### What this unblocks
- Bot outputs flowing to organized folders
- Easy archive + searching for past decisions
- Handoff documentation

### Steps

**5.1 — Create folder structure (15 min)**
```
□ Open Obsidian vault: C:/Users/kunal/Documents/ObsidianVault

□ Create these folders under PBM/:
  PBM/
  ├── Site/
  │   ├── Drafts/
  │   ├── QA/
  │   └── Published/
  ├── SEO/
  │   ├── Keyword Plans/
  │   ├── Content Briefs/
  │   ├── Audits/
  │   ├── Reports/
  │   └── State/
  ├── Funnels/
  │   ├── Email Sequences/
  │   └── Forms/
  ├── Blog/
  │   ├── Drafts/
  │   ├── Queue/
  │   ├── Published/
  │   └── State/
  ├── Images/
  │   ├── Library/
  │   └── Brand/
  ├── Ops/
  │   ├── Reports/
  │   ├── Alerts/
  │   └── State/
  └── State/
      ├── system-state.md
      ├── pending-approvals.md
      └── decision-log.md

□ In Obsidian, add each folder manually
```

**5.2 — Create state files (20 min)**
```
□ PBM/State/system-state.md

---
title: System State
last_updated: 2026-09-24
---

## Latest Status
- Content pipeline: Not running (awaiting Phase 3 dry-run)
- Lead gen: Manual only (Apify workflow in progress)
- Email outreach: Not active
- Hermes cron: [To be verified Sept 24]
- VPS backups: [To be verified Sept 24]

## Pending Approvals
- None

## Next scheduled tasks
- Monday Sept 25 09:00 IST: Complete n8n credentials (scheduled by Kunal)


□ PBM/State/pending-approvals.md

---
title: Pending Approvals
last_updated: 2026-09-24
---

## Awaiting go-ahead
- None currently

(This tracks things waiting for Kunal's yes/no)

□ PBM/State/decision-log.md

---
title: Decision Log
last_updated: 2026-09-24
---

## Sept 24, 2026
- Decision: Use Airtable for CRM (free tier, can scale to paid)
- Reason: Zapier integration easier than custom sheet automation
- Fallback: Google Sheet with ICP formula if Airtable too complex

(Keeps track of major choices + reasoning)
```

**5.3 — Create index / TOC (15 min)**
```
□ PBM/START_HERE.md

---
title: PBM Operations — Start Here
---

# Prime Bridge Media — Ops Hub

## Quick links
- [System state](PBM/State/system-state.md) — what's running right now
- [Pending approvals](PBM/State/pending-approvals.md) — waiting on me
- [Decision log](PBM/State/decision-log.md) — why we chose X over Y

## This week
- [ ] n8n dry-run complete by Tue Sept 26
- [ ] CRM scoring live by Wed Sept 27
- [ ] Cron verified by Thu Sept 28
- [ ] Backups + monitoring by Fri Sept 29

## Bots write to:
- **Blog drafts** → `PBM/Blog/Drafts/`
- **SEO reports** → `PBM/SEO/Reports/`
- **Lead reports** → (lead-gen bot TBA)
- **Ops alerts** → `PBM/Ops/Alerts/`
```

**5.4 — Test the structure (10 min)**
```
□ Create dummy file:
  Save "Test content" to PBM/Blog/Drafts/2026-09-24-test.md

□ Verify Obsidian shows it:
  Refresh vault view, search for "test"

□ If working: delete test file, done
□ If broken: restart Obsidian, try again
```

---

## BONUS (If time permits)

**5 min:** Create a Telegram reminder
```
@Mr_Morphus, set a reminder:
"PBM ops checklist — any blockers today? (n8n / CRM / cron / backups / vault)"

Every Monday 08:00 IST
```

**10 min:** Document what's next (Week 2)
```
Once blockers clear, Week 2 includes:
- Build lead-gen bot (Apify → CRM)
- Wire email campaign
- One keyword map (Doctors × Chandigarh)
```

---

## Success Criteria (by Fri Sept 27)

All 5 tasks completed = You're on track.

| Task | Done? | Proof |
|---|---|---|
| n8n credentials wired | ☐ | One dry-run successful (or error noted) |
| CRM scoring active | ☐ | Airtable base with ≥3 test leads scored |
| Cron verified | ☐ | `hermes cron status` shows "Gateway running" |
| Backups scheduled | ☐ | `/backups/` folder has files; UptimeRobot monitor live |
| Vault structure live | ☐ | Obsidian shows all folders + state files |

If 4/5 done by Friday, you're winning. If <3/5, circle back Monday.

---

**Finish line:** By Friday Sept 27, the core infrastructure is solid enough to build on top of it all next week.
