# Requirements Document

## Project Title

MSR Knowledge Base

## Project Overview

The MSR Knowledge Base is a simple web-based reference guide for Mining Software Repositories (MSR) researchers and new PhD students.

The system organizes useful MSR information into four main categories:

1. Data Sources
2. Collection Methods
3. Analysis Methods
4. Publication Venues

The website should be simple, professional, readable, and easy to navigate.

---

## User Stories

### User Story 1 - Navigation

As a new PhD student, I want to switch between the main MSR knowledge categories so that I can quickly find the type of information I need.

#### Acceptance Criteria

- The webpage provides navigation for four categories.
- The categories are Data Sources, Collection Methods, Analysis Methods, and Publication Venues.
- Selecting a category displays the appropriate content.

---

### User Story 2 - Data Sources

As a PhD student, I want to view common MSR data sources so that I can choose appropriate data for my research.

#### Acceptance Criteria

- Each data source has a name.
- The type of data provided by the source is shown.
- A short description of the source is provided.
- Examples include GitHub, Stack Overflow, JIRA, app stores, CI systems, mailing lists, and package registries.

---

### User Story 3 - Collection Methods

As a researcher, I want to compare different data collection methods so that I can select an appropriate method for collecting research data.

#### Acceptance Criteria

- Each collection method has a name.
- The purpose of each method is explained.
- Advantages and disadvantages are provided.
- Methods include REST APIs, GraphQL, web scraping, database dumps, and manual downloads.

---

### User Story 4 - Analysis Methods

As a researcher, I want to view common analysis methods so that I can select an appropriate method for analyzing collected data.

#### Acceptance Criteria

- Each analysis method has a name.
- The type of analysis is identified.
- Common uses of the method are provided.
- Methods include statistical analysis, regression analysis, thematic analysis, grounded theory, machine learning, time-series analysis, network analysis, and visualization.

---

### User Story 5 - Publication Venues

As a researcher, I want to compare software engineering publication venues so that I can choose an appropriate place to publish my research.

#### Acceptance Criteria

- Each venue has a name and abbreviation.
- The type of venue is identified.
- The main research focus is provided.
- Its relevance to MSR research is indicated.
- Both conferences and journals are included.

---

### User Story 6 - Readable Interface

As a researcher, I want a clean and readable interface so that I can find information without unnecessary distractions.

#### Acceptance Criteria

- The webpage uses simple and consistent styling.
- Information is organized clearly.
- Tables are easy to read.
- Navigation is easy to understand.
- The webpage has a professional appearance.

---

## Functional Requirements

The system shall:

- Provide navigation between the four main MSR categories.
- Display information about common MSR data sources.
- Display different data collection methods.
- Display common analysis methods.
- Display relevant conferences and journals.
- Allow the user to switch between categories without reloading the page.

## Non-Functional Requirements

The system should:

- Be simple to use.
- Have a clean and professional layout.
- Organize information consistently.
- Be readable on commonly used screen sizes.
- Use standard HTML, CSS, and JavaScript.
