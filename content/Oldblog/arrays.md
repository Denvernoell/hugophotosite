---
title: "Arrays"
date: 2020-11-16T16:57:52-08:00
draft: true
image: "/images/markers1.jpg"
#image: "/images/grid.svg"
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

VBA arrays can be very useful for taking data from one sheet and using that data through a procedure without having to refer back to the sheet. This data is saved in memory and can be accessed by looping.

To access a range of data while being on a separate sheet,
`Storage = Worksheets("SCADA_Inventory").Range("C10").CurrentRegion.Value2`
Current region will use all data that is touching the requested range. This will go until there is a gap of values.
This will store all values on Scada_Inventory that are touching C10 into an array

To use the values from the array, a loop like the following can be used

```vb
For x = LBound(myArray, 1) + Start - 1 To UBound(myArray, 1) - backcut
    If myArray(x, Facility) <> "" And myArray(x, Tag) <> "" Then
        myFacility = myArray(x, Facility)
        myZone = myArray(x, Zone)
        myTag = myArray(x, Tag)

        Debug.Print (myFacility)
        Call editChart(myType, myFacility, myZone, myTag)

    End If
Next x
```

Using Call will use another sub procedure and use the current values inputted in that procedure. This means that the same loop can be used for many procedures without the need for the loop to be in each procedure, reducing the amount of code that needs to be changed.

Another advantage of using arrays is the ability to choose which data to use. The if statements are able to check if a condition is met before executing further.
