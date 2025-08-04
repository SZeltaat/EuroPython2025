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

### Keynote van Savannah Bailey: [You don’t have to be a compiler engineer to work on Python](https://ep2025.europython.eu/session/you-dont-have-to-be-a-compiler-engineer-to-work-on-python)

Resources: 
- [slides](Assets/kn/Savannah-Bailey.pdf)
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


### [Teamwork makes the dream work](https://ep2025.europython.eu/session/teamwork-makes-the-dream-work)

Resources: 
- [slides](https://preludetech.github.io/pres-teamwork-europy-2025/)
- [The culture map book](https://www.bol.com/nl/nl/f/culture-map/9300000110083228/): Decoding How People Think, Lead, and Get Things Done Across Cultures.
- [On measuring software development productivity](https://www.youtube.com/watch?v=yuUBZ1pByzM)
- [On feedback cycles](https://www.youtube.com/watch?v=Oip7ufMm2Vk)

Thoughts:
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


## Fun Insights & Highlights

[Take the Python Quiz](https://mathspp.com/blog/python-quiz-europython-2025-edition)

Get familiar with the Pac-Man rule

![The Pac-Man Rule](Assets/Other%20resources/the-pac-man-rule.png)

