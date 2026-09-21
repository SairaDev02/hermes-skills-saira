# Requirements Elicitation Techniques

Reference guide for selecting and executing elicitation techniques during the
requirements gathering phase.

## Technique Selection Matrix

| Technique | Best For | Stakeholders | Time | Output Richness |
|-----------|----------|-------------|------|-----------------|
| Interviews | Deep individual perspectives | 1-2 | Medium-High | High |
| Surveys/Questionnaires | Broad quantitative data | Many | Low | Medium |
| Focus Groups | Group dynamics, consensus | 5-8 | Medium | High |
| Observation | tacit/unspoken workflows | N/A | High | High |
| Prototyping | Validating UI/UX expectations | 2-5 | High | Very High |
| Brainstorming | Generating new ideas | 4-10 | Low-Medium | Medium |
| Delphi Technique | Expert consensus without bias | 5-20 (remote) | High | High |
| Task Analysis | Step-by-step workflow detail | 1-3 SMEs | Medium | High |
| Document Analysis | Existing systems, regulations | N/A | Low-Medium | Medium |
| JAD/JRP Workshops | Rapid cross-functional alignment | 8-20 | Medium | Very High |

## When to Use Each Technique

### Interviews

**Use when:**
- You need deep understanding of a single stakeholder's perspective
- The stakeholder is a key decision-maker or domain expert
- Sensitive or political topics require one-on-one trust

**How to execute:**
1. Identify the interviewee and their role in the system
2. Prepare open-ended questions (avoid yes/no questions for exploration)
3. Record (with permission) or take detailed notes
4. Start with broad questions, then narrow to specifics
5. Ask for concrete examples and scenarios
6. Confirm your understanding by paraphrasing back to the interviewee
7. Transcribe and organize notes within 24 hours

**Output:** Individual stakeholder needs, pain points, expectations, and domain knowledge.

### Surveys/Questionnaires

**Use when:**
- You need input from a large number of geographically distributed stakeholders
- You need quantitative data to prioritize features
- Time and budget are limited

**How to execute:**
1. Define the survey goal and target audience
2. Write clear, unbiased questions (pilot-test with 2-3 people first)
3. Mix closed-ended (rating scales, rankings) and open-ended questions
4. Keep it short (5-15 minutes to complete)
5. Distribute and set a clear deadline
6. Analyze results — look for patterns and outliers

**Output:** Prioritized feature lists, satisfaction ratings, statistical preferences.

### Focus Groups

**Use when:**
- You need group interaction to surface diverse perspectives
- Stakeholders may not articulate needs individually but will in a group
- You need to observe consensus-building or conflict

**How to execute:**
1. Select 5-8 stakeholders representing different roles/perspectives
2. Appoint a skilled facilitator (not the requirements analyst)
3. Prepare a discussion guide (not a rigid script)
4. Record the session (audio/video with permission)
5. Note body language and group dynamics
6. Transcribe and analyze for themes, conflicts, and consensus

**Output:** Shared understanding, identified conflicts, prioritized needs.

### Observation (Ethnographic Study)

**Use when:**
- Stakeholders cannot articulate their workflow clearly
- Tacit knowledge drives the work process
- You need to understand the *actual* workflow vs. the *documented* workflow

**How to execute:**
1. Identify the work environment and tasks to observe
2. Obtain permission and explain the purpose
3. Observe without interfering (shadow the user)
4. Take notes on: actions, tools used, interruptions, workarounds, pain points
5. Ask clarifying questions *after* observation
6. Document the actual workflow step-by-step

**Output:** Current-state process model, unarticulated needs, pain points, workarounds.

### Prototyping

**Use when:**
- Stakeholders need to see/interact with something to articulate their needs
- Requirements are about UI/UX
- There is uncertainty about what the user actually wants

**How to execute:**
1. Determine fidelity (low-fidelity: paper/wireframes; high-fidelity: interactive mockup)
2. Build the prototype focused on the most uncertain requirements
3. Walk through scenarios with stakeholders
4. Capture feedback on what works and what doesn't
5. Iterate — refine and re-validate
6. Document the validated requirements (not the prototype itself — prototypes are
   disposable)

**Output:** Validated UI requirements, clarified interactions, eliminated misunderstandings.

### Brainstorming

**Use when:**
- You need to generate a broad set of ideas quickly
- The problem space is not well understood
- Creative solutions are needed

**How to execute:**
1. Define the problem clearly
2. Gather 4-10 diverse participants
3. Set a time limit (30-60 minutes)
4. Generate ideas without evaluation (no criticism during generation)
5. After generation, group and evaluate ideas
6. Document all ideas, even rejected ones (they may inform later work)

**Output:** Candidate requirements, creative solutions, out-of-scope ideas for backlog.

### Delphi Technique

**Use when:**
- Expert consensus is needed but experts cannot meet in person
- You need to avoid groupthink and dominant-personality bias
- Estimates or predictions are needed from multiple experts

**How to execute:**
1. Identify 5-20 experts
2. Send a questionnaire (round 1)
3. Summarize responses anonymously
4. Share summary with all experts; ask for revised responses (round 2)
5. Repeat 2-3 rounds until consensus converges
6. Document the final consensus and any persistent disagreements

**Output:** Expert consensus on requirements, estimates, or priorities.

### Task Analysis

**Use when:**
- You need detailed step-by-step understanding of user tasks
- The system automates or supports an existing manual process
- You need to define functional requirements from user tasks

**How to execute:**
1. Identify the tasks to analyze
2. Break each task into subtasks (hierarchical task analysis)
3. For each subtask, document: trigger, inputs, actions, outputs, exceptions
4. Identify decision points and alternative paths
5. Map tasks to proposed system functions

**Output:** Task decomposition, functional requirement candidates, exception handling needs.

### Document Analysis

**Use when:**
- Existing documentation (business rules, regulations, manuals, existing system specs)
  contains requirements
- You need to understand the regulatory or domain context
- The system replaces or integrates with an existing system

**How to execute:**
1. Collect relevant documents (business manuals, regulations, existing specs, standards)
2. Extract requirements, constraints, and rules
3. Note gaps and contradictions
4. Validate extracted requirements with stakeholders

**Output:** Extracted requirements, regulatory constraints, domain rules.

### JAD/JRP (Joint Application Development / Joint Requirements Planning) Workshops

**Use when:**
- You need rapid alignment across many stakeholders
- Cross-functional dependencies are complex
- A decision must be made quickly

**How to execute:**
1. Identify 8-20 key stakeholders across all affected functions
2. Prepare a detailed agenda and distribute pre-reading materials
3. Appoint a neutral facilitator and a scribe
4. Work through the agenda: present context → discuss → document decisions
5. Resolve conflicts in the room when possible
6. Produce a signed-off requirements document at the end

**Output:** Prioritized, agreed-upon requirements with stakeholder sign-off.

## Common Elicitation Pitfalls

1. **Asking stakeholders what they want** — stakeholders often describe solutions, not
   needs. Probe for the underlying problem: "What would that enable you to do?"
2. **Ignoring tacit knowledge** — users perform tasks automatically without being able to
   explain them. Use observation to capture these.
3. **Sampling only one stakeholder type** — different roles have different, sometimes
   conflicting, needs. Cover all stakeholder types.
4. **Treating elicitation as a one-time activity** — elicitation continues throughout the
   project. New requirements emerge during specification and design.
5. **Not documenting assumptions** — every assumption made during elicitation should be
   explicitly recorded and validated.
