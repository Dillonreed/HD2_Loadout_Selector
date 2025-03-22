#SingleInstance force
SleepDelay := "50"

; Reinforce
Numpad1::
NumpadEnd::
{
Send "{Alt down}"
Sleep SleepDelay

Send "{Up Down}"
Sleep SleepDelay
Send "{Up Up}"
Sleep SleepDelay

Send "{Down Down}"
Sleep SleepDelay
Send "{Down Up}"
Sleep SleepDelay

Send "{Right Down}"
Sleep SleepDelay
Send "{Right Up}"
Sleep SleepDelay

Send "{Left Down}"
Sleep SleepDelay
Send "{Left Up}"
Sleep SleepDelay

Send "{Up Down}"
Sleep SleepDelay
Send "{Up Up}"
Sleep SleepDelay

Send "{Alt Up}"
}

; Resupply
Numpad2::
NumpadDown::
{
Send "{Alt down}"
Sleep SleepDelay

Send "{Down Down}"
Sleep SleepDelay
Send "{Down Up}"
Sleep SleepDelay

Send "{Down Down}"
Sleep SleepDelay
Send "{Down Up}"
Sleep SleepDelay

Send "{Up Down}"
Sleep SleepDelay
Send "{Up Up}"
Sleep SleepDelay

Send "{Right Down}"
Sleep SleepDelay
Send "{Right Up}"
Sleep SleepDelay

Send "{Alt Up}"
}

; Eagle Resupply
Numpad3::
NumpadPgdn::
{
Send "{Alt down}"
Sleep SleepDelay

Send "{Up Down}"
Sleep SleepDelay
Send "{Up Up}"
Sleep SleepDelay

Send "{Up Down}"
Sleep SleepDelay
Send "{Up Up}"
Sleep SleepDelay

Send "{Left Down}"
Sleep SleepDelay
Send "{Left Up}"
Sleep SleepDelay

Send "{Up Down}"
Sleep SleepDelay
Send "{Up Up}"
Sleep SleepDelay

Send "{Right Down}"
Sleep SleepDelay
Send "{Right Up}"
Sleep SleepDelay

Send "{Alt Up}"
}

; Hellbomb
Numpad8::
NumpadUp::
{
Send "{Alt down}"
Sleep SleepDelay

Send "{Down Down}"
Sleep SleepDelay
Send "{Down Up}"
Sleep SleepDelay

Send "{Up Down}"
Sleep SleepDelay
Send "{Up Up}"
Sleep SleepDelay

Send "{Left Down}"
Sleep SleepDelay
Send "{Left Up}"
Sleep SleepDelay

Send "{Down Down}"
Sleep SleepDelay
Send "{Down Up}"
Sleep SleepDelay

Send "{Up Down}"
Sleep SleepDelay
Send "{Up Up}"
Sleep SleepDelay

Send "{Right Down}"
Sleep SleepDelay
Send "{Right Up}"
Sleep SleepDelay

Send "{Down Down}"
Sleep SleepDelay
Send "{Down Up}"
Sleep SleepDelay

Send "{Up Down}"
Sleep SleepDelay
Send "{Up Up}"
Sleep SleepDelay

Send "{Alt Up}"
}

; %1StratagemName
Numpad4::
NumpadLeft::
{
Send "{Alt down}"
Sleep SleepDelay

%1KeyCombination

Send "{Alt Up}"
}

; %2StratagemName
Numpad6::
NumpadRight::
{
Send "{Alt down}"
Sleep SleepDelay

%2KeyCombination

Send "{Alt Up}"
}

; %3StratagemName
Numpad7::
NumpadHome::
{
Send "{Alt down}"
Sleep SleepDelay

%3KeyCombination

Send "{Alt Up}"
}

; %4StratagemName
Numpad9::
NumpadPgup::
{
Send "{Alt down}"
Sleep SleepDelay

%4KeyCombination

Send "{Alt Up}"
}