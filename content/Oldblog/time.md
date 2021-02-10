---
title: "Time"
date: 2020-12-09T14:51:14-08:00
draft: true
image: "/images/Clock.jpg"
Summary: ""
#   Taxonomies
categories:
  - "VBA"
tags:
  - "Article"
#post type
type: "post"
HideDate: true
---

One of the benefits of VBA are functions that are not included in typical excel formulas. Some of these include formulas that involve time.

for example,

```vb

Debug.Print MonthName(12)
Debug.Print MonthName(12, True))

```

will return
December
Dec

and

`WeekdayName(6)`
will return friday

```vb

debug.print(DateAdd("d", 100, Date()))

```

will display the date 100 days from now

This will also work with

Syntax|Usage
-|-
d|day
ww|week
w|weekday
m|month
q|quarter
yyyy|year
y|day of the year
h|hour
n|minute
s|second
