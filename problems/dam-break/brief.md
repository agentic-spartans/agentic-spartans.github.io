# How fast does water run when a dam breaks?

Contributor: Phanikumar Mantha, Civil and Environmental Engineering, Michigan State University
Cartoon: A dam seen from straight above holds a lake on the left; below it a river runs right through a forested valley to a village and a bridge.
Video: Yellow water falls and spreads right beneath purple air in our side-view calculation. x/a is distance along the floor and y/a is height, both in starting block widths; T is time in units of about 0.076 seconds.
Run time: about 25 minutes per run
Run cost: about $0.20 per run
Model: GPT-6 Luna, high reasoning effort

## The problem

When a dam breaks, towns downstream need to know how fast the flood arrives. Engineers test flood programs on a lab experiment: a square block of water is released onto a dry floor. We compute the experiment that the researchers Martin and Moyce filmed in 1952 and compare with their numbers.

![A side view shows the starting block of water, side a, as a dashed outline and the spreading water in blue. The front is z from the back wall, the water at the wall is eta (η) high, and g is gravity.](sketch.png)

## What we want to find out

- How far does the front, the leading edge of the water, travel over time? Does it match the 1952 measurements for the small 2.25-inch block and the large 4.5-inch block?
- How fast does the water drop at the back wall, behind the block? Does it match the 1952 measurements?
- Does the answer change when the program cuts the water and air into more, smaller squares?
- Why does the shallow-water theory predict a faster front than Martin and Moyce measured? This simple theory treats the flood as a thin layer of water.

## What the agent team does

![The {{planner}} writes a {{plan}}, you approve it, and the {{orchestrator}} hands out the work. The {{implementer}} writes the program, the {{reviewer}} and {{verifier}} send flaws back, and the {{report writer}} writes your report.](team.png)

In the sample {{run}}, we approved the {{plan}} by typing "Approved, go ahead." The {{verifier}} then reruns the program on its own and checks its numbers against the 1952 tables and a hand calculation. You get the program, result tables, three plots, a video of the collapse and a report on the four questions.

## How we set up the calculation

Our program cuts the side view into small squares, 8, 12 or 16 across the block. We give the front distance Z and the wall height H in block widths, and time T in units of about 0.076 seconds for the small block. In these units, a small and a large block should fall the same way, so each block checks the other. The program leaves out surface tension, the pull that holds a water surface together, and friction at the walls; it stops at 3.5 time units, so we skip the last two 1952 height measurements.

## What you need to run it

A run stops when it has spent $3.

## What a good answer looks like

- The calculated front and wall height match the 1952 measurements. The front must stay within half a block width or 20 percent of each measurement, whichever is larger. The wall height must stay within 5 percent of its starting height. A rerun must give the same numbers. The program must also move a strip of water across the squares without loss, much smearing or false ripples.
- Smaller squares and the larger block barely change the answer. Over the first 3 time units, each step to smaller squares may shift the front by at most 0.3 block widths. It may shift the wall height by at most 0.02 of its starting height. The large and small blocks may differ by at most 0.05 block widths in front and 0.01 in wall height.
- Still water half a block deep must stay still and keep all its water. Pressure is the water's push on each bit of area. The pressure difference between the bottom and top must match a hand calculation within 0.01 percent.
- The report answers every question with numbers from the result tables. It says where our front is ahead of the measured front and where it is behind. It names every simplification as a limit. It ends by naming the AI model that wrote it and saying the two 1952 tables were the only data.

## What the team found

Our sample run met all four points above. Our own later check found one small slip in the program's formula for the water's stickiness. Fixing it moves the front by at most 0.004 block widths.

- We compared our numbers with 36 measurements from 1952: 29 front positions and 7 wall heights. Our front stays within the allowed gap at all 29, 19 for the small block and 10 for the large. Our front is ahead of the measured front early on and behind it later. The worst gap is about 0.25 block widths for the small block and 0.76 for the large one. The allowed gaps are wide, so passing them does not prove the calculation is that accurate.
- Our wall height stays within about 2.2 percent of the starting height at all 7 measurements. The worst gap is at 3.08 time units. There the experiment measured 0.33 of the starting height, and we got about 0.35. The 1952 release time is not known exactly, so the measured points could shift a little in time.
- From 8 to 12 squares across, the front changed by up to about 0.23 block widths. From 12 to 16, it changed by up to about 0.09. Both are within the allowed 0.3, but the front has not fully stopped changing. The wall height changed by less than 0.5 percent of its starting height, so it has stopped changing. The large block matches the small one within about 0.0014 block widths in front and 0.0002 in wall height. In the still-water test, the pressure difference matched the hand value to nine decimal places.
- The shallow-water theory says pressure depends only on depth. That needs little speeding up in the up-and-down direction; sideways speeding up is fine. The theory gives a front speed of 2 block widths per time unit. In our calculation the top of the block falls fast at first, so the pressure pushing the front drops: at 1 time unit the wall height is about 0.84, not 1. Our front speed from 2 to 3 time units is about 1.28, below the theory's 2 and the fastest measured speeds of 1.62 and 1.66. It rises from about 1.10 to 1.24 to 1.28 as the squares get smaller, so coarse squares also slow the front, and we cannot say how much of the gap comes from the physics.

![Our front distance Z over time T for each block and number of squares, with the 1952 measurements as crosses and the shallow-water theory as a dotted line far ahead. Redrawn from the sample's saved data for phone reading.](sample_1.png)

![Our wall height H over time T for the small block on three grids, with the 1952 measurements as crosses and the theory's dotted line at 1 until T = 1. Redrawn from the sample's saved data for phone reading.](sample_2.png)
