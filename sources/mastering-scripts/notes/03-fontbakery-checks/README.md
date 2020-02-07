# FontBakery checks

*(Start at 22:18, feb 2)*

Google Fonts uses FontBakery to check that fonts meet expectations for metadata and overall quality.

Some of these checks are very critical to follow, while others are a little less so. It's helpful to check in the FontBakery issues if you doubt something (and ask about it if there is not yet a filed issue about it).

## Things to change:

- [ ] google fonts asks for fonts to contain `0x00A0` (NO-BREAK SPACE)
- [ ] Check that OS/2 fsType is set to `0` ("Installable Embedding", no restrictions) – it is currently `4`
- [ ] set vendor ID. Maybe `ANDY`?
- [ ] eventually, copyright must be updated to `"This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL"`
- [ ] update version string to be standard, like: `Version 1.3; git-0d08353-release`
- [ ] add `EPAR` table (https://davelab6.github.io/epar/)
- [ ] set copyright: "Copyright 2019 The Familyname Project Authors (git url)"
- [ ] check named instances
- [ ] add named instances? we probably need at least one... google fonts expects folder of static instances (though this is a semi-soft requirement)
- [ ] check with ftxvalidator (maybe? I need to check the status of this tool)
- [ ] quick gftools fixes to make:
  - [ ] fix `gasp` table
  - [ ] fix `prep` table
  - [ ] add `dsig` table

*(Pause at 23:00, feb 2)*