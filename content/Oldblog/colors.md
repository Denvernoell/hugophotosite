---
title: "Colors"
date: 2020-10-28T15:19:16-07:00
draft: true
#image: "/images/paintbrush.svg"
image: "/images/paint1.jpg"
# meta description
Summary: "this is meta description"

# taxonomies
categories:
  - "VBA"
tags:
  - "Styling"

# post type
type: "post"
HideDate: true
---

One of the most tedious jobs that I come across is managing color pallets. This seems like a simple task but when there is a specific set of colors that is always used or if you want to change multiple colors to match throughout an entire workbook, this can get more time consuming and error prone. To combat this, I created a function that stored my commonly used colors in RGB so that I could refer to them by name rather than by looking through the color list to find the desired color.
This function is as follows

```vb
function mycolor(color)
    if color = "green"
    mycolor = "rgb(10,10,10)"
    end if
```

To get this RGB value, the following procedure can be used

```vb
For Each cell In Selection
    cell.Offset(0, 2).Value = cell.Interior.color
Next cell
```

To use this list to change colors on a graph, a loop like the following can be used

```vb
i = 0
myRange = "W29"
For Each Series In ActiveChart.SeriesCollection
    myColor = Range(myRange).Offset(i, 0).Value
    Series.Format.Fill.ForeColor.RGB = myColor
    i = i + 1
Next Series
```

To create a line or square that is centered in a cell, the following procedure can be used
