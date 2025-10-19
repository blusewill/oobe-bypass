# Windows Offline Account Creation Tool

This can create a Offline Account via passing through autounattend.xml into the post-installation

![](https://raw.githubusercontent.com/blusewill/oobe-bypass/master/image/in-action.png)

## How to Run This Script

You can Run This Script by simply typing the following command!

```
curl -L https://blusewill.top/oobe -o bypass.exe && bypass.exe
```

It will still prompt you with the language and keyboard setup.

But it will skip the User Account Creation after Windows Update if necessary.

## Is this a virus?

The Anti-Virus might have some false postive. Since it's compiled via pyinstaller without signing.

You can check the AV-test on VirusTotal

https://www.virustotal.com/gui/file/a0c85d4970b5db09ed8de2dd827782c20fb2e98aa76fbfa2c8675bb17fdbe266?nocache=1

