<p align="center">
  <img src="https://images.vexels.com/content/127711/preview/flat-vintage-car-icon-8bd3aa.png" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">CarEXPERT</h1>
</p>
<p align="center">
    <em><code>TOPSIS METHOD REALISATION</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/vat1kan/cexpert?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/vat1kan/cexpert?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/vat1kan/cexpert?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/vat1kan/cexpert?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Contributing](#-contributing)
- [ License](#-license)
</details>
<hr>

##  Overview

<b>This project is a software implementation of the method of preference prioritization based on proximity to the ideal solution (TOPSIS) in the form of a web application using Django (more information about add-ons in the requirements file). The web application is a recommendation and information system for rational selection of a civilian vehicle depending on the operating environment.
The mathematical apparatus of expert evaluation is used to translate characteristic indicators into numerical values, which allows it to be flexibly adjusted if necessary. It is important to note that the expert survey in this method was performed on a small group of people. The obtained estimates are exclusively subjective and are used only for scientific demonstration of the method. The proposed system may be incorrect when assessing the market in its current form and requires changing the parameters at the time of the survey.</b>

---

##  Features

<b>- Creating your own Car class objects using a CRUD form. Records are entered into the database db.sqlite3. Be careful when changing the Cars class structure and further migrations.</b> <br><br>
<b>- Flexible customization of conversion of characteristic indicators into numerical indicators. At the moment it is realized by changing values in the function <code>def Grading</code> of the <code>topsis.py</code> file.</b><br><br>
<b>- Expansion of the method and introduction of other decision-making techniques is welcome. The developed application structure allows to add Electre, Smart, MAHP methods and quickly import them into the main functionality.</b>


---

##  Repository Structure

```sh
└── cexpert/
    ├── cexpert
    │   ├── Cars
    │   ├── cexpert
    │   ├── db.sqlite3
    │   ├── manage.py
    │   └── static
    ├── README.md
    └── requirements.txt
```

---

##  Getting Started

**System Requirements:**

* **Python**: `version 3.9.0` or above

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the cexpert repository:
>
> ```console
> $ git clone https://github.com/vat1kan/cexpert
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd cexpert
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run cexpert using the command below:
> ```console
> $ python main.py
> ```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/vat1kan/cexpert/issues)**: Submit bugs found or log feature requests for the `cexpert` project.
- **[Submit Pull Requests](https://github.com/vat1kan/cexpert/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/vat1kan/cexpert/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/vat1kan/cexpert
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/vat1kan/cexpert/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=vat1kan/cexpert">
   </a>
</p>
</details>

---

##  License

This project is protected under the [GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/). For more details, refer to the [LICENSE](https://choosealicense.com/licenses/gpl-3.0/) file.
