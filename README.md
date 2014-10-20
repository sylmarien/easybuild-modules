easybuild-modules
=================

Python script to install a defined set of EasyBuild modules

# Description

This python script automatically a list of software defined in a YAML file.

# Usage

List the software you want to install in a YAML file using the following syntax:
```
softwareSet1:
  - software1
  - software2
softwareSet2:
  - software3
  - software4
  - software5
  ```
  Using the software set names you want.
  You can have as many software sets and software in a software set as you want.
  
  Then execute the script:
`python install.py [software set] [EasyBuild version]`

- The [software set] argument is mandatory and to be chosen among the software sets you defined in your YAML file. (At Uni.lu: core and experimental)
- The [EasyBuild version] argument is optional, and the format is simply the three digit version number of the EasyBuild version you want to use. (e.g. 1.15.2 to use EasyBuild version 1.15.2).
If not specified, the script will use the version chosen by default by your module command.

Example: To install the "core" set of softwares using the 1.15.2 version of Easybuild, simply use:
`python install.py core 1.15.2`
