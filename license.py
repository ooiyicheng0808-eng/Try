import streamlit as st
import datetime

# --- PART 1: THE OFFICIAL LICENSE TEXTS ---
# These are the templates that will be filled with the user's data.

mit_text = """MIT License

Copyright (c) {YEAR} {NAME}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

apache_text = """Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.
"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.
"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

2. Grant of Copyright License.
Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License.
Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work.

4. Redistribution.
You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:
(a) You must give any other recipients of the Work or Derivative Works a copy of this License; and
(b) You must cause any modified files to carry prominent notices stating that You changed the files; and
(c) You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work.

Copyright {YEAR} {NAME}
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0"""

gpl_text = """GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) {YEAR} {NAME}
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.

Preamble
The GNU General Public License is a free, copyleft license for software and other kinds of works.
The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users.

TERMS AND CONDITIONS

1. Source Code.
The "source code" for a work means the preferred form of the work for making modifications to it. "Object code" means any non-source form of a work.

2. Basic Permissions.
All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program.

3. Protecting Users' Legal Rights From Anti-Circumvention Law.
No covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty.

4. Conveying Verbatim Copies.
You may convey verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program.

5. Conveying Modified Source Versions.
You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:
a) The work must carry prominent notices stating that you modified it, and giving a relevant date.
b) The work must carry prominent notices stating that it is released under this License.
c) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy.

(Note: This is a condensed version of the GPLv3 for this educational system.)"""

# --- PART 2: THE APP LOGIC ---

st.set_page_config(page_title="License Generator", page_icon="🛡️")

st.title("🛡️ License Chooser System")
st.markdown("Automatically generate the correct legal documentation for your software project.")
st.divider()

# --- STEP 1: USER DETAILS ---
st.subheader("👤 Step 1: User Details")
col1, col2 = st.columns(2)

with col1:
    author_name = st.text_input("Enter Developer Name", placeholder="e.g. Leon Smith")

with col2:
    # Gets current year automatically
    project_year = st.number_input("Copyright Year", value=datetime.datetime.now().year, format="%d")

st.divider()

# --- STEP 2: REQUIREMENTS ---
st.subheader("📝 Step 2: Answer Requirements")

share_req = st.radio(
    "1. Must others share their modifications back to the public?", 
    ["Yes (Strict / Viral)", "No (Permissive)"]
)

st.write("") # Spacer

patent_req = st.radio(
    "2. Do you need explicit patent protection clauses?", 
    ["Yes (Corporate / Safe)", "No (Simple / Standard)"]
)

st.write("") # Spacer

# --- STEP 3: GENERATION LOGIC ---
if st.button("Generate License File", type="primary"):
    
    # Validation Check
    if not author_name:
        st.error("⚠️ Error: Please enter a Developer Name in Step 1.")
    else:
        license_body = ""
        license_name = ""
        
        # Decision Tree
        if "Yes (Strict / Viral)" in share_req:
            license_name = "GNU GPL v3"
            license_body = gpl_text.format(YEAR=project_year, NAME=author_name)
            st.warning("Recommendation: *GNU GPL v3*\n\nReason: You want to force 'Share Alike' behavior (Copyleft).")
            
        elif "Yes (Corporate / Safe)" in patent_req:
            license_name = "Apache 2.0"
            license_body = apache_text.format(YEAR=project_year, NAME=author_name)
            st.info("Recommendation: *Apache 2.0*\n\nReason: You need patent protection but want to allow closed-source use.")
            
        else:
            license_name = "MIT License"
            license_body = mit_text.format(YEAR=project_year, NAME=author_name)
            st.success("Recommendation: *MIT License*\n\nReason: You want the simplest, most permissive option.")

        # Display Result
        st.divider()
        st.subheader(f"📄 Result: {license_name}")
        st.text_area("File Preview (Copy this text):", value=license_body, height=350)
        
        # Download Button
        st.download_button(
            label="⬇️ Download LICENSE.txt",
            data=license_body,
            file_name="LICENSE.txt",
            mime="text/plain"
        )