---
title: "How To Get Started Using Auto Hot Key"
date: 2019-10-29T10:07:47+06:00
draft: true

# post thumb
image: "images/keyboard2.jpg"

# meta description
summary: "Automation on Windows"

# taxonomies
categories:
  - "Automation"
tags:
  - "Shortcuts"

# post type
type: "post"
HideDate: true
---

# Syntax

https://www.autohotkey.com/docs/Hotkeys.htm
Key names

| Syntax | Usage                                                                                  |
| ------ | -------------------------------------------------------------------------------------- |
| #      | Windows key                                                                            |
| +      | Shift                                                                                  |
| !      | Alt                                                                                    |
| ^      | Control                                                                                |
| &      | may be used between any two keys or mouse buttons to combine them into a custom hotkey |
| <      | left of one pair(left win)                                                             |
| >      | Right of one pair                                                                      |
| \*     | Use even if other are being pressed                                                    |

Capslock|
Esc|

:R\*?myKeys|
SendInput |Types keys
'n|Newline for SendInput

Run when

| Syntax                          | Usage |
| ------------------------------- | ----- |
| IfWin[Not]Active                |
| #IfWin[Not](Active/Exist)       |
| WinTrigger                      |
| #IfWinActive, ahk_class Notepad |

Repeating

| Syntax        | Usage                            |
| ------------- | -------------------------------- |
| Send {DEL 4}  | Presses the Delete key 4 times.  |
| Send {S 30}   | Sends 30 uppercase S characters. |
| Send +{TAB 4} | Presses Shift-Tab 4 times.       |

```ahk
#a::   ; Win+a
Loop, 10
{
    SendInput {Tab}
    Sleep, 3000
}
```

Use cases

| Syntax                                                                                 | Usage                                 |
| -------------------------------------------------------------------------------------- | ------------------------------------- |
| `#y::run, explorer "P:\PROJECTS\Yakima\20562 - 2020 Sewer-Storm System Master Plans\"` | Open file explorer to specific folder |
| `#b::run, C:\Program Files (x86)\BillQuick2020\BillQuick.exe`                          | Run specific program                  |

Media controls

| Syntax      |
| ----------- |
| Media_Next  |
| Media_Prev  |
| Volume_Up   |
| Volume_Down |

### Examples

Swapping keys

```ahk
Capslock::Esc
Esc::Esc
```

Returning date

```ahk
#a::
FormatTime, CurrentDateTime,, MMddyy
SendInput %CurrentDateTime%
return
```

Typing (myemail)

```ahk
:R*?:myemail
SendInput denvernoell@gmail.com
return
```

Volume change

```ahk
#=::Volume_Up
```

Change based on if scroll lock is on

```ahk
#If GetKeyState("ScrollLock", "T")=1
h::Send,{Left}
#If
```

Change based on if app is open

```ahk
strYourAppExeName := "notepad.exe"
strYourMessage := "denvernoell@gmail.com"

#If WinActive("ahk_exe " strYourAppExeName)
    ^+e::SendInput, %strYourMessage%
#if
```

### Running Your AHK Script on Windows Startup

Your hotkey script will only work if it’s running, and by default AHK scripts don’t start up when Windows boots up, so we’ll have to do that ourselves.

1. Find your hotkeys.ahk file in Windows explorer and copy the file itself

   1. Hit Win + r to run the Windows launcher (if you haven’t already overwrote that key) or
   2. Run shell:startup

   or

   1. Navigate to C:\Users\%USER%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

2. Right click anywhere and choose Paste shortcut to paste it into the Startup folder
3. Rename the file to hotkeys.ahk since the - Shortcut part isn’t useful
