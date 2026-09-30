# Python in the Smoke 💨 🐍 💨

### An Introduction to Python with London-specific examples and a focus on the cultural sector
**Repo:** [`python-in-the-smoke`](https://github.com/MarkGotham/python-in-the-smoke)

**By:** Mark Gotham

**Licence:** MIT

**About:**

"Python in the Smoke" is a beginner's introduction to Python, with no prior experience required.
This is a coherent series of self-contained Jupyter notebooks for learning Python from scratch.

The series is organised in two parts:
"Foundations" followed by "Applications".
It is designed to work 
_both_ as the basis of a formal, classroom course,
_and_ for those who are self-taught and self-paced.

The examples and exercises focus on
cultural / digital humanities data,
and draw on London-specific topics
(museums, tube stations, boroughs, etc.).


## Notebooks

**Part I: Foundations**

|   | Notebook                                                                          | Topics                                             | Colab                                                                                                                                                                                                    |
|---|-----------------------------------------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| a | [`a_getting_started.ipynb`](./Part_I/a_getting_started.ipynb)                     | Jupyter basics, numbers, text, types, variables    | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MarkGotham/python-in-the-smoke//blob/main/Part_I/a_getting_started.ipynb)           |
| b | [`b_lists_dictionaries.ipynb`](./Part_I/b_lists_dictionaries.ipynb)               | Lists, indices, slices, dicts                      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MarkGotham/python-in-the-smoke//blob/main/Part_I/b_lists_dictionaries.ipynb)        |
| c | [`c_booleans_conditionals.ipynb`](./Part_I/c_booleans_conditionals.ipynb)         | Comparisons, `and`/`or`, `if`/`elif`/`else`        | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MarkGotham/python-in-the-smoke//blob/main/Part_I/c_booleans_conditionals.ipynb)     |
| d | [`d_loops.ipynb`](./Part_I/d_loops.ipynb)                                         | `for`, `range`, accumulator pattern, looping dicts | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MarkGotham/python-in-the-smoke//blob/main/Part_I/d_loops.ipynb)                     |
| e | [`e_functions.ipynb`](./Part_I/e_functions.ipynb)                                 | `def`, parameters, `return`                        | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MarkGotham/python-in-the-smoke//blob/main/Part_I/e_functions.ipynb)                 |
| f | [`f_packages_dataframes.ipynb`](./Part_I/f_packages_dataframes.ipynb)             | packages, dataframes                               | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MarkGotham/python-in-the-smoke//blob/main/Part_I/f_packages_dataframes.ipynb)       |
| g | [`g_file_folder_import_export.ipynb`](./Part_I/g_file_folder_import_export.ipynb) | import/export files                                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MarkGotham/python-in-the-smoke//blob/main/Part_I/g_file_folder_import_export.ipynb) |

**Part II: Applications**

[notebooks to follow]


---

## Getting Started

Getting Started is a kind of "lesson 0" before we begin.
Then again, it can be the hardest part of starting to programme.

Certainly the _easiest_ way in is to use Colab (links in the last column of the table above).
But the _easiest_ is not necessarily the _best_.
Sooner or later, you will want to get set up on your own device,
e.g., so you can work without an internet connection and on locally stored data.
If in doubt, try to set up locally right from the beginning.
Instructions follow.

Setting up locally should be relatively straightforward with the following steps:
- Download an IDE which supports
both setting up Python and using notebooks, e.g., [PyCharm](https://www.jetbrains.com/pycharm/).
- [Download this repo (click here)](https://github.com/MarkGotham/python-in-the-smoke//archive/refs/heads/main.zip)
- Unzip the download (in most cases, simply clicking on it is enough to unzip)
- Open the IDE
(it will be in Applications, and also findable with tricks like the "Spotlight search" on Mac)
- Within the IDE, open this project
(you need to know where you downloaded it*)
- Follow the IDE's instructions for setting up an environment.

This setup phase is the most liable to go wrong.
In case of difficulties, read on.

### * Where are my files!

You need to know where your files are stored.
- **macOS**: the main navigator is called "Finder",
- **Windows**: the equivalent is called "File Explorer".

Open the relevant tool ("Finder" or "File Explorer")
and have a look around
(click with the mouse, or use up/down/left/right arrows).

For now, focus on getting started.
We return to this topic in notebook g.

### Environment

The extremely minimal [`requirements`](requirements.txt)
file that's included in this repo
aims to make set up as smooth as possible.
(This includes Jupyter/ipykernel and nothing else;
adding packages is a topic in itself, covered in notebook f.) 

If you're using a modern IDE,
it should see this file on the first load
and walk you through setting up a
"virtual environment" ("venv") in which to work.
You may be prompted for a Python version;
if so, choose `3.10` or later (`3.11`, `3.12`, `3.13`).
Earlier versions might fail in confusing ways. 

### Power users:

This [`requirements`](requirements.txt) file
is tool-agnostic so it should work with
`venv` (as above)
or any existing `conda` environment,
or even on Colab.

The list of packages is extremely minimal in this starting
file to minimise the risk of set up issues.
Later notebooks add packages to the environment.
Power users might chose to add them here from the outset.

```bash
pip install -r requirements.txt
```

There's also a [`smoke_test`](Part_I/smoke_test.ipynb) notebook
to help debug installation issues.
Speaking of which ...

---

## What's in a Name?

The title
[`python-in-the-smoke`](https://github.com/MarkGotham/python-in-the-smoke)
puns on
"The Smoke" (which is an old-fashioned slang term for London)
and
"smoke test"
(a term for quick checks that confirm a system works at all before embarking on more detailed testing).

However scary you might find the prospect of learning to programme,
hopefully, it's _less_ scary than coming across a Python in the smoke!


---

## Note to Students

Each notebook has the same symbol key summarised as below:

| Symbol | Meaning                              |
|--------|--------------------------------------|
| 🟢     | A block of information               |
| 🟣     | Core exercise (do these)             |
| ⭐      | Optional information and/or exercise |
| ✅      | Solution (scroll down to check)      |
| 📝     | important information to note        | 
| ⚠️     | Common errors (deliberate failures)  |

And here's a fuller explanation:

- **Work through the notebooks in order**:
Each one builds on topics and knowledge from the previous.
- **Notebooks are self-contained**:
You don't need to keep old notebooks open or re-run them.
Later notebooks sometimes return to previously seen data for pedagogical reasons,
but that data is always redefined from scratch.
- **Run every cell**:
This includes the "information" cells.
They should all be helpful, relevant, and informative.
- **Do the 🟣 core exercises before looking at the ✅ solution**:
Learn by doing!
The solutions are there to check your work. 
There should be enough scrolling distance from exercise to solution
that you don't see the answers by accident.
- **There are ⭐ optional exercises**:
These provide additional, relevant information.
They do not get used in the *main* material of later notebooks
unless they are explicitly (re-)introduced later as core content.
- **Errors are part of the process!**:
Every notebook has a Common Errors section near the end labelled ⚠️.
These deliberately show you code that fails
and the real error messages that follow.
Getting an error is normal, to be expected, and worth preparing for.
This part of the process should help you learn how to
read error messages and fix the erroneous code.
- **Set up your environment first**:
See the section on [Environment](#environment), below.
If you open this repo in a modern IDE,
complete with the [`requirements`](requirements.txt) file that's included,
then it should help you with this.

---

## Note to Instructors

Here are some notes on the design.
- Consistent structure with key symbols (🟢/🟣/⭐/✅), suitable for most users including most forms of colour-blindness.
- Spiral curriculum. Where it makes sense to do so, "new" ideas are tied to its earlier forms
e.g., `and` to `&`, `sorted` to `sort_values`.
- Misconceptions and errors are central. Each notebook includes a "Common Errors" section.
- Data-literacy appears early. For instance, we ask how many rows _say_ x, not assuming that the raw read out is correct.
- Practical scaffolding. Empty cells are provided for each exercise step, and full solutions are provided.
- Some (limited) analogies support the most unfamiliar topics, e.g., install vs import by analogy to apps.
- Explanatory notes on how outputs differ by context, e.g., by package version and cloud environment.
- Licences and permissions included, e.g., with The Open Government Licence attribution.
