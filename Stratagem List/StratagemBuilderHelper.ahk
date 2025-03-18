#SingleInstance force
SleepDelay := "50"

UpString := "
(
Send "{Up Down}"
Sleep SleepDelay
Send "{Up Up}"
Sleep SleepDelay


)"

DownString := "
(
Send "{Down Down}"
Sleep SleepDelay
Send "{Down Up}"
Sleep SleepDelay


)"

LeftString := "
(
Send "{Left Down}"
Sleep SleepDelay
Send "{Left Up}"
Sleep SleepDelay


)"

RightString := "
(
Send "{Right Down}"
Sleep SleepDelay
Send "{Right Up}"
Sleep SleepDelay


)"

;Up
Up::{
paste(UpString)
}

;Down
Down::{
paste(DownString)
}

;Left
Left::{
paste(LeftString)
}

;Right
Right::{
paste(RightString)
}

paste(string) {
	A_Clipboard := ''
	A_Clipboard := string
	If ClipWait(1)
		Send "^v"
}

