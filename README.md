# personal-site

Simple personal website made with easy configureable content, see it live [abisatya.info](https://abisatya.info)

## Acknowledgements
Build with :
 - Flask
 - Waitress
 - Tailwindcss
 - HTMX


## Installation

Install this project using [Rye](https://rye.astral.sh/guide/installation/) python package manager if you have, then clone and sync the project, otherwise install the dependency required

Clone the project

```bash
git clone https://github.com/abisatyaw/personal-website.git
```

Go to the project directory

```bash
cd personal-website
```

Install dependencies :

using Rye
```bash
rye sync
```

## Getting Started
Content of personal information could be adjusted from content.yaml, web layout are easily configurable directly on HTLM

Flask app will parse content.yaml and used templating engine to render it on HTML 

Run Tailwindcss to build change in css stye using Rye
```bash
rye run tw
```
Run site on dev mode
```bash
rye run dev
```
(Optionally) run on server, make sure nginx and port are configured correctly
```bash
rye run server
```
