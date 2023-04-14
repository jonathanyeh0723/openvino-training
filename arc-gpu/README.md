# Title TBD

## Configuration Verification

### xxx

Step 1 - Commands:
```
uname -r
```

Step 1 - Outputs:

```
5.14.0-1047-oem
```

Step 2 - Commands:
```
sudo apt install pip
python3 -m pip install --upgrade pip
sudo apt install python3.8-venv
python3 -m venv openvino_env
source openvino_env/bin/activate
pip install openvino-dev==2022.3.0
pip freeze | grep openvino
```

Step 2 - Logs:
```
openvino==2022.3.0
openvino-dev==2022.3.0
openvino-telemetry==2022.3.0
```

Step 3 - Commands:
```
ls /dev/dri
```


Step 3 - Logs:
```
by-path  card0  card1  renderD128  renderD129
```

Step 4 - Commands:
```
vainfo
```


Step 4 - Logs:
```
libva info: VA-API version 1.15.0
libva info: Trying to open /usr/lib/x86_64-linux-gnu/dri/iHD_drv_video.so
libva info: Found init function __vaDriverInit_1_15
libva info: va_openDriver() returns 0
vainfo: VA-API version: 1.15 (libva 2.15.0)
vainfo: Driver version: Intel iHD driver for Intel(R) Gen Graphics - 22.5.0 (7e9cc59)
vainfo: Supported profile and entrypoints
      VAProfileNone                   :	VAEntrypointVideoProc
      VAProfileNone                   :	VAEntrypointStats
      VAProfileMPEG2Simple            :	VAEntrypointVLD
      VAProfileMPEG2Main              :	VAEntrypointVLD
      VAProfileH264Main               :	VAEntrypointVLD
      VAProfileH264Main               :	VAEntrypointEncSliceLP
      VAProfileH264High               :	VAEntrypointVLD
      VAProfileH264High               :	VAEntrypointEncSliceLP
      VAProfileJPEGBaseline           :	VAEntrypointVLD
      VAProfileJPEGBaseline           :	VAEntrypointEncPicture
      VAProfileH264ConstrainedBaseline:	VAEntrypointVLD
      VAProfileH264ConstrainedBaseline:	VAEntrypointEncSliceLP
      VAProfileHEVCMain               :	VAEntrypointVLD
      VAProfileHEVCMain               :	VAEntrypointEncSliceLP
      VAProfileHEVCMain10             :	VAEntrypointVLD
      VAProfileHEVCMain10             :	VAEntrypointEncSliceLP
      VAProfileVP9Profile0            :	VAEntrypointVLD
      VAProfileVP9Profile0            :	VAEntrypointEncSliceLP
      VAProfileVP9Profile1            :	VAEntrypointVLD
      VAProfileVP9Profile1            :	VAEntrypointEncSliceLP
      VAProfileVP9Profile2            :	VAEntrypointVLD
      VAProfileVP9Profile2            :	VAEntrypointEncSliceLP
      VAProfileVP9Profile3            :	VAEntrypointVLD
      VAProfileVP9Profile3            :	VAEntrypointEncSliceLP
      VAProfileHEVCMain12             :	VAEntrypointVLD
      VAProfileHEVCMain422_10         :	VAEntrypointVLD
      VAProfileHEVCMain422_12         :	VAEntrypointVLD
      VAProfileHEVCMain444            :	VAEntrypointVLD
      VAProfileHEVCMain444            :	VAEntrypointEncSliceLP
      VAProfileHEVCMain444_10         :	VAEntrypointVLD
      VAProfileHEVCMain444_10         :	VAEntrypointEncSliceLP
      VAProfileHEVCMain444_12         :	VAEntrypointVLD
      VAProfileHEVCSccMain            :	VAEntrypointVLD
      VAProfileHEVCSccMain            :	VAEntrypointEncSliceLP
      VAProfileHEVCSccMain10          :	VAEntrypointVLD
      VAProfileHEVCSccMain10          :	VAEntrypointEncSliceLP
      VAProfileHEVCSccMain444         :	VAEntrypointVLD
      VAProfileHEVCSccMain444         :	VAEntrypointEncSliceLP
      VAProfileAV1Profile0            :	VAEntrypointVLD
      VAProfileAV1Profile0            :	VAEntrypointEncSliceLP
      VAProfileHEVCSccMain444_10      :	VAEntrypointVLD
      VAProfileHEVCSccMain444_10      :	VAEntrypointEncSliceLP
```

Step 5 - Commands:

```
hwinfo --display
```

Step 5 - Logs:

```
06: PCI 300.0: 0300 VGA compatible controller (VGA)             
  [Created at pci.386]
  Unique ID: svHJ.77hoq_qsqUD
  Parent ID: GA8e.mr2N3fBJq5F
  SysFS ID: /devices/pci0000:00/0000:00:01.0/0000:01:00.0/0000:02:01.0/0000:03:00.0
  SysFS BusID: 0000:03:00.0
  Hardware Class: graphics card
  Model: "Intel VGA compatible controller"
  Vendor: pci 0x8086 "Intel Corporation"
  Device: pci 0x5690 
  SubVendor: pci 0x8086 "Intel Corporation"
  SubDevice: pci 0x3026 
  Revision: 0x08
  Driver: "i915"
  Driver Modules: "i915"
  Memory Range: 0x6b000000-0x6bffffff (rw,non-prefetchable)
  Memory Range: 0x6000000000-0x63ffffffff (ro,non-prefetchable)
  Memory Range: 0x6c000000-0x6c1fffff (ro,non-prefetchable,disabled)
  IRQ: 191 (5628 events)
  Module Alias: "pci:v00008086d00005690sv00008086sd00003026bc03sc00i00"
  Driver Info #0:
    Driver Status: i915 is active
    Driver Activation Cmd: "modprobe i915"
  Config Status: cfg=new, avail=yes, need=no, active=unknown
  Attached to: #29 (PCI bridge)

30: PCI 02.0: 0300 VGA compatible controller (VGA)
  [Created at pci.386]
  Unique ID: _Znp.HMLUX1zIkGC
  SysFS ID: /devices/pci0000:00/0000:00:02.0
  SysFS BusID: 0000:00:02.0
  Hardware Class: graphics card
  Device Name: "Onboard - Video"
  Model: "Intel VGA compatible controller"
  Vendor: pci 0x8086 "Intel Corporation"
  Device: pci 0x46a6 
  SubVendor: pci 0x8086 "Intel Corporation"
  SubDevice: pci 0x3026 
  Revision: 0x0c
  Driver: "i915"
  Driver Modules: "i915"
  Memory Range: 0x644c000000-0x644cffffff (rw,non-prefetchable)
  Memory Range: 0x4000000000-0x400fffffff (ro,non-prefetchable)
  I/O Ports: 0x4000-0x403f (rw)
  Memory Range: 0x000c0000-0x000dffff (rw,non-prefetchable,disabled)
  IRQ: 190 (47 events)
  Module Alias: "pci:v00008086d000046A6sv00008086sd00003026bc03sc00i00"
  Driver Info #0:
    Driver Status: i915 is active
    Driver Activation Cmd: "modprobe i915"
  Config Status: cfg=new, avail=yes, need=no, active=unknown

Primary display adapter: #6
```

To retrieve the device name with correspondent settings:

```
(openvino_env) sertek@sertek-NUC12SNKi72:~$ python3
Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from openvino.runtime import Core
>>> core = Core()
>>> devices = core.available_devices
>>> for device in devices:
...     full_device_name = core.get_property(device, 'FULL_DEVICE_NAME')
...     print(device, full_device_name)
... 
CPU 12th Gen Intel(R) Core(TM) i7-12700H
GPU.0 Intel(R) Graphics [0x46a6] (iGPU)
GPU.1 Intel(R) Graphics [0x5690] (dGPU)
```
