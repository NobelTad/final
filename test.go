package main

import (
	"fmt"
	"os/exec"
	"syscall"
)

func main() {
	psCommand := `Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show("Hello")

`

	cmd := exec.Command("powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", psCommand)

	// Hide the PowerShell window
	cmd.SysProcAttr = &syscall.SysProcAttr{
		HideWindow: true,
	}

	// Get the output
	out, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println("Error:", err)
	}
	fmt.Println("Output:", string(out))
}
