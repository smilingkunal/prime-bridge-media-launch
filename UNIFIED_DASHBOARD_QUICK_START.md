# Unified Dashboard — Quick Start

**Single dashboard with 2 profiles: Himanshu + Kunal**  
Real-time sync, task management, progress tracking  

---

## 🔗 Live Link

```
https://cdn.jsdelivr.net/gh/smilingkunal/prime-bridge-media-launch@main/unified-dashboard.html
```

Or open locally: `C:/Users/kunal/pbm-launch-dashboard/unified-dashboard.html`

---

## 🎯 What You Have

### **For Himanshu (Content Producer)**
- ✅ Daily task list: Monday/Tuesday/Wednesday breakdown
- ✅ Clear task cards: niche, city, word count, type
- ✅ Checkbox to mark tasks done ✓
- ✅ Weekly progress bar (%)
- ✅ Stats: total tasks, completed, pending
- ✅ **No management/reporting complexity**

### **For Kunal (Operations Manager)**
- ✅ **Overview tab:** Himanshu's stats + your management tasks
- ✅ **Create Tasks tab:** Fill form, instantly create Himanshu's assignments
- ✅ **Monitor tab:** Progress bars per day + send updates
- ✅ Real-time sync: when you create/update, Himanshu sees it
- ✅ Send updates: message appears on his dashboard instantly

---

## 🚀 How It Works

### Login Screen
1. Open dashboard
2. Choose profile: **Himanshu** or **Kunal**
3. Go to your view

### Himanshu's View
- **Monday section:** Shows page + blog assignments
- **Tuesday section:** Shows social calendar task
- **Wednesday section:** Shows template creation task
- **Checkbox next to each task:** Mark done when complete
- **Progress bar at top:** Shows week completion %
- **Real-time updates:** When Kunal creates/updates tasks, they appear instantly

### Kunal's View

**Overview Tab:**
- KPIs: total tasks, completed, pending, week progress
- Your management checklist for this week
- Monthly goal tracker (16 pages + 16 blogs)

**Create Tasks Tab:**
- Form to create new assignments
- Select: day (Mon/Tue/Wed), type, niche, city, title, brief
- Click "Create Task" → instantly appears in Himanshu's view
- See recent tasks created

**Monitor Tab:**
- Progress bars for Monday/Tuesday/Wednesday tasks
- Overall week progress
- Send update message (appears on Himanshu's dashboard in real-time)

---

## 📊 Key Features

### ✅ Real-Time Sync
- When Kunal creates task → Himanshu sees it immediately
- When Himanshu marks done → Kunal's dashboard updates
- Sync indicator at bottom right: "Synced" or "Syncing..."

### ✅ Persistent Data
- Data saved to browser's localStorage
- Survives page refresh
- Same data across all tabs on same device

### ✅ Clean, Focused UI
- **Himanshu:** Only sees tasks. No noise.
- **Kunal:** All management tools in one place
- Mobile responsive

---

## 📋 Day-by-Day Usage

### **Monday 8 PM (You: Kunal)**
1. Go to Create Tasks tab
2. Day: Monday (for next week)
3. Type: Page
4. Niche: [select]
5. City: [select]
6. Title: [topic]
7. Word Count: 1800
8. Brief: [SEO brief]
9. Click "Create Task"
10. Repeat for Blog

**What Himanshu sees:** 2 new task cards appear on his Monday section. He knows exactly what to do.

### **Monday Morning (Himanshu)**
1. Open dashboard
2. Login as Himanshu
3. See Monday tasks
4. Work on page (1-2 hours)
5. Work on blog (2-3 hours)
6. Check when done ✓
7. Dashboard updates in real-time

### **Tuesday 8 PM (You: Kunal)**
1. Check Monitor tab → see if Monday tasks are done
2. Create Tuesday task (social calendar)
3. Send update if needed ("Great work on Monday page!")

### **Friday 5 PM (You: Kunal)**
1. Monitor tab → see week progress
2. Create feedback message
3. Click "Send Update" → appears on Himanshu's dashboard

---

## 🔄 Real-Time Sync (How It Works)

**Behind the scenes:**
- Browser's localStorage = shared "database"
- When one profile updates data → localStorage updates
- When other profile loads → it reads the latest data
- Refresh every 1-2 seconds to check for updates

**Same device (your laptop):**
- Open dashboard in 2 tabs (one as Himanshu, one as Kunal)
- Any changes sync instantly across tabs

**Different devices:**
- Himanshu on his phone, you on your laptop
- **If internet available:** Use version with Firebase (contact me for setup)
- **For now:** Use same device or manually refresh

---

## 📝 Task Creation (Step-by-Step)

1. **Login as Kunal**
2. **Click "Create Tasks" tab**
3. Fill in form:
   ```
   Day: Monday
   Type: Page
   Niche: Doctors
   City: Chandigarh
   Title: Google Business Profile Setup for Clinics
   Keyword: GBP for doctors Chandigarh
   Word Count: 1800
   Notes/Brief: [copy content brief here]
   ```
4. **Click "Create Task"**
5. Task appears in Himanshu's dashboard instantly
6. **Repeat for Blog** (same day or next)

---

## 💡 Tips

✅ **Keep task titles short but clear**  
❌ Bad: "Write a thing about clinics"  
✅ Good: "GBP Setup for Clinics"

✅ **Word count matters**  
- Pages: 1500–2000
- Blogs: 800–1200

✅ **Always fill the brief**  
- Even 1-2 lines helps Himanshu

✅ **Send updates weekly**  
- Positive feedback keeps him motivated
- "Page had great internal links, keep that structure"

✅ **Check Monday completion by 3 PM**  
- If behind, unblock early
- Don't wait until evening

---

## 🔧 Troubleshooting

| Issue | Fix |
|---|---|
| Tasks don't sync | Refresh page. Check localStorage in DevTools (F12 → Application → localStorage) |
| Data lost on refresh | Make sure browser allows localStorage. Check privacy settings. |
| Can't see Himanshu's tasks | Login as Kunal, go to Monitor tab. Or ask him to refresh his browser. |
| Update message doesn't appear | Refresh Himanshu's view after sending. Updates sync within 2 seconds. |
| Himanshu marks task but you don't see it | His changes are saved locally. Refresh your Monitor tab. |

---

## 📊 Sample Week (What It Looks Like)

### Monday 8 AM (Himanshu logs in)
```
📋 Your Tasks

📅 Monday — Publish Page + Blog

📄 Publish Page: Google Business Profile Setup for Clinics
   Niche: Doctors
   City: Chandigarh
   Type: Page
   Word Count: 1800
   Status: Pending ☐

📝 Publish Blog: 5 Ways Google Reviews Drive Foot Traffic
   Niche: Restaurants
   City: Mohali
   Type: Blog
   Word Count: 1000
   Status: Pending ☐
```

### Monday 1 PM
- Himanshu finishes page, checks the box ✓
- Kunal's Monitor dashboard updates: "Page: 50%"

### Monday 3 PM
- Himanshu finishes blog, checks the box ✓
- Kunal sees "Page: 100%, Blog: 100%"

### Tuesday Morning
- Kunal creates Tuesday task (social calendar)
- Himanshu sees new card appear on his Tuesday section

### Friday 5 PM
- Kunal sends update: "Great week! All Mon/Tue/Wed complete. Next week focus on Lawyers + Real Estate."
- Himanshu sees message on his dashboard

---

## 🎯 What Happens Next (With This System)

**Week 1–4:**
- 4 pages published (1 per Monday)
- 4 blogs published
- 84 social posts drafted
- 12–16 templates created
- Organic traffic starting to show

**Month 2+:**
- Scale to 2 pages + 2 blogs per Monday (if you want)
- 16 pages + 16 blogs live
- Top 5 pages ranking top 3 locally
- 50–100 leads flowing in
- System runs automatically (minimal management)

---

## ✨ You're All Set

**Send this link to Himanshu:**
```
https://cdn.jsdelivr.net/gh/smilingkunal/prime-bridge-media-launch@main/unified-dashboard.html
```

**Your setup:**
- Bookmark the link
- Login as Kunal
- Create this week's tasks
- Review Monitor tab daily
- Send updates on Friday

**Himanshu's setup:**
- Bookmark the link
- Login as Himanshu
- See tasks, work, check when done
- See your updates in real-time

**That's it. Go.** 🚀
