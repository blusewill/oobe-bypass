# Windows Offline Account Creation Tool

This can create a Offline Account via passing through autounattend.xml into the post-installation

![](https://raw.githubusercontent.com/blusewill/oobe-bypass/master/image/in-action.png)

## How to Run This Script

Press Shift + F10 While in the OOBE and run the following command.

```
curl -L https://blusewill.top/oobe -o bypass.exe && bypass.exe
```

It will still prompt you with the language and keyboard setup.

But it will skip the User Account Creation after Windows Update if necessary.

## Is this a virus?

The Anti-Virus might have some false postive. Since it's compiled via pyinstaller without signing.

You can check the AV-test on VirusTotal

https://www.virustotal.com/gui/file/67ffa7ff042aac7115b3d348bd0f6ff230f40077909fc2853af61169a7406cce?nocache=1

## Support me!

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/blusewill)
