# Software Requirements Specification

|   |   |
| ----------- | ----------- |
| Version | 1.0 |
| Prepared By | Nikki Wood |
| Document Status | DRAFT |
| Date Updated | 02/11/2021 | 

---

## Table of Contents
| **1.** | [**Introduction**](#introduction) |
| ------ | ---------------- |
| 1.1 | Purpose |
| 1.2 | Document Conventions |
| 1.3 | Intended Audience and Reading Suggestions |
| 1.4 | Product Scope | 
| 1.5 | References |
---
| **2.** | [**Overall Description**](#overall-description) |
| ------ | ---------------- |
| 2.1 | Product Perspective |
| 2.2 | Product Functions |
| 2.3 | User Classes and Characteristics |
| 2.4 | Operating Environment | 
| 2.5 | Design and Implementation Constraints |
| 2.6 | User Documentation |
| 2.7 | Assumptions and Dependencies |
---
| **3.** | **External Interface Requirements** |
| ------ | ---------------- |
| 3.1 | User Interfaces |
| 3.2 | Software Interfaces |
| 3.3 | Communications Interfaces |
---
| **4.** | **System Features** |
| ------ | ---------------- |
| 4.1 | System Feature 1 |
| 4.2 | System Feature 2 |
---
| **5.** | **Other Nonfunctional Requirements** |
| ------ | ---------------- |
| 5.1 | Performance Requirements |
| 5.2 | Security Requirements |
| 5.3 | Software Quality Attributes |
| 5.4 | Business Rules | 
---
| **6.** | **Other Requirements** |
| ------ | ---------------- |
### Appendix A: Glossary
### Appendix B: Analysis Models
### C: To Be Determined List

---
## Revision History
| Name | Date | Reason For Changes | Version |
| ---- | ---- | ------------------ | ------- |
| Initial Version (Draft) | 01/11/2021 | - | 0.1 |

## Introduction

### Purpose
This document is a representation of the Chromesthesia Response Replicator AI application. It describes how the user and software communicate to allow the user to view the sound-to-color synesthetic response of one individual. 

### Document Conventions
Within this document:
- "Sample" or "song sample" will refer to an inputted song.
- "Category" (relating to "response") will refer to one of the three categories our subject is using to describe her synesthetic response. Categories include: Luminosity, Color, and Texture.
- "response" will refer to the combination of 'correct answers' for each category. For example, a response to a song might be "smoky black", "light soft purple", etc.
- "the AI" will refer to the part of this project that will identify patterns and assign a response to an inputted song sample. 
- "the Application" will refer to the part of this project that will take an inputted song, compile a response (from the AI), and output that response to the user.
- "Software" will refer to the project itself, including both the AI and the application.
- "synesthete" will refer to any individual with synesthesia
- "synesthetic response" will refer to the visuals seen by any synesthete with sound-to-color synesthesia (chromesthesia).
- "Subject", "Client", and "our synesthete" will refer to Meredith Turner, the synesthete that will be providing our training set. She will also be assisting with this project.

### Intended Audience and Reading Suggestions.
This document is intended to be read by the Client, Nikki Wood, and Dr. Gary Cantrell. The Client should look for how this documentation represents how she intends the Software to function. Nikki Wood will use this document as she plans, builds, and tests the Software in order to fulfill the requirements and functions specified. Dr. Gary Cantrell will read and critique this document for errors and to give feedback.

### Product Scope
This Software will give those who do not have chromesthesia a taste of what it might be like to have these sound-to-color conversions. It will also amplify our Subject's understanding of the correlation between her visual responses and the different genres, tempos, or timbre (sound/tone quality) in music.

---
## Overall Description
### Product Perspective
The Software will allow users to input a song into the Application. This Sample will be sent to the AI to create a response prediction. The Application will then deliver the response back to the user, so that they might see the visual interpretation of their song through the eyes of a synesthete. See Figure 2.1
<br/>
![picture 2](../../images/6da32d20f6a561597d4c7ffaed7321fba0a2f2e8a034f70b3a4cb805a3df79e1.png)  

### Product Functions
The Software will function as shown in Figure 2.2

### User Classes and Characteristics
There exists only one class of User for this Software. This user class will be able to access all functions of the Software. 

### Operating Environment

TODO

### Design and Implementation Constraints
TODO

### User Documentation 
TODO

### Assumptions and Dependencies
TODO

---
## External Interface Requirements
### User Interfaces
TODO

### Software Interfaces
This Software will communicate with the AI as a library of files (link to YouTube?) TODO

### Communications Interfaces
This Software will be run on ________ and will communicate via HTTP(???? TODO)

---

## System Features

### Database Component Attributes
#### Description/ Priority




---
## Main Requirements
| # | Requirement Description | Success Metric | Notes |
| --- | --- | --- | --- |
| 1 | Reflect on the goal of finding the expected outcome for each category with 50% accuracy | 1 - 2 paragraph reflection: Was the AI's prediction correct at least 50% of the time? What parameters seemed to affect the success rate? | - |
| 2 | Application compiles each expected outcome and returns the 'correct answer' as one response (command line) | Given a song, does the program output a written description of the AI's prediction (e.g. "light, sparkly blue") | - |
| 3 | Minimum of 12 hours of research (Neural nets, similar AI projects, python application with AI, etc.) | On the project's Time Report, was there a minimum of 12 hours in the **Research** section? | - |
| 4 | Find at least 1 sample recorded for each combination | On the Training Samples excel sheet, was there at least 1 recorded sample for every combination? (154 possible) If not, was there an explanation from the subject as to why? | - |
| 5 | Reflect on the expansion of my knowledge and comprehension of Python | Minimum of 3 paragraphs: How did your understanding of Python expand through the course of this project? What did you learn about using Python with AI? | - |
| 6 | Keep detailed documentation throughout the process | Is there a Documentation folder easily found from GitHub? Does it include *at least* the following: Timeline, Contract, Process Model Justification, SRS, PRD,  | - | 
## User interaction and design
> After the team fleshes out the solution for each user story, link design explorations and wireframes to the page. 

|   |   |
| ----------- | ----------- |