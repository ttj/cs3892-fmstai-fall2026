# Case studies — the menu, and how to claim one

**CS 3892 / 5892, Fall 2026 · 5% of the course grade · one per student**

Each of you leads or co-leads **one** in-class case study: roughly **10 minutes**, early in a
session, on a real failure of software or an AI system. Sign-up opens **Thursday August 27** and
closes **Friday September 4**, the add/drop deadline. Anything unclaimed by then I assign.

## What a case study has to do

Three things, in this order, and the third is the one that matters:

1. **What happened.** Enough for the room to picture it. Dates, who was affected, scale.
2. **The mechanism.** Not "the software failed" — *what* failed, and why that produced *this*.
   A race condition, an unchecked conversion, a specification that did not cover the case, a model
   deployed outside its validation envelope.
3. **What formal method, if any, would have caught it** — and **be willing to answer "none."**
   That is a legitimate and interesting answer, and it is often the right one. A case study that
   concludes "model checking would have prevented this" without arguing *what property* would have
   been checked, *against what model*, is the failure mode of this assignment.

**Bring one primary source.** An incident report, an investigation, a court filing, a postmortem —
not a news article about the report. This course is about the difference between what is checked
and what is repeated, and a case study built on secondary coverage undercuts its own point.

## The menu

Claim any one. Two people may co-lead a single topic, and for the larger incidents that is the
better choice. **You may also propose your own** — email me the incident and one primary source.

### Classic software failure

| # | Incident | Year | Where to start |
|---|---|---|---|
| 1 | **Therac-25** radiation overdoses | 1985–87 | Leveson & Turner, *IEEE Computer* 26(7) |
| 2 | **Ariane 5 Flight 501** | 1996 | ESA Inquiry Board report |
| 3 | **Mars Climate Orbiter** | 1999 | NASA Mishap Investigation Board Phase I |
| 4 | **Northeast blackout** — race condition in the alarm system | 2003 | US–Canada Task Force final report |
| 5 | **Toyota unintended acceleration** | 2009–13 | NASA/NHTSA engineering report; Barr's trial testimony |
| 6 | **Knight Capital** — $440M in 45 minutes | 2012 | SEC administrative proceeding 34-70694 |
| 7 | **Heartbleed** | 2014 | CVE-2014-0160; the OpenSSL commit |
| 8 | **Log4Shell** | 2021 | CVE-2021-44228; CISA advisory |
| 9 | **CrowdStrike Falcon** — 8.5M Windows hosts | 2024 | CrowdStrike external technical root cause analysis |

### Autonomy and control

| # | Incident | Year | Where to start |
|---|---|---|---|
| 10 | **Uber ATG, Tempe** — Elaine Herzberg | 2018 | NTSB HAR-19/03 *(used in D1 — pick another unless you go deeper)* |
| 11 | **Boeing 737 MAX / MCAS** | 2018–19 | JATR report; House Committee final report |
| 12 | **Tesla Autopilot** — NHTSA's defect finding | 2024 | ODI EA22002 closing resume |
| 13 | **Cruise pedestrian dragging**, San Francisco | 2023 | CPUC / DMV suspension orders; Quinn Emanuel report |

### AI systems and decisions about people

| # | Incident | Year | Where to start |
|---|---|---|---|
| 14 | **COMPAS** recidivism scoring | 2016 | ProPublica; Chouldechova, *Big Data* 5(2) |
| 15 | **Amazon recruiting tool** | 2018 | Reuters reporting; note how thin the primary record is |
| 16 | **Apple Card** credit limits | 2019 | NY DFS investigation report |
| 17 | **Dutch childcare benefits** (*toeslagenaffaire*) | 2019–21 | Parliamentary inquiry *Ongekend onrecht* |
| 18 | **Robodebt**, Australia | 2016–20 | Royal Commission final report |
| 19 | **Post Office Horizon**, UK | 1999–2019 | *Bates v Post Office*; the statutory inquiry |
| 20 | **Epic Sepsis Model** | 2021 | Wong et al., *JAMA Intern Med* 181(8) — **and its erratum** |

### Generative AI and agents

| # | Incident | Year | Where to start |
|---|---|---|---|
| 21 | **Air Canada chatbot** — held to its own hallucination | 2024 | *Moffatt v. Air Canada*, BC CRT |
| 22 | **Hallucinated citations in court filings** | 2023– | *Mata v. Avianca*; the AI Hallucination Cases database |
| 23 | **A coding agent deletes a production database** | 2025 | The vendor postmortem — read it for what it does *not* claim |
| 24 | **Character.AI / *Garcia v. Character Technologies*** | 2024–25 | The May 2025 order on motions to dismiss |
| 25 | **Prompt injection in a deployed agent** — your choice of documented case | 2024– | Bring the writeup |

> **A note on #15, #23 and #25.** These have the weakest primary records on the list, and that is
> *why* they are worth taking: part of your job becomes showing the room how much of what "everyone
> knows" about the incident is actually established. That is a harder and better talk than a
> well-documented failure told straight.

## How to claim one

Sign-up is a **group self-enrolment** in Brightspace: **Course Tools → Groups → Case study sign-up**,
pick your topic, click **Join Group**. Each topic holds up to two people, and the list shows how
many places are left, so you can see what is still open.

- **One topic per student.** If you join and change your mind, leave the old group first.
- **Co-leading is fine and often better** — agree between you who covers mechanism and who covers
  the formal-methods question.
- **Closes Friday September 4, 11:59 p.m.** After that I assign what is left.
- **Proposing your own:** email me the incident and one primary source before September 4, and I
  will add it to the list so you can claim it.

Your session will be scheduled to sit near the relevant unit — the Therac-25 and Ariane failures
belong early, the neural-network cases belong in November. I will confirm dates once sign-up closes.
