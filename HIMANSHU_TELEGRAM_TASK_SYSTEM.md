# Daily Task Assignment System (Telegram Bot)

**Purpose:** Send Himanshu his next day's work assignment every evening at 8 PM IST  
**Platform:** Telegram (via n8n workflow)  
**Frequency:** Mon/Tue/Wed 8 PM IST → next day's task assigned  
**Format:** Structured message with brief, checklist, templates, and dashboard link

---

## Setup Instructions

### 1. Telegram Bot Configuration

**Your setup (you already have):**
- Bot ID: `8022669577` (your bot)
- Chat ID: `678550053` (your chat)

**Himanshu's setup (needs to be done):**
- Create a new bot via BotFather: `/newbot`
- Name it: `PBM Himanshu Bot`
- You'll get a `bot_token` (e.g., `123456789:ABCDefGhIjKlMnOpQrStUvWxYz`)
- Add the bot to a group or DM with Himanshu
- Get Himanshu's chat ID: ask him to `/start` the bot and check the webhook

### 2. n8n Workflow: Daily Task Assignment

**Create this workflow in n8n.kunaldahiya.me:**

**Trigger:** Schedule (Cron)
```
0 20 * * 1-3
(8 PM IST, Monday–Wednesday)
```

**Nodes:**

**Node 1: Determine Task Day**
```javascript
const dayOfWeek = new Date().getDay();
const taskType = {
  1: { day: 'Monday', task: 'Publish 1 Page + 1 Blog', duration: '4 hours' },
  2: { day: 'Tuesday', task: 'Build Social Media Calendar', duration: '2 hours' },
  3: { day: 'Wednesday', task: 'Create Templates', duration: '2 hours' }
};
return [{ json: taskType[dayOfWeek] }];
```

**Node 2: Get Content Brief from Google Sheets**
```
HTTP GET to Google Sheets API:
GET https://sheets.googleapis.com/v4/spreadsheets/[SHEET_ID]/values/'Content Queue'!A1:Z100

Filter for tomorrow's row:
- pipeline_status = 'ready_for_draft'
- validation_status = 'validated'
- Take first row
```

**Node 3: Format Task Message**
```javascript
const task = $json.content_brief;
const day = $json.day;

const message = `📋 Tomorrow's Work Assignment

📅 ${new Date(new Date().getTime() + 86400000).toISOString().split('T')[0]} | ${day}

🎯 Task: ${task.task}
⏱ Time: ${task.duration}

📄 BRIEF
Niche: ${task.niche}
City: ${task.city}
Topic: ${task.title}
Focus keyword: ${task.focus_keyword}
Word count: ${task.word_count}

✓ Checklist: https://primebridgemedia.com/quality-checklist
✓ Templates: [Canva folder link]
✓ Dashboard: https://cdn.jsdelivr.net/gh/smilingkunal/prime-bridge-media-launch@main/himanshu-work-tracker.html

Questions? Reply here or call @kunaldahiya`;

return [{ json: { message } }];
```

**Node 4: Send via Telegram**
```
HTTP POST to Telegram Bot API:
https://api.telegram.org/bot[HIMANSHU_BOT_TOKEN]/sendMessage

Body:
{
  "chat_id": [HIMANSHU_CHAT_ID],
  "text": {{ $json.message }},
  "parse_mode": "Markdown"
}
```

**Node 5: Log to Google Sheets**
```
Append to 'Task Log' sheet:
[Date sent, Day, Task, Status, Timestamp]
```

---

## Daily Message Template

This is what Himanshu receives every evening:

```
📋 Tomorrow's Work Assignment

📅 2026-09-25 | WEDNESDAY

🎯 Task: Create Post & Social Media Templates
⏱ Time: 2 hours

🎨 TEMPLATES NEEDED
- Instagram Carousel (5 slides): "Doctor tips for Google Reviews"
- LinkedIn Post: Professional angle on testimonials
- Twitter Thread: 5-step walkthrough

Brand colors: #004CB1, #F1F5F9
Canva link: [shared folder]

✓ Checklist: https://primebridgemedia.com/quality-checklist
✓ Quality gate: All templates must match brand guidelines
✓ Dashboard: [tracker link]
✓ Previous templates: [reference folder]

Questions? Reply here or call @kunaldahiya
```

---

## Alternative: Manual Message (If You Prefer)

If you don't want to automate it, send this template every evening:

**Copy/paste this into Telegram (customize for the day):**

```
📋 Tomorrow's Work Assignment

📅 [DATE] | MONDAY

🎯 Task: Publish 1 Page + 1 Blog

📄 PAGE BRIEF
Niche: Doctors
City: Chandigarh
Topic: GBP Setup for Clinics
Focus keyword: GBP for doctors Chandigarh
Word count: 1800
Content brief: [LINK to Google Doc]

📝 BLOG BRIEF
Niche: Restaurants
City: Mohali
Topic: 5 Ways Google Reviews Drive Foot Traffic
Focus keyword: Google reviews restaurants Mohali
Word count: 1000
Content brief: [LINK to Google Doc]

✓ Quality checklist: [LINK]
✓ Dashboard: [TRACKER LINK]
✓ Templates folder: [CANVA LINK]

Any blockers? Reply here or call @kunaldahiya
```

---

## Weekly Task Assignments (4-week rotation)

### Week 1 (Sept 23–29)

**Monday Sept 23:**
- Page: Doctors × Chandigarh — "GBP Setup for Clinics"
- Blog: Restaurants × Mohali — "Google Reviews Drive Foot Traffic"

**Tuesday Sept 24:**
- Calendar: Weekly social posts for above content (21 posts)

**Wednesday Sept 25:**
- Templates: IG carousel (doctor tips), LinkedIn post, Twitter thread

### Week 2 (Sept 30 – Oct 6)

**Monday Oct 1:**
- Page: Salons × Panchkula — "Google Business Profile for Salons"
- Blog: Gyms × Zirakpur — "5 Local SEO Tips for Fitness Studios"

**Tuesday Oct 2:**
- Calendar: Weekly social posts (21 posts)

**Wednesday Oct 3:**
- Templates: IG carousel (salon services), LinkedIn post, Twitter thread

### Week 3 (Oct 7–13)

**Monday Oct 8:**
- Page: Lawyers × Chandigarh — "Local SEO for Law Practices"
- Blog: Real Estate × Mohali — "Google Business Profile for Realtors"

**Tuesday Oct 9:**
- Calendar: Social posts (21 posts)

**Wednesday Oct 10:**
- Templates: IG carousel (legal practice), LinkedIn, Twitter

### Week 4 (Oct 14–20)

**Monday Oct 15:**
- Page: Jewellers × Panchkula — "Local SEO for Jewelry Stores"
- Blog: Doctors × Zirakpur — "Doctor Reviews: Building Trust Locally"

**Tuesday Oct 16:**
- Calendar: Social posts (21 posts)

**Wednesday Oct 17:**
- Templates: IG carousel (jewelry), LinkedIn, Twitter

---

## Feedback Loop (Every Friday 5 PM)

**You send Himanshu a Friday summary:**

```
✅ Week Summary (Sept 23–29)

Published:
✓ 4 pages (Doctors, Restaurants, Salons, Gyms)
✓ 4 blogs (matching niches)
✓ Social calendar: 21 posts × 4 days = 84 posts drafted
✓ Templates: 12 designs created

📊 Metrics:
- Avg Rank Math score: 76
- Avg word count: 1650 words (pages), 980 (blogs)
- Zero missed deadlines ✅

🎯 Next week focus:
- Lawyers (Page + Blog)
- Real Estate (Page + Blog)
- Continue calendar + templates

💡 Notes:
- Your FAQ sections are getting better! Keep that detail level.
- One page had broken internal link (fixed for you).
- Next week: try to get all pages to ≥78 on Rank Math.

Keep it up! 🚀
```

---

## Success Criteria (Track These)

**By Oct 31, 2026:**

| Metric | Target | Current | Status |
|---|---|---|---|
| Pages published | 16 | — | 🟡 In progress |
| Blogs published | 16 | — | 🟡 In progress |
| Avg Rank Math score | ≥75 | — | 🟡 In progress |
| Zero missed Mondays | 100% | — | 🟡 In progress |
| Social calendar on-time | 100% | — | 🟡 In progress |
| Templates on-brand | 100% | — | 🟡 In progress |
| Organic leads from content | 50–100 | — | 🟡 Pending |

---

## If Himanshu Gets Stuck

**Blocker escalation:**

1. **Himanshu messages Telegram immediately** with the blocker
2. **You respond within 2 hours** with either:
   - Answer (e.g., "Yes, use H2 for section headers")
   - Workaround (e.g., "Use this template instead")
   - Extension (e.g., "I'm extending Monday to Tuesday for this topic")
3. **He resumes work** and completes by EOD
4. **Note in Friday summary** what caused the block

---

## Tools He'll Use Daily

| Tool | Access | How |
|---|---|---|
| WordPress | primebridgemedia.com/wp-admin | Email (ask you for password) |
| Rank Math | Built into WP | Available in editor |
| Google Sheets | Shared folder | "PBM Content Production" |
| Canva | Shared account | You add him as collaborator |
| Telegram | [bot link] | Receives task assignments here |
| Work Tracker | himanshu-work-tracker.html | Marks tasks done/not done |
| Training Manual | HIMANSHU_TRAINING_MANUAL.md | Reference for any question |

---

## n8n Workflow JSON (Optional: Copy + Paste)

If you want the exact workflow, save this as `Himanshu-Daily-Task-Assigner.json` and import it:

```json
{
  "nodes": [
    {
      "parameters": {
        "triggerTz": "Asia/Kolkata",
        "rule": "0 20 * * 1-3"
      },
      "name": "Schedule Task (8 PM Mon-Wed)",
      "type": "n8n-nodes-base.cron",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "jsCode": "const dayOfWeek = new Date().getDay();\nconst taskType = {\n  1: { day: 'Monday', task: 'Publish 1 Page + 1 Blog', duration: '4 hours' },\n  2: { day: 'Tuesday', task: 'Build Social Media Calendar', duration: '2 hours' },\n  3: { day: 'Wednesday', task: 'Create Templates', duration: '2 hours' }\n};\nreturn [{ json: taskType[dayOfWeek] || { day: 'Unknown', task: '', duration: '' } }];"
      },
      "name": "Determine Task Day",
      "type": "n8n-nodes-base.code",
      "typeVersion": 1,
      "position": [450, 300]
    }
  ],
  "connections": {
    "Schedule Task (8 PM Mon-Wed)": {
      "main": [[{ "node": "Determine Task Day", "branch": 0, "socket": 0 }]]
    }
  }
}
```

---

## Quick Start Checklist

To launch this system:

- [ ] Get Himanshu's Telegram chat ID (ask him to `/start` bot)
- [ ] Get Himanshu's bot token (create via BotFather)
- [ ] Create n8n workflow with schedule trigger
- [ ] Test one message manually before automating
- [ ] Share training manual + dashboard link with Himanshu
- [ ] Send first task assignment (Monday evening)
- [ ] Review tracker every Friday

**Total setup time:** 1–2 hours  
**Ongoing maintenance:** 2 min per assignment (if manual) or 0 (if automated)
