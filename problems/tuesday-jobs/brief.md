# Pick a future by its Tuesday

Contributor: Spartan Agentic AI Studio, Michigan State University
Cartoon: An open diary on a desk seen from above, with a garden trowel, a wrench, a stick of chalk and a cup of coffee around it.
Run time: about 20 minutes per run
Run cost: about $0.24 per run
Model: GPT-6 Luna, high reasoning effort

## The problem

A job title makes you think about how respected the job is and who does it. What you actually live with is an ordinary working day, such as a Tuesday. This {{agent team}} lets you pick a job by diaries of its Tuesdays, built from moments such as finishing on time, before you see any job title.

![The eight boxes are the steps below, in order. The orange box is the verifier's check.](sketch.png)

- Step 1: The {{planner}}, an AI helper, writes the {{plan}}: the steps for this run and the checks its result must pass. It lists 10 rather different moments: small parts of a workday that some jobs have and others do not, such as working outdoors. It also picks 50 very different jobs so that each moment fits some of them. Each job gets a secret label, such as C36, so its name stays hidden from you.
- Step 2: You read the {{plan}} and approve it, or ask for changes. Then you look at the moments, not the jobs, and rate how much you like each one from 1 to 5. A 1 means you would rather not have it, and a 5 means you like it a lot.
- Step 3: Many diary writers, also AI helpers, work at once, one per job. Each invents a diary of an ordinary Tuesday in that job, about 150 words, never using a word of the job's name.
- Step 4: Many moment scorers work at once, one per diary, and never see the job names. They find how relevant each of your 10 moments is in the diary, from 0 if it never happens to 5 if it clearly happens. This mark is about the diary, not about how much you like the moment. For each mark they copy the line from the diary that shows it.
- Step 5: The {{verifier}} checks the work of the diary writers and moment scorers against the three points under "What a good answer looks like". Work that fails goes back to be redone before you see any diary.
- Step 6: The team ranks the diaries by how well their moments match your ratings, as "How the diaries are ranked" explains. You read the top few, such as the best five, shown only by their labels, and pick the Tuesday you like best.
- Step 7: Only now does the {{orchestrator}}, the AI helper you talk to, tell you the job behind your diary. That is the job whose Tuesday you liked best, chosen before you knew what it was.
- Step 8: The {{report writer}} writes your report as a Word file: the task, the checks, the results and how the team worked. You add your own judgment before you hand it in.

## What we want to find out

- What matters most to you in an ordinary workday?
- Which diary would you pick if you could not see the job title?
- What job is behind the diary you picked?

## What the agent team does

![The work moves from the planner to the diary writers, the moment scorers and the verifier. You approve the plan, rate the moments and pick a diary; a failed check goes back to the orchestrator.](team.png)

The {{orchestrator}} is the {{agent}} you talk to, and it gives every other {{agent}} one task. To start, open the downloaded folder in OpenCode and type /do followed by "Read the Tuesday task."

## How the diaries are ranked

- The team picks the rule and shows it with the best diaries.
- In our run, each moment gave a diary 6 points when its mark matched your rating, and 1 point less for each step apart. With 10 moments, the most a diary could get was 60.
- Pay, required schooling and the place of the job are not part of it. Only the moments you rate count, including finishing on time.

## What a good answer looks like

- No job name reaches you or the moment scorers before you pick.
- Every scored moment comes with a line copied word for word from its diary.
- Most moments show up in the diaries.

## What the team found

In our test, we ran the team once with 10 moments and 50 jobs.

- The best diary got 55 out of 60 points, and eight diaries got 53 or more. The team showed all eight by label.
- Our tester picked the best diary, without seeing any job names.
- That diary belonged to an environmental consultant. One moment was seeing a finished result by the end of the day, and our tester rated it 5. The scorers marked this diary 5 for it and quoted "left a little after five, with the main record complete."
- No diary named its own job, and every mark had a line copied word for word from its diary.
- Our run skipped two steps: it showed no {{plan}} for approval, and no report was written.
- In our run the {{orchestrator}}, not the {{planner}}, picked the 50 jobs.
- The first scorers saw our tester's ratings. The team marked all 50 diaries again without them, and these results use the second marks.
- The diary writers were told the kinds of moments to show, so the diaries may show them more often than real days would.
- The {{verifier}} first failed the check that no job name leaks, because diaries used words for people's roles. It passed when asked to look only for job titles.
