# EuroPython2025
My narrative of EuroPython 2025 in Prague

## General
- Link to the website: [EuroPython 2025](https://ep2025.europython.eu/)


## Workshops
### [Workshop 1: Rambo Python](https://ep2025.europython.eu/session/rambo-python)


Course material: https://github.com/Lenormju/python-royal/tree/english_translation

Mostly the tech stack we use at WSP: uv, ruff, mypy, pytest, pre-commit, ...

Got to play with streamlit a bit, which was fun.

Interesting take aways:

- [pydoit](https://pydoit.org/) for task management and cli automation
- [uv custom ca certificates](https://docs.astral.sh/uv/concepts/authentication/#custom-ca-certificates) for possible certificate problems

### [Workshop 2: GIL-free Python and the GPU](https://ep2025.europython.eu/session/gil-free-python-and-the-gpu-hands-on-experience)

Course material: https://learn.nvidia.com/dli-event
(Code: EUROPYTHON_GILFRPY_JUL25)

See the jupyter notebooks:  [no_gil_gpu.ipynb](Assets/ws2/no_gil_gpu.ipynb)

See the use of NVidia's nvic in [nvic.py](Assets/ws2/nvic.py)

Many tips and tricks on ThreadPoolExecutor and ProcessPoolExecutor both with and without the GIL. Also how to use the GPU with CUDA and Python.

### [Workshop 3: The Mighty Dot - Customize Attribute Access with Descriptors](https://ep2025.europython.eu/session/the-mighty-dot-customize-attribute-access-with-descriptors)

Course material: [mighty_dot.zip](Assets/ws3/mighty_dot.zip)

Very very interesting and well presented workshop by Mike Müller.

Take aways:

- A deep dive into properties and descriptors, also alternative ways to implement them.
- How and when to use them? What are the pitfalls?
- There is a WeakKeyDictionary in the `weakref` module to store weak references to objects, which can be useful for caching. Definitely something to look into.

### [Workshop 4: Speaking at EuroPython (or your favorite conference)](https://ep2025.europython.eu/session/speaking-at-europython-or-your-favorite-conference-yes-you-can)

Course material: [Presentation](Assets/ws4/SpeakingAtEuroPythonYesYouCan.pdf)

An interesting workshop on how to prepare a talk for EuroPython or any other conference, lots of tips and tricks.

Also prepared and presented a lightning talk for the first time, which was a fun experience.


## Talks

Here are some of the interesting talks I attended:

### Keynote: [You don’t have to be a compiler engineer to work on Python](https://ep2025.europython.eu/session/you-dont-have-to-be-a-compiler-engineer-to-work-on-python)

Resources: 
- [Slides](Assets/kn/Savannah-Bailey.pdf)
- [The home of Python’s code. Follow issues, submit 
PRs, or just watch the repo to learn.](http://github.com/python/cpython)
- [ Docs proposing/explaining major Python changes 
— how and why things work the way they do.](http://peps.python.org)
- [Where high-level discussion happens on features, 
governance, packaging, and ideas.](http://discuss.python.org)
- [ Everything you need to start contributing: setup, 
tools, triage process, testing, and more.](http://devguide.python.org)


Take aways:
- Once self-taught developer, now a core python developer.
- Triaging issues is a great way to contribute:
    - Reproducing issues
    - Finding minimum reproducers 
    - Helping categorize issues
    - Suggesting potential ﬁxes
- Updating docs and improving test coverage is also a great way to contribute.
- Do it scared ✨


### Talk: [Teamwork makes the dream work](https://ep2025.europython.eu/session/teamwork-makes-the-dream-work)

Resources: 
- [Slides](https://preludetech.github.io/pres-teamwork-europy-2025/)
- [The culture map book](https://www.bol.com/nl/nl/f/culture-map/9300000110083228/): Decoding How People Think, Lead, and Get Things Done Across Cultures.
- [Nonviolent communication](https://www.amazon.nl/-/en/Marshall-B-Rosenberg-PhD/dp/189200528X): Life-Changing Tools for Healthy Relationships
- [On measuring software development productivity](https://www.youtube.com/watch?v=yuUBZ1pByzM)
- [On feedback cycles](https://www.youtube.com/watch?v=Oip7ufMm2Vk)

Thoughts and take aways:
- What does good teamwork mean to you?
- Softwate development is a team sport.
    - Skilfully pass the ball and set the next person up for success.
- Put principles above processes.
- Ball passing in software development:
    - Pull requests: make a PR skilfully!
    - Code reviews: give feedback skilfully!
    - Apply feedback skilfully!
    - Ask for help skilfully!
    - Receive help skilfully!
    - Share status regularly!
    - To err is human!
    - To grow is human!
- Good teamwork is good business.
- [Google’s Project Aristotle](https://psychsafety.com/googles-project-aristotle/) found that psychological safety is the most important factor for high-performing teams. Definitely read the article!


### Talk: [How to deal with toxic people](https://ep2025.europython.eu/session/how-to-deal-with-toxic-people)

Resources:
- [Slides](Assets/talks/toxic_people.pdf)
- [Burn out by Emily & Amelia Nagoski](https://www.amazon.nl/Burnout-Secret-Unlocking-Stress-Cycle/dp/1984818325)
- [Why zebras don't get ulcers by Robert Sapolsky](https://www.amazon.nl/Zebras-Dont-Ulcers-Revised-Updated/dp/0805073698/)
- [The social contract of open source by Brett Cannon](https://snarky.ca/the-social-contract-of-open-source/)

Take aways:
- Understand the types of toxic feedback:
    - Entitlement: "Why is my problem not solved?"
    - Frustration: "Thanks for nothing!"
    - Attack: "🤬 U"
- Coping strategy:
    - Do not engage hot-headedly.
    - Go through your stress respoonse cycle:
    - Cool down
- Open source = No one owes you anything.
- Boundaries:
    - You deserve respect and decency.
    - Have a Code of Conduct and enforce it.
    - Don't accept abuse.


### Talk: [Design Pressure: The Invisible Hand That Shapes Your Code](https://ep2025.europython.eu/session/design-pressure-the-invisible-hand-that-shapes-your-code)

Resources:
- [Slides](https://speakerdeck.com/hynek/design-pressure)
- [Blog post by the speaker](https://www.youtube.com/watch?v=IhNSINolcSM&t=2s)
- [PyCon US 2025 version of the talk](https://www.youtube.com/watch?v=IhNSINolcSM)
- [The rising sea (by Mathew Drury) / The harbor coding problem](https://www.youtube.com/watch?v=AkBWb1fK6R8)

Take aways:
- Two pieces of code are coupled if they can only be understood by looking at both.
- Testable code is better code.
- The shape of your code should NOT be determined by the shape of your data.
- In software projects, you often have:
    - Database schemas (e.g. SQL tables)
    - API schemas (e.g. what your API sends/receives)
    - Business logic types (e.g. what your app actually works with in memory)
    - ORM models (e.g. how your code talks to the database)
    - These may look similar, but they serve different purposes and have different flexibility needs.
- If you force everything to use the same type (a “franken-type”), the rigid parts (e.g. the database) will limit flexibility everywhere.
    - Some parts (like the database) are harder to change.
    - Others (like your internal app logic) should be easy to change.
- It's better to define separate types in each layer.
    - Then, explicitly map between them (e.g. convert a DB object to an API response).
    - Yes, it’s a bit more work, but it keeps each part clean, flexible, and easy to maintain.
- Start with the `Domain model` based on your business logic:
    - This is the core logic of your app, independent of any external systems.
    - It should be clean, flexible, and easy to change.
- Complexity is not about how many keys I have to press – it’s about how difficult it is to reason about the consequences of what I’m doing.


### Lightnig talk: How to say "No" more easily:
- Rule#1: Don't say "Yes" unless it's been 24 hours since the request.
- Rule#2: Estimate the time, energy and the cost. Then multiply it by 4. Alternatively: make an optimistic estimate, make a pessimistic estimate, then sum them up!
- Rule#3: Future you is gonna at least as busy as present you.
- Rule#4: Tell your loved one(s) that you are going to say "No" to them by saying "Yes" to the oppurtunity.
- Rule#5: The "honor to be asked" is a trap. Don't fall for it.



### Session: [AI discussion panel](https://ep2025.europython.eu/session/ai-discussion-panel)

Key take aways:
- AI is a tool, not a replacement for human creativity.
- No AI expert can predict the future. Stop forecasting and definitely stop panicking.


## Fun Insights & Highlights

[Take the Python Quiz](https://mathspp.com/blog/python-quiz-europython-2025-edition)

The Pac-Man rule

![The Pac-Man Rule](Assets/Other%20resources/the-pac-man-rule.png)

### Intereseting tools:
- [Mermaid](https://mermaid.js.org/): A powerful tool to create diagrams and visualizations using text.
- [Obsidian](https://obsidian.md/): A powerful note-taking app that uses markdown files.