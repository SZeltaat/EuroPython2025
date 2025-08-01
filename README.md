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



## Have fun and learn

[Take the Python Quiz](https://mathspp.com/blog/python-quiz-europython-2025-edition)